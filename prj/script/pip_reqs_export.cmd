SET "script_dir=%~dp0"
SET "script_dir=%script_dir:~0,-1%"   

CALL %script_dir%\venv\Scripts\pip freeze > ..\pip_reqs.txt
