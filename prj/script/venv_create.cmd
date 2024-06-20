REM set HTTPS_PROXY= http://10.110.15.6:8080

@echo off
set script_dir=%~dp0
call %script_dir%\common.cmd

REM -----------------------------------------------------------
REM let caller (eg ci pipeline) override python version, by passing as arg to his script, eg
REM    - `venv_create.cmd 3.11`
REM  if none passed then the python version used is
REM    - that set in `common.scmd`  if any, or if not set there then
REM    - whatever is found as "python" on path
REM -----------------------------------------------------------
if "%1"=="" (
    echo "no python version (arg) passed to venv_create.cmd"
    if "%py_ver%"=="" (
        echo "no python version defined in common.cmd"
        REM Default to system Python if no version is specified
        set py_command=python
        echo " .... using versionless
    ) else (
        set py_command=py -%py_ver%
        echo "using py_ver from common.cmd" %py_ver%
    )
) else (
    set py_command=py -%1
)
echo "using py_command:" %py_command%
echo Using Python version: %py_ver%

REM -----------------------------------------------------------
REM -----------------------------------------------------------

REM Create the virtual environment using the py launcher
CALL %py_command% -m venv "%venv_dir%

echo ".....virtual environment created"

CALL %venv_dir%\Scripts\activate

echo ".....pip reqs installing...."

CALL  %script_dir%\pip_reqs_install.cmd

echo ".....pip reqs installed"

CALL %venv_dir%\Scripts\deactivate

echo ".....venv ready"


pause
