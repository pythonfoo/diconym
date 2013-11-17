# Laden
class whitelist(object):
	def __init__(self,filename):
		self.filename = filename
		step1 = read_file(filename)
		step2 = read_line(step1)
		step3 = ignore_lines_sharp(step2)
		step4 = ignore_lines_spaces(step3)
		step5 = string_converter(step4)
		return step5

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
