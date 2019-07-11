{
	"name": "Sensor Management",
	"version": "1.0", 
	"depends": [
		"base",
		"board"
	],
	"author": "Akhmad D. Sembiring [vitraining.com]",
	"category": "Accounting",
	'website': 'http://www.vitraining.com',
	'images': ['static/description/images/main_screenshot.jpg'],
	'price': '10',
	'license': 'OPL-1',
	'currency': 'USD',
	'summary': 'This is the summary',
	"description": """\

Manage
======================================================================

* this is my academic information system module
* created menu:
* created object
* created views
* logic:

""",
	"data": [
		"security/groups.xml",
		"security/ir.model.access.csv",
		"top_menu.xml",
		"view/sensor.xml",
		"view/reading.xml",
		# "view/humidity.xml",
		# "view/temperature.xml",
		# "view/vibration.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}