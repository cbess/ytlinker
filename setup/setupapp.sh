#!/bin/sh

echo getting flask
curl -o flask.zip https://nodeload.github.com/mitsuhiko/flask/zipball/0.7.2
unzip flask.zip
cp -r mitsuhiko-flask-*/flask ../

echo getting Werkzeug
curl -o Werkzeug.tar.gz http://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-0.7.1.tar.gz#md5=d5f2107fb2317944079b1c3019330c38
tar -xvzf Werkzeug.tar.gz
cp -r Werkzeug-*/werkzeug ../

echo getting Jinja2
curl -o jinja2.tar.gz http://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.5.tar.gz
tar -xvzf jinja2.tar.gz
cp -r Jinja2*/jinja2 ../

echo getting simplejson
curl -o simplejson.tar.gz http://pypi.python.org/packages/source/s/simplejson/simplejson-2.1.6.tar.gz#md5=2f8351f6e6fe7ef25744805dfa56c0d5
tar -xvzf simplejson.tar.gz
cp -r simplejson*/simplejson ../

echo "done getting py dependencies"