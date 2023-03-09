#----Imports------------------
import os
import sys
import numpy as np
import matplotlib.pyplot as plt


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

#----Extract all intensity data----
def ScanFiles(): 
    arrInt = np.zeros( (numberOfSpectra,numberOfPointsInSpectrum),dtype=np.float64)
    specIndex=0
    for txtFile in txtFileList: #For Each Spectrum
        arrIndex=0
        file = open(txtFile, 'rt')
        for line in file:  
            #extract the data
            wavelength,intensity=line.rstrip('\n').split(";")
            arrInt[specIndex,arrIndex]= intensity
            arrIndex+=1
        #end for
        specIndex+=1
    #end for
    return  arrInt 
            
arrInt  =   ScanFiles()

#checking some data to verify that everything was read correctly
print(arrInt);print()
print(arrInt[0,2300:2305]);print()
print(arrInt[:,0])
            
            
            
