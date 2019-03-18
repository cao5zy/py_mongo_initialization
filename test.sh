.env/bin/pylint src/app.py --rcfile=pylint.rc

nosetests tests -s --nologcapture -w ~/specialist/py_mongo_initialization/src
