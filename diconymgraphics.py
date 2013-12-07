#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       diconymgraphics.py
#       
#       Copyright 2013 Michael Stehmann <info@rechtsanwalt-stehmann.de>
#       Copyright (C) 2013 for the gettext integration: Mechtilde Stehmann <ooo@mechtilde.de
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
import core
import gettext

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

	def startdia(self):
		sdia = DialogMaker()
		stitle = "Diconym - Makes Dicom files anonymous"
		sdia.title(stitle)

		sdia.menu()
		sdia.topmenu("Tasks")
		sdia.menuentry("Choice directory...", self.choosedir)
		sdia.menuentry("Settings ...", self.settingsdia)
		sdia.exitmenupoint()

		status = sdia.statusbar("Start", 1, 0)

		stext = """Diconym is a program to make Dicom files anonymous for science, education. and more\n
It's Free Software - you can redistribute it and/or modify it\n
under the terms of the GNU General Public License as published by\n
the Free Software Foundation;\n
either version 3 of the License,\n
or (at your option) any later version."""

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

	start = MainDialog()
	start.startdia()


if __name__ == '__main__':
	main()

