#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This web application is designed to run on a Raspberry Pi.
# GPIOs are used to operate module relays then lights and stuff.
# Ver 2.0
# License GNU GPLv3 <https://www.gnu.org/licenses/gpl.html>
####
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()

