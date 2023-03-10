#----Imports------------------
import os
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


#---- Extracting first data----
def TryReadFirstDataset(txtFileList):
    #check if files were found
    if(len(txtFileList)==0):
        print("no txt files found!")
        return False
    
    #keep track of spectra
    numberOfPointsInSpectrum=0
    
    #Waveleghts column is assumed the same in all files from the same experiment
    Wavelegths,IntensitiesRef=[],[]
    try:
        #record launch time from first spectrum file name
        launchTime = txtFileList[0].split("_")
        launchTime[0] = launchTime[0][6:]
        #--------------------
        file = open(txtFileList[0], 'rt')
        for myline in file:
            numberOfPointsInSpectrum+=1
            #txt has a specific format with 2 columns seperated by ;
            wavelegth,intensity=myline.rstrip('\n').split(";")
            Wavelegths.append( float(wavelegth))
            IntensitiesRef.append( float(intensity))
    finally:
        file.close()
    
    Wavelegths = np.array(Wavelegths)
    IntensitiesRef=np.array(IntensitiesRef)
    return launchTime,numberOfPointsInSpectrum,Wavelegths,IntensitiesRef

# print(timeFirst[0:4])

def wavelengthToIndex(reqWav):
    searchIndex=0
    while(Wavelegths[searchIndex]<reqWav): searchIndex+=1
    return searchIndex

#Visualize the first Spectrum
def VisualizeFirst(Wavelegths):
    fig,ax=plt.subplots()
    ax.set_xlabel("Wavelength (nm)");ax.set_ylabel('Intensity')
    plt.plot(Wavelegths,IntensitiesRef,ms=0.5)

# VisualizeFirst(Wavelegths)    

def calculateTimeSinceLaunch(launchTime,time):
    return 24*(float(time[0])-float(launchTime[0]))+ (float(time[1])-float(launchTime[1]))+(float(time[2])-float(launchTime[2]))/60 +(float(time[3])-float(launchTime[3]))/3600
    

#----Extract all intensity data----
def ScanFiles(integrStartWav,integrFinishWav,timeFirst):
    #-allocate memory to store the data
    timesFromLaunchInHours=np.zeros(numberOfSpectra)
    intensities = np.zeros( (numberOfSpectra,numberOfPointsInSpectrum),dtype=np.float64)
    averageIntensities    =np.zeros(numberOfSpectra)
    
    #--------
    specIndex=0
    firstIndex=wavelengthToIndex(integrStartWav)
    lastIndex =wavelengthToIndex(integrFinishWav)

    integrFinishWav=1000
    for txtFile in txtFileList: #For Each Spectrum
        #get time from filenames    
        time = txtFile.split("_")
        time[0] = time[0][6:]
        #time calculation 
        timesFromLaunchInHours[specIndex]=calculateTimeSinceLaunch(timeFirst,time)
        #---------------------------------------
        arrIndex=0
        try:
            file = open(txtFile, 'rt')
            for line in file:  
                #extract the data
                wavelength,intensity=line.rstrip('\n').split(";")
                intensities[specIndex,arrIndex]= intensity
                arrIndex+=1
            #end for (lines)
            
        finally:
            file.close()
            
        #get the average intensity 
        averageIntensities[specIndex]= np.mean(intensities[specIndex,firstIndex:lastIndex])
        specIndex+=1
    #end for (files)
    return  timesFromLaunchInHours,intensities,averageIntensities
            

#-------------------------------------
def plotAverageOverTime(timeArr,averArr):
    fig2,ax2=plt.subplots()
    ax2.set_xlabel("time (h)");ax2.set_ylabel('Average Intensity')
    plt.plot(timeArr,averArr,ms=0.5)


#-----running-----
numberOfSpectra,txtFileList = locateData()    
launchTime,numberOfPointsInSpectrum,Wavelegths,IntensitiesRef = TryReadFirstDataset(txtFileList)
timesFromLaunchInHours,intensities,averageIntensities =  ScanFiles(integrStartWav,integrFinishWav,launchTime)
plotAverageOverTime(timesFromLaunchInHours,averageIntensities) 
#seems reasonable