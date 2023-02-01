# wcPAPI Wildcat! package
import os
import sys
import ctypes

DLL_SRV_LOADED = False
DLL_SMW_LOADED = False
DLL_SGATE_LOADED = False

def find_dll(dll_name):
    MAX_PATH = 260  # max length of a path in Windows
    buf = ctypes.create_unicode_buffer(MAX_PATH)
    size = ctypes.windll.kernel32.SearchPathW(None, dll_name, None, MAX_PATH, buf, None)
    if size == 0:
        raise FileNotFoundError("Could not find the DLL file: {0:s}".format(dll_name))
    return buf.value

def initialize_wcsrv_dll():
    wildcat_dll = None
    global DLL_SRV_LOADED
    if not DLL_SRV_LOADED:
       DLL_BASE_NAME   = "wcsrv2.dll"
       if sys.maxsize > 2**32-1:
          DLL_BASE_NAME   = "wcsrv2x64.dll"
       WildcatDll = find_dll(DLL_BASE_NAME)
       if not os.path.exists(WildcatDll):
          print("Error",ctypes.GetLastError()," loading [{0:s}]".format(WildcatDll))
          raise FileNotFoundError("Could not find the DLL file: {0:s}".format(DLL_BASE_NAME))
       wildcat_dll = ctypes.WinDLL(WildcatDll)
       DLL_SRV_LOADED = True
    return wildcat_dll

def initialize_wcsmw_dll():
    wildcat_dll = None
    global DLL_SMW_LOADED
    if not DLL_SMW_LOADED:
       DLL_BASE_NAME   = "wcsmw.dll"
       if sys.maxsize > 2**32-1:
          DLL_BASE_NAME   = "wcsmw64.dll"
       WildcatDll = find_dll(DLL_BASE_NAME)
       if not os.path.exists(WildcatDll):
          print("Error",ctypes.GetLastError()," loading [{0:s}]".format(WildcatDll))
          raise FileNotFoundError("Could not find the DLL file: {0:s}".format(DLL_BASE_NAME))
       wildcat_dll = ctypes.WinDLL(WildcatDll)
       DLL_SMW_LOADED = True
    return wildcat_dll

def initialize_wcsgate_dll():
    wildcat_dll = None
    global DLL_SGATE_LOADED
    if not DLL_SGATE_LOADED:
       DLL_BASE_NAME   = "wcsgate.dll"
       if sys.maxsize > 2**32-1:
          DLL_BASE_NAME   = "wcsgate64.dll"
       WildcatDll = find_dll(DLL_BASE_NAME)
       if not os.path.exists(WildcatDll):
          print("Error",ctypes.GetLastError()," loading [{0:s}]".format(WildcatDll))
          raise FileNotFoundError("Could not find the DLL file: {0:s}".format(DLL_BASE_NAME))
       wildcat_dll = ctypes.WinDLL(WildcatDll)
       DLL_SGATE_LOADED = True
    return wildcat_dll

