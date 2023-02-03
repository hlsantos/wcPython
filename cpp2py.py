#***********************************************************************
# (c) Copyright 1998-2023 Santronics Software, Inc. All Rights Reserved.
#***********************************************************************
#
# File Name : c:\local\sandbox\OpenAI\cpp2py.py
# Subsystem : Wildcat! Python API (wcPAPI)
# Date      : 01/29/23 10:51 am
# Version   : 1.0
# Author    : SSI
# About     : convert wcSDK headers to python ctypes
#
# Revision History:
# Version  Date      Author  Comments
# -------  --------  ------  -------------------------------------------
# 1.1      02/02/23  HLS     fixed PropertyStruct to handle utf-8
#***********************************************************************

import os
import sys
import re
import ctypes
import keyboard
import msvcrt
from datetime import datetime, date, time

debug1 = True
debug2 = True
debug3 = False
debug4 = True

debug1 = 0
debug2 = 0
debug3 = 0
debug4 = 0

dll_mapping = {"wcsrv":    ("wcsrv2.dll",  "wcsrv2x64.dll"),
               "wcsmw":    ("wcsmw.dll",   "wcsmw64.dll"),
               "wcsgate":  ("wcsgate.dll", "wcsgate64.dll"),
              }

"""
codeset = "UTF-8"
#errors  = "strict"
codeset = "ISO-8859-1"
errors  = "ignore"
errors  = "replace"  # try this to avoid exceptions

prop_struct  = "\n"
prop_struct  += "class PropertyStruct(ctypes.Structure):\n"
gettersetter = ""
gettersetter += "    def __getattribute__(self, name):\n"
gettersetter += "        val = object.__getattribute__(self, name)\n"
gettersetter += "        if isinstance(val, bytes):\n"
gettersetter += f"            return val.decode('{codeset}','{errors}')\n"
gettersetter += "        return val\n"
gettersetter += "    def __setattr__(self, name, value):\n"
gettersetter += "        if isinstance(value, str):\n"
gettersetter += f"            value = value.encode('{codeset}','{errors}')\n"
gettersetter += "        object.__setattr__(self, name, value)\n\n"
prop_struct  += gettersetter
"""

prop_struct = '''
class PropertyStruct(ctypes.Structure):
    def __getattribute__(self, name):
        val = object.__getattribute__(self, name)
        if isinstance(val, bytes):
            try:
              _val = val.decode('ISO-8859-1','ignore')
            except:
                try:
                  _val = val.decode('UTF-8','ignore')
                except:
                  _val = hex(val)
            return _val
        return val
    def __setattr__(self, name, value):
        if isinstance(value, str):
            value = value.encode('UTF-8','ignore')
        object.__setattr__(self, name, value)

'''



def structures_to_ctypes(input_file, output_file, do_extra_set = []):
    type_mapping = {"DWORD":      "DWORD",
                    "BOOL":       "BOOL",
                    "FILETIME":   "FILETIME",
                    "WORD":       "WORD",
                    "BYTE":       "BYTE",
                    "char":       "ctypes.c_char",
                    "long":       "LONG",
                    "ULONG":      "DWORD",
                    "TMakewild":  "TMakewild",
                    "TConfDesc":  "TConfDesc",
                    "TFileArea":  "TFileArea",
                    }

    print(f"- structures_to_ctypes: in: {input_file} out: {output_file} extra: {do_extra_set}")

    # Open the C header file
    with open(input_file, "r") as f: header_file_contents = f.read()

    # Remove C-based comments
    header_file_contents = re.sub(r"/\*.*?\*/", "", header_file_contents, flags=re.DOTALL)
    header_file_contents = re.sub(r"//.*", "", header_file_contents)

    # Find all struct definitions
    struct_defs = re.findall(r"typedef\s+(enum|struct\s+tag[\w]+)\s*\{([^}]+)\}\s*(\w+);", header_file_contents)

    # Create the output file
    with open(output_file, "w") as out_file:
        out_file.write(f"# Created by cpp2py on {datetime.now()}"+"\n")
        out_file.write("\n")
        out_file.write("import ctypes\n")
        out_file.write("from ctypes import wintypes\n")
        out_file.write("from ctypes.wintypes import *\n")
        out_file.write("from enum import IntEnum\n")
        out_file.write("from wcpapi.wctype_h import *\n")
        out_file.write("from wcpapi.wctype_constants_h import *\n")
        out_file.write("\n")

        # add PropertyStructure base class for ctypes.structure for structures with c strings.
        out_file.write(prop_struct)

        if "ExtraHeaders" in do_extra_set:
            func_proto = ""
            func_proto += "class TSecurityName(PropertyStruct):\n"
            func_proto += "    _fields_ = [('Name', ctypes.c_char*SIZE_SECURITY_NAME)]\n"
            func_proto += "    def __str__(self):\n"
            func_proto += "        return self.Name\n"
            func_proto += "\n"
            func_proto += "class TComputerName(PropertyStruct):\n"
            func_proto += "    _fields_ = [('Name', ctypes.c_char*SIZE_COMPUTER_NAME)]\n"
            func_proto += "    def __str__(self):\n"
            func_proto += "        return self.Name\n"
            func_proto += "\n"
            func_proto += "\n"
            func_proto += "class TShortFileName(PropertyStruct):\n"
            func_proto += "    _fields_ = [('Name', ctypes.c_char*SIZE_SHORT_FILE_NAME)]\n"
            func_proto += "    def __str__(self):\n"
            func_proto += "        return self.Name\n"
            func_proto += "\n"
            func_proto += "class TDoorName(PropertyStruct):\n"
            func_proto += "    _fields_ = [('Name', ctypes.c_char*SIZE_DOOR_NAME)]\n"
            func_proto += "    def __str__(self):\n"
            func_proto += "        return self.Name\n"
            func_proto += "\n"
            out_file.write(func_proto)

            func_proto = ""
            func_proto += "class CString(ctypes.c_char_p):\n"
            func_proto += "    def __init__(self, string=b''):\n"
            func_proto += "        super().__init__(string)\n"
            func_proto += "    def from_param(self):\n"
            func_proto += "        return self.encode()\n"
            func_proto += "\n"
            out_file.write(func_proto)


        # Convert each struct definition into a ctypes structure
        for struct_def in struct_defs:

            struct_type   = struct_def[0]
            struct_name   = struct_def[2]
            struct_fields = struct_def[1]
            addGetSet     = False

            if struct_type.startswith("struct"):
                if debug1 or debug2:
                   bShow = False
                   print("***S ",struct_name)
            elif struct_type == "enum":
                if debug1 or debug2:
                    bShow = False
                    print("***E ",struct_name)
                    print(">>>> ",struct_fields)

            #print(struct_fields)

            fields = []
            sre = r"(\w+)\s+(\w+)(\[([^;]+)?\])?;"
            for field in re.finditer(sre, struct_fields):

                type = type_mapping.get(field.group(1), "Unknown")

                if debug1:
                    bShow = debug2
                    if type == "Unknown": bShow = True
                    if bShow:
                        print(f"|{str(type):25}", end="")
                        print(f"|{field.group(1):15}", end="")
                        print(f"|{field.group(2):25}", end="")
                        print(f"|{field.group(3)}|", end="")
                        print("")

                if type == "Unknown":
                    # exclude some keywords
                    if field.group(1) == "ifdef": continue;

                    # using the original type for unknown and create a new structure for it:
                    type = type_mapping.get(field.group(2), field.group(1))

                    out_file.write(f"# auto-created for missing type {field.group(1)}\n")
                    snew = f"class {field.group(1)}:\n"
                    snew += "    _fields_ = []\n"
                    out_file.write(snew)
                    out_file.write("\n")
                    type_mapping[struct_name] = f'{struct_name}'

                if field.group(3) is None:
                    fields.append((field.group(2), type))
                else:
                    size = field.group(3).lstrip("[").rstrip("]").replace("][","*")
                    size1 = size
                    newClassName = type

                    if type == "ctypes.c_char":
                       newClassName = "ctypes.c_char"
                       addGetSet = True

                    if "][" in field.group(3):
                        # 2D array
                        size1,size2 = size.split("*")
                        newClassName = f"T{field.group(2).capitalize()}Item"
                        s  = f"class {newClassName}({addGetSet and 'PropertyStruct' or 'ctypes.Structure'}):\n"
                        s += f"    _fields_ = [('Item', {type}*{size2})]\n"
                        out_file.write(s)
                        out_file.write("\n")

                    fields.append((field.group(2), newClassName+"*"+size1))

            if debug3:
               if bShow: msvcrt.getch()

            class_definition = ""
            if struct_type.startswith("struct"):
                class_definition += f"class {struct_name}({addGetSet and 'PropertyStruct' or 'ctypes.Structure'}):\n"
                class_definition +=  "    _fields_ = [\n"
                for field in fields:
                    class_definition += f"        ('{field[0]}', {field[1]}{', ' + str(field[2]) if len(field) == 3 else ''}),\n"
                class_definition += "    ]\n"

            elif struct_type == "enum":
                enum_values = [val.strip() for val in struct_fields.split(',')]

                class_definition = f"class tag{struct_name}(IntEnum):\n"
                value = 0
                for val in enum_values:
                    val = val.strip()
                    if "=" in val:
                        val_name, val_value = val.split("=")
                        class_definition += f"   {val_name.strip():20} = {val_value.strip()}\n"
                    else:
                        value +=1
                        class_definition += f"   {val.strip():20} = {value}\n"
                class_definition += f"{struct_name} = DWORD\n"

            out_file.write(class_definition)
            out_file.write("\n")

            type_mapping[struct_name] = f'{struct_name}'

        if debug4:
           print("** final type_mapping")
           for m,v in type_mapping.items():
              print(f"{m:25}",v)

#---------------------------------------------------------------------

def functions_to_ctypes(header_file, output_file, dll_key):
    type_map = {
        'BOOL':             'ctypes.wintypes.BOOL',
        'DWORD':            'ctypes.wintypes.DWORD',
        'HANDLE':           'ctypes.wintypes.HANDLE',
        'HWND':             'ctypes.wintypes.HWND',
        'LONG':             'ctypes.wintypes.LONG',
        'int':              'ctypes.c_int',
        'long':             'ctypes.c_long',
        'char':             'ctypes.c_char',
        'char*':            'ctypes.c_char_p',
        'char *':           'ctypes.c_char_p',
        'BYTE':             'ctypes.c_byte',
        'BYTE*':            'ctypes.c_char_p',
        'VOID':             'ctypes.c_void_p',   # ??
        'void':             'ctypes.c_void_p',   # ??
        'void*':            'ctypes.c_void_p',
        'LPDWORD':          'ctypes.c_ulong',
        'LPCVOID':          'ctypes.c_void_p',
        'LPVOID':           'ctypes.c_void_p',
        'LPTSTR':           'ctypes.c_char_p',
        'LPCTSTR':          'ctypes.c_char_p',
        'LPCWSTR':          'ctypes.c_wchar_p',
        'unsigned __int64': 'ctypes.c_ulonglong',
        'unsigned __int64*':'ctypes.c_ulonglong',
        'TWildcatCallback': 'ctypes.c_void_p',
        'WCHANDLE':         'ctypes.wintypes.HANDLE',
    }

    print(f"- function_to_ctypes: in: {input_file} out: {output_file} dll: {dll_key}")

    pyhead = ""
    pyhead += f"# Auto-Created by cpp2py.py\n"
    pyhead += f"import os\n"
    pyhead += f"from wcpapi.wctype_constants_h import *\n"
    pyhead += f"from wcpapi.wctype_h import *\n"
    if dll_key == "wcsmw":
       pyhead += f"from wcpapi.wctypemw_constants_h import *\n"
       pyhead += f"from wcpapi.wctypemw_h import *\n"
    if dll_key == "wcsgate":
       pyhead += f"from wcpapi.wcgtype_constants_h import *\n"
       pyhead += f"from wcpapi.wcgtype_h import *\n"
    pyhead += f"from wcpapi.__init__ import *\n"
    pyhead += f"\n"
    pyhead += f"{dll_key}_dll = initialize_{dll_key}_dll()\n"
    pyhead += f"\n"
    if dll_key == "wcsrv":
       pyhead += f"class SYSTEMTIME(ctypes.Structure):\n"
       pyhead += f"    _fields_ = [('wYear', WORD),\n"
       pyhead += f"                ('wMonth', WORD),\n"
       pyhead += f"                ('wDayOfWeek', WORD),\n"
       pyhead += f"                ('wDay', WORD),\n"
       pyhead += f"                ('wHour', WORD),\n"
       pyhead += f"                ('wMinute', WORD),\n"
       pyhead += f"                ('wSecond', WORD),\n"
       pyhead += f"                ('wMilliseconds', WORD)]\n"
       pyhead += f"\n"

    with open(header_file, 'r') as f:
        with open(output_file, 'w') as outf:

            outf.write(pyhead)

            line = f.readline()
            while line:
                if '//' in line:
                    outf.write("#" + line)
                elif line.strip() == "":
                    outf.write(line)
                elif "APIENTRY" in line:
                    eof = ");" not in line
                    func_line = line
                    while eof:
                        line = f.readline()
                        eof = ");" not in line
                        func_line += line

                    func_line = func_line.strip().replace("  "," ")
                    func_line = func_line.replace("\n","").strip()

                    parts = re.findall(r'(\b\w+\b)\s+(APIENTRY)\s+(\b\w+\b)\s*\(([^\)]*)\);', func_line)

                    if parts:
                        ret_type, _, func_name, args = parts[0]

                        debug = func_name in ["SetNodeInfo", "xWcReadFile","WcCreateDirectory","xWcGetGeoIP","xGetWildcatServerInfo","xLoginRadiusUser","xWildcatLoggedIn","xFileSearch"]
                        debug = func_name in ["GetUserVariables"]
                        debug = func_name in ["SetUserProfileSystemTime"]
                        debug = func_name in ["WcLocalCopyToServer"]
                        debug = func_name in ["WildcatServerConnectSpecific"]
                        debug = func_name in ["GetConnectedServer"]
                        debug = func_name in ["GetSecurityProfileNames","GetAccessProfileNames","MwGetSecurityProfileNames", \
                                               "MwGetGroupNames","MwGetComputerConfigNames","MwGetFileVolumeNames","MwGetDoorNames"]
                        # wcsgate
                        #debug = func_name in ["MwFindFirstFile"]
                        #debug = func_name in ["MwFindFirstFile"]
                        debug = 0

                        if debug:
                           print("\n**",func_line)

                        outf.write(f"##{func_line}\n")

                        # start of special cases
                        if func_name in ["GetSecurityProfileNames","GetAccessProfileNames"]:
                            func_proto =""
                            func_proto += f"{func_name} = {dll_key}_dll.{func_name}\n"
                            func_proto += f"{func_name}.argtypes = [ctypes.c_ulong, ctypes.POINTER(TSecurityName)]\n"
                            func_proto += f"{func_name}.restype = ctypes.c_bool\n\n"
                            outf.write(func_proto)
                            if debug: print(func_proto)

                            line = f.readline()
                            if not line: break
                            continue
                        if func_name in ["MwGetGroupNames"]:
                            func_proto =""
                            func_proto += f"{func_name} = {dll_key}_dll.{func_name}\n"
                            func_proto += f"{func_name}.argtypes = [ctypes.POINTER(TSecurityName)]\n"
                            func_proto += f"{func_name}.restype = ctypes.c_bool\n\n"
                            outf.write(func_proto)
                            if debug: print(func_proto)

                            line = f.readline()
                            if not line: break
                            continue
                        if func_name in ["MwGetSecurityProfileNames"]:
                            func_proto =""
                            func_proto += f"{func_name} = {dll_key}_dll.{func_name}\n"
                            func_proto += f"{func_name}.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(TSecurityName)]\n"
                            func_proto += f"{func_name}.restype = ctypes.c_bool\n\n"
                            outf.write(func_proto)
                            if debug: print(func_proto)

                            line = f.readline()
                            if not line: break
                            continue
                        if func_name in ["MwGetComputerConfigNames"]:
                            func_proto =""
                            func_proto += f"{func_name} = {dll_key}_dll.{func_name}\n"
                            func_proto += f"{func_name}.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(TComputerName)]\n"
                            func_proto += f"{func_name}.restype = ctypes.c_bool\n\n"
                            outf.write(func_proto)
                            if debug: print(func_proto)

                            line = f.readline()
                            if not line: break
                            continue
                        if func_name in ["MwGetFileVolumeNames"]:
                            func_proto =""
                            func_proto += f"{func_name} = {dll_key}_dll.{func_name}\n"
                            func_proto += f"{func_name}.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(TShortFileName)]\n"
                            func_proto += f"{func_name}.restype = ctypes.c_bool\n\n"
                            outf.write(func_proto)
                            if debug: print(func_proto)

                            line = f.readline()
                            if not line: break
                            continue
                        if func_name in ["MwGetDoorNames"]:
                            func_proto =""
                            func_proto += f"{func_name} = {dll_key}_dll.{func_name}\n"
                            func_proto += f"{func_name}.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(TDoorName)]\n"
                            func_proto += f"{func_name}.restype = ctypes.c_bool\n\n"
                            outf.write(func_proto)
                            if debug: print(func_proto)

                            line = f.readline()
                            if not line: break
                            continue
                        # end of special cases


                        args = args.replace("\n","").strip()

                        #if debug: print(f"args:",args)

                        ret_type = type_map.get(ret_type, ret_type)
                        if args:
                            arg_list = args.split(',')
                            arg_list = [a.strip() for a in arg_list]
                            #arg_list = [a for a in arg_list if a]

                            #if debug:print(f"arg_list: ",arg_list)

                            args = []
                            for i, arg in enumerate(arg_list):

                                #if debug:print(i,arg)

                                arg_parts = arg.split(",")

                                if debug:print(i,arg_parts)

                                isConst   = 0
                                isPointer = 0

                                for part in arg_parts:
                                    atype,aname = part.rsplit(" ",1)
                                    isConst = atype.startswith("const ");
                                    if isConst:
                                       atype = atype.lstrip("const").strip()


                                    if aname.startswith("*"):
                                        isPointer = True;
                                        aname = aname.lstrip("*")
                                        atype = atype+"*"
                                    elif not isConst and aname.startswith("&"):
                                        isPointer = True;
                                        aname =  aname.lstrip("&")
                                        atype = atype+"*"
                                    elif aname.endswith("[]"):
                                        isPointer = True;
                                        aname = aname.rstrip("[]")
                                        atype = atype+"*"

                                    if atype.startswith("LPC"):
                                        isPointer = True
                                        isConst   = True
                                        #atype = atype.lstrip("LPC")

                                    if atype.startswith("LP"):
                                        isPointer = True
                                        #atype = atype.lstrip("LP")

                                    if debug: print(f"  |{atype.strip()}|{aname}|",isConst, isPointer)

                                    arg_type = type_map.get(atype.strip(), "unknown")

                                    if debug:
                                       print(f"  map atype |{atype}|{arg_type}|")

                                    if arg_type == "unknown" and atype.endswith("*"):
                                       arg_type = atype.rstrip("*")

                                    if arg_type == "unknown" and aname.startswith("&"):
                                       isPointer = True
                                       arg_type = atype

                                    if isConst and isPointer:
                                       isPointer = False

                                    if arg_type == "ctypes.c_char_p":
                                       isPointer = False
                                       if isConst: arg_type = "CString"

                                    arg_name = aname
                                    if isPointer: arg_type = f"ctypes.POINTER({arg_type})"
                                    args.append((arg_type, arg_name))


                            if debug:print(" ",args)

                            func_proto  = ""
                            func_proto += f"{func_name} = {dll_key}_dll.{func_name}\n"
                            func_proto += f'{func_name}.argtypes = [{", ".join([arg_type for arg_type, arg_name in args])}]\n'
                            func_proto += f"{func_name}.restype = {ret_type}\n\n"

                            if debug:print(func_proto)

                            outf.write(func_proto)
                        else:
                            func_proto  = ""
                            func_proto += f"{func_name} = {dll_key}_dll.{func_name}\n";
                            func_proto += f"{func_name}.restype = {ret_type}\n\n"
                            outf.write(func_proto)

                line = f.readline()
                if not line:
                    break

#------------------------------------------------------
# main
#------------------------------------------------------
if __name__ == "__main__":
    print("** running cpp2py.py")

    ## STRUCTURES & FUNCTIONS

    if 1:
       print(f"# Create base wcPython structures and functions")
       input_file  = "include/wctype.h"
       output_file = "wcpapi/wctype_h.py"
       structures_to_ctypes(input_file, output_file, ["ExtraHeaders"])

       input_file  = "include/wcserver.h"
       output_file = "wcpapi/wcserver_h.py"
       functions_to_ctypes(input_file, output_file, "wcsrv")

    if 1:
       print(f"# Create makewild wcPython structures and functions")
       input_file  = "include/wctypemw.h"
       output_file = "wcpapi/wctypemw_h.py"
       structures_to_ctypes(input_file, output_file)

       input_file  = "include/wcsmw.h"
       output_file = "wcpapi/wcsmw_h.py"
       functions_to_ctypes(input_file, output_file, "wcsmw")

    if 1:
       print(f"# Create mail gateway wcPython structures and functions")
       input_file  = "include/wcgtype.h"
       output_file = "wcpapi/wcgtype_h.py"
       structures_to_ctypes(input_file, output_file)

       input_file  = "include/wcsgate.h"
       output_file = "wcpapi/wcsgate_h.py"
       functions_to_ctypes(input_file, output_file, "wcsgate")


    #print("done")
    #msvcrt.getch()


