import os

class WhiteList(object):
	def __init__(self):
		pass

	def mainReadWhiteList(self,filename):
		filecontent = self._readFile(filename)
		lines = self._readLine(filecontent)
		lines = self._ignoreLinesSharp(lines)
		lines = self._ignoreBackslash(lines)
		lines = self._ignoreClearLines(lines)
		lines = self._ignoreLinesSpaces(lines)
		result = self._stringConverter(lines)
		return result

	def _readFile(self,filename):
		file1 = open(filename,'r')
		result = file1.read()
		file1.close()
		return result

	def _readLine(self,filecontent):
		result = filecontent.split('\n')
		return result

	def _ignoreLinesSharp(self,lines):
		result = []
		for line in lines:
			if line.startswith('#'):
				pass
			else:
				result.append(line)
		return result

	def _ignoreLinesSpaces(self,lines):
		result = []
		tmpLine = ''
		for line in lines:
			for lineChar in line:
				if lineChar != "\t" and lineChar != ' ':
					tmpLine += lineChar
				else:
					break
			result.append(tmpLine)
			tmpLine = ''
		return result
	
	def _ignoreBackslash(self,lines):
		result = []
		for line in lines:
			if '\r' in line:
				line = line.split('\r')
				result.append(line[0])
			else:
				result.append(line)
		return result
	
	def _ignoreClearLines(self,lines):
		result = []
		for line in lines:
			if line != '':
				result.append(line)
		return result
	
	def _stringConverter(self,lines):
		result = []
		tmpPart1 = ''
		tmpPart2 = ''
		for line in lines:
			tmp = line.split(',')
			tmpPart1 = tmp[0]
			tmpPart2 = tmp[1]
			result.append((tmpPart1,tmpPart2))
		return result	

	def mainListDir(self,fullpath):
		directory = os.listdir(fullpath)
		path = []
		for f in directory:
			path.append(str(fullpath+'/'+f))
		return path
		
	def categoryListFiles(self,fullpath):
		folderContent = os.listdir(fullpath)
		content = {}
		'''
		for folder in folderContent:
			tmpFolderContent = os.listdir(path + '/' + str(folder))
			counter = 0
			for f in tmpFolderContent:
				if '.txt' in f:
					f = f.replace('.txt','')
				tmpFolderContent[counter] = f
				counter += 1
					
			content[folder] = tmpFolderContent
		'''
		
		for folder in folderContent:
			tmpFolderContent = os.listdir(fullpath + '/' + folder)
			folderLength = len(tmpFolderContent)
			for i in range(folderLength):
				length = len(tmpFolderContent[i])
				if '.txt' in tmpFolderContent[i] and length > 4:
					tmpFolderContent[i] = tmpFolderContent[i][:-4]
			content[folder] = tmpFolderContent
		return content

if __name__ == '__main__':
	print 'Funktion wird aufgerufen'
	wl = WhiteList()
	tmpList = wl.categoryListFiles('../lists')
	print tmpList
	for category in tmpList:
		for list in tmpList[category]:
			tmp = wl.mainReadWhiteList('../lists/'+category +'/'+list+'.txt')
			print tmp