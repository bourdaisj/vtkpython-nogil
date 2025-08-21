#!/bin/bash
# download CPython 3.13.7
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd $ROOT_DIR
wget -O cpython-3.13.7.tar.gz https://github.com/python/cpython/archive/refs/tags/v3.13.7.tar.gz
tar xvf cpython-3.13.7.tar.gz
