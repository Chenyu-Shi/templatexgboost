mkdir -p build

pushd build
cmake ..
make -j4
popd

pushd python-package
sudo python3 setup.py install
popd
