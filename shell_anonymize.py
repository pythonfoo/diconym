__author__ = 'bison'


import sys
import os
import shutil
import core
from LadenUndSpeichernWL  import ladenWL2 as lW

sourceDir = ''
destDir = ''
if len(sys.argv) != 3:
	print 'Arguments have to be: "source_path" "dest_path"'
	exit(1)
	#sourceDir = '/home/bison/Dokumente/test/001_Anatomie_UK_Patient_1/DVT UK Patient 1'
	#destDir = '/home/bison/Dokumente/test/tmp'
else:
	sourceDir = sys.argv[1]
	destDir = sys.argv[2]

files = core.getFilesFromDir(sourceDir)
if not files:
	print 'no DICOM files found!'
	exit(1)


wl = lW.WhiteList()
categorys = wl.categoryListFiles('lists')
holdingTags = []
for whiteList in categorys['tags_to_hold']:
	holdingTags.append(wl.mainReadWhiteList('lists/tags_to_hold/'+whiteList+'.txt'))

print holdingTags
for f in files:
	baseName = os.path.basename(f)
	dstFile = os.path.join(destDir, baseName)
	print f
	#print dstFile
	#print 10*'*'
	core.anonymize_byWhitelist(holdingTags, f, dstFile)
	#print f

	#baseName = os.path.basename(f)
	#shutil.copy(f, os.path.join(destDir, baseName))
	#core.anonymize_byWhitelist()