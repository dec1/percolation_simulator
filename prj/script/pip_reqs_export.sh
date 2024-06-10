#!/bin/bash

source common.sh

# persist the exact dependencies (recursively)
${venv_dir}/bin/pip freeze > ${pip_reqs_dir}/pip_reqs.txt
