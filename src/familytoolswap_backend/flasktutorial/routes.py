'''
Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''
from flask import jsonify
from .. import app, postgres
from flask_cors import cross_origin

@app.route('/')
@cross_origin()
def get_root():
	cursor = postgres.cursor()
	cursor.execute("SELECT value FROM messages WHERE name = 'welcome'")
	value, = cursor.fetchone()
	return value

# a simple page that says hello
@app.route('/hello')
@cross_origin()
def hello():
	return 'Hello, World!'

# a simple page that says Welcome Dan
@app.route('/welcome_dan')
@cross_origin()
def welcome_dan():
  return 'Welcome Dan'

@app.route('/tt')
@cross_origin()
def inventory_table():
	cursor = postgres.cursor()
	cursor.execute("SELECT id, name, description FROM tool_inventory WHERE id = 4")
	id, name, description = cursor.fetchone()
	return f'The id is {id}. The name is {name}. The description is {description}'



@app.route("/sample")
@cross_origin()
def get_sample():
	idno4=4
	fancyname="Action Dan"
	result = {
		"id": idno4,
		"name": fancyname
	}

	return jsonify(result)


@app.route('/jayson')
@cross_origin()
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
@cross_origin()
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
@cross_origin()
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
@cross_origin()
def tool_search(description, type):
	# tool_search_sql = "SELECT id, name, description FROM tool_inventory JOIN owner ON tool_inventory.id = owner.owner_id WHERE description = '" + description +"'"
	# tool_search_sql = f"SELECT id, name, description FROM tool_inventory JOIN owner ON tool_inventory.id = owner.owner_id WHERE description = '{ description }'"
	tool_search_sql = ("SELECT id, name, description, type" +
		" FROM tool_inventory" +
		" JOIN owner ON tool_inventory.id = owner.owner_id" +
		" WHERE description = %s and type = %s")
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



#attempt at 
@app.route("/tool_search1, methods=['GET', 'POST']")
@cross_origin()
def tool_search1(type, name):
    if request.method == "POST":
        details = request.form
        type = details['type']
        name = details['name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO id(type, name) VALUES (%s, %s)", (type, name))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')