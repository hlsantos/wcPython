# Auto-created by cpp2wcerror.py on 2023-01-30 20:55:23.724135

# Wildcat! error constants start with the WC_STATUS_BASE

WC_STATUS_BASE = 0x20000000
WC_SUCCESS                     = 0 # HLS
WC_UNSUPPORTED_VERSION         = WC_STATUS_BASE + 1
WC_CONTEXT_NOT_INITIALIZED     = WC_STATUS_BASE + 2
WC_INVALID_NODE_NUMBER         = WC_STATUS_BASE + 3
WC_USER_NOT_FOUND              = WC_STATUS_BASE + 4
WC_INCORRECT_PASSWORD          = WC_STATUS_BASE + 5
WC_USER_NOT_LOGGED_IN          = WC_STATUS_BASE + 6
WC_INVALID_INDEX               = WC_STATUS_BASE + 7
WC_INVALID_OBJECT_ID           = WC_STATUS_BASE + 8
WC_GROUP_ALREADY_EXISTS        = WC_STATUS_BASE + 9
WC_GROUP_NOT_FOUND             = WC_STATUS_BASE + 10 # A
WC_DBASE_NOT_AVAILABLE         = WC_STATUS_BASE + 11 # B   # 454.6
WC_OBJECTID_ALREADY_EXISTS     = WC_STATUS_BASE + 12 # C
WC_NAME_NOT_FOUND              = WC_STATUS_BASE + 13 # D
WC_NAME_ALREADY_EXISTS         = WC_STATUS_BASE + 14 # E
WC_ALREADY_LOGGED_IN           = WC_STATUS_BASE + 15 # F
WC_ITEM_NOT_FOUND              = WC_STATUS_BASE + 16 # 10
WC_ITEM_REQUIRES_NAME          = WC_STATUS_BASE + 17 # 11
WC_ITEM_ALREADY_EXISTS         = WC_STATUS_BASE + 18 # 12
WC_ITEM_NAME_DIFFERENT         = WC_STATUS_BASE + 19 # 13
WC_RECORD_NOT_FOUND            = WC_STATUS_BASE + 20 # 14
WC_ACCESS_DENIED               = WC_STATUS_BASE + 21 # 15
WC_NODE_ALREADY_IN_USE         = WC_STATUS_BASE + 22 # 16
WC_USER_ALREADY_LOGGED_IN      = WC_STATUS_BASE + 23 # 17
WC_INVALID_CONNECTION_ID       = WC_STATUS_BASE + 24 # 18
WC_INVALID_CONFERENCE          = WC_STATUS_BASE + 25 # 19
WC_INVALID_CONFERENCEGROUP     = WC_STATUS_BASE + 26 # 1A
WC_INVALID_FILEAREA            = WC_STATUS_BASE + 27 # 1B
WC_INVALID_FILEGROUP           = WC_STATUS_BASE + 28 # 1C
WC_DUPLICATE_RECORD            = WC_STATUS_BASE + 29 # 1D
WC_NO_ACTION_TAKEN             = WC_STATUS_BASE + 30 # 1E
WC_ACCOUNT_LOCKED_OUT          = WC_STATUS_BASE + 31 # 1F
WC_FILE_SEARCH_SYNTAX          = WC_STATUS_BASE + 32 # 20
WC_REQUEST_NOT_ADDED           = WC_STATUS_BASE + 33 # 21
WC_CONTEXT_MULTI_REFS          = WC_STATUS_BASE + 34 # 22
WC_CONTEXT_ALREADY_INITIALIZED = WC_STATUS_BASE + 35 # 23
WC_NO_NODES_AVAILABLE          = WC_STATUS_BASE + 36 # 24
WC_COMPUTERNAME_NOT_FOUND      = WC_STATUS_BASE + 37 # 25
WC_DBASE_IX_MISMATCH           = WC_STATUS_BASE + 38 # 26
WC_DBASE_UPDATE_ERROR          = WC_STATUS_BASE + 39 # 27
WC_DBASE_RESERVED40            = WC_STATUS_BASE + 40 # 28
WC_DBASE_RESERVED41            = WC_STATUS_BASE + 41 # 29
WC_DBASE_RESERVED42            = WC_STATUS_BASE + 42 # 2A
WC_DBASE_RESERVED43            = WC_STATUS_BASE + 43 # 2B
WC_USER_OUT_OF_TIME            = WC_STATUS_BASE + 44 # 2C
WC_ACCOUNT_NOT_VALIDATED       = WC_STATUS_BASE + 45 # 2D 
WC_DOMAIN_ACCESS_DENIED        = WC_STATUS_BASE + 46 # 2E 
WC_BUFFER_TOO_SMALL            = WC_STATUS_BASE + 47 # 2F 
WC_DOMAIN_NOT_FOUND            = WC_STATUS_BASE + 48 # 30 
WC_PASSWORD_EXPIRED            = WC_STATUS_BASE + 49 # 31 
WC_PASSWORD_CHANGE_REQUIRED    = WC_STATUS_BASE + 50 # 32 
WC_ANONYMOUS_DENIED            = WC_STATUS_BASE + 51 # 33 
WC_HOURS_RESTRICTED            = WC_STATUS_BASE + 52 # 34 
WC_SECURITY_NOT_FOUND          = WC_STATUS_BASE + 53 # 35 
WC_INVALID_USERNAME            = WC_STATUS_BASE + 54 # 36 

# Error Map

wcerror_map = {
	WC_STATUS_BASE                     : ("WC_STATUS_BASE"                   , "Status Base"),
	WC_SUCCESS                         : ("WC_SUCCESS"                       , "Success"),
	WC_UNSUPPORTED_VERSION             : ("WC_UNSUPPORTED_VERSION"           , "Unsupported Version"),
	WC_CONTEXT_NOT_INITIALIZED         : ("WC_CONTEXT_NOT_INITIALIZED"       , "Context Not Initialized"),
	WC_INVALID_NODE_NUMBER             : ("WC_INVALID_NODE_NUMBER"           , "Invalid Node Number"),
	WC_USER_NOT_FOUND                  : ("WC_USER_NOT_FOUND"                , "User Not Found"),
	WC_INCORRECT_PASSWORD              : ("WC_INCORRECT_PASSWORD"            , "Incorrect Password"),
	WC_USER_NOT_LOGGED_IN              : ("WC_USER_NOT_LOGGED_IN"            , "User Not Logged In"),
	WC_INVALID_INDEX                   : ("WC_INVALID_INDEX"                 , "Invalid Index"),
	WC_INVALID_OBJECT_ID               : ("WC_INVALID_OBJECT_ID"             , "Invalid Object Id"),
	WC_GROUP_ALREADY_EXISTS            : ("WC_GROUP_ALREADY_EXISTS"          , "Group Already Exists"),
	WC_GROUP_NOT_FOUND                 : ("WC_GROUP_NOT_FOUND"               , "Group Not Found"),
	WC_DBASE_NOT_AVAILABLE             : ("WC_DBASE_NOT_AVAILABLE"           , "Dbase Not Available"),
	WC_OBJECTID_ALREADY_EXISTS         : ("WC_OBJECTID_ALREADY_EXISTS"       , "Objectid Already Exists"),
	WC_NAME_NOT_FOUND                  : ("WC_NAME_NOT_FOUND"                , "Name Not Found"),
	WC_NAME_ALREADY_EXISTS             : ("WC_NAME_ALREADY_EXISTS"           , "Name Already Exists"),
	WC_ALREADY_LOGGED_IN               : ("WC_ALREADY_LOGGED_IN"             , "Already Logged In"),
	WC_ITEM_NOT_FOUND                  : ("WC_ITEM_NOT_FOUND"                , "Item Not Found"),
	WC_ITEM_REQUIRES_NAME              : ("WC_ITEM_REQUIRES_NAME"            , "Item Requires Name"),
	WC_ITEM_ALREADY_EXISTS             : ("WC_ITEM_ALREADY_EXISTS"           , "Item Already Exists"),
	WC_ITEM_NAME_DIFFERENT             : ("WC_ITEM_NAME_DIFFERENT"           , "Item Name Different"),
	WC_RECORD_NOT_FOUND                : ("WC_RECORD_NOT_FOUND"              , "Record Not Found"),
	WC_ACCESS_DENIED                   : ("WC_ACCESS_DENIED"                 , "Access Denied"),
	WC_NODE_ALREADY_IN_USE             : ("WC_NODE_ALREADY_IN_USE"           , "Node Already In Use"),
	WC_USER_ALREADY_LOGGED_IN          : ("WC_USER_ALREADY_LOGGED_IN"        , "User Already Logged In"),
	WC_INVALID_CONNECTION_ID           : ("WC_INVALID_CONNECTION_ID"         , "Invalid Connection Id"),
	WC_INVALID_CONFERENCE              : ("WC_INVALID_CONFERENCE"            , "Invalid Conference"),
	WC_INVALID_CONFERENCEGROUP         : ("WC_INVALID_CONFERENCEGROUP"       , "Invalid Conferencegroup"),
	WC_INVALID_FILEAREA                : ("WC_INVALID_FILEAREA"              , "Invalid Filearea"),
	WC_INVALID_FILEGROUP               : ("WC_INVALID_FILEGROUP"             , "Invalid Filegroup"),
	WC_DUPLICATE_RECORD                : ("WC_DUPLICATE_RECORD"              , "Duplicate Record"),
	WC_NO_ACTION_TAKEN                 : ("WC_NO_ACTION_TAKEN"               , "No Action Taken"),
	WC_ACCOUNT_LOCKED_OUT              : ("WC_ACCOUNT_LOCKED_OUT"            , "Account Locked Out"),
	WC_FILE_SEARCH_SYNTAX              : ("WC_FILE_SEARCH_SYNTAX"            , "File Search Syntax"),
	WC_REQUEST_NOT_ADDED               : ("WC_REQUEST_NOT_ADDED"             , "Request Not Added"),
	WC_CONTEXT_MULTI_REFS              : ("WC_CONTEXT_MULTI_REFS"            , "Context Multi Refs"),
	WC_CONTEXT_ALREADY_INITIALIZED     : ("WC_CONTEXT_ALREADY_INITIALIZED"   , "Context Already Initialized"),
	WC_NO_NODES_AVAILABLE              : ("WC_NO_NODES_AVAILABLE"            , "No Nodes Available"),
	WC_COMPUTERNAME_NOT_FOUND          : ("WC_COMPUTERNAME_NOT_FOUND"        , "Computername Not Found"),
	WC_DBASE_IX_MISMATCH               : ("WC_DBASE_IX_MISMATCH"             , "Dbase Ix Mismatch"),
	WC_DBASE_UPDATE_ERROR              : ("WC_DBASE_UPDATE_ERROR"            , "Dbase Update Error"),
	WC_DBASE_RESERVED40                : ("WC_DBASE_RESERVED40"              , "Dbase Reserved40"),
	WC_DBASE_RESERVED41                : ("WC_DBASE_RESERVED41"              , "Dbase Reserved41"),
	WC_DBASE_RESERVED42                : ("WC_DBASE_RESERVED42"              , "Dbase Reserved42"),
	WC_DBASE_RESERVED43                : ("WC_DBASE_RESERVED43"              , "Dbase Reserved43"),
	WC_USER_OUT_OF_TIME                : ("WC_USER_OUT_OF_TIME"              , "User Out Of Time"),
	WC_ACCOUNT_NOT_VALIDATED           : ("WC_ACCOUNT_NOT_VALIDATED"         , "Account Not Validated"),
	WC_DOMAIN_ACCESS_DENIED            : ("WC_DOMAIN_ACCESS_DENIED"          , "Domain Access Denied"),
	WC_BUFFER_TOO_SMALL                : ("WC_BUFFER_TOO_SMALL"              , "Buffer Too Small"),
	WC_DOMAIN_NOT_FOUND                : ("WC_DOMAIN_NOT_FOUND"              , "Domain Not Found"),
	WC_PASSWORD_EXPIRED                : ("WC_PASSWORD_EXPIRED"              , "Password Expired"),
	WC_PASSWORD_CHANGE_REQUIRED        : ("WC_PASSWORD_CHANGE_REQUIRED"      , "Password Change Required"),
	WC_ANONYMOUS_DENIED                : ("WC_ANONYMOUS_DENIED"              , "Anonymous Denied"),
	WC_HOURS_RESTRICTED                : ("WC_HOURS_RESTRICTED"              , "Hours Restricted"),
	WC_SECURITY_NOT_FOUND              : ("WC_SECURITY_NOT_FOUND"            , "Security Not Found"),
	WC_INVALID_USERNAME                : ("WC_INVALID_USERNAME"              , "Invalid Username"),
}

def GetWildcatErrorStr(error_number):
    error_name, error_literal = wcerror_map.get(error_number, ("Unknown error", "Error not found in wcerror_map"))
    return f"{error_name} (0x{error_number:X}) - {error_literal}"

#if __name__ == '__main__':
#
#    print(GetWildcatErrorStr(WC_ACCOUNT_NOT_VALIDATED))
