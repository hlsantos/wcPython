# Auto-Created by cpp2py.py
import os
from wcpapi.wctype_constants_h import *
from wcpapi.wctype_h import *
from wcpapi.wctypemw_constants_h import *
from wcpapi.wctypemw_h import *
from wcpapi.__init__ import *

wcsmw_dll = initialize_wcsmw_dll()

#//***********************************************************************
#// (c) Copyright 1998-2002 Santronics Software, Inc. All Rights Reserved.
#//***********************************************************************
#//
#// File Name : wcsmw.h
#// Subsystem : header for to access configuration function
#// Date      :
#// Author    :
#//
#// Revision History:
#// Build  Date      Author  Comments
#// -----  --------  ------  ---------------------------------------------
#//***********************************************************************




#//!----------------------------------------------------------------
#//+ Group: Makewild Configuration
#//@ MwLogin
#//# Login as the configuration client
#//$ password  - configuration password, used "" if none. if a
#//$             password is required, you should prompt for the
#//$             password.
#//% returns TRUE if successful, otherwise see extended error
#//!----------------------------------------------------------------

##BOOL APIENTRY MwLogin(const char *password);
MwLogin = wcsmw_dll.MwLogin
MwLogin.argtypes = [CString]
MwLogin.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Makewild Configuration
#//@ MwGetMakewild
#//# return the configuration structure TWildcatServerPrivateConfig
#//$ mw - TWildcatServerPrivateConfig
#//% returns TRUE if successful, otherwise see extended error
#//& see also MwUpdateMakeWild
#//!----------------------------------------------------------------

##BOOL APIENTRY MwGetMakewild(TWildcatServerPrivateConfig &mw);
MwGetMakewild = wcsmw_dll.MwGetMakewild
MwGetMakewild.argtypes = [ctypes.POINTER(TWildcatServerPrivateConfig)]
MwGetMakewild.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Makewild Configuration
#//@ MwUpdateMakewild
#//# Save the configuration structure TWildcatServerPrivateConfig
#//$ mw - TWildcatServerPrivateConfig
#//% returns TRUE if successful, otherwise see extended error
#//& see also MwGetMakeWild
#//!----------------------------------------------------------------

##BOOL APIENTRY MwUpdateMakewild(TWildcatServerPrivateConfig &mw);
MwUpdateMakewild = wcsmw_dll.MwUpdateMakewild
MwUpdateMakewild.argtypes = [ctypes.POINTER(TWildcatServerPrivateConfig)]
MwUpdateMakewild.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Security Profile functions
#//!
#//! MwGetSecurityProfileCount    get number of security profiles
#//! MwGetSecurityProfileNames    get a string list of security names
#//! MwGetSecurityProfiles        get an array of TSecurityProfiles
#//! MwAddSecurityProfile         add a security profile
#//! MwUpdateSecurityProfile      update a security profile
#//! MwRemoveSecurityProfile      remote a security profile
#//!----------------------------------------------------------------

##DWORD APIENTRY MwGetSecurityProfileCount();
MwGetSecurityProfileCount = wcsmw_dll.MwGetSecurityProfileCount
MwGetSecurityProfileCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY MwGetSecurityProfileNames(DWORD index, DWORD count, char profilenames[][SIZE_SECURITY_NAME]);
MwGetSecurityProfileNames = wcsmw_dll.MwGetSecurityProfileNames
MwGetSecurityProfileNames.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(TSecurityName)]
MwGetSecurityProfileNames.restype = ctypes.c_bool

##BOOL APIENTRY MwGetSecurityProfiles(DWORD index, DWORD count, TSecurityProfile *profile);
MwGetSecurityProfiles = wcsmw_dll.MwGetSecurityProfiles
MwGetSecurityProfiles.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TSecurityProfile)]
MwGetSecurityProfiles.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwAddSecurityProfile(const TSecurityProfile &profile, DWORD &index);
MwAddSecurityProfile = wcsmw_dll.MwAddSecurityProfile
MwAddSecurityProfile.argtypes = [TSecurityProfile, ctypes.POINTER(DWORD)]
MwAddSecurityProfile.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateSecurityProfile(DWORD index, const TSecurityProfile &profile);
MwUpdateSecurityProfile = wcsmw_dll.MwUpdateSecurityProfile
MwUpdateSecurityProfile.argtypes = [ctypes.wintypes.DWORD, TSecurityProfile]
MwUpdateSecurityProfile.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwRemoveSecurityProfile(DWORD index);
MwRemoveSecurityProfile = wcsmw_dll.MwRemoveSecurityProfile
MwRemoveSecurityProfile.argtypes = [ctypes.wintypes.DWORD]
MwRemoveSecurityProfile.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Security Access Profile functions
#//! The "Group" functions apply to the access profiles, NOT the
#//! security profiles.
#//!
#//! MwCreateGroup                create a new group
#//! MwRemoveGroup                remove a group
#//! MwCloneGroup                 clone a group and all its flags
#//! MwGetGroupCount              get the number of groups
#//! MwGetGroupNames              get the current group names (and
#//!                              indexes implicitly by position in
#//!                              array)
#//! MwGetObjectFlags             get the object's flags in group
#//! MwGetMultipleObjectFlags     get multiple object flags in group
#//! MwSetObjectFlags             sets the object's flags in a group (will
#//!                              add the object to the group file if
#//!                              it needs to, or remove it if flags == 0)
#//! MwSetMultipleObjectFlags     set multiple object flags in group
#//! MwGetObjectFlagsInGroups     get the flags for an object in each
#//!                              group, indexes are relative to the
#//!                              group names returned by MwGetGroupNames()
#//! MwSetObjectFlagsInGroups     set the flags for an object in each group
#//!----------------------------------------------------------------

##BOOL APIENTRY MwCreateGroup(const char *groupname, DWORD &index);
MwCreateGroup = wcsmw_dll.MwCreateGroup
MwCreateGroup.argtypes = [CString, ctypes.POINTER(DWORD)]
MwCreateGroup.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwRemoveGroup(const char *groupname);
MwRemoveGroup = wcsmw_dll.MwRemoveGroup
MwRemoveGroup.argtypes = [CString]
MwRemoveGroup.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwCloneGroup(DWORD sourcegroupindex, const char *newgroupname, DWORD &newgroupindex);
MwCloneGroup = wcsmw_dll.MwCloneGroup
MwCloneGroup.argtypes = [ctypes.wintypes.DWORD, CString, ctypes.POINTER(DWORD)]
MwCloneGroup.restype = ctypes.wintypes.BOOL

##DWORD APIENTRY MwGetGroupCount();
MwGetGroupCount = wcsmw_dll.MwGetGroupCount
MwGetGroupCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY MwGetGroupNames(char groupnames[][SIZE_SECURITY_NAME]);
MwGetGroupNames = wcsmw_dll.MwGetGroupNames
MwGetGroupNames.argtypes = [ctypes.POINTER(TSecurityName)]
MwGetGroupNames.restype = ctypes.c_bool

##DWORD APIENTRY MwGetObjectFlags(DWORD groupindex, DWORD objectid);
MwGetObjectFlags = wcsmw_dll.MwGetObjectFlags
MwGetObjectFlags.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
MwGetObjectFlags.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY MwGetMultipleObjectFlags(DWORD groupindex, const DWORD *objectid, DWORD count, DWORD *flags);
MwGetMultipleObjectFlags = wcsmw_dll.MwGetMultipleObjectFlags
MwGetMultipleObjectFlags.argtypes = [ctypes.wintypes.DWORD, DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(DWORD)]
MwGetMultipleObjectFlags.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetObjectFlags(DWORD groupindex, DWORD objectid, DWORD flags);
MwSetObjectFlags = wcsmw_dll.MwSetObjectFlags
MwSetObjectFlags.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
MwSetObjectFlags.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetMultipleObjectFlags(DWORD groupindex, const DWORD *objectid, const DWORD *flags, DWORD count);
MwSetMultipleObjectFlags = wcsmw_dll.MwSetMultipleObjectFlags
MwSetMultipleObjectFlags.argtypes = [ctypes.wintypes.DWORD, DWORD, DWORD, ctypes.wintypes.DWORD]
MwSetMultipleObjectFlags.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwGetObjectFlagsInGroups(DWORD objectid, DWORD *flags);
MwGetObjectFlagsInGroups = wcsmw_dll.MwGetObjectFlagsInGroups
MwGetObjectFlagsInGroups.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(DWORD)]
MwGetObjectFlagsInGroups.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetObjectFlagsInGroups(DWORD objectid, const DWORD *flags);
MwSetObjectFlagsInGroups = wcsmw_dll.MwSetObjectFlagsInGroups
MwSetObjectFlagsInGroups.argtypes = [ctypes.wintypes.DWORD, DWORD]
MwSetObjectFlagsInGroups.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Computers/Load Balancing
#//! The "Computer" functions apply to the "Computers" setup in
#//! wcconfig.exe.  This help load balance the system by distributing
#//! the wconline setup of the internet servers across various
#//! machines. The default is a blank computer name - index 0.
#//!----------------------------------------------------------------

##DWORD APIENTRY MwGetComputerConfigCount();
MwGetComputerConfigCount = wcsmw_dll.MwGetComputerConfigCount
MwGetComputerConfigCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY MwGetComputerConfigNames(DWORD index, DWORD count, char computernames[][SIZE_COMPUTER_NAME]);
MwGetComputerConfigNames = wcsmw_dll.MwGetComputerConfigNames
MwGetComputerConfigNames.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(TComputerName)]
MwGetComputerConfigNames.restype = ctypes.c_bool

##BOOL APIENTRY MwGetComputerConfigs(DWORD index, DWORD count, TComputerConfig *cconfig);
MwGetComputerConfigs = wcsmw_dll.MwGetComputerConfigs
MwGetComputerConfigs.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TComputerConfig)]
MwGetComputerConfigs.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwAddComputerConfig(const TComputerConfig &ccoonfig, DWORD &index);
MwAddComputerConfig = wcsmw_dll.MwAddComputerConfig
MwAddComputerConfig.argtypes = [TComputerConfig, ctypes.POINTER(DWORD)]
MwAddComputerConfig.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateComputerConfig(DWORD index, TComputerConfig &cconfig);
MwUpdateComputerConfig = wcsmw_dll.MwUpdateComputerConfig
MwUpdateComputerConfig.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TComputerConfig)]
MwUpdateComputerConfig.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwRemoveComputerConfig(DWORD index);
MwRemoveComputerConfig = wcsmw_dll.MwRemoveComputerConfig
MwRemoveComputerConfig.argtypes = [ctypes.wintypes.DWORD]
MwRemoveComputerConfig.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Mail Conference Setup
#//! Mail conference setup functions
#//!----------------------------------------------------------------

##BOOL APIENTRY MwGetShortConfDescs(DWORD conference, DWORD count, TShortConfDesc *cd);
MwGetShortConfDescs = wcsmw_dll.MwGetShortConfDescs
MwGetShortConfDescs.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TShortConfDesc)]
MwGetShortConfDescs.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwGetConfDescs(DWORD conference, DWORD count, TWildcatServerPrivateConfDesc *cd);
MwGetConfDescs = wcsmw_dll.MwGetConfDescs
MwGetConfDescs.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TWildcatServerPrivateConfDesc)]
MwGetConfDescs.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetConferenceCount(DWORD count);
MwSetConferenceCount = wcsmw_dll.MwSetConferenceCount
MwSetConferenceCount.argtypes = [ctypes.wintypes.DWORD]
MwSetConferenceCount.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateConfDesc(DWORD conference, TWildcatServerPrivateConfDesc &cd);
MwUpdateConfDesc = wcsmw_dll.MwUpdateConfDesc
MwUpdateConfDesc.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TWildcatServerPrivateConfDesc)]
MwUpdateConfDesc.restype = ctypes.wintypes.BOOL


##BOOL APIENTRY MwGetConferenceGroups(DWORD group, DWORD count, TConferenceGroup *fg);
MwGetConferenceGroups = wcsmw_dll.MwGetConferenceGroups
MwGetConferenceGroups.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TConferenceGroup)]
MwGetConferenceGroups.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetConferenceGroupCount(DWORD count);
MwSetConferenceGroupCount = wcsmw_dll.MwSetConferenceGroupCount
MwSetConferenceGroupCount.argtypes = [ctypes.wintypes.DWORD]
MwSetConferenceGroupCount.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateConferenceGroup(DWORD group, TConferenceGroup &cg);
MwUpdateConferenceGroup = wcsmw_dll.MwUpdateConferenceGroup
MwUpdateConferenceGroup.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TConferenceGroup)]
MwUpdateConferenceGroup.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwGetConferenceGroupBits(DWORD group, DWORD bytes, BYTE *bits);
MwGetConferenceGroupBits = wcsmw_dll.MwGetConferenceGroupBits
MwGetConferenceGroupBits.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.c_char_p]
MwGetConferenceGroupBits.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetConferenceGroupBits(DWORD group, DWORD bytes, const BYTE *bits);
MwSetConferenceGroupBits = wcsmw_dll.MwSetConferenceGroupBits
MwSetConferenceGroupBits.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, CString]
MwSetConferenceGroupBits.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: File Area Setup
#//! File Area setup functions
#//!----------------------------------------------------------------

##BOOL APIENTRY MwGetShortFileAreas(DWORD area, DWORD count, TShortFileArea *fa);
MwGetShortFileAreas = wcsmw_dll.MwGetShortFileAreas
MwGetShortFileAreas.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TShortFileArea)]
MwGetShortFileAreas.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwGetFileAreas(DWORD area, DWORD count, TWildcatServerPrivateFileArea *fa);
MwGetFileAreas = wcsmw_dll.MwGetFileAreas
MwGetFileAreas.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TWildcatServerPrivateFileArea)]
MwGetFileAreas.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetFileAreaCount(DWORD count);
MwSetFileAreaCount = wcsmw_dll.MwSetFileAreaCount
MwSetFileAreaCount.argtypes = [ctypes.wintypes.DWORD]
MwSetFileAreaCount.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateFileArea(DWORD area, TWildcatServerPrivateFileArea &fa);
MwUpdateFileArea = wcsmw_dll.MwUpdateFileArea
MwUpdateFileArea.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TWildcatServerPrivateFileArea)]
MwUpdateFileArea.restype = ctypes.wintypes.BOOL


#//+ Group: File Area Group Setup

##BOOL APIENTRY MwGetFileGroups(DWORD group, DWORD count, TFileGroup *fg);
MwGetFileGroups = wcsmw_dll.MwGetFileGroups
MwGetFileGroups.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TFileGroup)]
MwGetFileGroups.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetFileGroupCount(DWORD count);
MwSetFileGroupCount = wcsmw_dll.MwSetFileGroupCount
MwSetFileGroupCount.argtypes = [ctypes.wintypes.DWORD]
MwSetFileGroupCount.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateFileGroup(DWORD group, TFileGroup &fg);
MwUpdateFileGroup = wcsmw_dll.MwUpdateFileGroup
MwUpdateFileGroup.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TFileGroup)]
MwUpdateFileGroup.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwGetFileGroupBits(DWORD group, DWORD bytes, BYTE *bits);
MwGetFileGroupBits = wcsmw_dll.MwGetFileGroupBits
MwGetFileGroupBits.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.c_char_p]
MwGetFileGroupBits.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetFileGroupBits(DWORD group, DWORD bytes, const BYTE *bits);
MwSetFileGroupBits = wcsmw_dll.MwSetFileGroupBits
MwSetFileGroupBits.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, CString]
MwSetFileGroupBits.restype = ctypes.wintypes.BOOL


#//+ Group: CD Volume Setup

##DWORD APIENTRY MwGetFileVolumeCount();
MwGetFileVolumeCount = wcsmw_dll.MwGetFileVolumeCount
MwGetFileVolumeCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY MwGetFileVolumeNames(DWORD index, DWORD count, char volumenames[][SIZE_SHORT_FILE_NAME]);
MwGetFileVolumeNames = wcsmw_dll.MwGetFileVolumeNames
MwGetFileVolumeNames.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(TShortFileName)]
MwGetFileVolumeNames.restype = ctypes.c_bool

##BOOL APIENTRY MwGetFileVolumes(DWORD index, DWORD count, TWildcatServerPrivateFileVolume *fv);
MwGetFileVolumes = wcsmw_dll.MwGetFileVolumes
MwGetFileVolumes.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TWildcatServerPrivateFileVolume)]
MwGetFileVolumes.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwAddFileVolume(TWildcatServerPrivateFileVolume &fv, DWORD &index);
MwAddFileVolume = wcsmw_dll.MwAddFileVolume
MwAddFileVolume.argtypes = [ctypes.POINTER(TWildcatServerPrivateFileVolume), ctypes.POINTER(DWORD)]
MwAddFileVolume.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateFileVolume(DWORD index, TWildcatServerPrivateFileVolume &fv);
MwUpdateFileVolume = wcsmw_dll.MwUpdateFileVolume
MwUpdateFileVolume.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TWildcatServerPrivateFileVolume)]
MwUpdateFileVolume.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwRemoveFileVolume(DWORD index);
MwRemoveFileVolume = wcsmw_dll.MwRemoveFileVolume
MwRemoveFileVolume.argtypes = [ctypes.wintypes.DWORD]
MwRemoveFileVolume.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Door Setup
#//! Door setup functions
#//!----------------------------------------------------------------

##BOOL APIENTRY MwGetDoorNames(DWORD index, DWORD count, char doornames[][SIZE_DOOR_NAME]);
MwGetDoorNames = wcsmw_dll.MwGetDoorNames
MwGetDoorNames.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(TDoorName)]
MwGetDoorNames.restype = ctypes.c_bool

##BOOL APIENTRY MwGetDoors(DWORD index, DWORD count, TDoorInfo *di);
MwGetDoors = wcsmw_dll.MwGetDoors
MwGetDoors.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TDoorInfo)]
MwGetDoors.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwAddDoor(TDoorInfo &di, DWORD &index);
MwAddDoor = wcsmw_dll.MwAddDoor
MwAddDoor.argtypes = [ctypes.POINTER(TDoorInfo), ctypes.POINTER(DWORD)]
MwAddDoor.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateDoor(DWORD index, const TDoorInfo &di);
MwUpdateDoor = wcsmw_dll.MwUpdateDoor
MwUpdateDoor.argtypes = [ctypes.wintypes.DWORD, TDoorInfo]
MwUpdateDoor.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwRemoveDoor(DWORD index);
MwRemoveDoor = wcsmw_dll.MwRemoveDoor
MwRemoveDoor.argtypes = [ctypes.wintypes.DWORD]
MwRemoveDoor.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Language Prompt Files Setup
#//! Language Setup functions
#//!----------------------------------------------------------------

##BOOL APIENTRY MwGetLanguages(DWORD index, DWORD count, TLanguageInfo *li);
MwGetLanguages = wcsmw_dll.MwGetLanguages
MwGetLanguages.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TLanguageInfo)]
MwGetLanguages.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwAddLanguage(const TLanguageInfo &li, DWORD &index);
MwAddLanguage = wcsmw_dll.MwAddLanguage
MwAddLanguage.argtypes = [TLanguageInfo, ctypes.POINTER(DWORD)]
MwAddLanguage.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateLanguage(DWORD index, const TLanguageInfo &li);
MwUpdateLanguage = wcsmw_dll.MwUpdateLanguage
MwUpdateLanguage.argtypes = [ctypes.wintypes.DWORD, TLanguageInfo]
MwUpdateLanguage.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwRemoveLanguage(DWORD index);
MwRemoveLanguage = wcsmw_dll.MwRemoveLanguage
MwRemoveLanguage.argtypes = [ctypes.wintypes.DWORD]
MwRemoveLanguage.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Modem Profiles Setup
#//! Modem Profiles setup functions
#//!----------------------------------------------------------------

##DWORD APIENTRY MwGetModemCount();
MwGetModemCount = wcsmw_dll.MwGetModemCount
MwGetModemCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY MwGetShortModemProfiles(DWORD index, DWORD count, TShortModemProfile *mp);
MwGetShortModemProfiles = wcsmw_dll.MwGetShortModemProfiles
MwGetShortModemProfiles.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TShortModemProfile)]
MwGetShortModemProfiles.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwGetModemProfile(DWORD index, TModemProfile &mp);
MwGetModemProfile = wcsmw_dll.MwGetModemProfile
MwGetModemProfile.argtypes = [ctypes.wintypes.DWORD, ctypes.POINTER(TModemProfile)]
MwGetModemProfile.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwAddModemProfile(const TModemProfile &mp, DWORD &index);
MwAddModemProfile = wcsmw_dll.MwAddModemProfile
MwAddModemProfile.argtypes = [TModemProfile, ctypes.POINTER(DWORD)]
MwAddModemProfile.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateModemProfile(DWORD index, const TModemProfile &mp);
MwUpdateModemProfile = wcsmw_dll.MwUpdateModemProfile
MwUpdateModemProfile.argtypes = [ctypes.wintypes.DWORD, TModemProfile]
MwUpdateModemProfile.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwRemoveModemProfile(DWORD index);
MwRemoveModemProfile = wcsmw_dll.MwRemoveModemProfile
MwRemoveModemProfile.argtypes = [ctypes.wintypes.DWORD]
MwRemoveModemProfile.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Node Configuration functions.
#//!----------------------------------------------------------------

##DWORD APIENTRY MwGetNodeConfigCount();
MwGetNodeConfigCount = wcsmw_dll.MwGetNodeConfigCount
MwGetNodeConfigCount.restype = ctypes.wintypes.DWORD

##BOOL APIENTRY MwGetNodeConfigs(DWORD node, DWORD count, TNodeConfig *nc);
MwGetNodeConfigs = wcsmw_dll.MwGetNodeConfigs
MwGetNodeConfigs.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.POINTER(TNodeConfig)]
MwGetNodeConfigs.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwUpdateNodeConfig(DWORD node, const TNodeConfig &nc);
MwUpdateNodeConfig = wcsmw_dll.MwUpdateNodeConfig
MwUpdateNodeConfig.argtypes = [ctypes.wintypes.DWORD, TNodeConfig]
MwUpdateNodeConfig.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Miscellaneous
#//! Check for the existence of server path with
#//! optional create option
#//!----------------------------------------------------------------

##BOOL APIENTRY MwCheckPath(const char *path, BOOL create);
MwCheckPath = wcsmw_dll.MwCheckPath
MwCheckPath.argtypes = [CString, ctypes.wintypes.BOOL]
MwCheckPath.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Domain Configuration Functions
#//!----------------------------------------------------------------

##BOOL APIENTRY MwSetDomainConfigVar(const char *szDomain, const char *szSection, const char *szKey, const char *szValue);
MwSetDomainConfigVar = wcsmw_dll.MwSetDomainConfigVar
MwSetDomainConfigVar.argtypes = [CString, CString, CString, CString]
MwSetDomainConfigVar.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwSetConfigFileVar(const char *szFilename, const char *szSection, const char *szKey, const char *szValue);
MwSetConfigFileVar = wcsmw_dll.MwSetConfigFileVar
MwSetConfigFileVar.argtypes = [CString, CString, CString, CString]
MwSetConfigFileVar.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwReloadDomainConfig();
MwReloadDomainConfig = wcsmw_dll.MwReloadDomainConfig
MwReloadDomainConfig.restype = ctypes.wintypes.BOOL


#//!----------------------------------------------------------------
#//+ Group: Server File Directory
#//!----------------------------------------------------------------

##WCHANDLE APIENTRY MwFindFirstFile(LPCTSTR fn, WIN32_FIND_DATA *fd);
MwFindFirstFile = wcsmw_dll.MwFindFirstFile
MwFindFirstFile.argtypes = [CString, ctypes.POINTER(WIN32_FIND_DATA)]
MwFindFirstFile.restype = ctypes.wintypes.HANDLE

##BOOL APIENTRY MwFindNextFile(WCHANDLE ff, WIN32_FIND_DATA *fd);
MwFindNextFile = wcsmw_dll.MwFindNextFile
MwFindNextFile.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(WIN32_FIND_DATA)]
MwFindNextFile.restype = ctypes.wintypes.BOOL

##BOOL APIENTRY MwFindClose(WCHANDLE ff);
MwFindClose = wcsmw_dll.MwFindClose
MwFindClose.argtypes = [ctypes.wintypes.HANDLE]
MwFindClose.restype = ctypes.wintypes.BOOL



#} // extern "C"

