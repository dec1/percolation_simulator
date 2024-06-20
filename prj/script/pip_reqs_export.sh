#!/bin/bash

script_dir=$(dirname "$0")
source ${script_dir}/common.sh

# persist the exact dependencies (recursively)
${venv_dir}/bin/python -m pip freeze > ${pip_reqs_dir}/pip_reqs.txt
