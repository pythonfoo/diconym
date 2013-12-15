#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

main = Tk()
main.title("Testdialog")
# create the canvas, size in pixels
canvas = Canvas(main, width = 350, height = 350, bg = "white")
# pack the canvas into a frame/form
canvas.grid(row=0, column=0)
#expand = YES, fill = BOTH)
# load the .gif image file
# put in your own gif file here, may need to add full path
# like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
path =  '/home/michael/git/diconym/UIelements/diconym_logo.gif'
gif1 = PhotoImage(file = path)
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(10, 10, image = gif1, anchor = NW)
# run it ...
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
