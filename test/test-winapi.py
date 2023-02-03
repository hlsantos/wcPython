# ----------------------------------------------------------
# WcPAPI testing. There are many test before that are turned
# on and off with the on `if 1:` or off `if 0:` blocks.
# ----------------------------------------------------------

import re
import os
import ctypes
from ctypes import *

import wcpapi
from wcpapi import wcserver_h, wcsmw_h
from wcpapi.wcserver_h import *
from wcpapi.wcserror_h import *
from wcpapi.wcsmw_h import *

#-----------------------------------------------------------
# Helper functions
#-----------------------------------------------------------

def WildcatVersionStr(wsi):
    major_version = (wsi.ServerVersion & 0xffff0000) >> 16
    minor_version = wsi.ServerVersion & 0x0000ffff
    major_build = (wsi.ServerBuild & 0xffff0000) >> 16
    minor_build = wsi.ServerBuild & 0x0000ffff
    return f"{major_version}.{minor_version}.{major_build}.{minor_build}"

def wcGetConnectedServer():
    server_name_buffer = create_string_buffer(1024)
    if GetConnectedServer(server_name_buffer, sizeof(server_name_buffer)):
       return server_name_buffer.value.decode();
    else:
       return ""

def WaitEnter():
    print("<<Pause>>", end="");
    return input()

#-----------------------------------------------------------
# MAIN
#-----------------------------------------------------------

print("#"*60)
print("* wcPython")
print("- Version:",GetWildcatVersion()," Build:",GetWildcatBuild())

serverName = "hdev21"
serverName = "NTBBS"
serverName = ""

if not WildcatServerConnectSpecific(None,serverName):
   # normally we don't print this out
   #error_code = GetLastError()
   #print(f"! connect error code: {GetWildcatErrorStr(GetLastError())}")
   exit(1)

if not WildcatServerCreateContext():
   error_code = GetLastError()
   print(f"! creating context error code: {GetWildcatErrorStr(error_code)}")
   exit(1)

if not LoginSystem():
   error_code = GetLastError()
   print(f"! LoginSystem() context error code: {GetWildcatErrorStr(error_code)}")

print("- Connected to server:",wcGetConnectedServer());

# ----------------------------------------------------------
# Testing Makewild
# ----------------------------------------------------------
if 0:
   mw = TMakewild()
   if GetMakewild(mw):
      print("** TMakewild")
      print("%-23s: %s" % ("Version", hex(mw.Version)))
      print("%-23s: %s" % ("BBSName", mw.BBSName))
      print("%-23s: %s" % ("BuildDate", mw.BuildDate))
      print("%-23s: %s" % ("DomainName", mw.DomainName))
      print("%-23s: %s" % ("SysopName", mw.SysopName))
      print("%-23s: %s" % ("City", mw.City))
      print("%-23s: %s" % ("FirstCall", mw.FirstCall))
      print("%-23s: %s" % ("PacketId", mw.PacketId))
      print("%-23s: %s" % ("RegString", mw.RegString))
      print("%-23s: %s" % ("SystemAccess", mw.SystemAccess))
      print("%-23s: %s" % ("MaxLoginAttempts", mw.MaxLoginAttempts))
      print("%-23s: %s" % ("LoginAskLocation", mw.LoginAskLocation))
      print("%-23s: %s" % ("NewUserSecurity", mw.NewUserSecurity))
      print("%-23s: %s" % ("DefaultExt", mw.DefaultExt))
      print("%-23s: %s" % ("DateFormat", mw.DateFormat))
      print("%-23s: %s" % ("TimeFormat", mw.TimeFormat))
      print("%-23s: %s" % ("DefaultDomain", mw.DefaultDomain))
      print("%-23s: %s" % ("AllowLogonEmail", mw.AllowLogonEmail))
      print("%-23s: %s" % ("CaseSensitivePasswords", mw.CaseSensitivePasswords))
      print("%-23s: %s" % ("MsgHeaderCaseMode", mw.MsgHeaderCaseMode))
      print("%-23s: %s" % ("SpamAllowAuth", mw.SpamAllowAuth))
      print("%-23s: %s" % ("InstalledComponents", mw.InstalledComponents))
      print("%-23s: %s" % ("WindowsCharset", mw.WindowsCharset))
      print("%-23s: %s" % ("LogonUserNameOnly", mw.LogonUserNameOnly))
   else:
      print("MakeWild error:",hex(GetLastError()))

# ----------------------------------------------------------
# Testing GetUserById() 
# ----------------------------------------------------------
if 0:
   # create a TUser struct to hold the result
   user = TUser()
   tid =  DWORD()

   # call the GetUserById function
   id = 1  
   if GetUserById(id, user, byref(tid)):
      try:
        print(f"Thread ID: {tid.value}")
        print(f"UserId: {user.Info.Id} found:", user.Info.Name)
        seclist = [user.Security[i].Item for i in range(NUM_USER_SECURITY) if user.Security[i].Item]
        print(seclist)
        """
        secs = ""
        for i in range(NUM_USER_SECURITY):
           if user.Security[i].Item != "": secs += f"{user.Security[i].Item:15}"
        print(f"{secs}")
        """
      except Exception as e:
        print(f"Error with name {user.Info.Name}",e)
      print("")

   else:
      print("User not found.")

# ----------------------------------------------------------
# Testing GetNextUser()
# ----------------------------------------------------------
if 0:
   print("- Total Users: ",GetTotalUsers())
   tid = DWORD()
   user = TUser()
   sortkey = UserNameKey
   sortkey = UserLastNameKey
   sortkey = UserIdKey
   n = 0
   while GetNextUser(sortkey, user, tid):
      n += 1
      try:
        seclist = [user.Security[i].Item for i in range(NUM_USER_SECURITY) if user.Security[i].Item]
        l = len(seclist)
        if l == 0 or l > 1:
           print(f"* id: {user.Info.Id:<5} {user.Info.Name:<25} ",end="")
           print(seclist)
      except Exception as e:
        print(f"Error with User Name {user.Info.Name}:",e)

# ----------------------------------------------------------
# Testing GetWildcatServerInfo()
# ----------------------------------------------------------
if 0:
   server_info = TWildcatServerInfo()
   if GetWildcatServerInfo(byref(server_info)):
       print("** TWildcatServerInfo")
       print(f"Total Calls    : {server_info.TotalCalls:10}")
       print(f"Total Users    : {server_info.TotalUsers:10}")
       print(f"Total Messages : {server_info.TotalMessages:10}")
       print(f"Total Files    : {server_info.TotalFiles:10}")
       print(f"Memory Usage   : {server_info.MemoryUsage:10}")
       print(f"Memory Load    : {server_info.MemoryLoad:10}")
       print(f"Last Message Id: {server_info.LastMessageId:10}")
       print(f"Last User Id   : {server_info.LastUserId:10}")
       print( "Version.Build  :",WildcatVersionStr(server_info))
   else:
       print("Error getting server information")

# ----------------------------------------------------------
# Testing GetFileArea()
# ----------------------------------------------------------
if 0:
   # Get the number of file areas
   file_area_count = GetFileAreaCount()
   print("- File Areas:",file_area_count)
   # Iterate through each file area
   for i in range(file_area_count):
       try:
           # Get the file area data
           # Allocate a TFileArea structure
           file_area = TFileArea()
           if GetFileArea(i+1, byref(file_area)):
              # Print the file area data
              print("File Area #%d:" % (i+1), " Name: %-25s" % file_area.Name)
              #print("  ObjectId           :", file_area.ObjectId)
              #print("  Number             :", file_area.Number)
              #print("  Name               :", file_area.Name)
              #print("  FtpDirectoryName   :", file_area.FtpDirectoryName)
              #print("  ExcludeFromNewFiles:", file_area.ExcludeFromNewFiles)
              #print("  PromptForPasswordProtect:", file_area.PromptForPasswordProtect)
              #print("  Options            :", hex(file_area.Options))
           #else:
           #   print(f"Error getting file area {i} data")
       except Exception as e:
           print("Error ",e)


# ----------------------------------------------------------
# Testing GetSecurityFileNames()
# ----------------------------------------------------------
if 0:
    count = GetSecurityProfileCount()
    print(f"Profile count: ",count)
    names = (TSecurityName * count)()
    if GetSecurityProfileNames(count, names):
        for i in range(count):
            print(names[i])
    else:
        print("Error getting security profile names")

# ----------------------------------------------------------
# Testing MwLogin()
# ----------------------------------------------------------
if 1:
    LogoutUser()
    csrv = wcGetConnectedServer()
    pwds = {"NTBBS" : "",
            "MAIN3" : "",
            "HDEV21": "",
            "MINIPC1" : "",
            }

    pwd = pwds.get(csrv,"")
    print(f"- Connected to server: {csrv} using pwd {pwd}")

    if not MwLogin(pwd):
        print(f"Error {GetWildcatErrorStr(GetLastError())}: MwLogin() Login Error")

    # get the number of security groups
    count = MwGetGroupCount()
    print(f"Group count: ",count)
    if not count:
        print(f"Error {GetWildcatErrorStr(GetLastError())}: count is zero?")

    # create an array of TSecurityName instances
    security_names = (TSecurityName * count)()

    # pass the address of the array to the MwGetGroupNames function
    if MwGetGroupNames(security_names):
        # if the function returns True, display all the security names
        for i in range(count):
            print(security_names[i])
    else:
        print(f"Error {GetWildcatErrorStr(GetLastError())}: getting security names")

# ----------------------------------------------------------
if not WildcatServerDeleteContext():
   print("Error Deleting Wildcat! Server Context")
   exit(1)

WaitEnter()
