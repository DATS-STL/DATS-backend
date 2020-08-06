'''
familytoolswap_backend: Main module

Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle
Licensed under GPLv3.0.
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Valid values of APP_ENVIRONMENT are as follows
# - "production_cloud" when hosted at https://familytoolswap-api.herokuapp.com
# - "development_cloud" when hosted at https://familytoolswap-devapi.herokuapp.com
# - "local" or unset when hosted at http://localhost:8000

if "APP_ENVIRONMENT" in os.environ:
	app_environment = os.environ["APP_ENVIRONMENT"]
	postgres = psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")
	app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
else:
	app_environment = "local"

	from .environment import (
			POSTGRES_HOST, POSTGRES_DATABASE,
			POSTGRES_USER, POSTGRES_PASSWORD)
	database_url = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DATABASE}"

	postgres = psycopg2.connect(database_url)
	app.config["SQLALCHEMY_DATABASE_URI"] = database_url

sa = SQLAlchemy(app)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

# List all files containing @app.route() annotated functions
from .flasktutorial import routes
from .user import routes

