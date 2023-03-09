#----Imports------------------
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

#----
integrStartWav=630
integrFinishWav=1000
    

#----Locating data----
def locateData():
    # locating input directory
    cwd = os.getcwd()
    targDir = os.chdir(cwd+"/Inputs")
    
    #extracting files
    fileList = os.listdir(targDir) #List ALL the files in working directory
    
    txtFileList=[]
    numberOfSpectra=0
    # filter for all the .txt files and store them
    for file in fileList:
        if file.endswith(".txt"):
            txtFileList.append(file)
            numberOfSpectra+=1
    return numberOfSpectra,txtFileList

numberOfSpectra,txtFileList = locateData()    

#---- Extracting first data----
def TryReadFirst():
    #check
    if(len(txtFileList)==0):
        print("no txt files found!")
        return False
    
    numberOfPointsInSpectrum=0
    
    WavelegthsRef,IntensitiesRef=[],[]
    try:
        timeFirst = txtFileList[0].split("_")
        timeFirst[0] = timeFirst[0][6:]
        #--------------------
        file = open(txtFileList[0], 'rt')
        for myline in file:
            numberOfPointsInSpectrum+=1
            #txt has a specific format with 2 columns seperated by ;
            wavelegth,intensity=myline.rstrip('\n').split(";")
            WavelegthsRef.append( float(wavelegth))
            IntensitiesRef.append( float(intensity))
    finally:
        file.close()
    
    WavelegthsRef = np.array(WavelegthsRef)
    IntensitiesRef=np.array(IntensitiesRef)
    return numberOfPointsInSpectrum,timeFirst,WavelegthsRef,IntensitiesRef

numberOfPointsInSpectrum,timeFirst,WavelegthsRef,IntensitiesRef = TryReadFirst()
print(timeFirst[0:4])

def wavToINdex(reqWav):
    searchIndex=0
    while(WavelegthsRef[searchIndex]<reqWav): searchIndex+=1
    return searchIndex
#Visualize the first Spectrum
def VisualizeFirst():
    fig,ax=plt.subplots()
    ax.set_xlabel("Wavelength (nm)");ax.set_ylabel('Intensity')
    plt.plot(WavelegthsRef,IntensitiesRef,ms=0.5)

# VisualizeFirst()    

#----Extract all intensity data----
def ScanFiles(integrStartWav,integrFinishWav,timeFirst):
    #---------
    averArr=np.zeros(numberOfSpectra)
    timeArr=np.zeros(numberOfSpectra)
    arrInt = np.zeros( (numberOfSpectra,numberOfPointsInSpectrum),dtype=np.float64)
    
    #--------
    specIndex=0
    firstIndex=wavToINdex(integrStartWav)
    lastIndex =wavToINdex(integrFinishWav)

    integrFinishWav=1000
    for txtFile in txtFileList: #For Each Spectrum
        time = txtFile.split("_")
        time[0] = time[0][6:]
        #in Hours
        timeSinceLaunch =24*(float(time[0])-float(timeFirst[0]))+ (float(time[1])-float(timeFirst[1]))+(float(time[2])-float(timeFirst[2]))/60 +(float(time[3])-float(timeFirst[3]))/3600
        timeArr[specIndex]=timeSinceLaunch
        #---------------------------------------
        arrIndex=0
        try:
            file = open(txtFile, 'rt')
            for line in file:  
                #extract the data
                wavelength,intensity=line.rstrip('\n').split(";")
                arrInt[specIndex,arrIndex]= intensity
                arrIndex+=1
            #end for (lines)
            
        finally:
            file.close()
            
        #get the average intensity 
        averArr[specIndex]= np.mean(arrInt[specIndex,firstIndex:lastIndex])
        specIndex+=1
    #end for (files)
    return  arrInt,averArr,timeArr
            
arrInt,averArr,timeArr =  ScanFiles(integrStartWav,integrFinishWav,timeFirst)

#-------------------------------------
def plotAverageOverTime(timeArr,averArr):
    fig2,ax2=plt.subplots()
    ax2.set_xlabel("time (h)");ax2.set_ylabel('Average Intensity')
    plt.plot(timeArr,averArr,ms=0.5)

print(timeArr)
print(averArr)
plotAverageOverTime(timeArr,averArr) #seems reasonable