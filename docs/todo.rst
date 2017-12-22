TODO
====

Below is a compilation of brainstormed tasks that could be done towards
improving the functionality and stability of duckpy.

* **Find new keyboard backend to replace pyautogui?** pyautogui works
  wonderfully, but it is not compatible with single user mode, which cuts off
  support for a lot of payloads.
* **Tests** Need to create unit tests (with coverage) and integration/build
  tests through a utility like travis-cli. Those kinds of tests will probably
  fail however, as the lack of an X server will prevent pyautogui from running.
* **In-Memory file support** Allow ``duck.DuckyScript`` to support loading from
  a StringIO instance.
* **Distribution via pip**