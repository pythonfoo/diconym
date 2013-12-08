#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       tkdialogmaker.py
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

from Tkinter import *
import tkMessageBox
from tkFileDialog import *
from tkFont import *
import os
from gettextintegration import TranslationIntegration


class DialogMaker(object):
	"""Methoden zur Erzeugung und Gestaltung von Tkinter-Dialogen"""

	def __init__(self):
		ti = TranslationIntegration("tkdialogmaker")
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
		eb = Button(self.dia, text = _("End"), fg="red", command = self.ende)
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

	def tablelistbox(self, liste, w, r, c):
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
		sb = tkMessageBox.showinfo(mbtitle, mbtext, type=btype)
		return sb

	def mwarning(self, mbtitle, mbtext, btype="ok"):
		sb = tkMessageBox.showwarning(mbtitle, mbtext, type=btype)
		return sb

	def merror(self, mbtitle, mbtext, btype="ok"):
		sb = tkMessageBox.showerror(mbtitle, mbtext, type=btype)
		return sb

	def fileOpenDialog(self):
		filename = askopenfilename(filetypes = [('all files','*.*')],title =_("Search for Dicom directories"))
		return(filename)
		
	def folderOpenDialog(self):
		foldername = askdirectory(title =_("Search for Dicom directories"))
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
		self.topmenu.add_command(label=_("Exit"), command=self.ende)


def main():
	
	sdia = DialogMaker()
	stitle = "Test"
	sdia.title(stitle)

	sdia.menu()
	sdia.topmenu("Tasks")
	sdia.exitmenupoint()

	stext = """Nothing happens.\n
	Just a test."""
	sdia.label(stext, 40,  0, 0, "yellow")

	sdia.mainloop()

	return 0

if __name__ == '__main__':
	main()

