REM set HTTPS_PROXY= http://10.110.15.6:8080

SET "script_dir=%~dp0"
SET "script_dir=%script_dir:~0,-1%"   

CALL python -m venv %script_dir%\venv

echo ".....virtual environment created"

CALL %script_dir%\venv\Scripts\activate

echo ".....pip reqs installing...."

CALL  %script_dir%\pip_reqs_install.cmd

echo ".....pip reqs installed"

CALL %script_dir%\\venv\Scripts\deactivate

echo ".....venv ready"


pause