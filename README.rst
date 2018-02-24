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

| **Clearing the timer:**
| 
| You can use the same instance to time additonal code blocks.  You must clear the timer first.
::

    from TimerWrapper import Timer
    
    timer_01 = Timer('block 01')
    <block of code>
    timer_01.stop_timer()

    timer_01.clear_timer()
    timer_01.start_timer()
    <block of code>
    timer_01.stop_timer('block 02')

| **Clearing the timer output:**
::

    <code block 01 output>
    process time: 00:00:05 block 01
    <code block 01 output>
    process time: 00:00:01 block 02