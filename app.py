#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This web application is designed to run on a Raspberry Pi.
# GPIOs are used to operate module relays then lights and stuff.
# Ver 2.0
# License GNU GPLv3 <https://www.gnu.org/licenses/gpl.html>
####
from flask import Flask, render_template, flash, request, redirect, make_response
app = Flask(__name__)
app.secret_key = b'BASE64HASH'
## Init DB
import os
from models import db,Rooms
POSTGRES = {
	'user' : os.environ['POSTGRES_USER'],
	'pass' : os.environ['POSTGRES_PASSWORD'],
	'db' : os.environ['POSTGRES_DB'],
	'host' : 'devops-db',
	'port' : '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pass)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)
## Init GPIO pins
#from gpiozero import LEDBoard
#leds = LEDBoard(4, 17, 27, 22, 26, 19, 13, 6)
#leds = {}
#gpios = db.session.query(Rooms.gpio).all()
#if gpios == []:
#	None
#else:
#	for g in gpios:
#		leds[g] = LED("BOARD"+str(g))
## Route URLs and do all the stuff
@app.route('/truhome/')
def main():
	rooms = Rooms.query.all()
	return render_template('index.html', result = rooms)

@app.route('/truhome/ctrl/<room>', methods=['GET'])
def ctrl_lights(room):
	"""
		Controls the light in a room through RPi GPIO pins.
		Simply mention the name of the room and the GPIO pin corresponding to the light will be found.
		Eg. 'GET /ctrl/kitchen' will turn on/off the light in the kitchen.
		In fact, each time ctrl_lights is called, we need to check GPIO pin status to inverse.
	"""
	rooms = Rooms.query.all()
	if rooms == []:
		return "Room %s does not exist. In fact there is no room created !" % (room)
	else:
		for r in rooms:
			if r.toList()[0] == room:
				#leds[r.toList[2]].toggle()
				flash("Light turned on/off")
				return redirect("/truhome")
			else:
				return "Room %s does not exist." % (room)
	abort(500)
	return "Error while querying the database."

@app.context_processor
def toTemplates():
	""" Allows functions to be available into templates. """
	#@app.template_filter('get_st')
	def get_status(room):
		"""
			Gets status of the light in a room.
			Simply mention the name of the room and the status of the corresponding GPIO pin will be found.
			Eg. In the template, get_st(kitchen) will return 0 or 1.
		"""
		gpios = db.session.query(Rooms.gpio).filter(Rooms.name == room).scalar()
		#status = leds[gpios].value
		if status == 0:
			return 0
		else:
			return 1
		abort(500)
		return "Error while reading GPIO input"
	return dict(get_st=get_status)
def getRooms():
	""" Gets the list of rooms in every template. """
	rooms = Rooms.query.all()
	return dict(result=rooms)

@app.route('/truhome/add', methods=['POST'])
def add_room():
	"""
		Adds a room in the database.
		A room has a name, a comment and a status field (light on/off).
		This method is designed to be called by an HTML form.
	"""
	room = request.form['name']
	desc = request.form['comment']
	pin = request.form['gpio']
	rooms = Rooms.query.all()
	if rooms == []:
		new_room = Rooms(name = room, comment = desc, gpio = pin)
		db.session.add(new_room)
		#leds[pin] = LED("BOARD"+str(pin))
	else:
		for r in rooms:
			if r.toList()[0] == room:
				return "Room %s already exists." % (room)
			else:
				new_room = Rooms(name = room, comment = desc, gpio = pin)
				db.session.add(new_room)
				#leds[pin] = LED("BOARD"+str(pin))
	db.session.commit()
	return "Room %s created !" % (room)

@app.route('/truhome/del', methods=['POST'])
def del_room():
	"""
		Removes a room from the database.
		This method is designed to ba called by an HTML form.
	"""
	room = request.form['room']
	rooms = Rooms.query.filter(Rooms.name == '%s') % (room)
	db.session.delete(rooms)
	db.session.flush()
	return "The room %s has been removed frome the database." % (room)

@app.route('/truhome/admin', methods=['GET'])
def admin():
	"""
	"""
	return render_template('admin.html')

@app.errorhandler(403)
def error403(error):
	response = make_response(render_template('403.html'), 403)
	return response

@app.errorhandler(404)
def error404(error):
	response = make_response(render_template('404.html'), 404)
	return response

@app.errorhandler(500)
@app.errorhandler(502)
@app.errorhandler(503)
@app.errorhandler(504)
def error50x(error):
	response = make_response(render_template('maintenance.html'), error.code)
	return response

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8084, debug=True)

