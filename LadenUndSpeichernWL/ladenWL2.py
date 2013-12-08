import os

class WhiteList(object):
	def __init__(self):
		pass

	def mainReadWhiteList(self,filename):
		filecontent = self.readFile(filename)
		lines = self.readLine(filecontent)
		lines = self.ignoreLinesSharp(lines)
		lines = self.ignoreLinesSpaces(lines)
		result = self.stringConverter(lines)
		return result

	def readFile(self,filename):
		file1 = open(filename,'r')
		result = file1.read()
		file1.close()
		return result

	def readLine(self,filecontent):
		result = filecontent.split('\n')
		return result

	def ignoreLinesSharp(self,lines):
		result = []
		for line in lines:
			if list(line)[0] == '#':
				pass
			else:
				result.append(line)
		return result

	def ignoreLinesSpaces(self,lines):
		result = []
		tmpLine = ''
		for line in lines:
			for i in range(len(line)):
				if list(line)[i] != '	' and list(line)[i] != ' ':
					tmpLine += list(line)[i]
				else:
					break
			result.append(tmpLine)
			tmpLine = ''
		return result

	def stringConverter(self,lines):
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
		
	def categoryListFiles(self,path):
		folderContent = os.listdir(path)
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
			tmpFolderContent = os.listdir(path + '/' + folder)
			folderLength = len(tmpFolderContent)
			for i in range(folderLength):
				length = len(tmpFolderContent[i])
				if '.txt' in tmpFolderContent[i] and length > 4:
					tmpFolderContent[i] = tmpFolderContent[i][:-4]
			content[folder] = tmpFolderContent
			
		print content
	
	def main():
		pass
if __name__ == '__main__':
	main()
wl = WhiteList()
wl.categoryListFiles('/media/M3NT0R/Privat/Projekte/git/diconym/lists')
