#----Imports------------------
import os
import sys
import numpy as np
import matplotlib.pyplot as plt


def locateData():
    cwd = os.getcwd()
    targDir = os.chdir(cwd+"/Inputs")
    
    fileList = os.listdir(targDir) #List ALL the files in the working directory 
    #print(fileList)#DEBUG: check that files were found successfully
    
    txtFileList=[]
    # filter for all the .txt files and store them
    for file in fileList:
        if file.endswith(".txt"): txtFileList.append(file)
    print(txtFileList)#DEBUG: check that txt files were found successfully
    
locateData()