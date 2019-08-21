'''
package import
'''

import time
from datetime import datetime
from datetime import timedelta

class Timer(object):
    '''
    This class makes is designed to time different methods as wells as 
    tracking progress and time in the development process.
    
    Requirements:
    package datetime
    package time

    Methods:
    start_timer()
        - clears the timer and sets the start of the timer
    
    stop_timer()
        - stops the timer and sets the variables to display the text desired

    clear_timer()
        - clears the timer variables for reuse

    Attributes:
        datetime_start
        datetime_stop
        timedelta_time_diff
        float_seconds
        string_start_time
        string_stop_time
        string_time_diff
        string_display
    '''
    
    def __init__(self):
        '''      
        this method initialized the class; ??
        
        Requirements:
        package datetime
        
        Inputs:
        None
        Type: n/a
        Desc: n/a
        
        Important Info:
        None
        
        Variables:
        datetime_start
        Type: datetime
        Desc: start time

        datetime_stop
        Type: datetime
        Desc: stop time

        timedelta_time_diff
        Type: timedelta
        Desc: difference in start and stop times

        string_display
        Type: string
        Desc: text to display
        '''
        
        # variables
        self.datetime_start = datetime.now()
        self.string_start_time = self.datetime_start.strftime('%d-%b-%Y %H:%M:%S')
        self.datetime_stop = None
        self.string_stop_time = None
        self.timedelta_time_diff = None
        self.float_seconds = None
        self.string_time_diff = None
        self.string_display = ''
               
    def stop_timer(self, m_string_text = '', m_bool_print = False):
        '''
        this method stops the timer and displays any text desired
    
        Requirements:
        package time
        package datetime
    
        Inputs:
        m_string_text
        Type: string
        Desc: text to display when timer is stopped

        m_bool_print
        Type: boolean
        Desc: flag to print on console
        
        Important Info:
        None
    
        Return:
        object
        Type: float
        Desc: seconds of the process
        '''

        if self.datetime_start == None:
            raise Exception('start for timer is not set')
        else:
            # stop time
            self.datetime_stop = datetime.now()
            self.string_stop_time = self.datetime_stop.strftime('%d-%b-%Y %H:%M:%S')
            self.timedelta_time_diff = self.datetime_stop - self.datetime_start
            self.float_seconds = self.timedelta_time_diff.total_seconds()

            # string time difference
            self.string_time_diff = time.strftime('%H:%M:%S', time.gmtime(
                                                    self.timedelta_time_diff.total_seconds()))
            if m_string_text == '':
                self.string_display = 'process time is: ' + self.string_time_diff
            else:
                self.string_display = m_string_text + '; process time is: ' + self.string_time_diff               

            # print if desired
            if m_bool_print:
                print(self.string_display)
            
            # return value
            return self.float_seconds

    def start_timer(self):
        '''
        this method sets the start time for the timer.

        Requirements:
        package datetime
    
        Inputs:
        None
        Type: n/a
        Desc: n/a
        
        Important Info:
        None
    
        Return:
        object
        Type: datetime
        Desc: start time
        '''
        # clear variables
        self.clear_timer()
        self.datetime_start = datetime.now()
        self.string_start_time = self.datetime_start.strftime('%d-%b-%Y %H:%M:%S')
        
        # return value
        return self.datetime_start

    def clear_timer(self):
        '''
        this method clear all variables for the timer
    
        Requirements:
        package time
        package datetime
    
        Inputs:
        None
        Type: n/a
        Desc: n/a
        
        Important Info:
        None
    
        Return:
        None
        Type: n/a
        Desc: n/a
        '''

        # reset variables
        self.datetime_start = None
        self.datetime_stop = None
        self.timedelta_time_diff = None
        self.float_seconds = None
        self.string_time_diff = None
        self.string_display = ''
