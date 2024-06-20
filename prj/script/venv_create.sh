#!/bin/bash

script_dir=$(dirname "$0")
source ${script_dir}/common.sh

echo "using python version: " ${py_ver}

python${py_ver} -m venv ${venv_dir}

echo ".....virtual environment created"

source ${venv_dir}/bin/activate

echo ".....pip reqs installing...."


source  ${script_dir}/pip_reqs_install.sh

echo ".....pip reqs installed"

#
# source $script_dir/venv/bin/deactivate

echo ".....venv ready"
