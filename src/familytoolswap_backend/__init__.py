'''
familytoolswap_backend: Main module

Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle
Licensed under GPLv3.0.
'''
from flask import Flask
from . import routes

app = Flask(__name__)

routes.setup(app)
