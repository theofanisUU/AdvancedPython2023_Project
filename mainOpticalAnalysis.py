import functionsForOpticalData as functs
import sys

#----User Input Section----
#Wavelength region of interest for averaging the recorded intensity
#The averaged intensity is ploted over time (default code functionality)
integrStartWav=630    #first wavelength in the region of interest
integrFinishWav=1000  #last wavelength in the region of interest

#Note: the actual first and last wavelengths will be dependent on the step chosen
#      by the recording software, eg when requesting finishWav=1000, the actual
#      "last wavelength for averaging" might be something like 1000.16 nm


#Wavelengths of interest requiring more information
selectedWavelengths=[600,700,800,900,1000]
#Note: Again, any quantities extracted and calculated for the "selected wavelengths"
#      will in reality correspond to wavelengths very close to the requested ones
#      within 0.5nm

#Optional: Choose whether to plot the first spectrum
plotFirstSpectrum=False

#Optional: Choose timestamps to compare intensities on selected wavelengths
#Functionality aimed on comparing thin films before and after H2 loading
unloadedTimeStamp=1
loadedTimeStamp  =8.5



#----Functionality Section----
#Here the user input is passed to the functions of module "functionsForOpticalData"
#in order to produce all the requested plots

#locating the .txt spectrum files in subDir ~/InputData
txtFilesFoundSuccessfully,numberOfSpectra,spectrumDataList = functs.locateData()
if(txtFilesFoundSuccessfully==False): sys.exit() #if no data found stop operations

#extract key info from the first spectum 
launchTime,numberOfPointsInSpectrum,wavelengths,IntensitiesRef = \
    functs.TryReadFirstDataset(spectrumDataList)
    
#extract intensity values for all wavelengths 
timesFromLaunchInHours,intensities,averageIntensities = \
    functs.ScanFiles(spectrumDataList,numberOfSpectra,numberOfPointsInSpectrum,launchTime,wavelengths,integrStartWav,integrFinishWav,selectedWavelengths)

#Optional: Plot Intensity vs Wavelength for the first "reference" spectrum
if(plotFirstSpectrum): functs.PlotFirstSpectrum(wavelengths,IntensitiesRef)


functs.plotAverageIntensityOverTime(timesFromLaunchInHours,averageIntensities)
selectedIntensities = functs.getSelectedWavelengthsAtTimeStamp(0.1,timesFromLaunchInHours,selectedWavelengths,wavelengths,intensities)

functs.printUnloadedVsLoadedComparison(unloadedTimeStamp,loadedTimeStamp,timesFromLaunchInHours,selectedWavelengths,wavelengths,intensities)
