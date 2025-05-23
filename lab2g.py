#!/usr/bin/env 

import sys

if len(sys.argv) == 2:
    n = int(sys.argv[1])
else:
    n = 3

while n > 0:
    print(n)
    n -= 1
print("blast off!")
