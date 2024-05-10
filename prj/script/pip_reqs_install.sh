#!/bin/bash

script_dir=$(dirname "$0")

$script_dir/venv/bin/python -m pip install --upgrade pip
$script_dir/venv/bin/pip install --upgrade setuptools


# Latest
# ------
# install (latest versions of) dependencies
$script_dir/venv/bin/pip install -r $script_dir/../pip_reqs_base.txt

# Exact
# ------
# alternatively, use this instead to install exact (recursive) dependencies previously 'frozen' by
# previous call to 'pip_reqs_export.sh'
#
# recommended for production
#./venv/bin/pip install -r ../pip_reqs_base.txt
