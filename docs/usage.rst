Usage
=====


Command-Line Execution
----------------------

duckpy is a **command-line executable** module (built with `argparse
<https://docs.python.org/3.6/library/argparse.html>`_), meaning that it can be
run using python's ``-m`` option. Here's the list of available options as
given by ``--help``:

.. code-block:: bash

   $ python3 -m duckpy --help

   usage: duckpy [-h] [-v] [-vv] dscript

   duckpy: Duckyscript interpreter written in Python

   positional arguments:
     dscript          duckyscript file to execute (should be plaintext)

   optional arguments:
     -h, --help       show this help message and exit
     -v, --verbose    Print log messages to screen (level INFO)
     -vv, --vverbose  Print log messages to screen (level DEBUG). Note that this
                      will print a lot of output.


Feature Set
-----------

Duckyscript is broken down into essentially three parts:

   1. **Commands:** These involve the workflow controls that duckyscript
      offers (REPEAT, DEFAULT_DELAY, DELAY, STRING, REM)
   2. **Keys:** These are the keyboard modifiers, macros and keys that can be
      executed (e.g. GUI, CTRL-ALT, ESCAPE, ENTER, etc)
   3. **Aliases:** A lot of keys and commands have two references that can be
      used to execute the same functionality. For instance DOWNARROW and
      DOWN will both press the downarrow key.

As of release 0.1, duckpy supports all the features found in the
duckyscript `documentation wiki
<https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript>`_. The goal
is to eventually support all keys specified in the
`duckencoder's
<https://github.com/hak5darren/USB-Rubber-Ducky/tree/master/Encoder>`_
`keyboard.properties
<https://github.com/hak5darren/USB-Rubber-Ducky/blob/master/Encoder/resources
/keyboard.properties>`_ file.


Failsafe
--------

The Rubber Ducky is a physical device, meaning that in a worst case scenario
it can be unplugged to stop the execution of a payload. Since duckpy isn't
physical and can't be unplugged, ``pyautogui``'s `failsafe
<http://pyautogui.readthedocs.io/en/latest/introduction.html#fail-safes>`_
feature has been utilized instead to stop execution. In the case of an
emergency, just move the mouse into the upper left hand corner of the screen
and duckpy will error out.


Logging/Debugging
-----------------

Passing the ``-v`` or ``-vv`` options will print out log output that could be
helpful while debugging payloads. For instance, here's a sample
*Hello World!* payload for OSX::

   REM hello.txt
   REM Set default delay
   DEFAULT_DELAY 500
   REM Open Text Edit
   GUI SPACE
   STRING text edit
   ENTER
   DELAY 500
   REM Type the greeting
   STRING Hello World!
   ENTER
   GUI s
   DELAY 500
   STRING a_duckpy_test
   ENTER

And here is the output that Duckpy spits out, when given the ``-v`` option::

   duckpy ❯ python3 -m duckpy -v hello.txt
   duckpy - 14:36:35 12/21 - INFO:load: Loading script at 'hello.txt'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 0): 'REM hello.txt\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 1): 'REM Set default delay\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 2): 'DEFAULT_DELAY 500\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 3): 'REM Open Text Edit\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 4): 'GUI SPACE\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 5): 'STRING text edit\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 6): 'ENTER\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 7): 'DELAY 500\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 8): 'REM Type the greeting\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 9): 'STRING Hello World!\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 10): 'ENTER\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 11): 'GUI s\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 12): 'DELAY 500\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 13): 'STRING a_duckpy_test\n'
   duckpy - 14:36:35 12/21 - INFO:load: Got line (lineno: 14): 'ENTER\n'
   duckpy - 14:36:35 12/21 - INFO:load: Finished loading
   duckpy - 14:36:35 12/21 - INFO:run: Executing script at: 'hello.txt'
   duckpy - 14:36:35 12/21 - INFO:run: Running line 0: 'REM hello.txt'
   duckpy - 14:36:35 12/21 - INFO:run: Running line 1: 'REM Set default delay'
   duckpy - 14:36:35 12/21 - INFO:run: Running line 2: 'DEFAULT_DELAY 500'
   duckpy - 14:36:35 12/21 - INFO:run: Running line 3: 'REM Open Text Edit'
   duckpy - 14:36:35 12/21 - INFO:run: Running line 4: 'GUI SPACE'
   duckpy - 14:36:35 12/21 - INFO:run: Running line 5: 'STRING text edit'
   duckpy - 14:36:36 12/21 - INFO:run: Running line 6: 'ENTER'
   duckpy - 14:36:37 12/21 - INFO:run: Running line 7: 'DELAY 500'
   duckpy - 14:36:38 12/21 - INFO:run: Running line 8: 'REM Type the greeting'
   duckpy - 14:36:38 12/21 - INFO:run: Running line 9: 'STRING Hello World!'
   duckpy - 14:36:38 12/21 - INFO:run: Running line 10: 'ENTER'
   duckpy - 14:36:39 12/21 - INFO:run: Running line 11: 'GUI s'
   duckpy - 14:36:40 12/21 - INFO:run: Running line 12: 'DELAY 500'
   duckpy - 14:36:41 12/21 - INFO:run: Running line 13: 'STRING a_duckpy_test'
   duckpy - 14:36:41 12/21 - INFO:run: Running line 14: 'ENTER'
   duckpy - 14:36:42 12/21 - INFO:run: Finished execution
   duckpy ❯

.. warning::

   The ``-vv`` option will print out substantial amounts of log output, so be
   sure to duck and cover before using.


Python Execution
----------------

Although it's meant to be executed from the CLI, duckpy can be used within
Python quite easily to run duckyscript commands, check available/supported
keys and check aliases. See the `duckpy <duckpy.html>`_ module documentation
for more information.
