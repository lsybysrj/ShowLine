import MyUtil
import math
import sys
if len(sys.argv)<5:
    print("usage: acc.py signalfile sampleFreq sampleNum indexs..")
    exit()

filename=sys.argv[1]
sampleFreq=int(sys.argv[2])
sampleNum=int(sys.argv[3])
index=[int(x) for x in sys.argv[4::]]
MyUtil.init()
MyUtil.drawYDataFromFileDWTAdd(filename,index,0,math.pi*2*sampleNum/sampleFreq)
MyUtil.show()

