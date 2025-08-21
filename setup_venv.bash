#!/bin/bash
set - e
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $ROOT_DIR

./python_free_threaded_install/bin/python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
