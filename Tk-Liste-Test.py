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

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
from tkFont import *
import core
import os

class DialogMaker(object):
	"""Methoden zur Erzeugung und Gestaltung von Tkinter-Dialogen"""

	def __init__(self):
		"""Erzeugt Tkinter-Dialog und setzt Dialogtitel"""
		self.dia=Tk()

	def title (self, title):
		self.diatitle(title)

	def diatitle (self, title):
		"""Setzt den Titel des Dialogs"""
		self.dia.title(title)

	def mainloop(self):
		"""Erzeugt Dialog"""
		self.dia.mainloop()

	def button(self, btext, befehl, r, c):
		"""Erzeugt den Auswahlbutton"""
		auswahlbutton = Button(self.dia, text = btext, command = befehl)
		auswahlbutton.grid(row=r, column=c, padx=10)

	def endebutton(self, r, c):
		"""Erzeugt den Button zum Beenden"""
		eb = Button(self.dia, text = "Ende", fg="red", command = self.ende)
		eb.grid(row=r, column=c)

	def ende(self):
		"""Beendet den Dialog"""
		self.dia.destroy()

	def label(self, ausgabetext, w, r, c, bgc, cs=1):
		"""Erzeugt ein Anzeigefeld"""
		lb = Label(self.dia, text = ausgabetext, width=w, bg=bgc)
		lb.grid(row=r, column=c, columnspan=cs)

	def eingabeFeld(self, w, r, c, cs=1):
		"""Erzeugt ein Eingabefeld"""
		e = Entry(self.dia, width=w)
		e.grid(row=r, column=c, columnspan=cs)
		return e

	def listbox(self, liste, w, r, c):
		"""Erzeugt ein Listenfeld"""
		self.listbox = Listbox(self.dia, width=w)
		_fontl = Font(family='Courier', size=10, underline=1)
		self.listbox.config(font=_fontl)
		#self.listbox.config(font=('Courier 10 Pitch', 10))
		for i in range(0,len(liste)):
			self.listbox.insert("end", "  "+liste[i])
		self.listbox.grid(row=r, column=c, padx=5)
		return self.listbox

	def auswahl(self, listbox):
		"""Stellt die im Listenfeld des Dialoges gewaehlte Auswahl fest"""
		auswahl=listbox.get("active").strip()
		return auswahl

	# Allgemeine Elemente

	def label(self, ausgabetext, w, r, c, bgc, cs=1):
		"""Erzeugt ein Anzeigefeld"""
		lb = Label(self.dia, text = ausgabetext, width=w, bg=bgc)
		lb.grid(row=r, column=c, columnspan=cs)

	def eingabeFeld(self, w, r, c, cs=1):
		"""Erzeugt ein Eingabefeld"""
		e = Entry(self.dia, width=w)
		e.grid(row=r, column=c, columnspan=cs, padx=20)
		return e

	def minfo(self, mbtitle, mbtext, btype="ok"):
		sb = messagebox.showinfo(mbtitle, mbtext, type=btype)
		return sb

	def mwarning(self, mbtitle, mbtext, btype="ok"):
		sb = messagebox.showwarning(mbtitle, mbtext, type=btype)
		return sb

	def merror(self, mbtitle, mbtext, btype="ok"):
		sb = messagebox.showerror(mbtitle, mbtext, type=btype)
		return sb

	def fileOpenDialog(self):
		filename = askopenfilename(filetypes = [('all files','*.*')],title ="Suche nach Dicom-Verzeichnissen")
		return(filename)
		
	def folderOpenDialog(self):
		foldername = askdirectory(title ="Suche nach Dicom-Verzeichnissen")
		return(foldername)

	def statusbar(self, sbtext, r, c, cs=1):
		pad = 1
		self.status = Label(self.dia, text="", bd=1, relief=SUNKEN, anchor=W)
		self.status.config(text=sbtext)
		self.status.grid(row=r, columnspan=cs, column=c, sticky=E+W, pady=pad, padx=pad)

	def menu(self):
		self.menu = Menu(self.dia)
		self.dia.config(menu=self.menu)

	def topmenu(self, topname):
		self.topmenu = Menu(self.menu)
		self.menu.add_cascade(label=topname, menu=self.topmenu)

	def menuentry(self, mlabel, mcommand):
		self.topmenu.add_command(label=mlabel, command=mcommand)

	def menuseparator(self):
		self.topmenu.add_separator()

	def exitmenupoint(self):
		self.topmenu.add_command(label="Exit", command=self.ende)


class MainDialog(object):
	"""Erzeugt den Hauptdialog"""

	def getMaxLenFromList(self, lst):
		longest = 0
		for element in lst:
			if len(element) > longest:
				longest = len(element)
		return longest
		
	def getFilesFromDir(self, dirPath):
		'''for testing prupose, simulate the function from
		core.getFilesFromDir()
		'''
		dirList = os.listdir(dirPath)                                               
		dcmFiles = {}                                           
		for fname in dirList:                                                       
			fPath = os.path.join(dirPath, fname)                                    
			dcmFiles[fPath] = fname                                              
		return dcmFiles  
		
				
	def startdia(self):
		sdia = DialogMaker()
		stitle = "Diconym - Makes Dicom files anonymous"
		sdia.title(stitle)
		
		'''
		eintrag11 = "Hallo"
		eintrag1 = eintrag11 + (15 - len(eintrag11))*" " + "| " + "Welt"+ 5*" "
		print (15 - len(eintrag11))
		eintrag21 = "Hallo Hallo"
		eintrag2 = eintrag21 + (15 - len(eintrag21))*" " + "| " + "Welt"+ 5*" "
		print (15 - len(eintrag21))
		_liste = [eintrag1, eintrag2]
		eintrag31 = "Wunderbare"
		eintrag3 = eintrag31 + (15 - len(eintrag31))*" " + "| " + "Welt"+ 5*" "
		print (15 - len(eintrag31))
		_liste = [eintrag1, eintrag2, eintrag3]
		sdia.listbox(_liste, 30, 0, 0)
		'''
		
		allFiles = self.getFilesFromDir(".")
		
		longestFullPath = self.getMaxLenFromList(allFiles.keys())
		longestFileName = self.getMaxLenFromList(allFiles.values())
		totalLineLen = longestFullPath + longestFileName + 4
			
			
		finalStringList = []
		for k in allFiles.keys():
			finalStringList.append(k.ljust(longestFullPath) + "|" + allFiles[k].rjust(longestFileName))

		
		sdia.listbox(finalStringList, totalLineLen, 0, 0)
		
		sdia.mainloop()	

def main():

	start = MainDialog()
	start.startdia()


if __name__ == '__main__':
	main()
