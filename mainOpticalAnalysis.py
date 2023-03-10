import functionsForOpticalData as func

#----Input----
integrStartWav=630
integrFinishWav=1000


#----Functionality----
numberOfSpectra,txtFileList = func.locateData()    
launchTime,numberOfPointsInSpectrum,Wavelengths,IntensitiesRef = \
    func.TryReadFirstDataset(txtFileList)
timesFromLaunchInHours,intensities,averageIntensities = \
    func.ScanFiles(txtFileList,numberOfSpectra,numberOfPointsInSpectrum,launchTime,Wavelengths,integrStartWav,integrFinishWav)

func.TryReadFirstDataset(txtFileList)
func.plotAverageOverTime(timesFromLaunchInHours,averageIntensities)
print("allok") 