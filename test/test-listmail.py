# example to list messages

import ctypes
import sys
import wcpapi
from wcpapi import wcserver_h, wcserror_h
from wcpapi.wcserver_h import *
from wcpapi.wcserror_h import *
import datetime

def FormatFileTime(lft):
    ft = ctypes.wintypes.FILETIME(lft.dwLowDateTime, lft.dwHighDateTime)
    st = SYSTEMTIME()
    ctypes.windll.kernel32.FileTimeToSystemTime(ctypes.byref(ft), ctypes.byref(st))
    dt = datetime.datetime(st.wYear, st.wMonth, st.wDay, st.wHour, st.wMinute, st.wSecond)
    return dt.strftime("%Y%m%d %H:%M:%S")

def GetLowestMessage(cnum, msg):
    msg.Conference = cnum
    return GetNextMessage(msg)

def GetHighestMessage(cnum, msg):
    msg.Conference = cnum
    return GetPrevMessage(msg)

def doit(cnum, bList):

    total = GetTotalMessagesInConference(cnum)
    low   = GetLowMessageNumber(cnum)
    high  = GetHighMessageNumber(cnum)
    print("Total: {} Low: {} High: {}: ".format(total, low, high))

    msg = TMsgHeader()
    if not GetLowestMessage(cnum, msg):
        print("Error {:08X} GetLowestMessage({})".format(ctypes.GetLastError(), cnum))
        return
    print("Lo: {:5} id: {:7} | {}".format(msg.Number, msg.Id, msg.To.Name))

    msg = TMsgHeader()
    if not GetHighestMessage(cnum, msg):
        print("Error ", GetWildcatErrorStr(ctypes.GetLastError()))
        #print("Error {:08X} GetHighestMessage({})".format(ctypes.GetLastError(), cnum))
        return
    print("Hi: {:5} id: {:7} | {}".format(msg.Number, msg.Id, msg.To.Name))

    if not bList:
        return

    print("-" * 76)
    print("{:5s}| {:9s} | {:6s} | {:9s} | {:8s} | {:17s} | {:40s} | {:40s} | {}".format(
        "", "Id", "Number", "Size", "Flags", "Date", "To.Name", "From.Name", "Subject"
    ))
    print("-" * 76)

    dwCnt = 0
    dwSize = 0
    msg = TMsgHeader()
    msg.Conference = cnum

    dbg_zoom = 0
    if 0:
       Id  = 1640286863; Number = 116245
       if not GetMessageById(cnum,Id,msg):
          print(f"** ZOOM id {Id} Not Found")
       else:
          print(f"** ZOOM id {Id}")
          dbg_zoom = 1
       input()

    while GetNextMessage(ctypes.byref(msg)):
        dwCnt += 1
        dwSize += msg.MsgSize
        try:
           print("{:5} {:9} | {:6} | {:9} | {:08x} | {:17} | {:40} | {:40} | {}".format(
              dwCnt, msg.Id, msg.Number, msg.MsgSize, msg.MailFlags,
              FormatFileTime(msg.MsgTime), msg.To.Name, msg.From.Name, msg.Subject
           ))
        except Exception as e:
           print("{:5} {:9} | {:6} | {:9} | {:08x} | {:17} | {}".format(
              dwCnt, msg.Id, msg.Number, msg.MsgSize, msg.MailFlags,
              FormatFileTime(msg.MsgTime), e
           ))

        if dbg_zoom: input()
    print("-" * 76)
    print("Total Msgs: {} Total Size: {}".format(dwCnt, dwSize))


#------------------------------------------------------
# main
#------------------------------------------------------
if __name__ == "__main__":

   if 0:
      cnum = 9
      bList = 1
   else:
      if len(sys.argv) < 2:
          print("usage: wcListMail conf# [/L]")
          print("show low/high message numbers.")
          print("/l will display headers")
          exit(1)

      cnum = int(sys.argv[1]) if len(sys.argv) >= 2 else 0
      bList = len(sys.argv) >= 3 and sys.argv[2].lower() == "/l"


   server = ""
   if not WildcatServerConnectSpecific(None,server):   exit(1)
   if not WildcatServerCreateContext(): exit(1)
   try:
       if not LoginSystem():
           print("Error {:08x} w/ login".format(ctypes.GetLastError()))
           exit(1)
       doit(cnum, bList)
   finally:
       WildcatServerDeleteContext()

