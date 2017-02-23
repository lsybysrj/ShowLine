import numpy as np
import matplotlib.pyplot as plt
import sys
import re
import pylab
import math

if len(sys.argv)!=4:
    print("usage: create.py signalFile sampleFreq sampleNum")
    print("Error: not enough arguments")
    exit()
filename=sys.argv[1]
sampleFreq=int(sys.argv[2])
sampleNum=int(sys.argv[3])

plt.figure()
yarray=open(filename).read().split(" ")
plt.plot([x for x in np.arange(0,math.pi*2*sampleNum/sampleFreq,math.pi*2/sampleFreq)],yarray)
plt.show()

