'''
Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''

def setup(app):
	# a simple page that says hello
	@app.route('/hello')
	def hello():
			return 'Hello, World!'
