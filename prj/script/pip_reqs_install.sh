#!/bin/bash

script_dir=$(dirname "$0")
source ${script_dir}/common.sh

${venv_dir}/bin/python -m pip install --upgrade pip
${venv_dir}/bin/python -m pip install --upgrade setuptools



# 1) install latest (versions of) dependencies
${venv_dir}/bin/python -m pip install -r ${pip_reqs_dir}/pip_reqs_base.txt

# 2) install exact (versions of) dependencies
#./venv/bin/python -m pip install -r ../pip_reqs.txt

# eg from previous call to 'pip_reqs_export.sh'
# recommended for production
