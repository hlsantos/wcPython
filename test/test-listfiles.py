# Example of using wcPython API (wcPAPI)
# List Files

import os
import wcpapi
from wcpapi import wcserver_h, wcsmw_h
from wcpapi.wcserver_h import *
from wcpapi.wcserror_h import *
from wcpapi.wcsmw_h import *

print("* List Files by Area/Name")

if not WildcatServerConnect(0)):
   exit(1)
if not WildcatServerCreateContext():
   print(f"Error Creating Context with WildcatServerCreateContext()")
   exit(1)
if not LoginSystem():
   print(f"Error LoginSystem()")
   exit(1)
 
frec = TFileRecord()
tid  =  DWORD()

# Since frec is cleared and tid is cleared (all zero), the first record 
# will be returned with GetNextFileRec().  If you set the frec.Area, then
# that is the conference it will begin.
while GetNextFileRec(FileAreaNameKey, frec, tid):
   print("* Area: {} | {} | {}".format(frec.Area, frec.SFName.ljust(15), frec.Name))

LogoutUser()
