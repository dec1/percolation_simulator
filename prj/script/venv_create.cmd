REM set HTTPS_PROXY= http://10.110.15.6:8080

@echo off
call common.cmd


CALL python -m venv %script_dir%\venv

echo ".....virtual environment created"

CALL %venv_dir%\Scripts\activate

echo ".....pip reqs installing...."

CALL  %script_dir%\pip_reqs_install.cmd

echo ".....pip reqs installed"

CALL %venv_dir%\Scripts\deactivate

echo ".....venv ready"


pause
