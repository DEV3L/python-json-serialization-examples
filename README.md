# python-json-serialization-examples
Repository containing simple example for serializing and de-serializing JSON in Python using marshmallow and json.dump/load

Tests exist to demonstrate the functionality of the code.

## Marshmallow
<https://pythonhosted.org/behave/>

## Python Standard Library - json
<https://docs.python.org/3/library/json.html>


# Prerequisites
* Python3 installed
    * <https://www.python.org/downloads/>
* Virtualenv installed
    * <https://virtualenv.pypa.io/en/latest/>
    * sudo pip install --upgrade pip virtualenv virtualenvwrapper

# Usage/Setup Instructions
1. From command line retrieve project from GitHub
    * git clone https://github.com/DEV3L/python-json-serialization-examples.git
2. Create a Python virtualenv for this project
    * mkvirtualenv -p /usr/bin/python3 python-json-serialization-examples
    * python setup.py develop
3. Execute test suite
    * py.test

```
(python-json-serialization-examples)➜  python-json-serialization-examples git:(master) py.test
============================================================================================ test session starts ============================================================================================
platform linux -- Python 3.4.3, pytest-2.8.5, py-1.4.31, pluggy-0.3.1
rootdir: /home/justin/WORKSPACE/PERSONAL/python-json-serialization-examples, inifile: 
collected 7 items 

python_json_serialization_examples/tests/unit/test_popo_schema.py ......
python_json_serialization_examples/tests/unit/test_psl_json.py .

========================================================================================= 7 passed in 0.11 seconds ==========================================================================================
(python-json-serialization-examples)➜  python-json-serialization-examples git:(master) 
```
