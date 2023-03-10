import functionsForOpticalData as func

#----Input----
integrStartWav=630
integrFinishWav=1000

selectedWavelengths=[600,700,800,900,1000]

unloadedTime=0.1

#----Functionality----
numberOfSpectra,spectrumDataList = func.locateData()    
launchTime,numberOfPointsInSpectrum,wavelengths,IntensitiesRef = \
    func.TryReadFirstDataset(spectrumDataList)
timesFromLaunchInHours,intensities,averageIntensities = \
    func.ScanFiles(spectrumDataList,numberOfSpectra,numberOfPointsInSpectrum,launchTime,wavelengths,integrStartWav,integrFinishWav,selectedWavelengths)


func.plotAverageOverTime(timesFromLaunchInHours,averageIntensities)
selectedIntensities = func.getSelectedWavelengthsAtTimeStamp(unloadedTime,timesFromLaunchInHours,selectedWavelengths,wavelengths,intensities)
print(selectedIntensities)