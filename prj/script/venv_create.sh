#!/bin/bash

script_dir=$(dirname "$0")

python3 -m venv $script_dir/venv

echo ".....virtual environment created"

source $script_dir/venv/bin/activate

echo ".....pip reqs installing...."

source  $script_dir/pip_reqs_install.sh

echo ".....pip reqs installed"

#
# source $script_dir/venv/bin/deactivate

echo ".....venv ready"
