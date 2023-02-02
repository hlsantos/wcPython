import os
import wcpapi
from wcpapi import wcserver_h, wcsmw_h
from wcpapi.wcserver_h import *
from wcpapi.wcserror_h import *
from wcpapi.wcsmw_h import *

print("* List Files by Area/Name")

WildcatServerConnect(0)
WildcatServerCreateContext()
LoginSystem()

frec = TFileRecord()
tid  =  DWORD()

while GetNextFileRec(FileAreaNameKey, frec, tid):
   print("* Area: {} | {} | {}".format(frec.Area, frec.SFName.ljust(15), frec.Name))

LogoutUser()
