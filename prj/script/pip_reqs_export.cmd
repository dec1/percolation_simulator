@echo off
call common.cmd

CALL %venv_dir%\Scripts\pip freeze > %pip_reqs_dir%\pip_reqs.txt
