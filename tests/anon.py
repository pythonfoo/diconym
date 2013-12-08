__author__ = 'bison'


import sys
import os
fPath = os.path.abspath(__file__)
path, filename = os.path.split(fPath)
sys.path.append(path)

#from .. import core
from ..LadenUndSpeichernWL  import ladenWL2 as lW

wl = lW.WhiteList()
print wl.mainListDir("lists/tags_to_anonymize")

