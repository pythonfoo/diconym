#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       gettextintegration.py
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

# Begin gettext integration

import locale
import os
import gettext

class TranslationIntegration(object):
	"""GNU-gettext for GNU/Linux"""

	def __init__(self, pname):

		self.moname = pname + ".mo"
		self.syslanguage()
		# check, whether it's a unix system installation
		_localepath = "/usr/share/locale/"

		_result = self.look4mo(_localepath)

		if _result == "xxx":
			self.syslanguage()
			_localepath = "locale/"
			_result = self.look4mo(_localepath)

		if not _result == "xxx":
			# chooses the right .mo file and installs translation
			trans = gettext.translation(pname, _localepath, [self.language])
			trans.install()
		else:
			# Translating the following strings is absurd!
			serror = "Bad package! No "+self.moname+" file found!"
			import tkMessageBox
			tkMessageBox.showerror('Error!', serror)
			import sys; sys.exit(1)

	def syslanguage(self):
		"""which is the language of the system (GNU/Linux)?"""
		_loclang = locale.getdefaultlocale()
		self.language = _loclang[0]
		return self.language

	def look4mo(self, localepath):
		"""choose only a language which a .mo file exists
		for, else use english or return 'xxx' """
		_lpath = localepath + self.language + "/LC_MESSAGES/" + self.moname
		
		if not os.path.exists(_lpath):

			_newlang = self.dosplit(self.language, "_")
			_lpath = localepath + _newlang + "/LC_MESSAGES/"+self.moname

			if os.path.exists(_lpath):
				self.language = _newlang
			else:
				_newlang = self.dosplit(self.language, "@")
				_lpath = localepath + _newlang + "/LC_MESSAGES/" + self.moname

				if os.path.exists(_lpath):
					self.language = _newlang
				else:     
					_lpath = localepath + "en/LC_MESSAGES/" + self.moname

					if os.path.exists(_lpath):
						self.language = "en"
					else:
						self.language = "xxx"

		return self.language

	def dosplit(self, language, splitter):

		"""
			splits language descriptor

			>>> gnugettext.dosplit(gnugettext, "de_DE", "_")
			'de'

			>>> gnugettext.dosplit(gnugettext, "be@latin", "@")
			'be'
		"""

		_newlang = language.split(splitter)
		_newlang = _newlang[0]
		
		return _newlang
		
# End gettext integration
