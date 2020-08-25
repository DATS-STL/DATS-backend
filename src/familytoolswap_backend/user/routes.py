'''
Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''
from flask import jsonify
from .. import app, postgres
from ..parse_request import parse_request
from flask_cors import cross_origin

@app.route("/users/authorize", methods=["POST"])
@cross_origin()
def user_authorize():
	username, password = parse_request("username", "password")

	# This function is a stub just to demonstrate separate components

	return jsonify({"authorization": None})

#This is the route to get user
@app.route('/users')
@cross_origin()
def users():
	cursor = postgres.cursor()
	cursor.execute('SELECT user_id, username, password FROM "user"')
	jaysonresults=[]
	for user_id, username, password in cursor.fetchall():
		row = {
			"user_id": user_id,
			"username": username,
			"password": password
		}
		jaysonresults.append(row)
	return jsonify(jaysonresults)

#Creating users
@app.route("/users", methods=["POST"])
@cross_origin()
def user_add():
	username, password = parse_request("username", "password")
	cursor = postgres.cursor()
	cursor.execute('INSERT INTO "user" (username, password) VALUES (%s, %s)', [username, password])

	# This function is a stub just to demonstrate separate components

	return jsonify({"authorization": None})
