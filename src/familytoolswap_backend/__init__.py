'''
familytoolswap_backend: Main module

Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle
Licensed under GPLv3.0.
'''
import os
from flask import Flask
import psycopg2

# Valid values of APP_ENVIRONMENT are as follows
# - "production_cloud" when hosted at https://familytoolswap-api.herokuapp.com
# - "development_cloud" when hosted at https://familytoolswap-devapi.herokuapp.com
# - "local" or unset when hosted at http://localhost:8000

if "APP_ENVIRONMENT" in os.environ:
	app_environment = os.environ["APP_ENVIRONMENT"]
	postgres = psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")
else:
	app_environment = "local"

	from .environment import (
			POSTGRES_HOST, POSTGRES_DATABASE,
			POSTGRES_USER, POSTGRES_PASSWORD)
	postgres = psycopg2.connect(
			host = POSTGRES_HOST, database = POSTGRES_DATABASE,
			user = POSTGRES_USER, password = POSTGRES_PASSWORD)


app = Flask(__name__)

from . import routes
