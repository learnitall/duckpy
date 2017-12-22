Installation
============

A ``setup.py`` file has been provided to assist in managing duckpy's
installation, packaging and development. Dependencies should be installed
first however.


Dependencies
------------

The only dependency required for use is `pyautogui
<https://github.com/asweigart/pyautogui>`_, whose installation instructions
can be found `here <https://pyautogui.readthedocs.io/en/latest/install.html>`_.

.. note::

   pyautogui has some platform-specific pre-install steps, which must be
   completed before duckpy is installed.


Running setup.py
----------------

Now that dependencies are ready to go, just pass the ``install`` command
to the provided ``setup.py`` script::

   $ python3 setup.py install

and duckpy should be ready to use!
