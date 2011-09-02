#!/bin/sh
# ref: http://www.franciscosouza.com/2010/08/flying-with-flask-on-google-app-engine/

echo grabbing flask
curl -o flask.zip https://nodeload.github.com/mitsuhiko/flask/zipball/0.7.2
unzip flask.zip
cp -r mitsuhiko-flask-*/flask ../

echo grabbing Werkzeug
curl -o Werkzeug.tar.gz http://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-0.7.1.tar.gz#md5=d5f2107fb2317944079b1c3019330c38
tar -xvzf Werkzeug.tar.gz
cp -r Werkzeug-*/werkzeug ../

echo grabbing Jinja2
curl -o jinja2.tar.gz http://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.5.tar.gz
tar -xvzf jinja2.tar.gz
cp -r Jinja2*/jinja2 ../

echo grabbing simplejson
curl -o simplejson.tar.gz http://pypi.python.org/packages/source/s/simplejson/simplejson-2.1.6.tar.gz#md5=2f8351f6e6fe7ef25744805dfa56c0d5
tar -xvzf simplejson.tar.gz
cp -r simplejson*/simplejson ../

echo grabbing gdata
curl -o gdata.zip http://gdata-python-client.googlecode.com/files/gdata-2.0.14.zip
unzip gdata.zip
cp -r gdata-*/src ../


echo "done grabbing gdata and flask dependencies"