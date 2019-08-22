import os
import tkinter
from tkinter import filedialog
from pathlib import Path, PurePath
from os import path
from os.path import splitext

def foldFix(foldList):
    for item in foldList:
        if("_" in item[0]):
            splitFold = item[0].split("_", 1)
            os.rename(PurePath(item[1]) / item[0], PurePath(item[1]) / (splitFold[1] + " " + splitFold[0]))

def fileFix(fileList):
    for item in fileList:
        fileExt = splitext(item[0])[1]
        if("-" in item[0]):
            fileNum = item[0].split("-", 1)
            if("_" in item[0]):
                splitFile = (splitext(fileNum[1])[0]).split("_", 1)
                os.rename(PurePath(item[1]) / item[0], PurePath(item[1]) / (fileNum[0] + "-" + splitFile[1] + " " + splitFile[0] + fileExt))
        elif("_" in item[0]):
            splitFile = (splitext(item[0])[0]).split("_", 1)
            os.rename(PurePath(item[1]) / item[0], PurePath(item[1]) / (splitFile[1] + " " + splitFile[0] + fileExt))


def main():
    tkinter.Tk().withdraw()
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to trim file names...'))
    foldList = []
    fileList = []
    for root, folders, files in os.walk(dirPath):
        for name in folders:
            foldObj = [name, root]
            foldList.append(foldObj)
        for name in files:
            fileObj = [name, root]
            fileList.append(fileObj)
    fileFix(fileList)
    foldFix(foldList)
if(__name__ == "__main__"):
    main()