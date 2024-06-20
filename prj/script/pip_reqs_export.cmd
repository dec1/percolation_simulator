@echo off
set script_dir=%~dp0
call %script_dir%\common.cmd

CALL %venv_dir%\Scripts\python -m pip freeze > %pip_reqs_dir%\pip_reqs.txt
