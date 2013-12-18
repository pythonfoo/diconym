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

	def dialogframe(self, title, statustext, c=1, cs=1):
		"""Common elemts for dialogs"""
		self.sdia = DialogMaker()
		self.sdia.title(title)
		self.sdia.menu()
		self.sdia.taskmenu(_("Tasks"))
		self.sdia.taskmenuentry(_("Choose directory..."), self.choosedir)
		self.sdia.taskmenuentry(_("Settings ..."), self.settingsdia)
		self.sdia.exitmenupoint()

		status = self.sdia.statusbar(statustext, c, 0, cs)

	def startdia(self):
		"""First dialog"""
		stitle = _("DICOnyM - Makes Dicom files anonymous")
		sstatustext = "Start"
		self.dialogframe(stitle, sstatustext, 2, 2)

		self.sdia.bilderfeld("UIelements/diconym_logo.gif", 350, 350, 0, 0)

		stext = _("""DICOnyM is a program to make Dicom files anonymous for science, education and more\n
It's Free Software - you can redistribute it and/or modify it\n
under the terms of the GNU General Public License as published by\n
the Free Software Foundation;\n
either version 3 of the License,\n
or (at your option) any later version.""")

		self.sdia.label(stext, 100,  0, 1, "yellow")
		self.ended = self.sdia
		self.sdia.mainloop()

	def endedia(self):
		self.ended.ende()


	def settingsdia(self):

		"""Dialog zum Setzen der Einstellungen"""
		self.endedia()
		
		print("hier")

	def choosedir(self):
		foldername = self.ended.folderOpenDialog()
		if foldername != "" and type(foldername) == str:
			self.filelistdia(foldername)

	def filelistdia(self, foldername):
		"""Second dialog"""
		allFiles = core.getFilesFromDir(foldername)

		if allFiles != {}:
			self.endedia()
			longestFullPath = self.getMaxLenFromList(allFiles.keys())
			longestFileName = self.getMaxLenFromList(allFiles.values())
			sumLineLen = longestFullPath + longestFileName + 4
			finalStringList = []
			for k in allFiles.keys():
				finalStringList.append("{k:{lFullPath}} | {val:{lFileName}}".format(k=k, lFullPath=longestFullPath,
																			val=allFiles[k], lFileName=longestFileName))

			stitle = _("DICOnyM - Makes Dicom files anonymous")
			sstatustext = _("File list")

			h = len(finalStringList)
			maxh = False # Listbox ohne Scrollbar
			mh = 10 # kann evt. hoeher gesetzt werden
			if h > mh: 
				h = mh
				maxh = True # Listbox mit Scrollbar
			self.dialogframe(stitle, sstatustext)
			self.sdia.tablelistbox(finalStringList, sumLineLen, h, 0, 0, maxh)

			self.sdia.editmenu(_("Edit"))
			self.sdia.editmenuentry(_("Choose selected files"), self.selectedfiles)
			self.ended = self.sdia
			self.sdia.mainloop()

		else:
			stitle = _("Nothing found!")
			stext = _("No dicom files found")
			self.sdia.mwarning(stitle, stext)
			self.choosedir()

	def selectedfiles(self):
		sfl = self.sdia.mehrfachauswahl(self.sdia.listbox)
		selectedfileslist = []
		sep = "|"
		for element in sfl:
			linesplit = element.split(sep)
			file = linesplit[0]
			file = file.strip()
			selectedfileslist.append(file)
		print(selectedfileslist) # nur zu Testzwecken

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

