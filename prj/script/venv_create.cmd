set HTTPS_PROXY=
REM http://10.110.15.6:8080

CALL python -m venv .\venv

echo ".....virtual environment created"

CALL .\venv\Scripts\activate

echo ".....pip reqs installing...."

CALL  .\pip_reqs_install.cmd

echo ".....pip reqs installed"

CALL .\venv\Scripts\deactivate

echo ".....venv ready"


pause