import MyUtil
import math
import sys

if len(sys.argv)<4:
    print("usage: split.py signalfile sampleFreq sampleNum ")
    exit()

filename=sys.argv[1]
sampleFreq=int(sys.argv[2])
sampleNum=int(sys.argv[3])

MyUtil.init()
MyUtil.drawYDataFromFileDWTSplit(False,filename,0,math.pi*2*sampleNum/sampleFreq)
MyUtil.show()

