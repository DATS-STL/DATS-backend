'''
Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''
from flask import jsonify
from .. import app, postgres
from ..parse_request import parse_request
from flask_cors import cross_origin

# Route to create tools in the tool table
@app.route('/tools', methods=["POST"])
@cross_origin()
def post_tools():
    user_id, type, name, description, brand = parse_request("user_id", "type", "name", "description", "brand")
    cursor = postgres.cursor()
    cursor.execute('INSERT INTO "tool" ("user_id", "type", "name", "description", "brand") VALUES (%s, %s, %s, %s, %s) RETURNING tool_id' , [user_id, type, name, description, brand])
    postgres.commit()
    toolid = cursor.fetchone()[0]
    return jsonify({"tool_id": toolid})

# Route to get tool
@app.route('/tools')
@cross_origin()
def get_all_tools():
    cursor = postgres.cursor()
    cursor.execute('SELECT tool_id, user_id, type, name, description, brand FROM "tool"')
    jaysonresults=[]
    for tool_id, user_id, type, name, description, brand in cursor.fetchall():
        row = {
            "tool_id": tool_id,
            "user_id": user_id,
            "type": type,
            "name": name,
            "description": description,
            "brand": brand
        }
        jaysonresults.append(row)
    return jsonify(jaysonresults)


# Route to update tool table

@app.route('/tools', methods= ["PUT"])
@cross_origin()
def put_tools():
    user_id, type, name, description, brand = parse_request("user_id", "type", "name", "description", "brand")
    cursor = postgres.cursor()
    cursor.execute('UPDATE "tool" SET ("user_id", "type", "name", "description", "brand") = (%s, %s, %s, %s, %s)' , [user_id, type, name, description, brand])
    postgres.commit()
    
    return jsonify({"authorization": None})


# Route to delete information in tool table

@app.route('/tools/<tool_id>', methods= ["DELETE"])
@cross_origin()
def delete_tools(tool_id):
    cursor = postgres.cursor()
    cursor.execute('DELETE FROM "tool" WHERE ("tool_id") = (%s)' , [tool_id])
    postgres.commit()
    
    return jsonify({"authorization": None})


# Route to return one tool with tool_id

@app.route('/tools/<tool_id>')
@cross_origin()
def get_one_tool(tool_id):
    cursor = postgres.cursor()
    cursor.execute('SELECT tool_id, user_id, type, name, description, brand FROM "tool" WHERE ("tool_id") = (%s)', [tool_id])
    tool_id, user_id, type, name, description, brand = cursor.fetchone()
    row = {
        "tool_id": tool_id,
        "user_id": user_id,
        "type": type,
        "name": name,
        "description": description,
        "brand": brand
    }
    return jsonify(row)
