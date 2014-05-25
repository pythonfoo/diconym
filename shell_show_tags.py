__author__ = 'bison'

import sys
import core
import dicom

filePath = '/home/bison/Dokumente/test/tmp/3DSlice1.dcm'
if len(sys.argv) != 2:
	print 'Arguments have to be: "path_to_image"'
	exit(1)
else:
	filePath = sys.argv[1]

if not core.isDicom(filePath):
	print 'This is not a DICOM file!'
	exit(1)

def getValMaxLen(val):
	tmp = str(val)
	if len(tmp) > 42:
		return tmp[:42] + '...'
	else:
		return tmp

dataset = dicom.read_file(filePath)

for dt in dataset.keys():
	print 'key:    ', dt
	try:
		print 'dataset:', dataset[dt]
		print 'value:  ', getValMaxLen(dataset[dt].value)
	except Exception as ex:
		print ex
	print 10*'#'