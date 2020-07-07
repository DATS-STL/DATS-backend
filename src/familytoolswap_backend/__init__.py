'''
familytoolswap_backend: Main module

Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle
Licensed under GPLv3.0.
'''
from flask import Flask
from . import environment
import psycopg2

app = Flask(__name__)
postgres = psycopg2.connect(
		host=    environment.POSTGRES_HOST,
		user=		 environment.POSTGRES_USER,
		password=environment.POSTGRES_PASSWORD,
		database=environment.POSTGRES_DATABASE)

from . import routes
