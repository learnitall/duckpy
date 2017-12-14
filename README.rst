===================================================
duckpy: a duckyscript interpreter written in Python
===================================================

..image: https://img.shields.io/badge/python-3-brightgreen.svg
..image: https://img.shields.io/badge/license-MIT-blue.svg


Ever find it tedious to write, modify and/or test a duckyscript? Ever wanted
to just execute it as if it was a script? duckpy has been written just for
this purpose. It converts duckyscript commands into Python functions (with
assistance from the `pyautogui <https://github.com/asweigart/pyautogui>`_
module) straight from the command line.

**Note:** This project is in very early development and should be considered
unstable.


Usage
-----

After installing, just run duckpy as a module and pass it the filepath to
a duckyscript for execution:

```
python3 -m duckpy [script name]
```

Use -v/--verbose to print logs:

```
python3 -m duckpy -v [script name]
```

Or use -vv/--vverbose to print all the logs!:

```
python3 -m duckpy -vv [script name]
```


Dependencies
------------

Requires pyautogui module. Installation instructions can be found
`here <https://pyautogui.readthedocs.io/en/latest/install.html>`_


Installation
------------

Just use the given `setup.py` script:

```
python3 setup.py install
```


.. include:: ./LICENSE.rst