TimerWrapper
-------------------------

| This is a very small package and is designed to time different parts of code that take more than
| a second.  This package is not intended to replace ``timeit`` or any other timer.  This is intended 
| for developers to make debugging a bit easier.

Installation
============
``pip install TimerWrapper``

Usage
=====

| **Example 01:**

::

    from TimerWrapper import Timer

    timer_00 = Timer()
    <block of code>
    timer_00.stop()

| **Example 01 Output (5 seconds)**:
::

    <code output>
    process time is: 00:00:05

| 
| The stop_timer() method has a variable where you can add a string.
| 
| **Example 02:**
| 

::

    from TimerWrapper import Timer
    
    timer_01 = Timer('added text')
    <block of code>
    timer_01.stop_timer()

| **Example 02 Output (5 seconds):**
::

    <code output>
    process time is: 00:00:05 added text

| Properties of class:

- ``endline_character`` - self-explanatory (default is endline character ``\n``)
- ``ignore_blank_lines`` - if set to ``True``, blank lines in the file will not be read or indexed (default is ``True``)
- ``values_delimiter`` - character used by the csv to separate values within a line (default is ``,``)
- ``quotechar`` - character used by the csv to surround values that contain the value delimiting character (default is ``"``)
- ``ignore_corrupt`` - if set to ``True``, lines with an invalid length will return blank instead of raising an exception (default is ``False``)
