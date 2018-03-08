#!/usr/bin/env python3
import time, saytime

t = time.localtime()
print("Content-type: text/html\n")
print(
    "In Kolkata, West Bengal, it is now " +
    saytime.saytime_t(t).words() +
    time.strftime(', on %A, %d %B %Y.')
)


