`script` dir contains bash and windows scripts for managing dependencies with **venv** and **pip**

- `venv_create` 
  - create python venv 
- `pip_reqs_install`
  - install pip reqs from pip_reqs/`pip_reqs_base`.txt (automatically called by _venv_create_)
- `pip_reqs_export` 
  - save (exact) currently installed versions of dependencies to pip_reqs/`pip_reqs`.txt
