#!/bin/bash

script_dir=$(dirname "$0")

# persist the exact dependencies (recursively)
$script_dir/venv/bin/pip freeze > $script_dir/../pip_reqs.txt
