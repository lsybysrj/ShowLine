import math
import sys
if len(sys.argv)!=4:
    print("usage: create.py signalFile sampleFreq sampleNum")
    print("Error: not enough arguments")
    exit()
filename=sys.argv[1]
sampleFreq=int(sys.argv[2])
sampleNum=int(sys.argv[3])
myfile=open(filename,"w")
for i in range(0,sampleNum-1):
    n=i*math.pi*2/sampleFreq
    myfile.write(str(5*math.sin(n*2)+6*math.sin(n*9)+9*math.sin(n*36))+" ")
myfile.write(str(5*math.sin(sampleNum*2)+6*math.sin(sampleNum*9)+9*math.sin(sampleNum*36)))
myfile.close()
