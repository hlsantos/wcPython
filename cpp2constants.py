#***********************************************************************
# (c) Copyright 1998-2023 Santronics Software, Inc. All Rights Reserved.
#***********************************************************************
#
# File Name : c:\local\sandbox\OpenAI\cpp2constants.py
# Subsystem : Wildcat! Python API (wcPAPI)
# Date      : 01/29/23 10:51 am
# Version   : 8.0.454.13
# Author    : SSI
# About     :
#
# Revision History:
# Build    Date      Author  Comments
# -----    --------  ------  -------------------------------------------
#***********************************************************************

from datetime import datetime, date, time
from io import StringIO

def get_print_output(*args, **kwargs):
    output = StringIO()
    print(*args, file=output, **kwargs)
    return output.getvalue()

DEBUG = 0
def PRINT(*args, **kwargs):
    s = get_print_output(*args,**kwargs)
    if DEBUG: print(f"{s}", end="")

def split_string(string):
    # split the string on spaces, brackets, semicolons and commas
    split_list = re.findall(r'[^{};,]+|[{};,]', string)
    result = []
    skip_until = None
    for item in split_list:
        #print(f"split_string item: {item}")
        if skip_until:
            if item == skip_until:
                skip_until = None
            continue
        if item == '/*':
            skip_until = '*/'
        elif item == ',' and not skip_until:
            result.extend([item, ''])
        else:
            result.append(item)
    return result


def extract_items_and_name(s):
    PRINT("** extract_items_and_name()")
    PRINT(f"s:|{s}|")

    if not '\n' in s and (all(word in s for word in ["typedef", "enum", "{", "}", ";"])):
        PRINT("# one line declaration")
        item_strings = split_string(s)
        for i, item in enumerate(item_strings):
            if "/*" in item:
                item_strings[i] = item.replace("/*","#").replace("*/","")
    else:
        s = s.replace("{","{\n")
        s = s.replace("}","}\n")
        s = s.replace(";",";\n")
        s = s.replace("typedef","typedef\n")
        s = s.replace("enum","enum\n")

        # Split the string by newline characters to separate the items
        item_strings = s.strip().split("\n")

        # Replace '\t' with ' ' to handle tab characters
        item_strings = [item_string.replace("\t", " ") for item_string in item_strings]

        # Replace '\n' with ' ' to handle newline characters and ravel the string
        item_strings = [" ".join(item_string.split()) for item_string in item_strings]

        # Remove the "typedef" prefix
        item_strings = [item_string.replace("typedef", "").strip() for item_string in item_strings]
        # Remove the "enum" prefix
        item_strings = [item_string.replace("enum", "").strip()for item_string in item_strings]

        # extend the list if necessary
        new_item_strings = []
        for item in item_strings:
            if len(item) > 1 and (item.endswith('}') or item.endswith(';')):
                new_item_strings.extend([item[:-1], item[-1]])
            else:
                new_item_strings.append(item)
        item_strings = new_item_strings

    PRINT("**")
    #PRINT(item_strings)
    #PRINT("--")
    enum_name  = ""
    enum_items = []
    left_brace = 0
    right_brace = 0
    done        = 0
    enum_value  = 0
    for i, item in enumerate(item_strings):
        #PRINT(f"item_string{i:2}: |{item}|")
        if item == "": continue
        if item == ",": continue
        if item.startswith("typedef"): continue

        if not left_brace and item == "{": left_brace = 1; continue
        if left_brace and not right_brace and item == "}": right_brace = 1; continue
        if right_brace and item == ";": done = 1; continue
        if right_brace and not done:
           enum_name = item
           continue

        PRINT(f"item_string{i:2}: |{item}|")

        # we should have an enum item here
        eitem    = item.split(",")

        ename    = eitem[0].strip()
        ecomment = eitem[1].strip() if len(eitem)>1 else ""
        evalue   = enum_value

        ename = ename.split("#")
        if len(ename) > 1:
           ecomment = "#"+ename[1]
        ename    = ename[0].strip()

        ename = ename.split("=")
        if len(ename) > 1:
           evalue = int(ename[1].split()[0].strip())
           enum_value = evalue
        ename  = ename[0].strip()

        #PRINT(f"item_string{i:2}: |{item}| eitem: {eitem}")
        enum_items.append((ename,evalue,ecomment.replace("//","#")))
        enum_value += 1


    PRINT("--")
    PRINT(f"enum_name: {enum_name}")
    for i, e in enumerate(enum_items):
        PRINT(f"{i:2}: |{e[0]:20}|{e[1]:10}|{e[2]}")
        #PRINT(f"{i:2}: |{e}|")

    PRINT("**")

    # Return the extracted items and name
    return enum_items, enum_name


def convert_c_to_python(input_file, output_file):
    constants = {}
    enums = {}

    output = ""
    output += f"# Auto-created by cpp2constant.py on {datetime.now()}\n"
    output += f"# input file : {input_file}\n"
    output += f"# output file: {output_file}\n"
    output += "\n"
    output += "from enum import IntEnum\n"
    output += "\n"

    with open(input_file, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("cpp_quote("): i += 1; continue;
            if line.startswith("#"): i += 1; continue;
            if line.startswith("#if"): i += 1; continue;
            if line.startswith("#endif"): i += 1; continue;

            if line.startswith("//!"):
                output += line.replace("//","#") + "\n"
                i += 1;
                continue;

            if line.startswith("//+"):
                output += line.replace("//","#") + "\n"
                i += 1;
                continue;

            if line.startswith("//"):
                i += 1;
                continue;

            if line == "":
                output += "\n"
                i += 1;
                continue;

            if line.startswith("const DWORD") or line.startswith("const int"):
                #PRINT(f"[{line}]")

                if line.startswith("const DWORD"): line = line.replace("const DWORD","").lstrip()
                elif line.startswith("const int"): line = line.replace("const int","").lstrip()

                cp = line.split(";")
                line = cp[0].strip()
                if len(cp) > 1: c = cp[1].strip().replace("//!","!")

                line = line.split("=")
                name = line[0].strip()
                value = line[1].strip()

                constants[name] = value
                output += f"{name:40} = {value}"
                if len(c):
                   output += f" #{c}\n"
                else:
                   output += "\n"

            elif line.startswith("enum"):
                output += "\n"
                line = line.lstrip("enum").lstrip()
                name = ""
                if line.startswith("{"):
                    # no name
                    line = line.lstrip("{").lstrip()
                else:
                    ep = line.split("{")
                    name = ep[0].strip()
                    line = ep[1].strip()

                items = []
                if "};" in line:
                    ep = line.split("};")[0].split(",")
                    for e in ep:
                       items.append(e.strip())
                else:
                    line = line.strip()
                    items = []
                    if len(line): items = [line]
                    i += 1
                    while i < len(lines) and "};" not in lines[i]:
                        items.append(lines[i].strip().rstrip(","))
                        i += 1


                evalue = 0
                for p in items:
                   p = p.split("//")
                   c = ""
                   if len(p)>1: c = p[1].replace("//!","!")
                   e = p[0].split(",")[0]
                   if len(e):
                      ev = e.split("=")
                      e = ev[0]
                      if len(ev) > 1: evalue = int(ev[1])
                      output += f"{e:40} = {evalue}"
                      if len(c):
                         output += f" #{c}\n"
                      else:
                         output += "\n"
                      evalue += 1
                   else:
                      if len(c):
                         output += f"#{c}\n"

                output += "\n"

            elif line.startswith("typedef enum"):

                line = line.lstrip("typedef").lstrip()

                #-----------------------------------------------------
                # this block should be similar in handling "enum {"
                #-----------------------------------------------------
                line = line.lstrip("enum").lstrip()

                PRINT(f"line: [{line.strip()}]")
                name = ""

                if line.startswith("{"):
                    # no name
                    line = line.lstrip("{").lstrip()
                else:
                    ep = line.split("{")
                    name = ep[0].strip()
                    line = ep[1].strip()

                items = []

                if "}" in line:
                    line = line.split("}")[0]
                    name = line[1].strip()
                    ep = line[0].split(",")
                    for e in ep:
                       items.append(e.strip())
                else:
                    line = line.strip()
                    items = []
                    if len(line): items = [line]
                    i += 1

                    elines = []
                    elines = ""
                    while i < len(lines):
                        line = lines[i]
                        if type(elines) == str:
                           elines += line
                        else:
                           elines.append(line)
                        if ";" in line: break;
                        i += 1

                    items, name = extract_items_and_name("typedef enum {"+elines)

                output += f"class {name}(IntEnum):\n"
                for ename,evalue,ecomment in items:
                    output += f"\t{ename:40} = {evalue}"
                    if len(ecomment): output += f" #{ecomment}"
                    output += "\n"
                output += "\n"
                #-----------------------------------------------------
                #input()

            ##
            i += 1


    # clean up string and write output
    if 1:
        while "\n\n\n" in output:
           output = output.replace("\n\n\n", "\n\n")
        with open(output_file, 'w') as outf:
           outf.write(output)


if __name__ == "__main__":

    in_file  = "include\\wctypemw.h"
    out_file = "wcpapi\\wctypemw_constants_h.py"
    convert_c_to_python(in_file, out_file)

    in_file  = "include\\wcgtype.h"
    out_file = "wcpapi\\wcgtype_constants_h.py"
    convert_c_to_python(in_file, out_file)

    in_file  = "include\\wctype.h"
    out_file = "wcpapi\\wctype_constants_h.py"
    convert_c_to_python(in_file, out_file)




