#!/bin/bash
set -e
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $ROOT_DIR

bash download_cpython.bash
echo "Building and installing free-threaded CPython..."
bash build_free_threaded_python.bash > cpython_build.log
bash setup_venv.bash
source .venv/bin/activate
bash build_vtk_wheel.bash > vtk_wheel_build.log
