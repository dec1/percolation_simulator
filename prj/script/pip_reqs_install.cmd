@echo off
set script_dir=%~dp0
call %script_dir%\common.cmd

CALL %venv_dir%\Scripts\python -m pip install --upgrade pip
CALl %venv_dir%\Scripts\python -m pip install --upgrade setuptools


REM 1) install latest (versions of) dependencies
CALL %venv_dir%\Scripts\python -m pip install -r %pip_reqs_dir%\pip_reqs_base.txt

REM 2) install exact (versions of) dependencies
REM CALL %venv_dir%\Scripts\python -m pip install  -r %pip_reqs_dir%\pip_reqs.txt
