'''
Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''
from flask import jsonify
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

# a simple page that says Welcome Dan
@app.route('/welcome_dan')
def welcome_dan():
  return 'Welcome Dan'

@app.route('/tt')
def inventory_table():
	cursor = postgres.cursor()
	cursor.execute("SELECT id, name, description FROM tool_inventory WHERE id = 4")
	id, name, description = cursor.fetchone()
	return f'The id is {id}. The name is {name}. The description is {description}'

	

@app.route("/sample")
def get_sample():
	idno4=4
	fancyname="Action Dan"
	result = {
		"id": idno4,
		"name": fancyname
	}

	return jsonify(result)


@app.route('/jayson')
def jayson():
	cursor = postgres.cursor()
	cursor.execute("SELECT id, name, description FROM tool_inventory WHERE id = 2")
	id, name, description = cursor.fetchone()
	jaysonresult = {
		"id": id,
		"name": name,
		"description": description
	}
	return jsonify(jaysonresult)


@app.route("/fetch_all_rows")
def fetch_all_rows():
	cursor = postgres.cursor()
	cursor.execute("SELECT id, name, description FROM tool_inventory")

	jaysonresults=[]
	for id, name, description in cursor.fetchall():
		print(description)
		row = {
			"id": id,
			"name": name,
			"description": description
		}
		jaysonresults.append(row)
	return jsonify(jaysonresults)


@app.route("/twotables")
def twotables():
	cursor = postgres.cursor()
	cursor.execute("SELECT id, name, description FROM tool_inventory JOIN owner ON tool_inventory.id = owner.owner_id")

	jaysonresults=[]
	for id, name, description in cursor.fetchall():
		row = {
			"id": id,
			"name": name,
			"description": description
		}
		jaysonresults.append(row)
	return jsonify(jaysonresults)


#@app.route("/customer/history/year/<year>", methods=["GET"])

@app.route("/tool_search/<description>/<type>")
def tool_search(description, type):
	# tool_search_sql = "SELECT id, name, description FROM tool_inventory JOIN owner ON tool_inventory.id = owner.owner_id WHERE description = '" + description +"'"
	# tool_search_sql = f"SELECT id, name, description FROM tool_inventory JOIN owner ON tool_inventory.id = owner.owner_id WHERE description = '{ description }'"
	tool_search_sql = "SELECT id, name, description, type" +
	" FROM tool_inventory" +
	" JOIN owner ON tool_inventory.id = owner.owner_id" +
	" WHERE description = %s and type = %s"
	cursor = postgres.cursor()
	cursor.execute(tool_search_sql, [description, type])
	jaysonresults=[]
	for id, name, description, type in cursor.fetchall():
		row = {
			"id": id,
			"name": name,
			"description": description,
			"type": type
		}
		jaysonresults.append(row)
	return jsonify(jaysonresults)

#Playing around with previous route

@app.route("/tool_search1/<description>/<type>")
def tool_search1(type):
	tool_search_sql = "SELECT id, name, description, type FROM tool_inventory JOIN owner ON tool_inventory.id = owner.owner_id WHERE type = %s"
	cursor = postgres.cursor()
	cursor.execute(tool_search_sql, [type])
	jaysonresults=[]
	for id, name, description, type in cursor.fetchall():
		print(description)
		row = {
			"id": id,
			"name": name,
			"description": description,
			"type": type
		}
		jaysonresults.append(row)
	return jsonify(jaysonresults)