__author__ = 'bison'


import sys
import os
fPath = os.path.abspath(__file__)
path, filename = os.path.split(fPath)
print 'fPath', fPath
print 'path', path
print 'f', os.path.split(path)[0] #os.path.join(path, 'tests')
sys.path.append(os.path.split(path)[0])

#from .. import core
from LadenUndSpeichernWL  import ladenWL2 as lW


print "anon test"
listRootPath = os.path.abspath('../lists')
wl = lW.WhiteList()
#print wl.mainListDir(os.path.abspath('../lists') + "/tags_to_anonymize")
categorys = wl.categoryListFiles(listRootPath)

categoryNeverDel = categorys['tags_to_hold']
print wl.mainReadWhiteList(listRootPath + '/tags_to_hold/' +  categoryNeverDel[0] + ".txt")
