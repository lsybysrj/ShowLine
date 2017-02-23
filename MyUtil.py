import numpy as np
import matplotlib.pyplot as plt;
def init():
    plt.figure(1)

def show():
    plt.show()

def save():
    plt.savefig("figure.svg")

def expandData(oldData,oldFrom,oldTo,times):
    newData=[0]*(oldTo-oldFrom)*times
    for n in range(0,oldTo-oldFrom):
        newData[n*times]=oldData[oldFrom+n]
    return newData
def addData(d1,d2):
    length=min(len(d1),len(d2))
    d=[0]*length
    for n in range(0,length):
        d[n]=float(d1[n])+float(d2[n])
    return d

def drawYDataFromFile(Ydatafile,xstart,xend):
   yarray=open(Ydatafile).read().split(" ")
   for i in np.arange(xstart,xend,(xend-xstart)/len(yarray)):
       xarray.append(i)
   plt.plot(xarray,yarray)

def getYDataFromFileDWT(Ydatafile):
    yarrayGroup=open(Ydatafile).read().split(",")
    num=len(yarrayGroup)
    for n in range(0,num):
        yarrayGroup[n]=yarrayGroup[n].split(" ")
    return yarrayGroup

def drawYDataFromFileDWTSplit(isoverlap,Ydatafile,xstart,xend):
    yarrayGroup=getYDataFromFileDWT(Ydatafile)
    num=len(yarrayGroup)
    for n in range(0,num):
        xarray=[]
        for i in np.arange(xstart,xend,(xend-xstart)/len(yarrayGroup[n])):
            xarray.append(i)
        if not isoverlap:
            plt.subplot(num,1,n+1)
            plt.ylabel("level "+str(n))
        plt.plot(xarray,yarrayGroup[n],"")

def drawYDataFromFileDWTAdd(Ydatafile,indexArray,xstart,xend):
    yarrayGroup=getYDataFromFileDWT(Ydatafile)
    lens=[]
    for n in range(0,len(indexArray)):
        lens.append(len(yarrayGroup[indexArray[n]]))
    maxLen=max(lens)
    totalYarray=[0]*maxLen
    for n in range(0,len(indexArray)):
        currentArray=yarrayGroup[indexArray[n]]
        currentArrayLen=len(currentArray)
        totalYarray=addData(expandData(currentArray,0,currentArrayLen,int(maxLen/currentArrayLen)),totalYarray)
    xarray=[]
    plt.plot([x for x in np.arange(xstart,xend,(xend-xstart)/len(totalYarray))],totalYarray)
