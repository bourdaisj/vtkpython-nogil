#!/bin/bash
set - e
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $ROOT_DIR

cd cpython-3.13.7
./configure --enable-optimizations --disable-gil --prefix $PWD/../python_free_threaded_install
make -j10
make install
