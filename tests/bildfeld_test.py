#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import os

main = Tk()
main.title("Testdialog")
# size in pixels
canvas = Canvas(main, width = 350, height = 350, bg = "white")
canvas.grid(row=0, column=0)


# find the image
bild = 'UIelements/diconym_logo.gif'
path = os.chdir("..")
path = os.path.abspath(".")
path = path + "/" + bild

gif1 = PhotoImage(file = path)

# put image on canvas
# image's upper left corner (NW) on the canvas is at x=10 y=10
canvas.create_image(10, 10, image = gif1, anchor = NW)

# some more elements
ausgabetext= """DICOnyM is a program to make Dicom files anonymous for science, education and more\n
It's Free Software - you can redistribute it and/or modify it\n
under the terms of the GNU General Public License as published by\n
the Free Software Foundation;\n
either version 3 of the License,\n
or (at your option) any later version."""
lb = Label(main, text = ausgabetext, width=100, bg="yellow")
lb.grid(row=0, column=1, columnspan=1)
lb = Label(main, text = path, width=45, bg="yellow")
lb.grid(row=1, column=0, columnspan=1)

main.mainloop()
