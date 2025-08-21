#!/bin/bash
set -e
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $ROOT_DIR

# # if the venv is activated with the free-threaded python interpreter, CMake should find it automatically
# cmake -S vtk -B vtk_build -GNinja -DVTK_MODULE_ENABLE_VTK_fmt=YES -DVTK_PYTHON_FULL_THREADSAFE=ON -DVTK_WHEEL_BUILD=ON -DVTK_WRAP_PYTHON=ON -DVTK_GROUP_ENABLE_Web=YES -DCMAKE_INSTALL_PREFIX=$PWD/vtk_install
# cmake --build vtk_build --parallel 10
# source .venv/bin/activate
cd vtk_build
# python setup.py bdist_wheel
# auditwheel show dist/*.whl > ../wheel_output.log
# auditwheel repair dist/*.whl >> ../wheel_output.log
