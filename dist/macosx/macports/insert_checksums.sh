#! /bin/bash

STFVERSION="0.16.0"
MPDIR=`pwd`

if [ "$1" != "" ]; then
    cd ../../../ && ./autogen.sh
    cd build/release
    ./conf_macports_release.sh
    make dist
    scp stimfit-${STFVERSION}.tar.gz p8210991@schmidt-hieber.de:/kunden/homepages/32/d34288459/htdocs/StimfitJ/
    cd ${MPDIR}
fi

RMD160=`openssl rmd160 -r ../../../build/release/stimfit-${STFVERSION}.tar.gz | awk '{print $1;}'`
SHA256=`openssl sha256 -r ../../../build/release/stimfit-${STFVERSION}.tar.gz | awk '{print $1;}'`

echo "rmd160:" ${RMD160}
echo "sha256:" ${SHA256}

GSED=`which gsed`
if [ "${GSED}" = "" ]
then
    GSED=`which sed`
fi

${GSED} 's/RMD160/'${RMD160}'/g' ${MPDIR}/science/stimfit/Portfile.in > ${MPDIR}/science/stimfit/Portfile
${GSED} -i 's/SHA256/'${SHA256}'/g' ${MPDIR}/science/stimfit/Portfile
${GSED} -i 's/STFVERSION/'${STFVERSION}'/g' ${MPDIR}/science/stimfit/Portfile
${GSED} 's/RMD160/'${RMD160}'/g' ${MPDIR}/python/py-stfio/Portfile.in > ${MPDIR}/python/py-stfio/Portfile
${GSED} -i 's/SHA256/'${SHA256}'/g' ${MPDIR}/python/py-stfio/Portfile
${GSED} -i 's/STFVERSION/'${STFVERSION}'/g' ${MPDIR}/python/py-stfio/Portfile

sudo portindex
sudo port uninstall stimfit
sudo port clean --all stimfit
sudo port uninstall py-stfio
sudo port clean --all py-stfio
sudo port uninstall py27-stfio
sudo port clean --all py27-stfio
sudo port uninstall py35-stfio
sudo port clean --all py35-stfio
sudo port uninstall py36-stfio
sudo port clean --all py36-stfio
sudo port uninstall py37-stfio
sudo port clean --all py37-stfio
