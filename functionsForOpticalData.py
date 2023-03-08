#----Imports------------------
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def locateData():
    # locating input directory
    cwd = os.getcwd()
    targDir = os.chdir(cwd+"/Inputs")
    
    #extracting files
    fileList = os.listdir(targDir) #List ALL the files in the working directory 

    txtFileList=[]
    # filter for all the .txt files and store them
    for file in fileList:
        if file.endswith(".txt"): txtFileList.append(file)
    return txtFileList
txtFileList = locateData()    
    

def TryReadFirst():
    #check
    if(len(txtFileList)==0):
        print("no txt files found!")
        return False
    
    numberOfPointsInSpectrum=0
    
    WavelegthsRef,IntensitiesRef=[],[]
    file = open(txtFileList[0], 'rt')
    for myline in file:
        numberOfPointsInSpectrum+=1
        #txt has a specific format with 2 columns seperated by ;
        wavelegth,intensity=myline.rstrip('\n').split(";")
        WavelegthsRef.append( float(wavelegth))
        IntensitiesRef.append( float(intensity))
    file.close()
    
    WavelegthsRef = np.array(WavelegthsRef)
    IntensitiesRef=np.array(IntensitiesRef)
    return numberOfPointsInSpectrum,WavelegthsRef,IntensitiesRef

numberOfPointsInSpectrum,WavelegthsRef,IntensitiesRef = TryReadFirst()

#first infp
print(txtFileList)
print(numberOfPointsInSpectrum)
print(WavelegthsRef[:10])
print(IntensitiesRef[:10])