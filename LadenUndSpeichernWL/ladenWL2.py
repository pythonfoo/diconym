import os

class whitelist(object):
	def __init__(self):
		pass

	def main_Read_WL(self,filename):
		filecontent = self.read_file(filename)
		lines = self.read_line(filecontent)
		lines = ignore_lines_sharp(lines)
		lines = ignore_lines_spaces(lines)
		result = string_converter(lines)
		return result

	def read_file(self,filename):
		file1 = open(filename,'r')
		result = file1.read()
		file1.close()
		return result

	def read_line(self,filecontent):
		result = filecontent.split('\n')
		return result

	def ignore_lines_sharp(self,lines):
		result = []
		for line in lines:
			if list(line)[0] == '#':
				pass
			else:
				result.append(line)
		return result

	def ignore_lines_spaces(self,lines):
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

	def string_converter(self,lines):
		result = []
		tmpPart1 = ''
		tmpPart2 = ''
		for line in lines:
			tmp = line.split(',')
			tmpPart1 = tmp[0]
			tmpPart2 = tmp[1]
			result.append((tmpPart1,tmpPart2))
		return result	

	def main_List_Dir(self,fullpath):
		directory = os.listdir(fullpath)
		path = []
		for f in directory:
			path.append(str(fullpath+'/'+f))
		return path