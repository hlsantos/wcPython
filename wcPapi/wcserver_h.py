# Auto-Created by cpp2py.py
import os
from wcpapi.wctype_constants_h import *
from wcpapi.wctype_h import *
from wcpapi.__init__ import *

wcsrv_dll = initialize_wcsrv_dll()

class SYSTEMTIME(ctypes.Structure):
    _fields_ = [('wYear', WORD),
                ('wMonth', WORD),
                ('wDayOfWeek', WORD),
                ('wDay', WORD),
                ('wHour', WORD),
                ('wMinute', WORD),
                ('wSecond', WORD),
                ('wMilliseconds', WORD)]

#//*******************************************************************
#// (c) Copyright 1999 Santronics Software, Inc. All Rights Reserved.
#//*******************************************************************
#//
#// File Name : wcserver.h
#// Created   : 07/02/99 06:40 pm
#// Updated   : 04/16/21 09:07 pm, 454.12
#// Programmer: SSI
#//
#// Revision History:
#// Build  Date     Author  Comments
#// -----  -------- ------  -------------------------------
#// 447B2  07/02/99 HLS     - cleaned up
#//        07/12/99 HLS     - new function: CheckMailIntegrity()
#// 450    05/11/00 SMC     - Added BCB support.  Not complete.
#//                           Functions dependent on TNodeInfo
#//                           and TMenuItem needed to be changed.
#// 450.7  04/25/03 HLS     - Removed UNICODE parameters (LPCTCHAR
#//                           and WIN32_FIND_DATA)
#//
#// 454.6  07/24/17 HLS     - Added WcGetGeoIP() function
#//
#// 454.8  03/17/19 HLS     - Added GetWildcatServerPlatform()
#//
#//*******************************************************************




#//+ Group: Client SDK Functions

#///////////////////////////////////////////////////////////////////////////
#//! Return the RPC Server 32 or 64 bit mode.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY WcGetServerPlatform();
WcGetServerPlatform = wcsrv_dll.WcGetServerPlatform
WcGetServerPlatform.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! The functions to get the Wildcat version and build can be called before
#//! WildcatServerConnect.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetWildcatVersion();
GetWildcatVersion = wcsrv_dll.GetWildcatVersion
GetWildcatVersion.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetWildcatBuild();
GetWildcatBuild = wcsrv_dll.GetWildcatBuild
GetWildcatBuild.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! The functions to get the Wildcat version and build at the server and
#//! can only be called after a context is created
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY WcGetServerVersion();
WcGetServerVersion = wcsrv_dll.WcGetServerVersion
WcGetServerVersion.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY WcGetServerBuild();
WcGetServerBuild = wcsrv_dll.WcGetServerBuild
WcGetServerBuild.restype = ctypes.wintypes.DWORD


#////////////////////////////////////////////////////////////////////////////
#//! WildcatServerConnect should be called once per application to connect to
#//! the Wildcat server.  The window handle is used as the parent window when
#//! the server connect dialog box is displayed.  If there is no convenient
#//! window handle available, pass NULL.  Console mode applications should
#//! also pass NULL.  WildcatServerConnectSpecific can be called if you know
#//! the machine name of the server you would like to connect to.
#//! WildcatServerDialog allows the user to pick a server from a dialog box.
#//!
#//! WildcatServerConnectLocal() was added in v5.7 to support connections
#//! only to the local computer. Performs no broadcasting.
#////////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY WildcatServerConnect(HWND parent);
WildcatServerConnect = wcsrv_dll.WildcatServerConnect
WildcatServerConnect.argtypes = [ctypes.wintypes.HWND]
WildcatServerConnect.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WildcatServerConnectSpecific(HWND parent, const char *computername);
WildcatServerConnectSpecific = wcsrv_dll.WildcatServerConnectSpecific
WildcatServerConnectSpecific.argtypes = [ctypes.wintypes.HWND, CString]
WildcatServerConnectSpecific.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WildcatServerConnectLocal(HWND parent);
WildcatServerConnectLocal = wcsrv_dll.WildcatServerConnectLocal
WildcatServerConnectLocal.argtypes = [ctypes.wintypes.HWND]
WildcatServerConnectLocal.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WildcatServerDialog(HWND parent, char *computername, DWORD namesize);
WildcatServerDialog = wcsrv_dll.WildcatServerDialog
WildcatServerDialog.argtypes = [ctypes.wintypes.HWND, ctypes.c_char_p, ctypes.wintypes.DWORD]
WildcatServerDialog.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetWildcatErrorMode(BOOL verbose);
SetWildcatErrorMode = wcsrv_dll.SetWildcatErrorMode
SetWildcatErrorMode.argtypes = [ctypes.wintypes.BOOL]
SetWildcatErrorMode.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WildcatServerShutdown(const char *pwd, const BOOL force);
WildcatServerShutdown = wcsrv_dll.WildcatServerShutdown
WildcatServerShutdown.argtypes = [CString, ctypes.wintypes.BOOL]
WildcatServerShutdown.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! GetConnectedServer retrieves the computer name of the connected server
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetConnectedServer(char *computername, DWORD namesize);
GetConnectedServer = wcsrv_dll.GetConnectedServer
GetConnectedServer.argtypes = [ctypes.c_char_p, ctypes.wintypes.DWORD]
GetConnectedServer.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions start and stop a thread-specific context for this client
#//! on the server.  Even if an application only has one thread, the
#//! WildcatServerCreateContext function must be called before any other
#//! functions will work.
#//!
#//! WildcatServerCreateContextFromHandle creates a new client context that
#//! refers to an existing context on the server.  The handle is generally
#//! retrieved using GetWildcatServerContextHandle in one application, and
#//! passed to WildcatServerCreateContextFromHandle in another application.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY WildcatServerCreateContext();
WildcatServerCreateContext = wcsrv_dll.WildcatServerCreateContext
WildcatServerCreateContext.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WildcatServerCreateContextFromHandle(DWORD context);
WildcatServerCreateContextFromHandle = wcsrv_dll.WildcatServerCreateContextFromHandle
WildcatServerCreateContextFromHandle.argtypes = [ctypes.wintypes.DWORD]
WildcatServerCreateContextFromHandle.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WildcatServerCreateContextFromChallenge(const char *challenge);
WildcatServerCreateContextFromChallenge = wcsrv_dll.WildcatServerCreateContextFromChallenge
WildcatServerCreateContextFromChallenge.argtypes = [CString]
WildcatServerCreateContextFromChallenge.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY GetWildcatServerContextHandle();
GetWildcatServerContextHandle = wcsrv_dll.GetWildcatServerContextHandle
GetWildcatServerContextHandle.restype = ctypes.wintypes.DWORD

#//DWORD APIENTRY GetWildcatServerContextRefCount(); (deprecated)
##BOOL APIENTRY WildcatServerDeleteContext();
WildcatServerDeleteContext = wcsrv_dll.WildcatServerDeleteContext
WildcatServerDeleteContext.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! This function sets up a callback for the client application.
#//! Channel messages are presented to the client through this
#//! callback mechanism.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY SetupWildcatCallback(TWildcatCallback cbproc, DWORD userdata);
SetupWildcatCallback = wcsrv_dll.SetupWildcatCallback
SetupWildcatCallback.argtypes = [ctypes.c_void_p, ctypes.wintypes.DWORD]
SetupWildcatCallback.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY RemoveWildcatCallback();
RemoveWildcatCallback = wcsrv_dll.RemoveWildcatCallback
RemoveWildcatCallback.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! This function is used to grant another thread in the same application
#//! equivalent access as the thread that calls this function.  It causes the
#//! other thread to refer to the same server context.  This is a lightweight
#//! version of WildcatServerCreateContextFromHandle.  One difference is that
#//! since this function does not create a new client context,
#//! WildcatServerDeleteContext must only be called once for this context,
#//! even though there may be more than one thread accessing it.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GrantThreadAccess(DWORD tid);
GrantThreadAccess = wcsrv_dll.GrantThreadAccess
GrantThreadAccess.argtypes = [ctypes.wintypes.DWORD]
GrantThreadAccess.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These two functions allow you to more directly manipulate the Wildcat
#//! server context associated with the current thread.  Like
#//! GrantThreadAccess, the Wildcat server is only aware of one instance of
#//! the context, so WildcatServerDeleteContext must only be called once per
#//! server context.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetWildcatThreadContext();
GetWildcatThreadContext = wcsrv_dll.GetWildcatThreadContext
GetWildcatThreadContext.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY SetWildcatThreadContext(DWORD context);
SetWildcatThreadContext = wcsrv_dll.SetWildcatThreadContext
SetWildcatThreadContext.argtypes = [ctypes.wintypes.DWORD]
SetWildcatThreadContext.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Returns the current node number, or 0 if no node number has been
#//! allocated.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetNode();
GetNode = wcsrv_dll.GetNode
GetNode.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! Set the current node status (nsDown, nsUp, nsSigningOn, nsLoggedIn).
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY SetNodeStatus(DWORD nodestatus);
SetNodeStatus = wcsrv_dll.SetNodeStatus
SetNodeStatus.argtypes = [ctypes.wintypes.DWORD]
SetNodeStatus.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Set the node down status (ndNone, ndRefuseLogin, ndDown).
#///////////////////////////////////////////////////////////////////////////

#//BOOL  APIENTRY SetNodeStatusDown(DWORD node, DWORD downstatus); (deprecated, see SetPortState)

#///////////////////////////////////////////////////////////////////////////
#//! Get the TMakewild global configuration record.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetMakewild(TMakewild &mw);
GetMakewild = wcsrv_dll.GetMakewild
GetMakewild.argtypes = [ctypes.POINTER(TMakewild)]
GetMakewild.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetComputerConfig(TComputerConfig &cc);
GetComputerConfig = wcsrv_dll.GetComputerConfig
GetComputerConfig.argtypes = [ctypes.POINTER(TComputerConfig)]
GetComputerConfig.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Get the challenge string used for MD5 password authentication.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetChallengeString(char *buf, DWORD bufsize);
GetChallengeString = wcsrv_dll.GetChallengeString
GetChallengeString.argtypes = [ctypes.c_char_p, ctypes.wintypes.DWORD]
GetChallengeString.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Log in to the Wildcat server as the 'system'.  This gives unrestricted
#//! access to all aspects of the server.  The computer from which this
#//! function is called must have been set up with the Wildcat System
#//! password, if any.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY LoginSystem();
LoginSystem = wcsrv_dll.LoginSystem
LoginSystem.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Look up a user account by name, and return basic account information.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY LookupName(const char *name, TUserInfo &uinfo);
LookupName = wcsrv_dll.LookupName
LookupName.argtypes = [CString, ctypes.POINTER(TUserInfo)]
LookupName.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Allocate a node for a particular call type.  If a specific node is
#//! required, pass it in the 'node' parameter, otherwise pass zero.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY AllocateNode(DWORD node, DWORD calltype, const char *speed);
AllocateNode = wcsrv_dll.AllocateNode
AllocateNode.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, CString]
AllocateNode.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Log in to the userver under a user account.  All further access to the
#//! server is checked based on the access profile(s) of the user.  The
#//! password can either be plaintext or an MD5 digest string.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY LoginUser(DWORD userid, const char *password, TUser &user);
LoginUser = wcsrv_dll.LoginUser
LoginUser.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(TUser)]
LoginUser.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY LoginUserEx(DWORD userid, const char *password, DWORD calltype, const char *speed, TUser &user);
LoginUserEx = wcsrv_dll.LoginUserEx
LoginUserEx.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.wintypes.DWORD, CString, ctypes.POINTER(TUser)]
LoginUserEx.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY LoginRadiusUser(DWORD userid, BYTE chapid, const BYTE *challenge, DWORD challengesize, const BYTE *challresponse, TUser &user);
LoginRadiusUser = wcsrv_dll.LoginRadiusUser
LoginRadiusUser.argtypes = [ctypes.wintypes.DWORD, ctypes.c_byte, CString, ctypes.wintypes.DWORD, CString, ctypes.POINTER(TUser)]
LoginRadiusUser.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Log out of the server.  This is called no matter whether you log in to
#//! the server using LoginSystem or LoginUser.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY LogoutUser();
LogoutUser = wcsrv_dll.LogoutUser
LogoutUser.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Checks to see whether the current context is logged in or not.  Returns
#//! the user record if it is logged in as a user.  See clSessionXXXX
#//! constants
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY WildcatLoggedIn(TUser *user);
WildcatLoggedIn = wcsrv_dll.WildcatLoggedIn
WildcatLoggedIn.argtypes = [ctypes.POINTER(TUser)]
WildcatLoggedIn.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! Gets the number of users currently online.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetUsersOnline();
GetUsersOnline = wcsrv_dll.GetUsersOnline
GetUsersOnline.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! Get the object flags for a particular access profile.  This may be
#//! called before a user is logged in.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetProfileObjectFlags(const char *profile, DWORD objectid);
GetProfileObjectFlags = wcsrv_dll.GetProfileObjectFlags
GetProfileObjectFlags.argtypes = [CString, ctypes.wintypes.DWORD]
GetProfileObjectFlags.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! The Wildcat server file API functions are modeled after the Win32 file
#//! API functions.  See the Win32 API documentation for details regarding
#//! these functions. See WCPATHS.DOC for information regarding the format of
#//! the path names that may be used with these functions.
#///////////////////////////////////////////////////////////////////////////

##BOOL   APIENTRY WcCloseHandle(WCHANDLE h);
WcCloseHandle = wcsrv_dll.WcCloseHandle
WcCloseHandle.argtypes = [ctypes.wintypes.HANDLE]
WcCloseHandle.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcCreateDirectory(const char * dir);
WcCreateDirectory = wcsrv_dll.WcCreateDirectory
WcCreateDirectory.argtypes = [CString]
WcCreateDirectory.restype = ctypes.wintypes.BOOL

#BOOL     APIENTRY WcRemoveDirectory(const char * dir);  // 450.3
##WCHANDLE APIENTRY WcCreateFile(const char * fn, DWORD access, DWORD sharemode, DWORD create);
WcCreateFile = wcsrv_dll.WcCreateFile
WcCreateFile.argtypes = [CString, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
WcCreateFile.restype = ctypes.wintypes.HANDLE

##BOOL   APIENTRY WcDeleteFile(const char * fn);
WcDeleteFile = wcsrv_dll.WcDeleteFile
WcDeleteFile.argtypes = [CString]
WcDeleteFile.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcExistFile(const char * fn);
WcExistFile = wcsrv_dll.WcExistFile
WcExistFile.argtypes = [CString]
WcExistFile.restype = ctypes.wintypes.BOOL

##WCHANDLE APIENTRY WcFindFirstFile(const char * fn, WIN32_FIND_DATAA *fd);
WcFindFirstFile = wcsrv_dll.WcFindFirstFile
WcFindFirstFile.argtypes = [CString, ctypes.POINTER(WIN32_FIND_DATAA)]
WcFindFirstFile.restype = ctypes.wintypes.HANDLE

##BOOL   APIENTRY WcFindNextFile(WCHANDLE ff, WIN32_FIND_DATAA *fd);
WcFindNextFile = wcsrv_dll.WcFindNextFile
WcFindNextFile.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(WIN32_FIND_DATAA)]
WcFindNextFile.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcFindClose(WCHANDLE ff);
WcFindClose = wcsrv_dll.WcFindClose
WcFindClose.argtypes = [ctypes.wintypes.HANDLE]
WcFindClose.restype = ctypes.wintypes.BOOL

##DWORD  APIENTRY WcGetFileSize(WCHANDLE h);
WcGetFileSize = wcsrv_dll.WcGetFileSize
WcGetFileSize.argtypes = [ctypes.wintypes.HANDLE]
WcGetFileSize.restype = ctypes.wintypes.DWORD

##BOOL   APIENTRY WcGetFileTime(WCHANDLE h, FILETIME &ft);
WcGetFileTime = wcsrv_dll.WcGetFileTime
WcGetFileTime.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(FILETIME)]
WcGetFileTime.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcGetFileTimeByName(const char * fn, FILETIME &ft);
WcGetFileTimeByName = wcsrv_dll.WcGetFileTimeByName
WcGetFileTimeByName.argtypes = [CString, ctypes.POINTER(FILETIME)]
WcGetFileTimeByName.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcMoveFile(const char * src, const char * dest);
WcMoveFile = wcsrv_dll.WcMoveFile
WcMoveFile.argtypes = [CString, CString]
WcMoveFile.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcReadFile(WCHANDLE h, LPVOID buffer, DWORD requested, LPDWORD read);
WcReadFile = wcsrv_dll.WcReadFile
WcReadFile.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(ctypes.c_void_p), ctypes.wintypes.DWORD, ctypes.POINTER(ctypes.c_ulong)]
WcReadFile.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcReadLine(WCHANDLE h, LPVOID buffer, DWORD buflen);
WcReadLine = wcsrv_dll.WcReadLine
WcReadLine.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(ctypes.c_void_p), ctypes.wintypes.DWORD]
WcReadLine.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcSetEndOfFile(WCHANDLE h);
WcSetEndOfFile = wcsrv_dll.WcSetEndOfFile
WcSetEndOfFile.argtypes = [ctypes.wintypes.HANDLE]
WcSetEndOfFile.restype = ctypes.wintypes.BOOL

##DWORD  APIENTRY WcSetFilePointer(WCHANDLE h, LONG dist, DWORD movemethod);
WcSetFilePointer = wcsrv_dll.WcSetFilePointer
WcSetFilePointer.argtypes = [ctypes.wintypes.HANDLE, ctypes.wintypes.LONG, ctypes.wintypes.DWORD]
WcSetFilePointer.restype = ctypes.wintypes.DWORD

##BOOL   APIENTRY WcSetFileTime(WCHANDLE h, FILETIME &ft);
WcSetFileTime = wcsrv_dll.WcSetFileTime
WcSetFileTime.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(FILETIME)]
WcSetFileTime.restype = ctypes.wintypes.BOOL

##BOOL   APIENTRY WcWriteFile(WCHANDLE h, LPCVOID buffer, DWORD requested, LPDWORD written);
WcWriteFile = wcsrv_dll.WcWriteFile
WcWriteFile.argtypes = [ctypes.wintypes.HANDLE, ctypes.c_void_p, ctypes.wintypes.DWORD, ctypes.POINTER(ctypes.c_ulong)]
WcWriteFile.restype = ctypes.wintypes.BOOL

#BOOL     APIENTRY WcRenameFile(const char * from, const char * toname); // 450.3

#// 451.8h 07/17/06 07:26 pm
#// Internal usage only
##BOOL   APIENTRY WcResolvePathName(const char *wfname, DWORD &access, DWORD &share, DWORD &create, char *dest, const DWORD destsize);
WcResolvePathName = wcsrv_dll.WcResolvePathName
WcResolvePathName.argtypes = [CString, ctypes.POINTER(DWORD), ctypes.POINTER(DWORD), ctypes.POINTER(DWORD), ctypes.c_char_p, ctypes.wintypes.DWORD]
WcResolvePathName.restype = ctypes.wintypes.BOOL

#//

#///////////////////////////////////////////////////////////////////////////
#//! Get the connection Id for the current context.  Connection Ids are
#//! unique and can reasonably be assumed not to repeat during the time the
#//! server is up.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetConnectionId();
GetConnectionId = wcsrv_dll.GetConnectionId
GetConnectionId.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! Get the total number of calls made to the system (not server API calls,
#//! user calls). The 'increment' parameter determines whether or not the
#//! count is increased by one before returning the result.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetTotalCalls(BOOL increment);
GetTotalCalls = wcsrv_dll.GetTotalCalls
GetTotalCalls.argtypes = [ctypes.wintypes.BOOL]
GetTotalCalls.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! This function combines a WcCreateFile, WcReadFile, and WcCloseHandle
#//! into one operation.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetText(const char *fn, char *buf, DWORD bufsize, DWORD &retsize);
GetText = wcsrv_dll.GetText
GetText.argtypes = [CString, ctypes.c_char_p, ctypes.wintypes.DWORD, ctypes.POINTER(DWORD)]
GetText.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! The following functions access the security data in the Wildcat server.
#//! Each 'securable' object (conference, file area, door, etc) has a unique
#//! Object Id stored with it.  Access profiles are tables of Object Ids and
#//! access flags. When a user logs in, a composite access table consisting
#//! of the logical OR of all the flags in the user' access profiles is
#//! created.  These functions access the information in that composite
#//! array.
#//!
#//! Object flags are often simply zero or one to indicate no access or allow
#//! access, but the individual bits may mean different things such as
#//! Join/Read/Write/Sysop access in a conference area.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetObjectFlags(DWORD objectid);
GetObjectFlags = wcsrv_dll.GetObjectFlags
GetObjectFlags.argtypes = [ctypes.wintypes.DWORD]
GetObjectFlags.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetMultipleObjectFlags(const DWORD *objectid, DWORD count, DWORD *flags);
GetMultipleObjectFlags = wcsrv_dll.GetMultipleObjectFlags
GetMultipleObjectFlags.argtypes = [DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(DWORD)]
GetMultipleObjectFlags.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetObjectById(DWORD objectid, TObjectName &objectname);
GetObjectById = wcsrv_dll.GetObjectById
GetObjectById.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TObjectName)]
GetObjectById.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetMultipleObjectsById(const DWORD *objectid, DWORD count, TObjectName *objectname);
GetMultipleObjectsById = wcsrv_dll.GetMultipleObjectsById
GetMultipleObjectsById.argtypes = [DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TObjectName)]
GetMultipleObjectsById.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetObjectByName(DWORD classid, const char *name, TObjectName &objectname, DWORD &tid);
GetObjectByName = wcsrv_dll.GetObjectByName
GetObjectByName.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(TObjectName), ctypes.POINTER(DWORD)]
GetObjectByName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetNextObjectByName(TObjectName &objectname, DWORD &tid);
GetNextObjectByName = wcsrv_dll.GetNextObjectByName
GetNextObjectByName.argtypes = [ctypes.POINTER(TObjectName), ctypes.POINTER(DWORD)]
GetNextObjectByName.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY GetStringObjectId(DWORD objectclass, const char *name);
GetStringObjectId = wcsrv_dll.GetStringObjectId
GetStringObjectId.argtypes = [ctypes.wintypes.DWORD, CString]
GetStringObjectId.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetStringObjectFlags(DWORD objectclass, const char *name);
GetStringObjectFlags = wcsrv_dll.GetStringObjectFlags
GetStringObjectFlags.argtypes = [ctypes.wintypes.DWORD, CString]
GetStringObjectFlags.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! These functions access the list of security profiles in the server.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetSecurityProfileCount();
GetSecurityProfileCount = wcsrv_dll.GetSecurityProfileCount
GetSecurityProfileCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetSecurityProfileNames(DWORD count, char names[][SIZE_SECURITY_NAME]);
GetSecurityProfileNames = wcsrv_dll.GetSecurityProfileNames
GetSecurityProfileNames.argtypes = [ctypes.c_ulong, ctypes.POINTER(TSecurityName)]
GetSecurityProfileNames.restype = ctypes.c_bool

##BOOL APIENTRY GetSecurityProfileByIndex(DWORD index, TSecurityProfile &profile);
GetSecurityProfileByIndex = wcsrv_dll.GetSecurityProfileByIndex
GetSecurityProfileByIndex.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TSecurityProfile)]
GetSecurityProfileByIndex.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetSecurityProfileByName(const char *name, TSecurityProfile &profile);
GetSecurityProfileByName = wcsrv_dll.GetSecurityProfileByName
GetSecurityProfileByName.argtypes = [CString, ctypes.POINTER(TSecurityProfile)]
GetSecurityProfileByName.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions access the list of access profile names in the server.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetAccessProfileCount();
GetAccessProfileCount = wcsrv_dll.GetAccessProfileCount
GetAccessProfileCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetAccessProfileNames(DWORD count, char names[][SIZE_SECURITY_NAME]);
GetAccessProfileNames = wcsrv_dll.GetAccessProfileNames
GetAccessProfileNames.argtypes = [ctypes.c_ulong, ctypes.POINTER(TSecurityName)]
GetAccessProfileNames.restype = ctypes.c_bool

##BOOL APIENTRY GetAccessProfileName(DWORD index, char name[SIZE_SECURITY_NAME]);
GetAccessProfileName = wcsrv_dll.GetAccessProfileName
GetAccessProfileName.argtypes = [ctypes.wintypes.DWORD, ctypes.c_char]
GetAccessProfileName.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions access the list of conferences (message areas) in
#//! the server.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetConferenceCount();
GetConferenceCount = wcsrv_dll.GetConferenceCount
GetConferenceCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetConfDesc(DWORD conference, TConfDesc &cd);
GetConfDesc = wcsrv_dll.GetConfDesc
GetConfDesc.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TConfDesc)]
GetConfDesc.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions access the list of conference groups in the server.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetConferenceGroupCount();
GetConferenceGroupCount = wcsrv_dll.GetConferenceGroupCount
GetConferenceGroupCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetConferenceGroup(DWORD index, TConferenceGroup &cg);
GetConferenceGroup = wcsrv_dll.GetConferenceGroup
GetConferenceGroup.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TConferenceGroup)]
GetConferenceGroup.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions access the list of file areas in the server.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetFileAreaCount();
GetFileAreaCount = wcsrv_dll.GetFileAreaCount
GetFileAreaCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetFileArea(DWORD area, TFileArea &fa);
GetFileArea = wcsrv_dll.GetFileArea
GetFileArea.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileArea)]
GetFileArea.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions access the list of file groups in the server.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetFileGroupCount();
GetFileGroupCount = wcsrv_dll.GetFileGroupCount
GetFileGroupCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetFileGroup(DWORD index, TFileGroup &fg);
GetFileGroup = wcsrv_dll.GetFileGroup
GetFileGroup.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileGroup)]
GetFileGroup.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions access the list of doors in the server.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetDoorCount();
GetDoorCount = wcsrv_dll.GetDoorCount
GetDoorCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetDoor(DWORD index, TDoorInfo &di);
GetDoor = wcsrv_dll.GetDoor
GetDoor.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TDoorInfo)]
GetDoor.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions access the list of languages in the server.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetLanguageCount();
GetLanguageCount = wcsrv_dll.GetLanguageCount
GetLanguageCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetLanguage(DWORD index, TLanguageInfo &li);
GetLanguage = wcsrv_dll.GetLanguage
GetLanguage.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TLanguageInfo)]
GetLanguage.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! This function gets a specific modem profile from the server.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetModemProfile(const char *name, TModemProfile &mp);
GetModemProfile = wcsrv_dll.GetModemProfile
GetModemProfile.argtypes = [CString, ctypes.POINTER(TModemProfile)]
GetModemProfile.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Get the current maximum number of nodes that have been allocated.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetNodeCount();
GetNodeCount = wcsrv_dll.GetNodeCount
GetNodeCount.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! Get the maximum number of concurrent users supported by this
#//! installation of Wildcat.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetMaximumUserCount();
GetMaximumUserCount = wcsrv_dll.GetMaximumUserCount
GetMaximumUserCount.restype = ctypes.wintypes.DWORD


#///////////////////////////////////////////////////////////////////////////
#//! Get a node configuration record for the specified node.  Use
#//! by Wconline to start modem nodes.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetNodeConfig(DWORD node, TNodeConfig &nc);
GetNodeConfig = wcsrv_dll.GetNodeConfig
GetNodeConfig.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TNodeConfig)]
GetNodeConfig.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Get a node information record for a specific node.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetNodeInfo(DWORD node, TwcNodeInfo &ni);
GetNodeInfo = wcsrv_dll.GetNodeInfo
GetNodeInfo.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TwcNodeInfo)]
GetNodeInfo.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Get a node information record for a specific connection Id.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetNodeInfoByConnectionId(DWORD id, TwcNodeInfo &ni);
GetNodeInfoByConnectionId = wcsrv_dll.GetNodeInfoByConnectionId
GetNodeInfoByConnectionId.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TwcNodeInfo)]
GetNodeInfoByConnectionId.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Get a node information record for a specific name.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetNodeInfoByName(const char *name, TwcNodeInfo &ni);
GetNodeInfoByName = wcsrv_dll.GetNodeInfoByName
GetNodeInfoByName.argtypes = [CString, ctypes.POINTER(TwcNodeInfo)]
GetNodeInfoByName.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Get multiple node information records starting at a specific node.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetNodeInfos(DWORD node, DWORD count, TwcNodeInfo *ni);
GetNodeInfos = wcsrv_dll.GetNodeInfos
GetNodeInfos.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TwcNodeInfo)]
GetNodeInfos.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Set the current node's information record.  Only non-critical fields are
#//! allowed to be changed by this function.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY SetNodeInfo(const TwcNodeInfo &ni);
SetNodeInfo = wcsrv_dll.SetNodeInfo
SetNodeInfo.argtypes = [TwcNodeInfo]
SetNodeInfo.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Set the current activity string for the current node.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY SetNodeActivity(const char *activity);
SetNodeActivity = wcsrv_dll.SetNodeActivity
SetNodeActivity.argtypes = [CString]
SetNodeActivity.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Server State Functions
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY SetServerState(const char *port, DWORD state);
SetServerState = wcsrv_dll.SetServerState
SetServerState.argtypes = [CString, ctypes.wintypes.DWORD]
SetServerState.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetServerState(DWORD index, TServerState &ss);
GetServerState = wcsrv_dll.GetServerState
GetServerState.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TServerState)]
GetServerState.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetNodeServerState(DWORD node, DWORD state);
SetNodeServerState = wcsrv_dll.SetNodeServerState
SetNodeServerState.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
SetNodeServerState.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! The following functions access the file database in Wildcat.  The
#//! functions should be straightforward with the following notes:
#//!
#//! - GetFileRecByXxx gets a specific record by key.  SearchFileRecByXxx
#//!   searches for matching record, or the next record in the database,
#//!   based on a key.
#//!
#//! - FileSearch returns an array of __int64 (64-bit integers).  The high 32
#//!   bits indicates the file area of the record, and the low 32 bits
#//!   indicates the absolute reference number of the record.
#//!   GetFileRecAbsolute gets a specific file record.
#//!
#//! - Most functions return a TFileRecord which does not contain the long
#//!   file description. To retrieve the long file description, use
#//!   GetFullFileRec.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY AddFileRec(TFullFileRecord &f);
AddFileRec = wcsrv_dll.AddFileRec
AddFileRec.argtypes = [ctypes.POINTER(TFullFileRecord)]
AddFileRec.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY DeleteFileRec(const TFileRecord &f, BOOL disktoo);
DeleteFileRec = wcsrv_dll.DeleteFileRec
DeleteFileRec.argtypes = [TFileRecord, ctypes.wintypes.BOOL]
DeleteFileRec.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY FileSearch(const char *s, DWORD &n, unsigned __int64 *&p);
FileSearch = wcsrv_dll.FileSearch
FileSearch.argtypes = [CString, ctypes.POINTER(DWORD), ctypes.POINTER(ctypes.c_ulonglong)]
FileSearch.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetFileRecAbsolute(DWORD ref, TFileRecord &f);
GetFileRecAbsolute = wcsrv_dll.GetFileRecAbsolute
GetFileRecAbsolute.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord)]
GetFileRecAbsolute.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetFileRecByNameArea(const char *name, DWORD area, TFileRecord &f, DWORD &tid);
GetFileRecByNameArea = wcsrv_dll.GetFileRecByNameArea
GetFileRecByNameArea.argtypes = [CString, ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
GetFileRecByNameArea.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetFileRecByAreaName(DWORD area, const char *name, TFileRecord &f, DWORD &tid);
GetFileRecByAreaName = wcsrv_dll.GetFileRecByAreaName
GetFileRecByAreaName.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
GetFileRecByAreaName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetFileRecByAreaDate(DWORD area, const FILETIME &t, TFileRecord &f, DWORD &tid);
GetFileRecByAreaDate = wcsrv_dll.GetFileRecByAreaDate
GetFileRecByAreaDate.argtypes = [ctypes.wintypes.DWORD, FILETIME, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
GetFileRecByAreaDate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetFileRecByUploader(DWORD id, TFileRecord &f, DWORD &tid);
GetFileRecByUploader = wcsrv_dll.GetFileRecByUploader
GetFileRecByUploader.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
GetFileRecByUploader.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetFirstFileRec(DWORD keynum, TFileRecord &f, DWORD &tid);
GetFirstFileRec = wcsrv_dll.GetFirstFileRec
GetFirstFileRec.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
GetFirstFileRec.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetFullFileRec(TFileRecord &f, TFullFileRecord &full);
GetFullFileRec = wcsrv_dll.GetFullFileRec
GetFullFileRec.argtypes = [ctypes.POINTER(TFileRecord), ctypes.POINTER(TFullFileRecord)]
GetFullFileRec.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetLastFileRec(DWORD keynum, TFileRecord &f, DWORD &tid);
GetLastFileRec = wcsrv_dll.GetLastFileRec
GetLastFileRec.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
GetLastFileRec.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetNextFileRec(DWORD keynum, TFileRecord &f, DWORD &tid);
GetNextFileRec = wcsrv_dll.GetNextFileRec
GetNextFileRec.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
GetNextFileRec.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetPrevFileRec(DWORD keynum, TFileRecord &f, DWORD &tid);
GetPrevFileRec = wcsrv_dll.GetPrevFileRec
GetPrevFileRec.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
GetPrevFileRec.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY GetTotalFiles();
GetTotalFiles = wcsrv_dll.GetTotalFiles
GetTotalFiles.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetTotalFilesInArea(DWORD area);
GetTotalFilesInArea = wcsrv_dll.GetTotalFilesInArea
GetTotalFilesInArea.argtypes = [ctypes.wintypes.DWORD]
GetTotalFilesInArea.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetTotalFilesInGroup(DWORD group);
GetTotalFilesInGroup = wcsrv_dll.GetTotalFilesInGroup
GetTotalFilesInGroup.argtypes = [ctypes.wintypes.DWORD]
GetTotalFilesInGroup.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY IncrementDownloadCount(TFileRecord &f);
IncrementDownloadCount = wcsrv_dll.IncrementDownloadCount
IncrementDownloadCount.argtypes = [ctypes.POINTER(TFileRecord)]
IncrementDownloadCount.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchFileRecByNameArea(const char *name, DWORD area, TFileRecord &f, DWORD &tid);
SearchFileRecByNameArea = wcsrv_dll.SearchFileRecByNameArea
SearchFileRecByNameArea.argtypes = [CString, ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
SearchFileRecByNameArea.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchFileRecByAreaName(DWORD area, const char *name, TFileRecord &f, DWORD &tid);
SearchFileRecByAreaName = wcsrv_dll.SearchFileRecByAreaName
SearchFileRecByAreaName.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
SearchFileRecByAreaName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchFileRecByAreaDate(DWORD area, const FILETIME &t, TFileRecord &f, DWORD &tid);
SearchFileRecByAreaDate = wcsrv_dll.SearchFileRecByAreaDate
SearchFileRecByAreaDate.argtypes = [ctypes.wintypes.DWORD, FILETIME, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
SearchFileRecByAreaDate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchFileRecByDateArea(const FILETIME &t, DWORD area, TFileRecord &f, DWORD &tid);
SearchFileRecByDateArea = wcsrv_dll.SearchFileRecByDateArea
SearchFileRecByDateArea.argtypes = [FILETIME, ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
SearchFileRecByDateArea.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchFileRecByUploader(DWORD id, TFileRecord &f, DWORD &tid);
SearchFileRecByUploader = wcsrv_dll.SearchFileRecByUploader
SearchFileRecByUploader.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileRecord), ctypes.POINTER(DWORD)]
SearchFileRecByUploader.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY UpdateFileRec(TFileRecord &f);
UpdateFileRec = wcsrv_dll.UpdateFileRec
UpdateFileRec.argtypes = [ctypes.POINTER(TFileRecord)]
UpdateFileRec.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY UpdateFullFileRec(TFullFileRecord &f);
UpdateFullFileRec = wcsrv_dll.UpdateFullFileRec
UpdateFullFileRec.argtypes = [ctypes.POINTER(TFullFileRecord)]
UpdateFullFileRec.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! The following functions access the message databases in Wildcat.
#//! Messages are identified by there conference number and Id.  Message Ids
#//! are assigned when the message is added to the database and never
#//! reassigned.  Message Ids are very large numbers, so a separate message
#//! 'Number' is provided for convenience.  Message numbers are assigned
#//! sequentially within a conference.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY AddMessage(TMsgHeader &msg, const char *text);
AddMessage = wcsrv_dll.AddMessage
AddMessage.argtypes = [ctypes.POINTER(TMsgHeader), CString]
AddMessage.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY DeleteMessage(TMsgHeader &msg);
DeleteMessage = wcsrv_dll.DeleteMessage
DeleteMessage.argtypes = [ctypes.POINTER(TMsgHeader)]
DeleteMessage.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY GetHighMessageNumber(DWORD conf);
GetHighMessageNumber = wcsrv_dll.GetHighMessageNumber
GetHighMessageNumber.argtypes = [ctypes.wintypes.DWORD]
GetHighMessageNumber.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetLowMessageNumber(DWORD conf);
GetLowMessageNumber = wcsrv_dll.GetLowMessageNumber
GetLowMessageNumber.argtypes = [ctypes.wintypes.DWORD]
GetLowMessageNumber.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetMessageById(DWORD conf, DWORD msgid, TMsgHeader &msg);
GetMessageById = wcsrv_dll.GetMessageById
GetMessageById.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TMsgHeader)]
GetMessageById.restype = ctypes.wintypes.BOOL

#//BOOL  APIENTRY GetMessageByRef(DWORD conf, DWORD refid, TMsgHeader &msg);
##DWORD APIENTRY GetMsgIdFromNumber(DWORD conf, DWORD number);
GetMsgIdFromNumber = wcsrv_dll.GetMsgIdFromNumber
GetMsgIdFromNumber.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetMsgIdFromNumber.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetMsgNumberFromId(DWORD conf, DWORD msgid);
GetMsgNumberFromId = wcsrv_dll.GetMsgNumberFromId
GetMsgNumberFromId.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetMsgNumberFromId.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GetNextMessage(TMsgHeader &msg);
GetNextMessage = wcsrv_dll.GetNextMessage
GetNextMessage.argtypes = [ctypes.POINTER(TMsgHeader)]
GetNextMessage.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetPrevMessage(TMsgHeader &msg);
GetPrevMessage = wcsrv_dll.GetPrevMessage
GetPrevMessage.argtypes = [ctypes.POINTER(TMsgHeader)]
GetPrevMessage.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY GetTotalMessages();
GetTotalMessages = wcsrv_dll.GetTotalMessages
GetTotalMessages.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetTotalMessagesInConference(DWORD conf);
GetTotalMessagesInConference = wcsrv_dll.GetTotalMessagesInConference
GetTotalMessagesInConference.argtypes = [ctypes.wintypes.DWORD]
GetTotalMessagesInConference.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetTotalMessagesInGroup(DWORD group);
GetTotalMessagesInGroup = wcsrv_dll.GetTotalMessagesInGroup
GetTotalMessagesInGroup.argtypes = [ctypes.wintypes.DWORD]
GetTotalMessagesInGroup.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY IncrementReplyCount(TMsgHeader &msg);
IncrementReplyCount = wcsrv_dll.IncrementReplyCount
IncrementReplyCount.argtypes = [ctypes.POINTER(TMsgHeader)]
IncrementReplyCount.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY IncrementReadCount(TMsgHeader &msg);
IncrementReadCount = wcsrv_dll.IncrementReadCount
IncrementReadCount.argtypes = [ctypes.POINTER(TMsgHeader)]
IncrementReadCount.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MarkMessageRead(TMsgHeader &msg);
MarkMessageRead = wcsrv_dll.MarkMessageRead
MarkMessageRead.argtypes = [ctypes.POINTER(TMsgHeader)]
MarkMessageRead.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MessageSearch(DWORD conf, DWORD msgid, DWORD msflags, const char *text, TMsgHeader &msg);
MessageSearch = wcsrv_dll.MessageSearch
MessageSearch.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, CString, ctypes.POINTER(TMsgHeader)]
MessageSearch.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchMessageById(DWORD conf, DWORD msgid, TMsgHeader &msg);
SearchMessageById = wcsrv_dll.SearchMessageById
SearchMessageById.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TMsgHeader)]
SearchMessageById.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetMessagePrivate(TMsgHeader &msg, BOOL pvt);
SetMessagePrivate = wcsrv_dll.SetMessagePrivate
SetMessagePrivate.argtypes = [ctypes.POINTER(TMsgHeader), ctypes.wintypes.BOOL]
SetMessagePrivate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY UpdateMessageFidoInfo(TMsgHeader &msg);
UpdateMessageFidoInfo = wcsrv_dll.UpdateMessageFidoInfo
UpdateMessageFidoInfo.argtypes = [ctypes.POINTER(TMsgHeader)]
UpdateMessageFidoInfo.restype = ctypes.wintypes.BOOL


#//BOOL  APIENTRY MessageSearchEx(DWORD conf,
#//                               DWORD msgid,
#//                               DWORD msflags,
#//                               const char *text,
#//                               TMsgHeader &msg,
#//                               // RPC_ASYNC_STATE *Async
#//                               PVOID Async);

#//////////////////////////////////////////////////////////////////////////////
#//! Use this function to define a group of conference numbers and to retrieve
#//! the highest msgid for each conference.
#//////////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetHighMessageIds(DWORD count, const DWORD *conferences, DWORD *ids);
GetHighMessageIds = wcsrv_dll.GetHighMessageIds
GetHighMessageIds.argtypes = [ctypes.wintypes.DWORD, DWORD, ctypes.POINTER(DWORD)]
GetHighMessageIds.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetMessageExported(TMsgHeader &msg, BOOL exported);
SetMessageExported = wcsrv_dll.SetMessageExported
SetMessageExported.argtypes = [ctypes.POINTER(TMsgHeader), ctypes.wintypes.BOOL]
SetMessageExported.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! The following functions access the user database in Wildcat.  Like the
#//! file database, GetUserByXxx gets a specific record, and SearchUserByXxx
#//! looks for a matching or the next higher record in the database.
#//! GetUserVariable and SetUserVariable can be used to store private
#//! application-specific information in a user record.  They are similar in
#//! use to the profile functions in the Windows API.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY AddNewUser(TUser &u);
AddNewUser = wcsrv_dll.AddNewUser
AddNewUser.argtypes = [ctypes.POINTER(TUser)]
AddNewUser.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY DeleteOtherUser(const TUser &u);
DeleteOtherUser = wcsrv_dll.DeleteOtherUser
DeleteOtherUser.argtypes = [TUser]
DeleteOtherUser.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserById(DWORD id, TUser &u, DWORD &tid);
GetUserById = wcsrv_dll.GetUserById
GetUserById.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetUserById.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserByLastName(const char *name, TUser &u, DWORD &tid);
GetUserByLastName = wcsrv_dll.GetUserByLastName
GetUserByLastName.argtypes = [CString, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetUserByLastName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserByName(const char *name, TUser &u, DWORD &tid);
GetUserByName = wcsrv_dll.GetUserByName
GetUserByName.argtypes = [CString, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetUserByName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserBySecurity(const char *security, TUser &u, DWORD &tid);
GetUserBySecurity = wcsrv_dll.GetUserBySecurity
GetUserBySecurity.argtypes = [CString, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetUserBySecurity.restype = ctypes.wintypes.BOOL

#BOOL  APIENTRY GetUserByLastCall(const FILETIME &ft, TUser &u, DWORD &tid);   // 452.1f
##BOOL APIENTRY GetUserVariable(DWORD id, const char *section, const char *key, const char *def, char *dest, DWORD destsize);
GetUserVariable = wcsrv_dll.GetUserVariable
GetUserVariable.argtypes = [ctypes.wintypes.DWORD, CString, CString, CString, ctypes.c_char_p, ctypes.wintypes.DWORD]
GetUserVariable.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserVariables(DWORD id, void *buffer, DWORD requested, DWORD *read);
GetUserVariables = wcsrv_dll.GetUserVariables
GetUserVariables.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(ctypes.c_void_p), ctypes.wintypes.DWORD, ctypes.POINTER(DWORD)]
GetUserVariables.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetFirstUser(DWORD keynum, TUser &u, DWORD &tid);
GetFirstUser = wcsrv_dll.GetFirstUser
GetFirstUser.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetFirstUser.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetLastUser(DWORD keynum, TUser &u, DWORD &tid);
GetLastUser = wcsrv_dll.GetLastUser
GetLastUser.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetLastUser.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetNextUser(DWORD keynum, TUser &u, DWORD &tid);
GetNextUser = wcsrv_dll.GetNextUser
GetNextUser.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetNextUser.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetPrevUser(DWORD keynum, TUser &u, DWORD &tid);
GetPrevUser = wcsrv_dll.GetPrevUser
GetPrevUser.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetPrevUser.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY GetTotalUsers();
GetTotalUsers = wcsrv_dll.GetTotalUsers
GetTotalUsers.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY SearchUserById(DWORD id, TUser &u, DWORD &tid);
SearchUserById = wcsrv_dll.SearchUserById
SearchUserById.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
SearchUserById.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchUserByLastName(const char *name, TUser &u, DWORD &tid);
SearchUserByLastName = wcsrv_dll.SearchUserByLastName
SearchUserByLastName.argtypes = [CString, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
SearchUserByLastName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchUserByName(const char *name, TUser &u, DWORD &tid);
SearchUserByName = wcsrv_dll.SearchUserByName
SearchUserByName.argtypes = [CString, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
SearchUserByName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SearchUserBySecurity(const char *security, TUser &u, DWORD &tid);
SearchUserBySecurity = wcsrv_dll.SearchUserBySecurity
SearchUserBySecurity.argtypes = [CString, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
SearchUserBySecurity.restype = ctypes.wintypes.BOOL

#BOOL  APIENTRY SearchUserByLastCall(const FILETIME &ft, TUser &u, DWORD &tid);   // 452.1f
##BOOL APIENTRY SetUserVariable(DWORD id, const char *section, const char *key, const char *data);
SetUserVariable = wcsrv_dll.SetUserVariable
SetUserVariable.argtypes = [ctypes.wintypes.DWORD, CString, CString, CString]
SetUserVariable.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY UpdateUser(TUser &u);
UpdateUser = wcsrv_dll.UpdateUser
UpdateUser.argtypes = [ctypes.POINTER(TUser)]
UpdateUser.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Convenience functions for accessing the set of conferences that the user
#//! can access.  The 'flags' parameter in these functions refers to the
#//! user's per-conference read flags.  Using 0 as the 'flags' parameter
#//! means ignore it when looking for conferences.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetEffectiveConferenceGroupCount();
GetEffectiveConferenceGroupCount = wcsrv_dll.GetEffectiveConferenceGroupCount
GetEffectiveConferenceGroupCount.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetEffectiveConferenceCount(DWORD group, DWORD flags);
GetEffectiveConferenceCount = wcsrv_dll.GetEffectiveConferenceCount
GetEffectiveConferenceCount.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetEffectiveConferenceCount.restype = ctypes.wintypes.DWORD

##long APIENTRY GetFirstConference(DWORD group, DWORD flags);
GetFirstConference = wcsrv_dll.GetFirstConference
GetFirstConference.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetFirstConference.restype = ctypes.c_long

##long APIENTRY GetLastConference(DWORD group, DWORD flags);
GetLastConference = wcsrv_dll.GetLastConference
GetLastConference.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetLastConference.restype = ctypes.c_long

##long APIENTRY GetNextConference(DWORD group, DWORD flags, DWORD conf);
GetNextConference = wcsrv_dll.GetNextConference
GetNextConference.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetNextConference.restype = ctypes.c_long

##long APIENTRY GetPrevConference(DWORD group, DWORD flags, DWORD conf);
GetPrevConference = wcsrv_dll.GetPrevConference
GetPrevConference.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetPrevConference.restype = ctypes.c_long

##long APIENTRY GetFirstConferenceUnread();
GetFirstConferenceUnread = wcsrv_dll.GetFirstConferenceUnread
GetFirstConferenceUnread.restype = ctypes.c_long

##long APIENTRY GetNextConferenceUnread(DWORD conf);
GetNextConferenceUnread = wcsrv_dll.GetNextConferenceUnread
GetNextConferenceUnread.argtypes = [ctypes.wintypes.DWORD]
GetNextConferenceUnread.restype = ctypes.c_long

##long APIENTRY GetPrevConferenceUnread(DWORD conf);
GetPrevConferenceUnread = wcsrv_dll.GetPrevConferenceUnread
GetPrevConferenceUnread.argtypes = [ctypes.wintypes.DWORD]
GetPrevConferenceUnread.restype = ctypes.c_long

##BOOL APIENTRY IsConferenceInGroup(DWORD group, DWORD conf);
IsConferenceInGroup = wcsrv_dll.IsConferenceInGroup
IsConferenceInGroup.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
IsConferenceInGroup.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Convenience functions for accessing the set of file areas that the user
#//! can access.  Unlike the conference functions, the 'flags' parameter in
#//! these functions refers to the user's access flags in the file area
#//! (that is, list/download/upload/sysop).  Using 0 as the 'flags' parameter
#//! means ignore it when looking for file areas.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetEffectiveFileGroupCount();
GetEffectiveFileGroupCount = wcsrv_dll.GetEffectiveFileGroupCount
GetEffectiveFileGroupCount.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetEffectiveFileAreaCount(DWORD group, DWORD flags);
GetEffectiveFileAreaCount = wcsrv_dll.GetEffectiveFileAreaCount
GetEffectiveFileAreaCount.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetEffectiveFileAreaCount.restype = ctypes.wintypes.DWORD

##long APIENTRY GetFirstFileArea(DWORD group, DWORD flags);
GetFirstFileArea = wcsrv_dll.GetFirstFileArea
GetFirstFileArea.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetFirstFileArea.restype = ctypes.c_long

##long APIENTRY GetLastFileArea(DWORD group, DWORD flags);
GetLastFileArea = wcsrv_dll.GetLastFileArea
GetLastFileArea.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetLastFileArea.restype = ctypes.c_long

##long APIENTRY GetNextFileArea(DWORD group, DWORD flags, DWORD area);
GetNextFileArea = wcsrv_dll.GetNextFileArea
GetNextFileArea.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetNextFileArea.restype = ctypes.c_long

##long APIENTRY GetPrevFileArea(DWORD group, DWORD flags, DWORD area);
GetPrevFileArea = wcsrv_dll.GetPrevFileArea
GetPrevFileArea.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetPrevFileArea.restype = ctypes.c_long

##BOOL APIENTRY IsFileAreaInGroup(DWORD group, DWORD area);
IsFileAreaInGroup = wcsrv_dll.IsFileAreaInGroup
IsFileAreaInGroup.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
IsFileAreaInGroup.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Functions to get and set the current user's per-conference information.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetLastRead(DWORD conf);
GetLastRead = wcsrv_dll.GetLastRead
GetLastRead.argtypes = [ctypes.wintypes.DWORD]
GetLastRead.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetFirstUnread(DWORD conf);
GetFirstUnread = wcsrv_dll.GetFirstUnread
GetFirstUnread.argtypes = [ctypes.wintypes.DWORD]
GetFirstUnread.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetConfFlags(DWORD conf);
GetConfFlags = wcsrv_dll.GetConfFlags
GetConfFlags.argtypes = [ctypes.wintypes.DWORD]
GetConfFlags.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY SetLastRead(DWORD conf, DWORD lastread);
SetLastRead = wcsrv_dll.SetLastRead
SetLastRead.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
SetLastRead.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetConfFlags(DWORD conf, DWORD flags);
SetConfFlags = wcsrv_dll.SetConfFlags
SetConfFlags.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
SetConfFlags.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Functions to get and set an arbitrary user's per-conference information.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY GetUserLastRead(DWORD userid, DWORD conf);
GetUserLastRead = wcsrv_dll.GetUserLastRead
GetUserLastRead.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetUserLastRead.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetUserFirstUnread(DWORD userid, DWORD conf);
GetUserFirstUnread = wcsrv_dll.GetUserFirstUnread
GetUserFirstUnread.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetUserFirstUnread.restype = ctypes.wintypes.DWORD

##DWORD APIENTRY GetUserConfFlags(DWORD userid, DWORD conf);
GetUserConfFlags = wcsrv_dll.GetUserConfFlags
GetUserConfFlags.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GetUserConfFlags.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY SetUserLastRead(DWORD userid, DWORD conf, DWORD lastread);
SetUserLastRead = wcsrv_dll.SetUserLastRead
SetUserLastRead.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
SetUserLastRead.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetUserConfFlags(DWORD userid, DWORD conf, DWORD flags);
SetUserConfFlags = wcsrv_dll.SetUserConfFlags
SetUserConfFlags.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
SetUserConfFlags.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Write an entry to a log file.  The 'fname' parameter must NOT contain a
#//! full path, just a file name.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY WriteLogEntry(const char *fname, const char *text);
WriteLogEntry = wcsrv_dll.WriteLogEntry
WriteLogEntry.argtypes = [CString, CString]
WriteLogEntry.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Write an entry to the current node's activity log file.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY WriteActivityLogEntry(const char *text);
WriteActivityLogEntry = wcsrv_dll.WriteActivityLogEntry
WriteActivityLogEntry.argtypes = [CString]
WriteActivityLogEntry.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Check the spelling of a string based on the server's spelling dictionary.
#//! Returns the position and length of the bad word, if any.
#//! - Suggest alternate spellings for a misspelled word.
#//! - Add a word to the auxiliary dictionary.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY SpellCheckLine(const char *s, DWORD startpos, DWORD &badpos, DWORD &badlen);
SpellCheckLine = wcsrv_dll.SpellCheckLine
SpellCheckLine.argtypes = [CString, ctypes.wintypes.DWORD, ctypes.POINTER(DWORD), ctypes.POINTER(DWORD)]
SpellCheckLine.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY SpellCheckSuggest(const char *s, TSpellSuggestList &sl);
SpellCheckSuggest = wcsrv_dll.SpellCheckSuggest
SpellCheckSuggest.argtypes = [CString, ctypes.POINTER(TSpellSuggestList)]
SpellCheckSuggest.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY SpellCheckAddWord(const char *s);
SpellCheckAddWord = wcsrv_dll.SpellCheckAddWord
SpellCheckAddWord.argtypes = [CString]
SpellCheckAddWord.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Open a communications channel.  Channels are named, and created on the
#//! fly as necessary.  Messages can either be broadcast ('destid'=0), or
#//! directed to a specific recipient.  The 'userdata' parameter can be used
#//! to distinguish different formats of the message data.
#///////////////////////////////////////////////////////////////////////////

##DWORD APIENTRY OpenChannel(const char *name);
OpenChannel = wcsrv_dll.OpenChannel
OpenChannel.argtypes = [CString]
OpenChannel.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY CloseChannel(DWORD chandle);
CloseChannel = wcsrv_dll.CloseChannel
CloseChannel.argtypes = [ctypes.wintypes.DWORD]
CloseChannel.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WriteChannel(DWORD chandle, DWORD destid, DWORD userdata, const void *data, DWORD datasize);
WriteChannel = wcsrv_dll.WriteChannel
WriteChannel.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.c_void_p, ctypes.wintypes.DWORD]
WriteChannel.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Get the Qwk packet size limits based on the user's reported speed.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetQwkBaudLimits(DWORD &perpacket, DWORD &perconference);
GetQwkBaudLimits = wcsrv_dll.GetQwkBaudLimits
GetQwkBaudLimits.argtypes = [ctypes.POINTER(DWORD), ctypes.POINTER(DWORD)]
GetQwkBaudLimits.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Retrieve a service record by name.  The service record contains an
#//! appropriate IP address and port to pass to connect() to establish
#//! communications with the service.  Since the communications with the
#//! service does not take place through the Wildcat server, no security or
#//! authentication is provided by default.  The
#//! GetWildcatServerContextHandle and WildcatServerCreateContextByHandle
#//! functions are useful if you need to communicate with the Wildcat server
#//! under the context of a logged in user.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetServiceByName(const char *name, TWildcatService &service);
GetServiceByName = wcsrv_dll.GetServiceByName
GetServiceByName.argtypes = [CString, ctypes.POINTER(TWildcatService)]
GetServiceByName.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Register a service with the Wildcat server.  The port number must be
#//! filled in before calling this function.  The service remains registered
#//! until the process running the service is disconnected from the Wildcat
#//! server.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY RegisterService(TWildcatService &service);
RegisterService = wcsrv_dll.RegisterService
RegisterService.argtypes = [ctypes.POINTER(TWildcatService)]
RegisterService.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY CheckNetworkAddress(DWORD clientip);
CheckNetworkAddress = wcsrv_dll.CheckNetworkAddress
CheckNetworkAddress.argtypes = [ctypes.wintypes.DWORD]
CheckNetworkAddress.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! These functions are used to arbitrate access to CD-ROM changers and such
#//! when files are marked for copy-before-download.  After submitting the
#//! pathnames of the files to be retrieved, with a unique Id for each file,
#//! GetNextCopyRequest should be called in a loop to determine which file to
#//! copy next.  If a positive number is returned, it is the id of a request
#//! to copy.  If 0 is returned, there are no more requests.  If -1 is
#//! returned there are still requests pending and the application should
#//! delay for a short time and keep trying.  When a file has finished
#//! copying, RemoveCopyRequest must be called so that other clients may
#//! access files they have queued.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY SubmitCopyRequest(DWORD id, const char *fn);
SubmitCopyRequest = wcsrv_dll.SubmitCopyRequest
SubmitCopyRequest.argtypes = [ctypes.wintypes.DWORD, CString]
SubmitCopyRequest.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY GetNextCopyRequest();
GetNextCopyRequest = wcsrv_dll.GetNextCopyRequest
GetNextCopyRequest.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY RemoveCopyRequest(DWORD id);
RemoveCopyRequest = wcsrv_dll.RemoveCopyRequest
RemoveCopyRequest.argtypes = [ctypes.wintypes.DWORD]
RemoveCopyRequest.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Return connection info for the given connectionid or the next higher
#//! connectionid. Returns FALSE when there is no higher connectionid.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetConnectionInfo(DWORD connectionid, TConnectionInfo &ci);
GetConnectionInfo = wcsrv_dll.GetConnectionInfo
GetConnectionInfo.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TConnectionInfo)]
GetConnectionInfo.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! Modify the amount of time the current user has remaining for the day.
#//! Negative values are ok.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY AdjustUserTime(long minutes);
AdjustUserTime = wcsrv_dll.AdjustUserTime
AdjustUserTime.argtypes = [ctypes.c_long]
AdjustUserTime.restype = ctypes.wintypes.BOOL


#//$SDK(0)
#///////////////////////////////////////////////////////////////////////////
#//! These functions are for tracking current PPP connections. There is
#//! a background thread in Wconline that periodically calls
#//! GetValidPPPAddresses so it can close sockets associated with a PPP
#//! connection that has been terminated.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY RegisterPPPAddress(DWORD address);
RegisterPPPAddress = wcsrv_dll.RegisterPPPAddress
RegisterPPPAddress.argtypes = [ctypes.wintypes.DWORD]
RegisterPPPAddress.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY UnregisterPPPAddress(DWORD address);
UnregisterPPPAddress = wcsrv_dll.UnregisterPPPAddress
UnregisterPPPAddress.argtypes = [ctypes.wintypes.DWORD]
UnregisterPPPAddress.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetValidPPPAddresses(DWORD *addrs, DWORD &addrlen);
GetValidPPPAddresses = wcsrv_dll.GetValidPPPAddresses
GetValidPPPAddresses.argtypes = [ctypes.POINTER(DWORD), ctypes.POINTER(DWORD)]
GetValidPPPAddresses.restype = ctypes.wintypes.BOOL

#//$SDK(1)

#//////////////// NEW SERVER FUNCTION BUILD 446 //////////////

##BOOL APIENTRY GetWildcatServerInfo(TWildcatServerInfo &si);
GetWildcatServerInfo = wcsrv_dll.GetWildcatServerInfo
GetWildcatServerInfo.argtypes = [ctypes.POINTER(TWildcatServerInfo)]
GetWildcatServerInfo.restype = ctypes.wintypes.BOOL


#//////////////// NEW SERVER FUNCTION BUILD 447B2 //////////////

##BOOL APIENTRY GetUserByKeyIndex(DWORD keynum, DWORD idx, TUser &u, DWORD &tid);
GetUserByKeyIndex = wcsrv_dll.GetUserByKeyIndex
GetUserByKeyIndex.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TUser), ctypes.POINTER(DWORD)]
GetUserByKeyIndex.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY CheckClientAddress(DWORD clientip, const char *szIPFile);
CheckClientAddress = wcsrv_dll.CheckClientAddress
CheckClientAddress.argtypes = [ctypes.wintypes.DWORD, CString]
CheckClientAddress.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY CheckClientAddressEx(DWORD clientip, const char *szIPFile);
CheckClientAddressEx = wcsrv_dll.CheckClientAddressEx
CheckClientAddressEx.argtypes = [ctypes.wintypes.DWORD, CString]
CheckClientAddressEx.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY CheckMailIntegrity(DWORD conf, DWORD level);
CheckMailIntegrity = wcsrv_dll.CheckMailIntegrity
CheckMailIntegrity.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
CheckMailIntegrity.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY UpdateMessageFlags(TMsgHeader &msg);
UpdateMessageFlags = wcsrv_dll.UpdateMessageFlags
UpdateMessageFlags.argtypes = [ctypes.POINTER(TMsgHeader)]
UpdateMessageFlags.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY DeleteMessageAttachment(TMsgHeader &msg);
DeleteMessageAttachment = wcsrv_dll.DeleteMessageAttachment
DeleteMessageAttachment.argtypes = [ctypes.POINTER(TMsgHeader)]
DeleteMessageAttachment.restype = ctypes.wintypes.BOOL


#/////////////////// HELPER FUNCTIONS (NON RPC) /////////////////

#///////////////////////////////////////////////////////////////////////////
#//! Given computer name, return the server options for the particular machine.
#//! If computer name is "" or null, it will turn the default settings for the
#//! system wide services.  If you want the current computer server settings,
#//! use GetComputerConfig(cc) instead.
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GetComputerConfigEx(char *szComputerName, TComputerConfig &cc);
GetComputerConfigEx = wcsrv_dll.GetComputerConfigEx
GetComputerConfigEx.argtypes = [ctypes.c_char_p, ctypes.POINTER(TComputerConfig)]
GetComputerConfigEx.restype = ctypes.wintypes.BOOL


#///////////////////////////////////////////////////////////////////////////
#//! User Extended Database/Profile Helper Functions
#///////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY ProfileDateToFileDate(const char *szInt64, FILETIME &ft);
ProfileDateToFileDate = wcsrv_dll.ProfileDateToFileDate
ProfileDateToFileDate.argtypes = [CString, ctypes.POINTER(FILETIME)]
ProfileDateToFileDate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserVariableDate(DWORD id,const char *section,const char *key,FILETIME &ft);
GetUserVariableDate = wcsrv_dll.GetUserVariableDate
GetUserVariableDate.argtypes = [ctypes.wintypes.DWORD, CString, CString, ctypes.POINTER(FILETIME)]
GetUserVariableDate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserProfileDate(DWORD id,const char *key,FILETIME &ft);
GetUserProfileDate = wcsrv_dll.GetUserProfileDate
GetUserProfileDate.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(FILETIME)]
GetUserProfileDate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserProfileDateStr(DWORD id,const char *key,const char *format,char *dest,DWORD destsize);
GetUserProfileDateStr = wcsrv_dll.GetUserProfileDateStr
GetUserProfileDateStr.argtypes = [ctypes.wintypes.DWORD, CString, CString, ctypes.c_char_p, ctypes.wintypes.DWORD]
GetUserProfileDateStr.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserProfileTimeStr(DWORD id,const char *key,const char *format,char *dest,DWORD destsize);
GetUserProfileTimeStr = wcsrv_dll.GetUserProfileTimeStr
GetUserProfileTimeStr.argtypes = [ctypes.wintypes.DWORD, CString, CString, ctypes.c_char_p, ctypes.wintypes.DWORD]
GetUserProfileTimeStr.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetUserVariableDate(DWORD id,const char *section,const char *key,FILETIME &ft);
SetUserVariableDate = wcsrv_dll.SetUserVariableDate
SetUserVariableDate.argtypes = [ctypes.wintypes.DWORD, CString, CString, ctypes.POINTER(FILETIME)]
SetUserVariableDate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetUserProfileDate(DWORD id, const char *key, FILETIME &ft);
SetUserProfileDate = wcsrv_dll.SetUserProfileDate
SetUserProfileDate.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(FILETIME)]
SetUserProfileDate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetUserProfileSystemTime(DWORD id,const char *key,SYSTEMTIME &st);
SetUserProfileSystemTime = wcsrv_dll.SetUserProfileSystemTime
SetUserProfileSystemTime.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(SYSTEMTIME)]
SetUserProfileSystemTime.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GetUserProfileBool(DWORD id, const char *key, BOOL &flag);
GetUserProfileBool = wcsrv_dll.GetUserProfileBool
GetUserProfileBool.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(BOOL)]
GetUserProfileBool.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY SetUserProfileBool(DWORD id, const char *key, BOOL flag);
SetUserProfileBool = wcsrv_dll.SetUserProfileBool
SetUserProfileBool.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.wintypes.BOOL]
SetUserProfileBool.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY wcCopyFileToTemp(DWORD area, const char *fn);
wcCopyFileToTemp = wcsrv_dll.wcCopyFileToTemp
wcCopyFileToTemp.argtypes = [ctypes.wintypes.DWORD, CString]
wcCopyFileToTemp.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY UpdateUserEx(TUser &user, const char *oldpwd, const char *newpwd);
UpdateUserEx = wcsrv_dll.UpdateUserEx
UpdateUserEx.argtypes = [ctypes.POINTER(TUser), CString, CString]
UpdateUserEx.restype = ctypes.wintypes.BOOL


#//!
#//! Wildcat! SASL functions for authentication services
#//!
##BOOL APIENTRY WcSASLGetMethodName(char *szMethod,                 const DWORD dwSize,                 const DWORD dwIndex);
WcSASLGetMethodName = wcsrv_dll.WcSASLGetMethodName
WcSASLGetMethodName.argtypes = [ctypes.c_char_p, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
WcSASLGetMethodName.restype = ctypes.wintypes.BOOL


#//!
#//! Check the SASL Login credentials (user is logged in)
#//!
##DWORD APIENTRY WcSASLAuthenticateUser(TWildcatSASLContext *ctx,                   const char *szFromClient,                   char *szResponse,                   const DWORD dwResponseSize,                   TUser &u);
WcSASLAuthenticateUser = wcsrv_dll.WcSASLAuthenticateUser
WcSASLAuthenticateUser.argtypes = [ctypes.POINTER(TWildcatSASLContext), CString, ctypes.c_char_p, ctypes.wintypes.DWORD, ctypes.POINTER(TUser)]
WcSASLAuthenticateUser.restype = ctypes.wintypes.DWORD


#//!
#//! Check the SASL Login credentials (user is logged in)
#//!
##DWORD APIENTRY WcSASLAuthenticateUserEx(TWildcatSASLContext *ctx,                    const char *szFromClient,                    char *szResponse,                    const DWORD dwResponseSize,                    const DWORD dwCallType,                    const char *szSpeed,                    TUser &u);
WcSASLAuthenticateUserEx = wcsrv_dll.WcSASLAuthenticateUserEx
WcSASLAuthenticateUserEx.argtypes = [ctypes.POINTER(TWildcatSASLContext), CString, ctypes.c_char_p, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, CString, ctypes.POINTER(TUser)]
WcSASLAuthenticateUserEx.restype = ctypes.wintypes.DWORD


#//!
#//! Check the SASL Login credentials (user is not logged in)
#//!
##DWORD APIENTRY WcSASLCheckAuthentication(TWildcatSASLContext *ctx,                     const char *szFromClient,                     char *szResponse,                     const DWORD dwResponseSize);
WcSASLCheckAuthentication = wcsrv_dll.WcSASLCheckAuthentication
WcSASLCheckAuthentication.argtypes = [ctypes.POINTER(TWildcatSASLContext), CString, ctypes.c_char_p, ctypes.wintypes.DWORD]
WcSASLCheckAuthentication.restype = ctypes.wintypes.DWORD


#//!
#//! Get the wildcat server process running times
#//!
##BOOL APIENTRY WcGetProcessTimes(TWildcatProcessTimes &pt);
WcGetProcessTimes = wcsrv_dll.WcGetProcessTimes
WcGetProcessTimes.argtypes = [ctypes.POINTER(TWildcatProcessTimes)]
WcGetProcessTimes.restype = ctypes.wintypes.BOOL


#//!
#//! Set the context peer address
#//!
##BOOL APIENTRY SetContextPeerAddress(const DWORD address);
SetContextPeerAddress = wcsrv_dll.SetContextPeerAddress
SetContextPeerAddress.argtypes = [ctypes.wintypes.DWORD]
SetContextPeerAddress.restype = ctypes.wintypes.BOOL


#//! Wildcat! INI File Functions. These Wildcat! INI file
#//! functions work similar to the Win32 equivalent private
#//! profile functions. The key difference is that Win32
#//! INI files are local to the machine, where these Wildcat!
#//! INI functions use server side files using the Wildcat!
#//! file naming syntax, i.e., "wc:\data\productxyz.ini"
#//!

##BOOL APIENTRY WcGetPrivateProfileString         (const char *sect,          const char *key,          const char *defvalue,          char *dest,          DWORD *destsize,          const char *inifile);
WcGetPrivateProfileString = wcsrv_dll.WcGetPrivateProfileString
WcGetPrivateProfileString.argtypes = [CString, CString, CString, ctypes.c_char_p, ctypes.POINTER(DWORD), CString]
WcGetPrivateProfileString.restype = ctypes.wintypes.BOOL


##BOOL APIENTRY WcWritePrivateProfileString         (const char *sect,          const char *key,          const char *value,          const char *inifile);
WcWritePrivateProfileString = wcsrv_dll.WcWritePrivateProfileString
WcWritePrivateProfileString.argtypes = [CString, CString, CString, CString]
WcWritePrivateProfileString.restype = ctypes.wintypes.BOOL


##BOOL APIENTRY WcGetPrivateProfileSection         (const char *sect,          char *dest,          DWORD *destsize,          const char *inifile);
WcGetPrivateProfileSection = wcsrv_dll.WcGetPrivateProfileSection
WcGetPrivateProfileSection.argtypes = [CString, ctypes.c_char_p, ctypes.POINTER(DWORD), CString]
WcGetPrivateProfileSection.restype = ctypes.wintypes.BOOL



#//! Extended WcCreateFileEx() function returns TwcOpenFileInfo
#//! structure. Useful when you need to open a file and obtain
#//! file information in one single RPC call.

##WCHANDLE APIENTRY WcCreateFileEx         (const char *fn,          DWORD access,          DWORD sharemode,          DWORD create,          TwcOpenFileInfo *pwcofi);
WcCreateFileEx = wcsrv_dll.WcCreateFileEx
WcCreateFileEx.argtypes = [CString, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TwcOpenFileInfo)]
WcCreateFileEx.restype = ctypes.wintypes.HANDLE


#//! GetConnectionInfoFromChallenge() function returns TConnectionInfo
#//! for a given challenge.

##BOOL APIENTRY GetConnectionInfoFromChallenge(const char *challenge,                       TConnectionInfo &ci);
GetConnectionInfoFromChallenge = wcsrv_dll.GetConnectionInfoFromChallenge
GetConnectionInfoFromChallenge.argtypes = [CString, ctypes.POINTER(TConnectionInfo)]
GetConnectionInfoFromChallenge.restype = ctypes.wintypes.BOOL


#//! DeleteUserVariable - delete extended user section or key

##BOOL APIENTRY DeleteUserVariable(DWORD id,                 const char *section,                 const char *key);
DeleteUserVariable = wcsrv_dll.DeleteUserVariable
DeleteUserVariable.argtypes = [ctypes.wintypes.DWORD, CString, CString]
DeleteUserVariable.restype = ctypes.wintypes.BOOL


#//! WcCheckUserName - Return FALSE if user name has invalid characters

##BOOL APIENTRY WcCheckUserName(const char *szName);
WcCheckUserName = wcsrv_dll.WcCheckUserName
WcCheckUserName.argtypes = [CString]
WcCheckUserName.restype = ctypes.wintypes.BOOL


#//! WcSetMessageAttachments - helps prepare attachment field

##BOOL APIENTRY WcSetMessageAttachment(TMsgHeader &msg,                   const char *szFileName,                   const BOOL bCopyTo);
WcSetMessageAttachment = wcsrv_dll.WcSetMessageAttachment
WcSetMessageAttachment.argtypes = [ctypes.POINTER(TMsgHeader), CString, ctypes.wintypes.BOOL]
WcSetMessageAttachment.restype = ctypes.wintypes.BOOL


#//! WcLocalCopyToServer - copy local side file to server side wc:\ file

##BOOL APIENTRY WcLocalCopyToServer(const char *szLocal,                 const char *szServer,                 const int msSlice);
WcLocalCopyToServer = wcsrv_dll.WcLocalCopyToServer
WcLocalCopyToServer.argtypes = [CString, CString, ctypes.c_int]
WcLocalCopyToServer.restype = ctypes.wintypes.BOOL



#//! Domain Server Functions

##BOOL APIENTRY GetMakewildEx(const char *szDomain, const BOOL setdomain, TMakewild &mw);
GetMakewildEx = wcsrv_dll.GetMakewildEx
GetMakewildEx.argtypes = [CString, ctypes.wintypes.BOOL, ctypes.POINTER(TMakewild)]
GetMakewildEx.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcSetCurrentDomain(const char *szDomain);
WcSetCurrentDomain = wcsrv_dll.WcSetCurrentDomain
WcSetCurrentDomain.argtypes = [CString]
WcSetCurrentDomain.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetCurrentDomain(char *szDomain, DWORD dwSize);
WcGetCurrentDomain = wcsrv_dll.WcGetCurrentDomain
WcGetCurrentDomain.argtypes = [ctypes.c_char_p, ctypes.wintypes.DWORD]
WcGetCurrentDomain.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetDefaultDomain(char *szBuffer, const DWORD dwSize);
WcGetDefaultDomain = wcsrv_dll.WcGetDefaultDomain
WcGetDefaultDomain.argtypes = [ctypes.c_char_p, ctypes.wintypes.DWORD]
WcGetDefaultDomain.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY WcGetDomainCount();
WcGetDomainCount = wcsrv_dll.WcGetDomainCount
WcGetDomainCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY WcGetDomain(const DWORD index, char *szDomain, DWORD dwSize);
WcGetDomain = wcsrv_dll.WcGetDomain
WcGetDomain.argtypes = [ctypes.wintypes.DWORD, ctypes.c_char_p, ctypes.wintypes.DWORD]
WcGetDomain.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetDomainConfigString(const char *szDomain, const char *szSection, const char *szKey, char *szValue, const DWORD dwSize, const char *szDefault);
WcGetDomainConfigString = wcsrv_dll.WcGetDomainConfigString
WcGetDomainConfigString.argtypes = [CString, CString, CString, ctypes.c_char_p, ctypes.wintypes.DWORD, CString]
WcGetDomainConfigString.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetDomainConfigBool(const char *szDomain, const char *szSection, const char *szKey, BOOL *bVal, BOOL bDef);
WcGetDomainConfigBool = wcsrv_dll.WcGetDomainConfigBool
WcGetDomainConfigBool.argtypes = [CString, CString, CString, ctypes.POINTER(BOOL), ctypes.wintypes.BOOL]
WcGetDomainConfigBool.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetDomainConfigInt(const char *szDomain, const char *szSection, const char *szKey, DWORD *dwValue, DWORD dwDefault);
WcGetDomainConfigInt = wcsrv_dll.WcGetDomainConfigInt
WcGetDomainConfigInt.argtypes = [CString, CString, CString, ctypes.POINTER(DWORD), ctypes.wintypes.DWORD]
WcGetDomainConfigInt.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetDomainConfigSection(const char *szDomain, const char *szSection, char *szBuffer, const DWORD dwBufSize, DWORD *dwSize);
WcGetDomainConfigSection = wcsrv_dll.WcGetDomainConfigSection
WcGetDomainConfigSection.argtypes = [CString, CString, ctypes.c_char_p, ctypes.wintypes.DWORD, ctypes.POINTER(DWORD)]
WcGetDomainConfigSection.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetHttpConfigVar(const char *szSection, const char *szKey, char *szValue, const DWORD dwSize, const char *szDefault);
WcGetHttpConfigVar = wcsrv_dll.WcGetHttpConfigVar
WcGetHttpConfigVar.argtypes = [CString, CString, ctypes.c_char_p, ctypes.wintypes.DWORD, CString]
WcGetHttpConfigVar.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetConfigFileVar(const char *szFile, const char *szSection, const char *szKey, char *szValue, const DWORD dwSize, const char *szDefault);
WcGetConfigFileVar = wcsrv_dll.WcGetConfigFileVar
WcGetConfigFileVar.argtypes = [CString, CString, CString, ctypes.c_char_p, ctypes.wintypes.DWORD, CString]
WcGetConfigFileVar.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetVirtualDomainBool(const char *szDomain, const char *szSection, const char *szKey, BOOL *bVal, BOOL bDef);
WcGetVirtualDomainBool = wcsrv_dll.WcGetVirtualDomainBool
WcGetVirtualDomainBool.argtypes = [CString, CString, CString, ctypes.POINTER(BOOL), ctypes.wintypes.BOOL]
WcGetVirtualDomainBool.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY WcGetVirtualDomainVar(const char *szDomain,                  const char *szSection,                  const char *szKey,                  char *szValue,                  const DWORD dwSize,                  const char *szDefault);
WcGetVirtualDomainVar = wcsrv_dll.WcGetVirtualDomainVar
WcGetVirtualDomainVar.argtypes = [CString, CString, CString, ctypes.c_char_p, ctypes.wintypes.DWORD, CString]
WcGetVirtualDomainVar.restype = ctypes.wintypes.BOOL


#//! Set Context/Connection Status (activity)

##BOOL APIENTRY WcSetConnectionStatus(const char *activity);
WcSetConnectionStatus = wcsrv_dll.WcSetConnectionStatus
WcSetConnectionStatus.argtypes = [CString]
WcSetConnectionStatus.restype = ctypes.wintypes.BOOL


#//! Get unique server guid across all clients, see structure TWildcatServerGuid
#//!

##BOOL APIENTRY WcGetWildcatServerGuid(TWildcatServerGuid &wg);
WcGetWildcatServerGuid = wcsrv_dll.WcGetWildcatServerGuid
WcGetWildcatServerGuid.argtypes = [ctypes.POINTER(TWildcatServerGuid)]
WcGetWildcatServerGuid.restype = ctypes.wintypes.BOOL


#//! Get unique QUEUE guid, see structure TWildcatServerGuid
#//!

##BOOL APIENTRY WcGetWildcatQueueGuid(const char *qname, TWildcatServerGuid &wg);
WcGetWildcatQueueGuid = wcsrv_dll.WcGetWildcatQueueGuid
WcGetWildcatQueueGuid.argtypes = [CString, ctypes.POINTER(TWildcatServerGuid)]
WcGetWildcatQueueGuid.restype = ctypes.wintypes.BOOL


#//! Get Geographical Location Information by IP Address
#//!

##BOOL APIENTRY WcGetGeoIP(const char *ip, TWildcatGeoIP &geoip, const char *lang);
WcGetGeoIP = wcsrv_dll.WcGetGeoIP
WcGetGeoIP.argtypes = [CString, ctypes.POINTER(TWildcatGeoIP), CString]
WcGetGeoIP.restype = ctypes.wintypes.BOOL



#} // extern "C"

