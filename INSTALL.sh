cd examples/python
make && cd ..
cp ../musci8/__init__.py python/infomap
cp ../musci8/clustering.py python/infomap
cp ../musci8/setup.py python/
cd python
cp infomap/_infomap.so /usr/local/lib/python2.7/dist-packages/infomap/
python setup.py install
