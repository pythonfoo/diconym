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

	def startdia(self):
		sdia = DialogMaker()
		stitle = _("Diconym - Makes Dicom files anonymous")
		sdia.title(stitle)

		sdia.menu()
		sdia.topmenu(_("Tasks"))
		sdia.menuentry(_("Choice directory..."), self.choosedir)
		sdia.menuentry(_("Settings ..."), self.settingsdia)
		sdia.exitmenupoint()

		status = sdia.statusbar(_("Start"), 1, 0)

		stext = _("""Diconym is a program to make Dicom files anonymous for science, education. and more\n
It's Free Software - you can redistribute it and/or modify it\n
under the terms of the GNU General Public License as published by\n
the Free Software Foundation;\n
either version 3 of the License,\n
or (at your option) any later version.""")

		sdia.label(stext, 120,  0, 0, "yellow")
		self.ended = sdia
		sdia.mainloop()

	def endedia(self):
		self.ended.ende()


	def settingsdia(self):

		"""Dialog zum Setzen der Einstellungen"""
		self.endedia()
		
		print "hier"

	def choosedir(self):
		foldername = self.ended.folderOpenDialog()
		self.endedia()
		dcmfiles = core.getFileFromDir(foldername)
		print dcmfiles

def main():

	ti = TranslationIntegration("diconym")
	start = MainDialog()
	start.startdia()


if __name__ == '__main__':
	main()

