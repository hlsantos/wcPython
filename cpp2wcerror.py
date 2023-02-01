#***********************************************************************
# (c) Copyright 1998-2023 Santronics Software, Inc. All Rights Reserved.
#***********************************************************************
#
# File Name : c:\local\sandbox\OpenAI\cpp2wcerror.py
# Subsystem : Wildcat! Python API (wcPAPI)
# Date      : 01/25/23 10:07 am
# Version   : 8.0.454.13
# Author    : SSI
# About     :
#
# Revision History:
# Build    Date      Author  Comments
# -----    --------  ------  -------------------------------------------
#***********************************************************************

from datetime import datetime, date, time

def current_method(in_file, out_file):

    # for collecting const dword lines
    error_lines = ""

    # Create a dictionary to map error number to its name and value
    # { error_number : ("error_name, error_literal), ... }

    error_map   = {}

    with open(in_file, "r") as file:
        nLines = 0
        for line in file:
            if line.startswith("const DWORD"):
                # first collect const lines to create python constants.
                line   = line.lstrip("const").strip()
                line   = line.lstrip("DWORD").strip()
                line   = line.replace("//","#")
                line   = line.replace("/*","#").replace("*/","")
                error_lines += line.replace(";","")+'\n'
                #print(line)

                # now lets create it parts

                parts  = line.split(";")
                line   = parts[0]
                comment = ""
                if len(parts) == 2: comment = parts[1];
                #print(line,comment)

                parts  = line.split(" ")
                parts = [a for a in parts if a]
                #print(f"{len(parts):3}",parts,comment)
                #print(f"{len(parts):3}",line,comment)


                #error_number = f"{parts[2]} {parts[3]}  {parts[4]}"
                error_name   = parts[0]
                error_number = f"{parts[2]}"
                if len(parts) > 3: error_number += f"{parts[3]}  {parts[4]}"
                #print(f"{len(parts):3}-{error_name:35} {error_number}")

                if error_name == "WC_STATUS_BASE":  error_number = "WC_STATUS_BASE"
                elif error_name == "WC_SUCCESS":    error_number = "WC_SUCCESS"

                error_literal   = error_name.replace("_"," ").lstrip("WC").strip().title()

                #error_map[error_name] = (error_number, '"'+error_literal+'"')
                error_map[error_name] = (error_name, '"'+error_literal+'"')


    # Translate the constants to Python
    with open(out_file, "w") as file:
        file.write(f"# Auto-created by cpp2wcerror.py on {datetime.now()}\n")
        file.write("\n")
        file.write("# Wildcat! error constants start with the WC_STATUS_BASE\n")
        file.write("\n")
        file.write(error_lines)
        file.write("\n# Error Map\n\n")
        file.write("wcerror_map = {\n")
        for error_number, (error_name, error_literal) in error_map.items():
            #file.write(f"\t{error_number:35}: ({error_name:35}, {error_literal}),\n")
            foo = '"'+error_number+'"'
            file.write(f"\t{error_number:35}: ({foo:35}, {error_literal}),\n")
        file.write("}\n")

        get_def = '''
def GetWildcatErrorStr(error_number):
    error_name, error_literal = wcerror_map.get(error_number, ("Unknown error", "Error not found in wcerror_map"))
    return f"{error_name} (0x{error_number:X}) - {error_literal}"

#if __name__ == '__main__':
#
#    print(GetWildcatErrorStr(WC_ACCOUNT_NOT_VALIDATED))
'''
        file.write(get_def)


if __name__ == '__main__':
   print("** cpp2wcerror.py v0.1")

   in_file   = "c:/local/wc8/include/wcserror.h"
   out_file  = "wcPapi/wcserror_h.py"
   current_method(in_file, out_file)

##input()
##exit(1)



