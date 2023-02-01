# title: wcPAPI Wildcat! Python API
# date : 01/30/23 07:30 pm

# wcSDK to Python translators.
# Use wcpapi-make.cmd to run the scripts

wcpapi-make.cmd         runs the cpp2*.py translators, creates wcpapi\wc*_h.py files

    cpp2py.py           wcPAPI functions and types
    cpp2wcerror.py      wcPAPI errors
    cpp2constants.py    wcPAPI constants

wcpapi-install.cmd      do first time to pip install dist\* file.

    dist/wcpapi-8.0.454.13.tar.gz

wcpapi-update.cmd       do to update the pip installation.
wcpapi-backup.cmd       edit the change zip name to create backup

# Package Files

setup.py
wcPapi/wcgtype_constants_h.py
wcPapi/wcgtype_h.py
wcPapi/wcserror_h.py
wcPapi/wcserver_h.py
wcPapi/wcsgate_h.py
wcPapi/wcsmw_h.py
wcPapi/wctypemw_constants_h.py
wcPapi/wctypemw_h.py
wcPapi/wctype_constants_h.py
wcPapi/wctype_h.py
wcPapi/__init__.py

# wcSDK C-based RPC client headers v8.0.454.12

include/wcgtype.h
include/wcserver.h
include/wcsgate.h
include/wcsmw.h
include/wctype.h
include/wctypemw.h

# testing code

test\test-winapi.py
test\test-listfiles.py

