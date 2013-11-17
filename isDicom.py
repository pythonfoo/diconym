import os
import dicom

__author__ = 'bison'


def isDicom(fullpath):
	isOk = True
	try:
		dcm = dicom.ReadFile(fullpath)
	except Exception as ex:
		isOk = False
		print fullpath
		print ex
	return isOk

def getFileFromDir(dirPath):
	dirList = os.listdir(dirPath)
	dcmFiles = []
	for fname in dirList:
		fPath = os.path.join(dirPath, fname)
		if isDicom(fPath):
			dcmFiles.append(fPath)
	print dcmFiles


path = "../testFiles/001 Anatomie UK Patient 1/DVT UK Patient 1"  # insert the path to the directory of interest
getFileFromDir(path)