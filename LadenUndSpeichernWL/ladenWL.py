# Laden
def read_file(filename):
	file1 = open(filename,'r')
	result = file1.read()
	file1.close()
	return result

def read_line(filecontent):
	result = filecontent.split('\n')
	return result

def ignore_lines_sharp(lines):
	result = []
	for line in lines:
		if list(line)[0] == '#':
			pass
		else:
			result.append(line)
	return result

def ignore_lines_spaces(lines):
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

def main(filename):
	step1 = read_file(filename)
	step2 = read_line(step1)
	step3 = ignore_lines_sharp(step2)
	step4 = ignore_lines_spaces(step3)
	return step4
print main('keys2hold.txt')