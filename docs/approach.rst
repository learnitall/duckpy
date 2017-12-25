Approach
========

Here's a breakdown of the thinking behind duckpy and its inner workings.


Usage Scenarios
---------------

Since duckpy is essentially just another programmable keyboard, there are
a lot of usage scenarios that it could be deployed to. However, duckpy was
built as a tool to help aid students in learning the ins and outs of
programming a `Rubber Ducky
<https://hakshop.com/products/usb-rubber-ducky-deluxe>`_. Some might see
Duckies as just toys, whereas some might see them as legitimate threats, but
whatever the case they can be utilized quite well as an educational vector
for system security and exploitation.

There are of course a few problems however that Duckies are facing in the
classroom:

   1. Testing payloads can take quite a bit of time and as a result, can be
      fairly tedious for some. This can be debated of course, but the goal of
      Rubber Duckies is to have students learn how to exploit a system,
      not how to fix the minute bugs that may exist within their code.
      Therefore, the more time that students allocate towards writing and
      testing the 'beefy' parts of their code that do the heavy lifting, the
      better.
   2. Rubber Duckies are expensive (around $50), possibly making it difficult
      for some classrooms to have one ducky per student. Again this can be
      debated, but each student in the classroom should have the ability to
      'exploit at will', even while they are at home. Having this ability gives
      them more time to test (and therefore to write) their payloads.
   3. The above can also apply to self-learning students who are not in a class
      that has a Rubber Ducky up for loan (i.e. they need to buy their own).
      The price tag might become discouraging.

These are the problems that duckpy seeks to address. The goal is for duckpy to
be a free, open-source Rubber Ducky that students can use to efficiently test
their payloads with ease, so that they may have a more enjoyable experience
learning this part of the security field.


Code Breakdown
--------------

The functionalities that a Rubber Ducky can perform can be done fairly simply
in Python. It really comes down to just delays and keystrokes, which there are
plenty of modules that can perform these actions (see `usage
<usage.html#feature-set>`_ for an overview of the duckyscript functions that
duckpy can perform). The true work that duckpy performs is translating raw
duckyscript into functions. This is done in a six step manner:

   1. Read the duckyscript script (that sounds weird, I know) and parse it
      into lines. This is performed in :py:meth:`duckpy.duck.DuckyScript.load`.
   2. Split each line into two sections: command and parameter.
   3. Parse the command into its 'true' identity if it's an alias (for
      instance if ``DEFAULTDELAY`` is given it will be parsed to
      ``DEFAULT_DELAY``). This accomplished through the function
      :py:func:`duckpy.duck.get_alias_target`.
   4. Determine the appropriate function that matches the duckyscript command.
      This is completed with the basic ``if-elif-else`` decision tree.
   5. If key names are found in the duckyscript line, then they are translated
      into names that the backend keystroke module understands. This is done
      through :py:func:`duckpy.duck.translate_key`.
   6. Construct the Python function. After the appropriate function is
      determined, :py:func:`duckpy.duck._set_args` is used to pre-set the
      Python function with the arguments necessary for execution. For instance,
      the line::

         STRING Hello world!

      would translate to:

      .. code-block:: python

         pyautogui.typewrite("Hello world!")

      therefore the constructed function will just pass ``"Hello World!"`` to
      :py:func:`pyautogui.typewrite`.

This whole process (steps 3-6) essentially takes place in
:py:meth:`duckpy.duck.DuckyCommand._to_python`, so check out its source code
for additional information. After this process is complete, native Python
objects are used to control the execution of duckyscript.
