# TimerWrapper

This is a very small package and is designed to time different parts of code that take more than a second.  This package is not intended to replace ``timeit`` or any other timer.  This is intended for developers to make debugging a bit easier.

### Installation

```pip install TimerWrapper```

### Usage

**Example 01:**
```python
from TimerWrapper import Timer

timer_00 = Timer()
<block of code>
float_time = timer_00.stop()
print(float_time)
```

**Example 01 Output (5 seconds):**
```
<code output>
5.0
```

**Example 02:** 
```python

from TimerWrapper import Timer

timer_01 = Timer('added text')
<block of code>
timer_01.stop_timer(m_bool_print = True)
```

**Example 02 Output (5 seconds):**
```
<code output>
process time is: 00:00:05 added text
```

**Clearing the timer:**
 
You can use the same instance to time additonal code blocks.  You must clear the timer first.
```python
from TimerWrapper import Timer

timer_01 = Timer()
<block of code>
float_time_00 = timer_01.stop_timer()

timer_01.clear_timer()
timer_01.start_timer()
<block of code>
float_time_01 = timer_01.stop_timer()
```

```float_time_00``` and ```float_time_01``` are different.