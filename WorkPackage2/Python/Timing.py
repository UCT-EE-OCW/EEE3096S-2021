#!/usr/bin/python3
"""
Python Practical 2 Code for Timing
Keegan Crankshaw
EEE3096S Prac 2 2019
Date: 7 June 2019

Adapted from Paul McGuire's answer on Stack Overflow
https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution/12344609#12344609
"""

from time import time, strftime, localtime
from datetime import timedelta

start = ''

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def startlog():
    global start
    start = time()
    log("Starting log")


def log(s, elapsed=None):
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)

def endlog():
    global start
    end = time()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

