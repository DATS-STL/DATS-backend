'''
Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''

from . import app, postgres

@app.route('/')
def get_root():
	cursor = postgres.cursor()
	cursor.execute("SELECT value FROM messages WHERE name = 'welcome'")
	value, = cursor.fetchone()
	return value

# a simple page that says hello
@app.route('/hello')
def hello():
	return 'Hello, World!'
