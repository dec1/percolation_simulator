SET "script_dir=%~dp0"
SET "script_dir=%script_dir:~0,-1%"   

CALL %script_dir%\venv\Scripts\python -m pip install --upgrade pip
CALl %script_dir%\venv\Scripts\pip install --upgrade setuptools


REM Latest
REM ------
REM install (latest versions of) dependencies
REM ------
CAll %script_dir%\venv\Scripts\pip install -r ..\pip_reqs_base.txt

REM Exact
REM ------
REM alternatively, use this instead to install exact (recursive) dependencies previously 'frozen' by
REM previous call to 'pip_reqs_export.sh'
REM
REM recommended for production
REM ------
REM CAll .\venv\Scripts\pip install -r ..\pip_reqs.txt
