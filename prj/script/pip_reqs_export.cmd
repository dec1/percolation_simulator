@echo off
call common.cmd

CALL %venv_dir%\Scripts\python -m pip freeze > %pip_reqs_dir%\pip_reqs.txt
