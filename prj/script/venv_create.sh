#!/bin/bash

source ./common.sh


python3 -m venv ${venv_dir}

echo ".....virtual environment created"

source ${venv_dir}/bin/activate

echo ".....pip reqs installing...."


source  ${script_dir}/pip_reqs_install.sh

echo ".....pip reqs installed"

#
# source $script_dir/venv/bin/deactivate

echo ".....venv ready"
