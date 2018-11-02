#!/usr/bin/env python
import sys
import math
f = open(sys.argv[1].strip())
x = int(f.read())
y = math.sqrt(x)


f = open("sqrt.txt","w")
f.write(str(y) + "\n")

f.close()
