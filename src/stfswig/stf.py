# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.39
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

"""
The stf module allows to access a running stimfit
application from the embedded python shell.
"""

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_stf', [dirname(__file__)])
        except ImportError:
            import _stf
            return _stf
        if fp is not None:
            try:
                _mod = imp.load_module('_stf', fp, pathname, description)
            finally:
                fp.close()
                return _mod
    _stf = swig_import_helper()
    del swig_import_helper
else:
    import _stf
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



def _get_trace_fixedsize(*args):
  """
    _get_trace_fixedsize(outvec, trace, channel)

    Returns a trace as a 1-dimensional NumPy array.
    This returns an array of a given size.
    Don't use this, use get_trace instead.
          
    Arguments:
    size --    Size of the array to be filled.       
    trace --   ZERO-BASED index of the trace within the channel.
               Note that this is one less than what is shown
               in the drop-down box.
               The default value of -1 returns the currently
               displayed trace.
    channel -- ZERO-BASED index of the channel. This is independent
               of whether a channel is active or not.
               The default value of -1 returns the currently
               active channel.
    Returns:
    The trace as a 1D NumPy array.
    """
  return _stf._get_trace_fixedsize(*args)

def new_window(*args):
  """
    new_window(invec) -> bool

    Creates a new window showing a
    1D NumPy array.
          
    Arguments:
    invec --   The NumPy array to be shown.

    Returns:
    True upon successful completion, false otherwise.
    """
  return _stf.new_window(*args)

def _new_window_gMatrix():
  """
    _new_window_gMatrix() -> bool

    Creates a new window from the global matrix.
    Do not use directly.
    """
  return _stf._new_window_gMatrix()

def new_window_matrix(*args):
  """
    new_window_matrix(inarr) -> bool

    Creates a new window showing a
    2D NumPy array.
          
    Arguments:
    inarr --   The NumPy array to be shown. First dimension
               are the traces, second dimension the sampling
               points within the traces.

    Returns:
    True upon successful completion, false otherwise.
    """
  return _stf.new_window_matrix(*args)

def new_window_selected_this():
  """
    new_window_selected_this() -> bool

    Creates a new window showing the
    selected traces of the current file.
    Returns:
    True if successful.
    """
  return _stf.new_window_selected_this()

def new_window_selected_all():
  """
    new_window_selected_all() -> bool

    Creates a new window showing the
    selected traces of all open files.
    Returns:
    True if successful.
    """
  return _stf.new_window_selected_all()

def get_size_recording():
  """
    get_size_recording() -> int

    Retrieves the number of channels in a 
    recording.
       
    Returns:
    The number of channels in a recording.
    """
  return _stf.get_size_recording()

def get_sampling_interval():
  """
    get_sampling_interval() -> double

    Returns the sampling interval.

    Returns:
    The sampling interval.
    """
  return _stf.get_sampling_interval()

def get_xunits():
  """
    get_xunits() -> char

    Returns the x units of the specified section.
    X units are assumed to be the same for the entire file.

    Returns:
    The x units as a string.
    """
  return _stf.get_xunits()

def set_xunits(*args):
  """
    set_xunits(units) -> bool

    Sets the x unit string for the entire file.

    Arguments:
    units --   The new x unit string.

    Returns:
    True if successful.
    """
  return _stf.set_xunits(*args)

def set_sampling_interval(*args):
  """
    set_sampling_interval(si) -> bool

    Sets a new sampling interval.

    Argument:
    si --     The new sampling interval.

    Returns:
    False upon failure.
    """
  return _stf.set_sampling_interval(*args)

def select_all():
  """
    select_all()

    Selects all traces in the current file. Stores 
    the baseline along with the trace index.
    """
  return _stf.select_all()

def unselect_all():
  """
    unselect_all()

    Unselects all previously selected traces in the
    current file.
    """
  return _stf.unselect_all()

def subtract_base():
  """
    subtract_base() -> bool

    Subtracts the baseline from the selected traces
    of the current file, then displays the subtracted
    traces in a new window.

    Returns:
    True if the subtraction was successful, False otherwise.
    """
  return _stf.subtract_base()

def leastsq_param_size(*args):
  """
    leastsq_param_size(fselect) -> int

    Retrieves the number of parameters for a
    function.

    Arguments:
    fselect -- Zero-based index of the function as it appears in the fit
               selection dialog.

    Returns:
    The number of parameters for the function with index fselect, or a 
    negative value upon failure.
    """
  return _stf.leastsq_param_size(*args)

def check_doc():
  """
    check_doc() -> bool

    Checks whether a file is open.

    Returns:
    True if a file is open, False otherwise.
    """
  return _stf.check_doc()

def get_filename():
  """
    get_filename() -> char

    Returns the name of the current file.
    """
  return _stf.get_filename()

def _gMatrix_resize(*args):
  """
    _gMatrix_resize(channels, sections)

    Resizes the global matrix. Do not use directly.
       
    Arguments:
    channels -- New number of channels of the global matrix.
    sections -- New number of sections of the global matrix.


    """
  return _stf._gMatrix_resize(*args)

def _gMatrix_at(*args):
  """
    _gMatrix_at(invec, channel, section)

    Sets the valarray at the specified position of
    the global matrix. Do not use directly.
    Arguments:
    invec --   The NumPy array to be used.
    channel -- The channel index within the global matrix.
    section -- The seciton index within the global matrix.

    """
  return _stf._gMatrix_at(*args)

def _gNames_resize(*args):
  """
    _gNames_resize(channels)

    Resizes the global names. Do not use directly.
       
    Arguments:
    channels -- New number of channels of the global names.


    """
  return _stf._gNames_resize(*args)

def _gNames_at(*args):
  """
    _gNames_at(name, channel)

    Sets the channel name of the specifies channel.
    Do not use directly.
    Arguments:
    name --   The new channel name
    channel -- The channel index within the global names.

    """
  return _stf._gNames_at(*args)

def file_open(*args):
  """
    file_open(filename) -> bool

    Opens a file.
       
    Arguments:
    filename -- The file to be opened. On Windows, use double back-
                slashes ("\\\\") between directories to avoid con-
                version to special characters such as "\\t" or "\\n".
                Example usage in Windows:
                file_open("C:\\\data\\\datafile.dat")
                Example usage in Linux:
                file_open("/home/cs/data/datafile.dat")
                This is surprisingly slow when called from python. 
                Haven't figured out the reason yet.

    Returns:
    True if the file could be opened, False otherwise.
    """
  return _stf.file_open(*args)

def file_save(*args):
  """
    file_save(filename) -> bool

    Saves a file.
       
    Arguments:
    filename -- The file to be saved. On Windows, use double back-
                slashes ("\\\\") between directories to avoid con-
                version to special characters such as "\\t" or "\\n".
                Example usage in Windows:
                file_save("C:\\\data\\\datafile.dat")
                Example usage in Linux:
                file_save("/home/cs/data/datafile.dat")
                This is surprisingly slow when called from python. 
                Haven't figured out the reason yet.

    Returns:
    True if the file could be saved, False otherwise.
    """
  return _stf.file_save(*args)

def get_recording_time():
  """
    get_recording_time() -> char

    Returns the time at which the recording was 
    started as a string.
    """
  return _stf.get_recording_time()

def get_recording_date():
  """
    get_recording_date() -> char

    Returns the date at which the recording was 
    started as a string.
    """
  return _stf.get_recording_date()

def get_recording_comment():
  """
    get_recording_comment() -> string

    Returns a comment about the recording.

    """
  return _stf.get_recording_comment()

def set_recording_date(*args):
  """
    set_recording_date(date) -> bool

    Sets a date about the recording.

    Argument:
    date -- A date string.

    Returns:
    True upon successful completion.
    """
  return _stf.set_recording_date(*args)

def set_recording_time(*args):
  """
    set_recording_time(time) -> bool

    Sets a time about the recording.

    Argument:
    time -- A time string.

    Returns:
    True upon successful completion.
    """
  return _stf.set_recording_time(*args)

def set_recording_comment(*args):
  """
    set_recording_comment(comment) -> bool

    Sets a comment about the recording.

    Argument:
    comment -- A comment string.

    Returns:
    True upon successful completion.
    """
  return _stf.set_recording_comment(*args)

def close_all():
  """
    close_all() -> bool

    Closes all open files.
       
    Returns:
    True if all files could be closed.
    """
  return _stf.close_all()

def close_this():
  """
    close_this() -> bool

    Closes the currently active file.
       
    Returns:
    True if the file could be closed.
    """
  return _stf.close_this()

def get_base():
  """
    get_base() -> double

    Returns the current baseline value. Uses the 
    currently measured values, i.e. does not update measurements if the 
    peak or base window cursors have changed.

    Returns:
    The current baseline.
    """
  return _stf.get_base()

def get_peak():
  """
    get_peak() -> double

    Returns the current peak value, measured from
    zero (!). Uses the currently measured values, i.e. does not update 
    measurements if the peak or base window cursors have changed.
             
    Returns:
    The current peak value, measured from zero (again: !).
    """
  return _stf.get_peak()
peak_index_cb = _stf.peak_index_cb
maxrise_index_cb = _stf.maxrise_index_cb
foot_index_cb = _stf.foot_index_cb
t50left_index_cb = _stf.t50left_index_cb
t50right_index_cb = _stf.t50right_index_cb

def set_peak_mean(*args):
  """
    set_peak_mean(pts) -> bool

    Sets the number of points used for the peak 
    calculation.

    Arguments:
    pts -- A moving average (aka sliding, boxcar or running average) is 
           used to determine the peak value. Pts specifies the number of
           sampling points used for the moving window.
           Passing a value of -1 will calculate the average of all
           sampling points within the peak window.

    Returns:
    False upon failure (such as out-of-range).
    """
  return _stf.set_peak_mean(*args)
set_peak_mean = _stf.set_peak_mean

def set_peak_direction(*args):
  """
    set_peak_direction(direction) -> bool

    Sets the direction of the peak detection.

    Arguments:
    direction -- A string specifying the peak direction. Can be one of:
                 "up", "down" or "both"

    Returns:
    False upon failure.
    """
  return _stf.set_peak_direction(*args)
set_peak_direction = _stf.set_peak_direction

def measure():
  """
    measure() -> bool

    Updates all measurements (e.g. peak, baseline, 
    latency) according to the current cursor settings. As if you had
    pressed "Enter" in the main window.
    Returns:
    False upon failure, True otherwise.
    """
  return _stf.measure()
measure = _stf.measure

def get_selected_indices():
  """
    get_selected_indices() -> PyObject

    Returns a tuple with the indices (ZERO-BASED) 
    of the selected traces.
    """
  return _stf.get_selected_indices()
get_selected_indices = _stf.get_selected_indices

def set_trace(*args):
  """
    set_trace(trace) -> bool

    Sets the currently displayed trace to a new
    index. Subsequently updates all measurements (e.g. peak, base,
    latency, i.e. you don't need to call measure() yourself.)

    Arguments:
    trace -- The zero-based index of the new trace to be displayed.

    Returns:
    True upon success, false otherwise (such as out-of-range).
    """
  return _stf.set_trace(*args)
set_trace = _stf.set_trace

def get_trace_index():
  """
    get_trace_index() -> int

    Returns the ZERO-BASED index of the currently
    displayed trace (this is one less than what is shown in the combo box).

    """
  return _stf.get_trace_index()
get_trace_index = _stf.get_trace_index

def set_marker(*args):
  """
    set_marker(x, y) -> bool

    Sets a marker to the specified position in the
    current trace.

    Arguments:
    x -- The horizontal marker position in units of sampling points.
    y -- The vertical marker position in measurement units (e.g. mV).

    Returns:
    False upon failure (such as out-of-range).
    """
  return _stf.set_marker(*args)
set_marker = _stf.set_marker

def erase_markers():
  """erase_markers() -> bool"""
  return _stf.erase_markers()
erase_markers = _stf.erase_markers
import numpy as N

def get_trace(trace = -1, channel = -1):
    """Returns a trace as a 1-dimensional NumPy array.
      
    Arguments:       
    trace --   ZERO-BASED index of the trace within the channel.
               Note that this is one less than what is shown
               in the drop-down box.
               The default value of -1 returns the currently
               displayed trace.
    channel -- ZERO-BASED index of the channel. This is independent
               of whether a channel is active or not.
               The default value of -1 returns the currently
               active channel.
    Returns:
    The trace as a 1D NumPy array.
    """
    return _get_trace_fixedsize(get_size_trace(trace, channel), trace, channel)
    
def new_window_list( array_list ):
    """Creates a new window showing a sequence of
    1D NumPy arrays, or a sequence of a sequence of 1D
    NumPy arrays. As opposed to new_window_matrix(), this
    has the advantage that the arrays need not have equal sizes.
      
    Arguments:       
    array_list -- A sequence (e.g. list or tuple) of numpy arrays, or
                  a sequence of a sequence of numpy arrays.

    Returns:
    True upon successful completion, false otherwise.
    """
    
    try: 
        it = iter(array_list)
    except TypeError: 
        print "Argument is not a sequence"
        return False

    
    try: 
        it = iter(array_list[0])
    except TypeError: 
        print "Argument is not a sequence of sequences."
        print "You can either pass a sequence of 1D NumPy arrays,"
        print "Or a sequence of sequences of 1D NumPy arrays."
        return False
        
    
    is_3d = True
    try: 
        it = iter(array_list[0][0])
    except TypeError: 
        is_3d = False
        n_channels = 1

    if is_3d:
        n_channels = len(array_list)

    if is_3d:
        _gMatrix_resize( n_channels, len(array_list[0]) )
        for (n_c, c) in enumerate(array_list):
            for (n_s, s) in enumerate(c):
                _gMatrix_at( s, n_c, n_s )
        
    else:
        _gMatrix_resize( n_channels, len(array_list) )
        for (n, a) in enumerate(array_list):
            _gMatrix_at( a, 0, n )

    return _new_window_gMatrix( )

def cut_traces( pt ):
    """Cuts the selected traces at the sampling point pt,
    and shows the cut traces in a new window.
    Returns True upon success, False upon failure."""
    
    if not get_selected_indices():
        return False
    new_list = list()
    for n in get_selected_indices():
        if not set_trace(n): return False
        
        if pt < get_size_trace():
            new_list.append( get_trace()[:pt] )
            new_list.append( get_trace()[pt:] )
        else:
            print "Cutting point", pt, "is out of range"

    if len(new_list) > 0: new_window_list( new_list )
    
    return True
    
def cut_traces_multi( pt_list ):
    """Cuts the selected traces at the sampling points
    in pt_list and shows the cut traces in a new window.
    Returns True upon success, False upon failure."""
    if not get_selected_indices():
        return False
    new_list = list()
    for n in get_selected_indices():
        if not set_trace(n): return False
        old_pt = 0
        for pt in pt_list:
            if pt < get_size_trace():
                new_list.append( get_trace()[old_pt:pt] )
                old_pt = pt
            else:
                print "Cutting point", pt, "is out of range"
        if len(new_list) > 0: new_list.append( get_trace()[old_pt:] )
    new_window_list( new_list )
    return True



def show_table(*args):
  """
    show_table(dict, caption = "Python table") -> bool
    show_table(dict) -> bool

    Shows a python dictionary in a results table.
    The dictionary has to have the form "string" : float

    Arguments:
    dict --    A dictionary with strings as key values and floating point
               numbers as values.
    caption -- An optional caption for the table.

    Returns:
    True if successful.
    """
  return _stf.show_table(*args)

def show_table_dictlist(*args):
  """
    show_table_dictlist(dict, caption = "Python table", reverse = True) -> bool
    show_table_dictlist(dict, caption = "Python table") -> bool
    show_table_dictlist(dict) -> bool

    Shows a python dictionary in a results table.
    The dictionary has to have the form "string" : list. 

    Arguments:
    dict --    A dictionary with strings as key values and lists of 
               floating point numbers as values.
    caption -- An optional caption for the table.
    reverse -- If True, The table will be filled in column-major order,
               i.e. dictionary keys will become column titles. Setting
               it to False has not been implemented yet.

    Returns:
    True if successful.
    """
  return _stf.show_table_dictlist(*args)

def get_size_trace(*args):
  """
    get_size_trace(trace = -1, channel = -1) -> int
    get_size_trace(trace = -1) -> int
    get_size_trace() -> int

    Retrieves the number of sample points of a trace.
       
    Arguments:
    trace --   ZERO-BASED index of the trace. Default value of -1
               will use the currently displayed trace. Note that
               this is one less than what is displayed in the drop-
               down list.
    channel -- ZERO-BASED index of the channel. Default value of
               -1 will use the current channel.
    Returns:
    The number of sample points.
    """
  return _stf.get_size_trace(*args)

def get_size_channel(*args):
  """
    get_size_channel(channel = -1) -> int
    get_size_channel() -> int

    Retrieves the number of traces in a channel.
    Note that at present, stimfit only supports equal-sized channels, i.e. 
    all channels within a file need to have the same number of traces. The
    channel argument is only for future extensions. 
       
    Arguments:
    channel -- ZERO-BASED index of the channel. Default value of
               -1 will use the current channel. 
    Returns:
    The number traces in a channel.
    """
  return _stf.get_size_channel(*args)

def get_yunits(*args):
  """
    get_yunits(trace = -1, channel = -1) -> char
    get_yunits(trace = -1) -> char
    get_yunits() -> char

    Returns the y units of the specified trace.
    Y units are not allowed to change between traces at present.

    Arguments:
    trace -- The zero-based index of the trace of interest. If < 0, the
          	   name of the active trace will be returned.
    channel -- The zero-based index of the channel of interest. If < 0, the
          	   active channel will be used.

    Returns:
    The x units as a string.
    """
  return _stf.get_yunits(*args)

def set_yunits(*args):
  """
    set_yunits(units, trace = -1, channel = -1) -> bool
    set_yunits(units, trace = -1) -> bool
    set_yunits(units) -> bool

    Sets the y unit string of the specified trace.
    Y units are not allowed to change between traces at present.

    Arguments:
    units --   The new y unit string.
    trace --   The zero-based index of the trace of interest. If < 0, the
          	   name of the active trace will be returned.
    channel -- The zero-based index of the channel of interest. If < 0, the
          	   active channel will be used.

    Returns:
    True if successful.
    """
  return _stf.set_yunits(*args)

def select_trace(*args):
  """
    select_trace(trace = -1) -> bool
    select_trace() -> bool

    Selects a trace. Checks for out-of-range
    indices and stores the baseline along with the trace index.
       
    Arguments:
    trace --   ZERO-BASED index of the trace. Default value of -1
               will select the currently displayed trace. Note that
               this is one less than what is displayed in the drop-
               down list.
    Returns:
    True if the trace could be selected, False otherwise.
    """
  return _stf.select_trace(*args)

def leastsq(*args):
  """
    leastsq(fselect, refresh = True) -> PyObject
    leastsq(fselect) -> PyObject

    Fits a function to the data between the current
    fit cursors.

    Arguments:
    fselect -- Zero-based index of the function as it appears in the fit
               selection dialog.
    refresh -- To avoid flicker during batch analysis, this may be set to
               False so that the fitted function will not immediately
               be drawn.

    Returns:
    A dictionary with the best-fit parameters and the least-squared
    error, or a null pointer upon failure.
    """
  return _stf.leastsq(*args)

def peak_index(active = True):
  """
    peak_index(active = True) -> double
    peak_index() -> double

    Returns the zero-based index of the current
    peak position in the specified channel. Uses the currently measured
    values, i.e. does not update measurements if the peak window cursors
    have changed.
       
    Arguments:
    active -- If True, returns the current peak index of the active channel.
              Otherwise, returns the current peak index of the inactive channel.
              
    Returns:
    The zero-based index in units of sampling points. May be interpolated
    if more than one point is used for the peak calculation. Returns a 
    negative value upon failure.
    """
  return _stf.peak_index(active)
peak_index = _stf.peak_index

def maxrise_index(active = True):
  """
    maxrise_index(active = True) -> double
    maxrise_index() -> double

    Returns the zero-based index of the maximal
    slope of rise in the specified channel. Uses the currently measured
    values, i.e. does not update measurements if the peak window cursors
    have changed.
       
    Arguments:
    active -- If True, returns the current index of the maximal slope of 
              rise within the active channel. Otherwise, returns the 
              current index of the maximal slope of rise within the 
              inactive channel.
              
    Returns:
    The zero-based index of the maximal slope of  rise in units of 
    sampling points. Interpolated between adjacent sampling points.
    Returns a negative value upon failure.
    """
  return _stf.maxrise_index(active)
maxrise_index = _stf.maxrise_index

def foot_index(active = True):
  """
    foot_index(active = True) -> double
    foot_index() -> double

    Returns the zero-based index of the foot of 
    an event in the active channel. The foot is the intersection of an
    interpolated line through the points of 20 and 80% rise with the
    baseline. Uses the currently measured values, i.e. does not update 
    measurements if the peak or base window cursors have changed.
       
    Arguments:
    active -- If True, returns the current index of the foot within the 
              active channel. Only implemented for the active channel
              at this time. Will return a negative value and show an 
              error message if active == False.
              
    Returns:
    The zero-based index of the foot of an event in units of sampling 
    points. Interpolates between sampling points.
    Returns a negative value upon failure.
    """
  return _stf.foot_index(active)
foot_index = _stf.foot_index

def t50left_index(active = True):
  """
    t50left_index(active = True) -> double
    t50left_index() -> double

    Returns the zero-based index of the left half-
    maximal amplitude of an event in the specified channel. Uses the 
    currently measured values, i.e. does not update measurements if the 
    peak or base window cursors have changed.
       
    Arguments:
    active -- If True, returns the current index of the left half-
              maximal amplitude within the active channel. If False, 
              returns the current index of the left half-maximal amplitude
              within the inactive channel.
              
    Returns:
    The zero-based index of the left half-maximal amplitude in units of 
    sampling points. Interpolates between sampling points. Returns a 
    negative value upon failure.
    """
  return _stf.t50left_index(active)
t50left_index = _stf.t50left_index

def t50right_index(active = True):
  """
    t50right_index(active = True) -> double
    t50right_index() -> double

    Returns the zero-based index of the right half-
    maximal amplitude of an event in the active channel. Uses the 
    currently measured values, i.e. does not update measurements if the 
    peak or base window cursors have changed.
       
    Arguments:
    active -- If True, returns the current index of the right half-
              maximal amplitude within the active channel. Only 
              implemented for the active channel at this time. Will return 
              a negative value and show an error message if 
              active == False.
              
    Returns:
    The zero-based index of the right half-maximal amplitude in units of 
    sampling points. Interpolates between sampling points. Returns a 
    negative value upon failure.
    """
  return _stf.t50right_index(active)
t50right_index = _stf.t50right_index

def get_fit_start(is_time = False):
  """
    get_fit_start(is_time = False) -> double
    get_fit_start() -> double

    Returns the zero-based index or the time point
    of the fit start cursor.

    Arguments:
    is_time -- If False (default), returns the zero-based index. If True,
               returns the time from the beginning of the trace to the
               cursor position.          

    """
  return _stf.get_fit_start(is_time)
get_fit_start = _stf.get_fit_start

def get_fit_end(is_time = False):
  """
    get_fit_end(is_time = False) -> double
    get_fit_end() -> double

    Returns the zero-based index or the time point
    of the fit end cursor.

    Arguments:
    is_time -- If False (default), returns the zero-based index. If True,
               returns the time from the beginning of the trace to the
               cursor position.          

    """
  return _stf.get_fit_end(is_time)
get_fit_end = _stf.get_fit_end

def set_fit_start(*args):
  """
    set_fit_start(pos, is_time = False) -> bool
    set_fit_start(pos) -> bool

    Sets the fit start cursor to a new position.

    Arguments:
    pos --     The new cursor position, either in units of sampling points
               if is_time == False (default) or in units of time if
               is_time == True.
    is_time -- see above.

    Returns:
    False upon failure (such as out-of-range).
    """
  return _stf.set_fit_start(*args)
set_fit_start = _stf.set_fit_start

def set_fit_end(*args):
  """
    set_fit_end(pos, is_time = False) -> bool
    set_fit_end(pos) -> bool

    Sets the fit end cursor to a new position.

    Arguments:
    pos --     The new cursor position, either in units of sampling points
               if is_time == False (default) or in units of time if
               is_time == True.
    is_time -- see above.

    Returns:
    False upon failure (such as out-of-range).
    """
  return _stf.set_fit_end(*args)
set_fit_end = _stf.set_fit_end

def get_peak_start(is_time = False):
  """
    get_peak_start(is_time = False) -> double
    get_peak_start() -> double

    Returns the zero-based index or the time point
    of the peak start cursor.

    Arguments:
    is_time -- If False (default), returns the zero-based index. If True,
               returns the time from the beginning of the trace to the
               cursor position.          

    """
  return _stf.get_peak_start(is_time)
get_peak_start = _stf.get_peak_start

def get_peak_end(is_time = False):
  """
    get_peak_end(is_time = False) -> double
    get_peak_end() -> double

    Returns the zero-based index or the time point
    of the peak end cursor.

    Arguments:
    is_time -- If False (default), returns the zero-based index. If True,
               returns the time from the beginning of the trace to the
               cursor position.          

    """
  return _stf.get_peak_end(is_time)
get_peak_end = _stf.get_peak_end

def set_peak_start(*args):
  """
    set_peak_start(pos, is_time = False) -> bool
    set_peak_start(pos) -> bool

    Sets the peak start cursor to a new position.
    This will NOT update the peak calculation. You have to either call 
    measure() or hit enter in the main window to achieve that.

    Arguments:
    pos --     The new cursor position, either in units of sampling points
               if is_time == False (default) or in units of time if
               is_time == True.
    is_time -- see above.

    Returns:
    False upon failure (such as out-of-range).
    """
  return _stf.set_peak_start(*args)
set_peak_start = _stf.set_peak_start

def set_peak_end(*args):
  """
    set_peak_end(pos, is_time = False) -> bool
    set_peak_end(pos) -> bool

    Sets the peak end cursor to a new position.
    This will NOT update the peak calculation. You have to either call 
    measure() or hit enter in the main window to achieve that.

    Arguments:
    pos --     The new cursor position, either in units of sampling points
               if is_time == False (default) or in units of time if
               is_time == True.
    is_time -- see above.

    Returns:
    False upon failure (such as out-of-range).
    """
  return _stf.set_peak_end(*args)
set_peak_end = _stf.set_peak_end

def get_base_start(is_time = False):
  """
    get_base_start(is_time = False) -> double
    get_base_start() -> double

    Returns the zero-based index or the time point
    of the base start cursor.

    Arguments:
    is_time -- If False (default), returns the zero-based index. If True,
               returns the time from the beginning of the trace to the
               cursor position.
    """
  return _stf.get_base_start(is_time)
get_base_start = _stf.get_base_start

def get_base_end(is_time = False):
  """
    get_base_end(is_time = False) -> double
    get_base_end() -> double

    Returns the zero-based index or the time point
    of the base end cursor.

    Arguments:
    is_time -- If False (default), returns the zero-based index. If True,
               returns the time from the beginning of the trace to the
               cursor position.
    """
  return _stf.get_base_end(is_time)
get_base_end = _stf.get_base_end

def set_base_start(*args):
  """
    set_base_start(pos, is_time = False) -> bool
    set_base_start(pos) -> bool

    Sets the base start cursor to a new position.
    This will NOT update the baseline calculation. You have to either call 
    measure() or hit enter in the main window to achieve that.

    Arguments:
    pos --     The new cursor position, either in units of sampling points
               if is_time == False (default) or in units of time if
               is_time == True.
    is_time -- see above.

    Returns:
    False upon failure (such as out-of-range).
    """
  return _stf.set_base_start(*args)
set_base_start = _stf.set_base_start

def set_base_end(*args):
  """
    set_base_end(pos, is_time = False) -> bool
    set_base_end(pos) -> bool

    Sets the base end cursor to a new position.
    This will NOT update the baseline calculation. You have to either call 
    measure() or hit enter in the main window to achieve that.

    Arguments:
    pos --     The new cursor position, either in units of sampling points
               if is_time == False (default) or in units of time if
               is_time == True.
    is_time -- see above.

    Returns:
    False upon failure (such as out-of-range).
    """
  return _stf.set_base_end(*args)
set_base_end = _stf.set_base_end

def get_channel_index(active = True):
  """
    get_channel_index(active = True) -> int
    get_channel_index() -> int

    Returns the ZERO-BASED index of the specified
    channel.

    Arguments:

    active -- If True, returns the index of the active (black) channel.
    If False, returns the index of the inactive (red) channel.

    """
  return _stf.get_channel_index(active)
get_channel_index = _stf.get_channel_index

def get_channel_name(*args):
  """
    get_channel_name(index = -1) -> char
    get_channel_name() -> char

    Returns the name of the channel with the 
    specified index.

    Arguments:

    index -- The zero-based index of the channel of interest. If < 0, the
          	 name of the active channel will be returned.

    Returns:
    the name of the channel with the specified index.
    """
  return _stf.get_channel_name(*args)
get_channel_name = _stf.get_channel_name

def set_channel_name(*args):
  """
    set_channel_name(name, index = -1) -> bool
    set_channel_name(name) -> bool

    Sets the name of the channel with the 
    specified index.

    Arguments:
    name  -- The new name of the channel.
    index -- The zero-based index of the channel of interest. If < 0, the
          	 active channel will be used.

    Returns:
    True upon success.
    """
  return _stf.set_channel_name(*args)
set_channel_name = _stf.set_channel_name

def get_trace_name(*args):
  """
    get_trace_name(trace = -1, channel = -1) -> char
    get_trace_name(trace = -1) -> char
    get_trace_name() -> char

    Returns the name of the trace with the 
    specified index.

    Arguments:
    trace -- The zero-based index of the trace of interest. If < 0, the
          	   name of the active trace will be returned.
    channel -- The zero-based index of the channel of interest. If < 0, the
          	   active channel will be used.

    Returns:
    the name of the trace with the specified index.
    """
  return _stf.get_trace_name(*args)
get_trace_name = _stf.get_trace_name

def align_selected(*args):
  """
    align_selected(alignment, active = False)
    align_selected(alignment)

    Aligns the selected traces to the index that is 
    returned by the alignment function, and then creates a new window 
    showing the aligned traces.
    Arguments:       
    alignment -- The alignment function to be used. Accepts any function
                 returning a valid index within a trace. These are some
                 predefined possibilities:
                 maxrise_index (default; maximal slope during rising phase)
                 peak_index (Peak of an event)
                 foot_index (Beginning of an event)
                 t50left_index 
                 t50right_index (Left/right half-maximal amplitude)
    active --    If True, the alignment function will be applied to
                 the active channel. If False (default), it will be applied
                 to the inactive channel.
    zeropad --   Not yet implemented:
                 If True, missing parts at the beginning or end of a trace 
                 will be padded with zeros after the alignment. If False
                 (default), traces will be cropped so that all traces have
                 equal sizes.

    """
  return _stf.align_selected(*args)
align_selected = _stf.align_selected

