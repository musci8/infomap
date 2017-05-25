cd examples/python
make && cd ..
cp ../musci8/__init__.py python/infomap
cp ../musci8/clustering.py python/infomap
cp ../musci8/setup.py python/
cd python
python setup.py install
cp infomap/_infomap.so /usr/local/lib/python2.7/dist-packages/infomap/
