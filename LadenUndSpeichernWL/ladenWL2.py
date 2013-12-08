import os

class whitelist(object):
	def __init__(self):
		pass

	def mainReadWhitelist(self,filename):
		filecontent = self.readFile(filename)
		lines = self.readLine(filecontent)
		lines = ignoreLinesSharp(lines)
		lines = ignoreLinesSpaces(lines)
		result = stringConverter(lines)
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