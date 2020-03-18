mkdir -p build

pushd build
cmake ..
makke -j4
popd

pushd python-package
sudo python3 setup.py install
popd
