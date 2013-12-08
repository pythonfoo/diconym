__author__ = 'bison'


import sys
import os
fPath = os.path.abspath(__file__)
path, filename = os.path.split(fPath)
sys.path.append(path)

#from .. import core
from LadenUndSpeichernWL  import ladenWL2 as lW


print "anon test"
listRootPath = os.path.abspath('../lists')
wl = lW.WhiteList()
#print wl.mainListDir(os.path.abspath('../lists') + "/tags_to_anonymize")
categorys = wl.categoryListFiles(listRootPath)

categoryNeverDel = categorys['tags_to_hold']
print wl.mainReadWhiteList(listRootPath + '/tags_to_hold/' +  categoryNeverDel[0] + ".txt")