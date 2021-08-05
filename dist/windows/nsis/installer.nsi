; installer.nsi
;
; NSI script for stimfit

; This may slightly reduce the executable size, but compression is slower.
SetCompressor lzma

; RequestExecutionLevel admin ;Require admin rights on NT6+ (When UAC is turned on)

;--------------------------------
; Use modern interface
!include MUI2.nsh
;--------------------------------
!include LogicLib.nsh

!define PRODUCT_VERSION "0.16.0"
!define WXW_VERSION "3.0.2.0"
!define WXW_VERSION_DIR "3.0.2"
!define WXW_VERSION_SHORT "30"
!define PY_VERSION "2.7.14"
!define PY_MAJOR "2.7"
!define PY_MAJOR_SHORT "27"
!define PY_MIN "2.7"
!define PY_INST_FILE "python-${PY_VERSION}.amd64.msi"
Var PY_ACT
!define NP_VERSION ""
!define MPL_VERSION ""
!define EMF_VERSION ""
!define EXE_NAME "Stimfit"
!define REG_NAME "Stimfit 0.15"
!define REG_NAME_IO "stfio 0.15"
!define PRODUCT_PUBLISHER "Christoph Schmidt-Hieber"
!define PRODUCT_WEB_SITE "http://www.stimfit.org"
!define STFDIR "..\..\..\..\stimfit"
!define BUILDTARGETDIR "${STFDIR}\dist\windows\VS2008\${EXE_NAME}\x64\Release"
!define PYSTFDIR "${STFDIR}\src\stimfit\py"
!define PYSTFIODIR "${STFDIR}\src\pystfio"
!define MSIDIR "..\..\..\..\Downloads"
!define WXWDIR "..\..\..\..\wx"
!define WXPDIR "..\..\..\..\wxPython"
!define FFTDIR "..\..\..\..\fftw"
!define HDF5DIR "..\..\..\..\hdf5"
!define BIOSIGDIR "..\..\..\..\biosig"
!define PYEMFDIR "${STFDIR}\src\stimfit\py\emf"
!define PRODIR "C:\Program Files"
!define ALTPRODIR "C:\Program Files (x86)"
!define FULL_WELCOME "This wizard will guide you through the installation \
of ${REG_NAME} and wxPython. You will need an internet connection during the installation to download required Python packages. \
It is strongly recommended that you uninstall any earlier version of Stimfit (< 0.11) before \
proceeding. You can optionally \
install Python ${PY_VERSION}, NumPy ${NP_VERSION} \
Matplotlib ${MPL_VERSION} and PyEMF ${EMF_VERSION}\
if you don't have them on your machine."
!define UPDATE_WELCOME "This wizard will install \
${REG_NAME} on your computer. It is strongly recommended that you uninstall any \
previous versions (< 0.11) first. Please make sure Python ${PY_MAJOR}, \
NumPy and Matplotlib are installed before proceeding."
; The name of the installer
Name "${REG_NAME}"


; The file to write
!ifdef UPDATE
OutFile "${EXE_NAME}-${PRODUCT_VERSION}-core.exe"
!else
OutFile "${EXE_NAME}-${PRODUCT_VERSION}-bundle.exe"
!endif

; The default installation directory
InstallDir "$PROGRAMFILES64\${REG_NAME}"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

!define STRING_PYTHON_NOT_FOUND "Python ${PY_MIN} (or newer) is not installed on this system. \
$\nPlease install Python first. \
$\nClick OK to cancel installation and remove installation files."

;--------------------------------
;Variables

Var StartMenuFolder
Var StrNoUsablePythonFound

;--------------------------------

; Function .onInit
; UserInfo::GetAccountType
; pop $0
; ${If} $0 != "admin" ;Require admin rights on NT4+
    ; MessageBox mb_iconstop "Administrator rights required!"
    ; SetErrorLevel 740 ;ERROR_ELEVATION_REQUIRED
    ; Quit
; ${EndIf}
; FunctionEnd

; Pages
!ifdef UPDATE
!define MUI_WELCOMEPAGE_TEXT "${UPDATE_WELCOME}"
!else
!define MUI_WELCOMEPAGE_TEXT "${FULL_WELCOME}"
!endif
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "${STFDIR}\gpl-2.0.txt"
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY

;Start Menu Folder Page Configuration
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\${REG_NAME}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"

!insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder

!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

;--------------------------------
;Languages

!insertmacro MUI_LANGUAGE "English"

;--------------------------------

; The stuff to install
!ifndef UPDATE
Section "Python ${PY_VERSION}" 0

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR

  ; Put installer into installation dir temporarily
  File "${MSIDIR}\${PY_INST_FILE}"

  ExecWait '"Msiexec.exe" /i "$INSTDIR\${PY_INST_FILE}"'

  ; Delete installer once we are done
  Delete "$INSTDIR\${PY_INST_FILE}"

  ; Install PyEMF
  ExecWait 'cd "${PYEMFDIR}"; "c:\python${PY_MAJOR_SHORT}\python.exe" setup.py install'
  RMDir /r "${PYEMFDIR}"

  ; Install / upgrade numpy, scipy, matplotlib, nptdms
  ExecWait '"c:\Python${PY_MAJOR_SHORT}\Scripts\pip.exe" install --upgrade numpy scipy matplotlib nptdms'

SectionEnd
!endif

Section "!Program files and Python modules" 1 ; Core program files and Python modules

  ;This section is required : readonly mode
  SectionIn RO

  ; Create default error message
  StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_NOT_FOUND}"

  ClearErrors
  SetRegView 64
  ReadRegStr $9 HKEY_LOCAL_MACHINE "SOFTWARE\Python\PythonCore\${PY_MAJOR}\InstallPath" ""
  IfErrors 0 +9
    ClearErrors
    ReadRegStr $9 HKEY_LOCAL_MACHINE "SOFTWARE\Python\PythonCore\${PY_MIN}\InstallPath" ""
    IfErrors 0 +8
	  ClearErrors
	  ReadRegStr $9 HKEY_CURRENT_USER "Software\Python\PythonCore\${PY_MIN}\InstallPath" ""
	  IfErrors 0 +5
        MessageBox MB_OK "$StrNoUsablePythonFound"
        Quit
  SetRegView 32
  StrCpy $PY_ACT "${PY_MAJOR}"
  Goto +2
  StrCpy $PY_ACT "${PY_MIN}"

  ClearErrors
  DetailPrint "Found a Python $PY_ACT installation at '$9'"

  ; Add a path to the installation directory in the python site-packages folder
  FileOpen $0 $9\Lib\site-packages\stimfit.pth w
  FileWrite $0 "$INSTDIR"
  FileClose $0

  IfErrors 0 +3
    MessageBox MB_OK "Couldn't create path for python module"
    Quit

  ClearErrors

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR

  Delete "$INSTDIR\*.exe"
  Delete "$INSTDIR\*.dll"
  Delete "$INSTDIR\wx*"
  RMDir /r "$INSTDIR\wx-${WXW_VERSION_DIR}-msw-unicode"
  RMDir /r "$INSTDIR\wx-${WXW_VERSION_DIR}-msw"
  RMDir /r "$INSTDIR\*site-packages"
  File "${FFTDIR}\libfftw3-3.dll"
  File "${HDF5DIR}\bin\hdf5_hl.dll"
  File "${HDF5DIR}\bin\hdf5.dll"
  File "${HDF5DIR}\bin\szip.dll"
  File "${HDF5DIR}\bin\zlib.dll"
  File "${BIOSIGDIR}\lib\libbiosig.dll"
  File "${WXWDIR}\lib\vc90_x64_dll\wxmsw${WXW_VERSION_SHORT}u_core_vc90_x64.dll"
  File "${WXWDIR}\lib\vc90_x64_dll\wxbase${WXW_VERSION_SHORT}u_vc90_x64.dll"
  File "${WXWDIR}\lib\vc90_x64_dll\wxmsw${WXW_VERSION_SHORT}u_aui_vc90_x64.dll"
  File "${WXWDIR}\lib\vc90_x64_dll\wxmsw${WXW_VERSION_SHORT}u_adv_vc90_x64.dll"
  File "${WXWDIR}\lib\vc90_x64_dll\wxbase${WXW_VERSION_SHORT}u_net_vc90_x64.dll"
  File "${WXWDIR}\lib\vc90_x64_dll\wxmsw${WXW_VERSION_SHORT}u_html_vc90_x64.dll"
  File "${WXWDIR}\lib\vc90_x64_dll\wxmsw${WXW_VERSION_SHORT}u_stc_vc90_x64.dll"
  File "${HDF5DIR}\bin\msvcp90.dll"
  File "${HDF5DIR}\bin\msvcr90.dll"
  File /r "${WXPDIR}\wx*"
  File "${BUILDTARGETDIR}\${EXE_NAME}.exe"
  File "${BUILDTARGETDIR}\libstimfit.dll"
  File "${BUILDTARGETDIR}\libstfio.dll"
  File "${BUILDTARGETDIR}\libstfnum.dll"
  File "${BUILDTARGETDIR}\_stf.pyd"
  File "${PYSTFDIR}\stf.py"
  File "${PYSTFDIR}\ivtools.py"
  File "${PYSTFDIR}\mintools.py"
  File "${PYSTFDIR}\natools.py"
  File "${PYSTFDIR}\minidemo.py"
  File "${PYSTFDIR}\charlie.py"
  File "${PYSTFDIR}\hdf5tools.py"
  File "${PYSTFDIR}\spells.py"
  File "${PYSTFDIR}\tdms.py"
  File "${PYSTFDIR}\embedded_init.py"
  File "${PYSTFDIR}\embedded_stf.py"
  File "${PYSTFDIR}\embedded_mpl.py"
  File "${PYSTFDIR}\embedded_ipython.py"
  File "${PYSTFDIR}\heka.py"
  File "${PYSTFDIR}\extensions.py"
  File /r /x .hg "${STFDIR}\src"

  ;Store installation folder
  WriteRegStr HKCU "Software\${REG_NAME}" "" $INSTDIR
  WriteRegStr HKCU "Software\${REG_NAME}" "InstallLocation" $INSTDIR
  WriteRegExpandStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${REG_NAME}" "UninstallString" '"$INSTDIR\Uninstall.exe"'
  WriteRegExpandStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${REG_NAME}" "InstallLocation" "$INSTDIR"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${REG_NAME}" "DisplayName" "${REG_NAME}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${REG_NAME}" "DisplayIcon" "$INSTDIR\${EXE_NAME}.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${REG_NAME}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${REG_NAME}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"

  ; Associate files to amaya
  WriteRegStr HKCR "${REG_NAME}" "" "${REG_NAME} Files"
  WriteRegStr HKCR "${REG_NAME}\DefaultIcon" "" "$INSTDIR\${EXE_NAME}.exe"
  WriteRegStr HKCR "${REG_NAME}\shell" "" "open"
  WriteRegStr HKCR "${REG_NAME}\shell\open\command" "" '"$INSTDIR\${EXE_NAME}.exe" "/d=$INSTDIR" "%1"'

  ; Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"

  ; Install for all users
  SetShellVarContext all

  ;Start Menu
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application

    ; Create shortcuts
    CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
    CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
    CreateShortCut "$SMPROGRAMS\$StartMenuFolder\${REG_NAME}.lnk" "$INSTDIR\${EXE_NAME}.exe"

 !insertmacro MUI_STARTMENU_WRITE_END

  ; Create desktop link
  CreateShortCut "$DESKTOP\${REG_NAME}.lnk" "$INSTDIR\${EXE_NAME}.exe"

SectionEnd ; end the section

Section "!stfio standalone module" 2 ; Standalone python file i/o module

  ;This section is required : readonly mode
  SectionIn RO

  ; Create default error message
  StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_NOT_FOUND}"

  ClearErrors
  SetRegView 64
  ReadRegStr $9 HKEY_LOCAL_MACHINE "SOFTWARE\Python\PythonCore\${PY_MAJOR}\InstallPath" ""
  IfErrors 0 +9
    ClearErrors
    ReadRegStr $9 HKEY_LOCAL_MACHINE "SOFTWARE\Python\PythonCore\${PY_MIN}\InstallPath" ""
    IfErrors 0 +8
	  ClearErrors
	  ReadRegStr $9 HKEY_CURRENT_USER "Software\Python\PythonCore\${PY_MIN}\InstallPath" ""
	  IfErrors 0 +5
        MessageBox MB_OK "$StrNoUsablePythonFound"
        Quit
  SetRegView 32
  StrCpy $PY_ACT "${PY_MAJOR}"
  Goto +2
  StrCpy $PY_ACT "${PY_MIN}"

  ClearErrors
  DetailPrint "Found a Python $PY_ACT installation at '$9'"

  !define STFIODIR "$9\Lib\site-packages\stfio"
  ; Add a path to the installation directory in the python site-packages folder
  ; FileOpen $0 $9\Lib\site-packages\stfio.pth w
  ; FileWrite $0 ${STFIODIR}
  ; FileClose $0

  IfErrors 0 +3
    MessageBox MB_OK "Couldn't create path for python module"
    Quit

  ClearErrors

  ; Set output path to the installation directory.
  RMDir /r ${STFIODIR}
  CreateDirectory ${STFIODIR}
  SetOutPath ${STFIODIR}

  File "${FFTDIR}\libfftw3-3.dll"
  File "${HDF5DIR}\bin\hdf5_hl.dll"
  File "${HDF5DIR}\bin\hdf5.dll"
  File "${HDF5DIR}\bin\szip.dll"
  File "${HDF5DIR}\bin\zlib.dll"
  File "${BIOSIGDIR}\lib\libbiosig.dll"
  File "${HDF5DIR}\bin\msvcp90.dll"
  File "${HDF5DIR}\bin\msvcr90.dll"
  File "${BUILDTARGETDIR}\_stfio.pyd"
  File "${BUILDTARGETDIR}\libstfio.dll"
  File "${BUILDTARGETDIR}\libstfnum.dll"
  File "${PYSTFIODIR}\__init__.py"
  File "${PYSTFIODIR}\stfio.py"
  File "${PYSTFIODIR}\stfio_plot.py"
  File "${PYSTFIODIR}\stfio_neo.py"
  File "${PYSTFIODIR}\unittest_stfio.py"

  ; Install for all users
  SetShellVarContext all

SectionEnd ; end the section

Section "Uninstall"

  SetDetailsPrint textonly
  DetailPrint "Deleting program files..."
  SetDetailsPrint listonly

  ;Uninstall Stimfit for all users
  SetShellVarContext all

  ReadRegStr $StartMenuFolder HKCU "Software\${REG_NAME}" "Start Menu Folder"
  IfFileExists "$SMPROGRAMS\$StartMenuFolder\${EXE_NAME}.lnk" stimfit_smp_installed
    Goto stimfit_smp_notinstalled
  stimfit_smp_installed:
  Delete "$SMPROGRAMS\$StartMenuFolder\${EXE_NAME}.lnk"
  Delete "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk"
  RMDir "$SMPROGRAMS\$StartMenuFolder"
  stimfit_smp_notinstalled:

  RMDir /r "$INSTDIR"
  Delete "$DESKTOP\${EXE_NAME}.lnk"

  ClearErrors
  ReadRegStr $9 HKEY_LOCAL_MACHINE "SOFTWARE\Python\PythonCore\${PY_MAJOR}\InstallPath" ""
  IfErrors 0 +8
    ClearErrors
    ReadRegStr $9 HKEY_LOCAL_MACHINE "SOFTWARE\Python\PythonCore\${PY_MIN}\InstallPath" ""
    IfErrors 0 +7
	  ClearErrors
	  ReadRegStr $9 HKEY_CURRENT_USER "Software\Python\PythonCore\${PY_MIN}\InstallPath" ""
	  IfErrors 0 +4
        DetailPrint "$StrNoUsablePythonFound"
  StrCpy $PY_ACT "${PY_MAJOR}"
  Goto +2
  StrCpy $PY_ACT "${PY_MIN}"

  ClearErrors
  DetailPrint "Found a Python $PY_ACT installation at '$9'"

  !define STFIORMDIR "$9\Lib\site-packages\stfio"

  Delete ${STFIORMDIR}\..\stfio.pth
  Delete ${STFIORMDIR}\..\stimfit.pth
  RMDir /r ${STFIORMDIR}

  SetDetailsPrint textonly
  DetailPrint "Deleting registry keys..."
  SetDetailsPrint listonly

  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${REG_NAME}"
  DeleteRegKey HKLM "Software\${REG_NAME}"
  DeleteRegKey HKCR "${REG_NAME}"
  DeleteRegKey HKCU "Software\${REG_NAME}"
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${REG_NAME_IO}"
  DeleteRegKey HKLM "Software\${REG_NAME_IO}"
  DeleteRegKey HKCR "${REG_NAME_IO}"
  DeleteRegKey HKCU "Software\${REG_NAME_IO}"

  ; uninstall files associations
  ; --> .dat
  ReadRegStr $R0 HKCR ".dat" ""
  StrCmp $R0 "${REG_NAME}" 0 +3
    ReadRegStr $R0 HKCR ".dat" "AM_OLD_VALUE"
    WriteRegStr HKCR ".dat" "" $R0

  ; --> .cfs
  ReadRegStr $R0 HKCR ".cfs" ""
  StrCmp $R0 "${REG_NAME}" 0 +3
    ReadRegStr $R0 HKCR ".cfs" "AM_OLD_VALUE"
    WriteRegStr HKCR ".cfs" "" $R0

  ; --> .h5
  ReadRegStr $R0 HKCR ".h5" ""
  StrCmp $R0 "${REG_NAME}" 0 +3
    ReadRegStr $R0 HKCR ".h5" "AM_OLD_VALUE"
    WriteRegStr HKCR ".h5" "" $R0

  ; --> .axgd
  ReadRegStr $R0 HKCR ".axgd" ""
  StrCmp $R0 "${REG_NAME}" 0 +3
    ReadRegStr $R0 HKCR ".axgd" "AM_OLD_VALUE"
    WriteRegStr HKCR ".axgd" "" $R0

  ; --> .axgx
  ReadRegStr $R0 HKCR ".axgx" ""
  StrCmp $R0 "${REG_NAME}" 0 +3
    ReadRegStr $R0 HKCR ".axgx" "AM_OLD_VALUE"
    WriteRegStr HKCR ".axgx" "" $R0

  ; --> .abf
  ReadRegStr $R0 HKCR ".abf" ""
  StrCmp $R0 "${REG_NAME}" 0 +3
    ReadRegStr $R0 HKCR ".abf" "AM_OLD_VALUE"
    WriteRegStr HKCR ".abf" "" $R0

  ; --> .atf
  ReadRegStr $R0 HKCR ".atf" ""
  StrCmp $R0 "${REG_NAME}" 0 +3
    ReadRegStr $R0 HKCR ".atf" "AM_OLD_VALUE"
    WriteRegStr HKCR ".atf" "" $R0

  ; --> .tdms
  ReadRegStr $R0 HKCR ".tdms" ""
  StrCmp $R0 "${REG_NAME}" 0 +3
    ReadRegStr $R0 HKCR ".tdms" "AM_OLD_VALUE"
    WriteRegStr HKCR ".tdms" "" $R0

  SetDetailsPrint textonly
  DetailPrint "Successfully uninstalled stimfit"
  SetDetailsPrint listonly
SectionEnd

; File associations
SubSection "File associations" SecFileAss

; --> .dat
Section ".dat (CED filing system)" SecAssDAT
  ReadRegStr $R0 HKCR ".dat" ""
  StrCmp $R0 "${REG_NAME}" already_stf no_stf
  no_stf:
    WriteRegStr HKCR ".dat" "AM_OLD_VALUE" $R0
  WriteRegStr HKCR ".dat" "" "${REG_NAME}"
  already_stf:
SectionEnd

; --> .cfs
Section ".cfs (CED filing system)" SecAssCFS
  ReadRegStr $R0 HKCR ".cfs" ""
  StrCmp $R0 "${REG_NAME}" already_stf no_stf
  no_stf:
    WriteRegStr HKCR ".cfs" "AM_OLD_VALUE" $R0
  WriteRegStr HKCR ".cfs" "" "${REG_NAME}"
  already_stf:
SectionEnd

; --> .h5
Section ".h5 (HDF5)" SecAssH5
  ReadRegStr $R0 HKCR ".h5" ""
  StrCmp $R0 "${REG_NAME}" already_stf no_stf
  no_stf:
    WriteRegStr HKCR ".h5" "AM_OLD_VALUE" $R0
  WriteRegStr HKCR ".h5" "" "${REG_NAME}"
  already_stf:
SectionEnd

; --> .axgd
Section ".axgd (Axograph digitized)" SecAssAxgd
  ReadRegStr $R0 HKCR ".axgd" ""
  StrCmp $R0 "${REG_NAME}" already_stf no_stf
  no_stf:
    WriteRegStr HKCR ".axgd" "AM_OLD_VALUE" $R0
  WriteRegStr HKCR ".axgd" "" "${REG_NAME}"
  already_stf:
SectionEnd

; --> .axgx
Section ".axgx (Axograph X)" SecAssAxgx
  ReadRegStr $R0 HKCR ".axgx" ""
  StrCmp $R0 "${REG_NAME}" already_stf no_stf
  no_stf:
    WriteRegStr HKCR ".axgx" "AM_OLD_VALUE" $R0
  WriteRegStr HKCR ".axgx" "" "${REG_NAME}"
  already_stf:
SectionEnd

; --> .abf
Section ".abf (Axon binary file)" SecAssABF
  ReadRegStr $R0 HKCR ".abf" ""
  StrCmp $R0 "${REG_NAME}" already_stf no_stf
  no_stf:
    WriteRegStr HKCR ".abf" "AM_OLD_VALUE" $R0
  WriteRegStr HKCR ".abf" "" "${REG_NAME}"
  already_stf:
SectionEnd

; --> .atf
Section ".atf (Axon text file)" SecAssATF
  ReadRegStr $R0 HKCR ".atf" ""
  StrCmp $R0 "${REG_NAME}" already_stf no_stf
  no_stf:
    WriteRegStr HKCR ".atf" "AM_OLD_VALUE" $R0
  WriteRegStr HKCR ".atf" "" "${REG_NAME}"
  already_stf:
SectionEnd

; --> .tdms
Section ".tdms (Mantis TDMS file)" SecAssTDMS
  ReadRegStr $R0 HKCR ".tdms" ""
  StrCmp $R0 "${REG_NAME}" already_stf no_stf
  no_stf:
    WriteRegStr HKCR ".tdms" "AM_OLD_VALUE" $R0
  WriteRegStr HKCR ".tdms" "" "${REG_NAME}"
  already_stf:
SectionEnd

SubSectionEnd

;--------------------------------
;Descriptions

  ;Assign descriptions to sections
!ifndef UPDATE
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT 0 "Python ${PY_MIN} or ${PY_MAJOR} is required to run stimfit. Unselect this if it's already installed on your system."
    !insertmacro MUI_DESCRIPTION_TEXT 1 "The core program files and wxPython 2.9 (mandatory)."
    !insertmacro MUI_DESCRIPTION_TEXT 2 "Standalone Python file i/o module."
    !insertmacro MUI_DESCRIPTION_TEXT 3 "Selects Stimfit as the default application for files of these types."
  !insertmacro MUI_FUNCTION_DESCRIPTION_END
!else
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT 1 "The core program files and wxPython 2.9 (mandatory)."
    !insertmacro MUI_DESCRIPTION_TEXT 2 "Standalone Python file i/o module."
    !insertmacro MUI_DESCRIPTION_TEXT 3 "Selects Stimfit as the default application for files of these types."
  !insertmacro MUI_FUNCTION_DESCRIPTION_END
!endif
