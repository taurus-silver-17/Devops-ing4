#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This web application is designed to run on a Raspberry Pi.
# GPIOs are used to operate module relays then lights and stuff.
# Ver 2.0
# License GNU GPLv3 <https://www.gnu.org/licenses/gpl.html>
####
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Rooms(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, nullable=False)
	comment = db.Column(db.String(128), unique=True, nullable=False)
	gpio = db.Column(db.Integer, unique=True, nullable=False)

	def __repr__(self):
		return "{0}-{1}-{2}".format(self.name, self.comment, self.gpio)

	def toList(self):
		return [self.name, self.comment, self.gpio]

#class Lights(db.Model):
#	id = db.Column(db.Integer, primary_key=True)
#	name = db.Column(db.String(64), unique=True, nullable=False)
#	status = db.Column(db.Boolean, nullable=False)
#	room = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
#
#	def __repr__(self):
#		return '<Lights {} Room {} Status {}>'.format(self.name, (self.room).name, self.status)

#class Users(db.Model):
#	id = db.Column(db.Integer, primary_key=True)
#	name = db.Column(db.String(8), unique=True, nullable=False)
#	pass = db.Column(db.String(128), unique=False, nullable=False)

