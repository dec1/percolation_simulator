#!/bin/bash

script_dir=$(dirname "$0")
source ${script_dir}/common.sh

# let caller (eg ci pipeline) override python version, by passing as arg to his script, eg
#   - `venv_create.sh 3.11`
# if none passed then the python version used is
#   - that set in `common.sh`  if any, or if not set there then
#   - whatever is found as "python" on path
py_ver=${1:-$py_ver}
echo "using python version: " ${py_ver}


echo "creating venv..... "
python${py_ver} -m venv ${venv_dir}
echo ".....venv created"

source ${venv_dir}/bin/activate

echo ".....installing pip reqs ...."
source  ${script_dir}/pip_reqs_install.sh
echo ".....pip reqs installed"


source $script_dir/venv/bin/deactivate
echo ".....venv ready"
