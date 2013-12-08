#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       diconymgraphics.py
#       
#       Copyright 2013 Michael Stehmann <info@rechtsanwalt-stehmann.de>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

# In Debian muessen folgende Pakete zusaetzlich installiert werden:
# -- python-tk

from UIelements.tkdialogmaker import DialogMaker
from UIelements.gettextintegration import TranslationIntegration

import core


class MainDialog(object):
	"""Erzeugt den Hauptdialog"""

	def dialogframe(self, title, statustext):
		"""Common elemts for dialogs"""
		self.sdia = DialogMaker()
		self.sdia.title(title)
		self.sdia.menu()
		self.sdia.topmenu(_("Tasks"))
		self.sdia.menuentry(_("Choice directory..."), self.choosedir)
		self.sdia.menuentry(_("Settings ..."), self.settingsdia)
		self.sdia.exitmenupoint()

		status = self.sdia.statusbar(_(statustext), 1, 0)

	def startdia(self):
		"""First dialog"""
		stitle = _("DICOnyM - Makes Dicom files anonymous")

		sstatustext = "Start"
		self.dialogframe(stitle, sstatustext)

		stext = _("""DICOnyM is a program to make Dicom files anonymous for science, education and more\n
It's Free Software - you can redistribute it and/or modify it\n
under the terms of the GNU General Public License as published by\n
the Free Software Foundation;\n
either version 3 of the License,\n
or (at your option) any later version.""")

		self.sdia.label(stext, 120,  0, 0, "yellow")
		self.ended = self.sdia
		self.sdia.mainloop()

	def endedia(self):
		self.ended.ende()


	def settingsdia(self):

		"""Dialog zum Setzen der Einstellungen"""
		self.endedia()
		
		print "hier"

	def choosedir(self):
		foldername = self.ended.folderOpenDialog()
		self.endedia()
		self.filelistdia(foldername)

	def filelistdia(self, foldername):
		"""Second dialog"""
		allFiles = core.getFilesFromDir(foldername)

		if allFiles != {}:
			print(allFiles)
			longestFullPath = self.getMaxLenFromList(allFiles.keys())
			longestFileName = self.getMaxLenFromList(allFiles.values())
			sumLineLen = longestFullPath + longestFileName + 4


			finalStringList = []
			for k in allFiles.keys():
				finalStringList.append("{k:{lFullPath}} | {val:{lFileName}}".format(k=k, lFullPath=longestFullPath,
																			val=allFiles[k], lFileName=longestFileName))

			stitle = _("DICOnyM - Makes Dicom files anonymous")

			sstatustext = "File list"
			self.dialogframe(stitle, sstatustext)
			self.sdia.tablelistbox(finalStringList, sumLineLen, 0, 0)
			self.ended = self.sdia
			self.sdia.mainloop()

		else:
			stitle = _("Nothing found!")
			stext = _("No dicom files found")
			wmb = DialogMaker()
			wmb.mwarning(stitle, stext)
			self.ended = wmb
			self.choosedir()

	def getMaxLenFromList(self, lst):
		longest = 0
		for element in lst:
			if len(element) > longest:
				longest = len(element)
		return longest

def main():

	ti = TranslationIntegration("diconym")
	start = MainDialog()
	start.startdia()


if __name__ == '__main__':
	main()

