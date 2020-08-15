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
    cursor.execute('INSERT INTO "tool" (user_id, type, name, description, brand) VALUES (%s, %s, %s, %s)' , [user_id, type, name, description, brand])
    
    return jsonify({"authorization": None})

# Route to get tool
@app.route('/tools')
@cross_origin()
def tools():
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
    
