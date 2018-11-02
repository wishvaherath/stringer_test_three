#!/usr/bin/env python
import sys
import math
f = open(sys.argv[1].strip())
x = int(f.read())
y = int(math.sqrt(x))


f = open(sys.argv[2].strip(),"w")
f.write(str(y) + "\n")

f.close()
