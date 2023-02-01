@echo off

    echo *** making wcPAPI functions and types
    py cpp2py.py
    if errorlevel 1 goto :eof

    echo *** making wcPAPI errors
    py cpp2wcerror.py
    if errorlevel 1 goto :eof

    echo *** making wcPAPI constants
    py cpp2constants.py
    if errorlevel 1 goto :eof


