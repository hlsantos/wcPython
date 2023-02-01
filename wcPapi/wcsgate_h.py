# Auto-Created by cpp2py.py
import os
from wcpapi.wctype_constants_h import *
from wcpapi.wctype_h import *
from wcpapi.wcgtype_constants_h import *
from wcpapi.wcgtype_h import *
from wcpapi.__init__ import *

wcsgate_dll = initialize_wcsgate_dll()

#//***********************************************************************
#// (c) Copyright 1998-2002 Santronics Software, Inc. All Rights Reserved.
#//***********************************************************************
#//
#// File Name : wcsgate.h
#// Subsystem : header for to access networking structures
#// Date      :
#// Author    :
#//
#// Revision History:
#// Build  Date      Author  Comments
#// -----  --------  ------  ---------------------------------------------
#//***********************************************************************




#//+ Group: Configuration Gateway SDK Functions

##DWORD APIENTRY GateGetQwkHostCount();
GateGetQwkHostCount = wcsgate_dll.GateGetQwkHostCount
GateGetQwkHostCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GateGetQwkHostByIndex(DWORD index, TGateQwkHost &host);
GateGetQwkHostByIndex = wcsgate_dll.GateGetQwkHostByIndex
GateGetQwkHostByIndex.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TGateQwkHost)]
GateGetQwkHostByIndex.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateGetQwkHostByName(const char *hostname, TGateQwkHost &host);
GateGetQwkHostByName = wcsgate_dll.GateGetQwkHostByName
GateGetQwkHostByName.argtypes = [CString, ctypes.POINTER(TGateQwkHost)]
GateGetQwkHostByName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateAddQwkHost(const TGateQwkHost &host, DWORD &index);
GateAddQwkHost = wcsgate_dll.GateAddQwkHost
GateAddQwkHost.argtypes = [TGateQwkHost, ctypes.POINTER(DWORD)]
GateAddQwkHost.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateUpdateQwkHost(DWORD index, const TGateQwkHost &host);
GateUpdateQwkHost = wcsgate_dll.GateUpdateQwkHost
GateUpdateQwkHost.argtypes = [ctypes.wintypes.DWORD, TGateQwkHost]
GateUpdateQwkHost.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateRemoveQwkHost(DWORD index);
GateRemoveQwkHost = wcsgate_dll.GateRemoveQwkHost
GateRemoveQwkHost.argtypes = [ctypes.wintypes.DWORD]
GateRemoveQwkHost.restype = ctypes.wintypes.BOOL


##BOOL APIENTRY GateGetQwkConf(const char *hostname, DWORD conference, TGateQwkConf &conf);
GateGetQwkConf = wcsgate_dll.GateGetQwkConf
GateGetQwkConf.argtypes = [CString, ctypes.wintypes.DWORD, ctypes.POINTER(TGateQwkConf)]
GateGetQwkConf.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateGetQwkHubConf(const char *hostname, DWORD hubconference, TGateQwkConf &conf);
GateGetQwkHubConf = wcsgate_dll.GateGetQwkHubConf
GateGetQwkHubConf.argtypes = [CString, ctypes.wintypes.DWORD, ctypes.POINTER(TGateQwkConf)]
GateGetQwkHubConf.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateSetQwkConf(const char *hostname, DWORD conference, const TGateQwkConf &conf);
GateSetQwkConf = wcsgate_dll.GateSetQwkConf
GateSetQwkConf.argtypes = [CString, ctypes.wintypes.DWORD, TGateQwkConf]
GateSetQwkConf.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateUnsetQwkConf(const char *hostname, DWORD conference);
GateUnsetQwkConf = wcsgate_dll.GateUnsetQwkConf
GateUnsetQwkConf.argtypes = [CString, ctypes.wintypes.DWORD]
GateUnsetQwkConf.restype = ctypes.wintypes.BOOL


##DWORD APIENTRY GateGetQwkHighMessage(const char *hostname, DWORD conf);
GateGetQwkHighMessage = wcsgate_dll.GateGetQwkHighMessage
GateGetQwkHighMessage.argtypes = [CString, ctypes.wintypes.DWORD]
GateGetQwkHighMessage.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GateSetQwkHighMessage(const char *hostname, DWORD conf, DWORD id);
GateSetQwkHighMessage = wcsgate_dll.GateSetQwkHighMessage
GateSetQwkHighMessage.argtypes = [CString, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GateSetQwkHighMessage.restype = ctypes.wintypes.BOOL


#// returns a maximum of 99 tagline characters
##BOOL APIENTRY GateGetTaglineList(char *taglist, DWORD size);
GateGetTaglineList = wcsgate_dll.GateGetTaglineList
GateGetTaglineList.argtypes = [ctypes.c_char_p, ctypes.wintypes.DWORD]
GateGetTaglineList.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateGetTagline(char tag, char *tagimport, char *tagexport, DWORD size);
GateGetTagline = wcsgate_dll.GateGetTagline
GateGetTagline.argtypes = [ctypes.c_char, ctypes.c_char_p, ctypes.c_char_p, ctypes.wintypes.DWORD]
GateGetTagline.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateSetTagline(char tag, const char *tagimport, const char *tagexport);
GateSetTagline = wcsgate_dll.GateSetTagline
GateSetTagline.argtypes = [ctypes.c_char, CString, CString]
GateSetTagline.restype = ctypes.wintypes.BOOL


#////////////////////////////////////////////////////////////////////////////////

##BOOL APIENTRY GateGetUucpConfig(TGateUucpConfig &config);
GateGetUucpConfig = wcsgate_dll.GateGetUucpConfig
GateGetUucpConfig.argtypes = [ctypes.POINTER(TGateUucpConfig)]
GateGetUucpConfig.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateUpdateUucpConfig(const TGateUucpConfig &config);
GateUpdateUucpConfig = wcsgate_dll.GateUpdateUucpConfig
GateUpdateUucpConfig.argtypes = [TGateUucpConfig]
GateUpdateUucpConfig.restype = ctypes.wintypes.BOOL


##DWORD APIENTRY GateGetUucpHostCount();
GateGetUucpHostCount = wcsgate_dll.GateGetUucpHostCount
GateGetUucpHostCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GateGetUucpHost(DWORD index, TGateUucpHost &host);
GateGetUucpHost = wcsgate_dll.GateGetUucpHost
GateGetUucpHost.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TGateUucpHost)]
GateGetUucpHost.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateAddUucpHost(const TGateUucpHost &host, DWORD &index);
GateAddUucpHost = wcsgate_dll.GateAddUucpHost
GateAddUucpHost.argtypes = [TGateUucpHost, ctypes.POINTER(DWORD)]
GateAddUucpHost.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateUpdateUucpHost(DWORD index, const TGateUucpHost &host);
GateUpdateUucpHost = wcsgate_dll.GateUpdateUucpHost
GateUpdateUucpHost.argtypes = [ctypes.wintypes.DWORD, TGateUucpHost]
GateUpdateUucpHost.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateRemoveUucpHost(DWORD index);
GateRemoveUucpHost = wcsgate_dll.GateRemoveUucpHost
GateRemoveUucpHost.argtypes = [ctypes.wintypes.DWORD]
GateRemoveUucpHost.restype = ctypes.wintypes.BOOL


##DWORD APIENTRY GateGetUucpHighMessage(DWORD conf);
GateGetUucpHighMessage = wcsgate_dll.GateGetUucpHighMessage
GateGetUucpHighMessage.argtypes = [ctypes.wintypes.DWORD]
GateGetUucpHighMessage.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GateSetUucpHighMessage(DWORD conf, DWORD id);
GateSetUucpHighMessage = wcsgate_dll.GateSetUucpHighMessage
GateSetUucpHighMessage.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GateSetUucpHighMessage.restype = ctypes.wintypes.BOOL


##BOOL APIENTRY GateIsNewsgroupSubscribed(const char *host, const char *newsgroup);
GateIsNewsgroupSubscribed = wcsgate_dll.GateIsNewsgroupSubscribed
GateIsNewsgroupSubscribed.argtypes = [CString, CString]
GateIsNewsgroupSubscribed.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateAddNewsgroup(const char *host, const char *newsgroup);
GateAddNewsgroup = wcsgate_dll.GateAddNewsgroup
GateAddNewsgroup.argtypes = [CString, CString]
GateAddNewsgroup.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateRemoveNewsgroup(const char *host, const char *newsgroup);
GateRemoveNewsgroup = wcsgate_dll.GateRemoveNewsgroup
GateRemoveNewsgroup.argtypes = [CString, CString]
GateRemoveNewsgroup.restype = ctypes.wintypes.BOOL


##DWORD APIENTRY GateGetAutoResponseCount();
GateGetAutoResponseCount = wcsgate_dll.GateGetAutoResponseCount
GateGetAutoResponseCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GateGetAutoResponseName(DWORD index, char name[SIZE_USER_NAME]);
GateGetAutoResponseName = wcsgate_dll.GateGetAutoResponseName
GateGetAutoResponseName.argtypes = [ctypes.wintypes.DWORD, ctypes.c_char]
GateGetAutoResponseName.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateGetAutoResponseText(const char *name, char *&text);
GateGetAutoResponseText = wcsgate_dll.GateGetAutoResponseText
GateGetAutoResponseText.argtypes = [CString, ctypes.c_char_p]
GateGetAutoResponseText.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateSetAutoResponse(const char *name, const char *text, DWORD &index);
GateSetAutoResponse = wcsgate_dll.GateSetAutoResponse
GateSetAutoResponse.argtypes = [CString, CString, ctypes.POINTER(DWORD)]
GateSetAutoResponse.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateRemoveAutoResponse(const char *name);
GateRemoveAutoResponse = wcsgate_dll.GateRemoveAutoResponse
GateRemoveAutoResponse.argtypes = [CString]
GateRemoveAutoResponse.restype = ctypes.wintypes.BOOL


##DWORD APIENTRY GateGetMailingListCount();
GateGetMailingListCount = wcsgate_dll.GateGetMailingListCount
GateGetMailingListCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GateGetMailingList(DWORD index, TGateMailingList &ml);
GateGetMailingList = wcsgate_dll.GateGetMailingList
GateGetMailingList.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TGateMailingList)]
GateGetMailingList.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateAddMailingList(const TGateMailingList &ml, DWORD &index);
GateAddMailingList = wcsgate_dll.GateAddMailingList
GateAddMailingList.argtypes = [TGateMailingList, ctypes.POINTER(DWORD)]
GateAddMailingList.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateUpdateMailingList(DWORD index, const TGateMailingList &ml);
GateUpdateMailingList = wcsgate_dll.GateUpdateMailingList
GateUpdateMailingList.argtypes = [ctypes.wintypes.DWORD, TGateMailingList]
GateUpdateMailingList.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateRemoveMailingList(DWORD index);
GateRemoveMailingList = wcsgate_dll.GateRemoveMailingList
GateRemoveMailingList.argtypes = [ctypes.wintypes.DWORD]
GateRemoveMailingList.restype = ctypes.wintypes.BOOL


#////////////////////////////////////////////////////////////////////////////////

                                        
##DWORD APIENTRY GateGetHostTranslateCount(DWORD host);
GateGetHostTranslateCount = wcsgate_dll.GateGetHostTranslateCount
GateGetHostTranslateCount.argtypes = [ctypes.wintypes.DWORD]
GateGetHostTranslateCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY GateGetHostTranslate(DWORD host, DWORD index, TGateTranslateEntry &te);
GateGetHostTranslate = wcsgate_dll.GateGetHostTranslate
GateGetHostTranslate.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TGateTranslateEntry)]
GateGetHostTranslate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateAddHostTranslate(DWORD host, const TGateTranslateEntry &te, DWORD &index);
GateAddHostTranslate = wcsgate_dll.GateAddHostTranslate
GateAddHostTranslate.argtypes = [ctypes.wintypes.DWORD, TGateTranslateEntry, ctypes.POINTER(DWORD)]
GateAddHostTranslate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateUpdateHostTranslate(DWORD host, DWORD index, const TGateTranslateEntry &te);
GateUpdateHostTranslate = wcsgate_dll.GateUpdateHostTranslate
GateUpdateHostTranslate.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, TGateTranslateEntry]
GateUpdateHostTranslate.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY GateRemoveHostTranslate(DWORD host, DWORD index);
GateRemoveHostTranslate = wcsgate_dll.GateRemoveHostTranslate
GateRemoveHostTranslate.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
GateRemoveHostTranslate.restype = ctypes.wintypes.BOOL


#} // extern "C"

