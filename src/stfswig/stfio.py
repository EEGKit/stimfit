# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

"""
The stfio module provides functions to read/write data from/to
common electrophysiology file formats
"""

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_stfio', [dirname(__file__)])
        except ImportError:
            import _stfio
            return _stfio
        if fp is not None:
            try:
                _mod = imp.load_module('_stfio', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _stfio = swig_import_helper()
    del swig_import_helper
else:
    import _stfio
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Recording(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Recording, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Recording, name)
    __repr__ = _swig_repr
    __swig_setmethods__["dt"] = _stfio.Recording_dt_set
    __swig_getmethods__["dt"] = _stfio.Recording_dt_get
    if _newclass:dt = _swig_property(_stfio.Recording_dt_get, _stfio.Recording_dt_set)
    __swig_setmethods__["file_description"] = _stfio.Recording_file_description_set
    __swig_getmethods__["file_description"] = _stfio.Recording_file_description_get
    if _newclass:file_description = _swig_property(_stfio.Recording_file_description_get, _stfio.Recording_file_description_set)
    __swig_setmethods__["time"] = _stfio.Recording_time_set
    __swig_getmethods__["time"] = _stfio.Recording_time_get
    if _newclass:time = _swig_property(_stfio.Recording_time_get, _stfio.Recording_time_set)
    __swig_setmethods__["date"] = _stfio.Recording_date_set
    __swig_getmethods__["date"] = _stfio.Recording_date_get
    if _newclass:date = _swig_property(_stfio.Recording_date_get, _stfio.Recording_date_set)
    __swig_setmethods__["comment"] = _stfio.Recording_comment_set
    __swig_getmethods__["comment"] = _stfio.Recording_comment_get
    if _newclass:comment = _swig_property(_stfio.Recording_comment_get, _stfio.Recording_comment_set)
    __swig_setmethods__["xunits"] = _stfio.Recording_xunits_set
    __swig_getmethods__["xunits"] = _stfio.Recording_xunits_get
    if _newclass:xunits = _swig_property(_stfio.Recording_xunits_get, _stfio.Recording_xunits_set)
    def __init__(self, *args): 
        this = _stfio.new_Recording(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _stfio.delete_Recording
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _stfio.Recording___getitem__(self, *args)
    def __len__(self): return _stfio.Recording___len__(self)
    def write(self, *args):
        """
        Reads a file and returns a Recording object.

            Arguments:
            fname  -- file name
            ftype  -- file type (string). At present, only "hdf5" is supported.

            Returns:
            True upon successful completion.
        Reads a file and returns a Recording object.

            Arguments:
            fname  -- file name
            ftype  -- file type (string). At present, only "hdf5" is supported.

            Returns:
            True upon successful completion.
        """
        return _stfio.Recording_write(self, *args)

Recording_swigregister = _stfio.Recording_swigregister
Recording_swigregister(Recording)

class Channel(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Channel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Channel, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _stfio.Channel_name_set
    __swig_getmethods__["name"] = _stfio.Channel_name_get
    if _newclass:name = _swig_property(_stfio.Channel_name_get, _stfio.Channel_name_set)
    __swig_setmethods__["yunits"] = _stfio.Channel_yunits_set
    __swig_getmethods__["yunits"] = _stfio.Channel_yunits_get
    if _newclass:yunits = _swig_property(_stfio.Channel_yunits_get, _stfio.Channel_yunits_set)
    def __init__(self, *args): 
        this = _stfio.new_Channel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _stfio.delete_Channel
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _stfio.Channel___getitem__(self, *args)
    def __len__(self): return _stfio.Channel___len__(self)
Channel_swigregister = _stfio.Channel_swigregister
Channel_swigregister(Channel)

class Section(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Section, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Section, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _stfio.new_Section(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _stfio.delete_Section
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _stfio.Section___getitem__(self, *args)
    def __len__(self): return _stfio.Section___len__(self)
    def asarray(self):
        """Returns the section as a numpy array."""
        return _stfio.Section_asarray(self)

Section_swigregister = _stfio.Section_swigregister
Section_swigregister(Section)


def _read(*args):
  """
    _read(filename, ftype, Data) -> bool

    Reads a file and returns a recording object.
          
    Arguments:
    filename -- file name
    ftype    -- File type

    Returns:
    A recording object.
    """
  return _stfio._read(*args)
import os


class StfIOException(Exception):
    """ raises Exceptions for the Stfio module """
    def __init__(self, error_msg):
        self.msg = error_msg 

    def __str__(self):
        return repr(self.msg)

filetype = {
    '.dat':'cfs',
    '.h5':'hdf5',
    '.abf':'abf',
    '.atf':'atf',
    '.axgd':'axg',
    '.axgx':'axg'}

def read(fname, ftype=None):
    """Reads a file and returns a Recording object.

    Arguments:
    fname  -- file name
    ftype  -- file type (string); can be one of:
              "cfs"  - CED filing system
              "hdf5" - HDF5
              "abf"  - Axon binary file
              "atf"  - Axon text file
              "axg"  - Axograph X binary file
              if ftype is None (default), it will be guessed from the
              extension.

    Returns:
    A Recording object.
    """
    if not os.path.exists(fname):
        raise StfIOException('File %s does not exist' % fname)
    
    if ftype is None:
        
        ext = os.path.splitext(fname)[1]
        try:
            ftype = filetype[ext]
        except KeyError:
            raise StfIOException('Couldn\'t guess file file from extension (%s)' % ext)

    rec = Recording()
    if not _read(fname, ftype, rec):
        raise StfIOException('Error reading file')

    return rec




