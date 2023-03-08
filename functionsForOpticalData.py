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
        if file.endswith(".txt"):
            txtFileList.append(file)
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

#Test Scan the more txt files
def ScanFiles(): 
    for txtFile in txtFileList: #For Each Spectrum
        #print(f"reading {txtFile}")
        arrWav = np.zeros(numberOfPointsInSpectrum,dtype=np.float64)
        arrInt = np.zeros(numberOfPointsInSpectrum,dtype=np.float64)
        arrIndex=0
        file = open(txtFile, 'rt')
        for line in file:  
            #extract the data
            
            wavelength,intensity=line.rstrip('\n').split(";")
            arrWav[arrIndex]= wavelength
            arrInt[arrIndex]= intensity
            arrIndex+=1
    return  arrWav, arrInt 
            
arrWav, arrInt  =   ScanFiles()

#read data from last  
print(arrWav[100:105]) 
print(arrInt[100:105])
print()
            
            
            
