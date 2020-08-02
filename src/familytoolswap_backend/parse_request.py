'''
Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''

from flask import request, abort

# Reads in the `request` object from flask, and grabs the requested parameters
# (`params`) from the request. It can accept HTTP form arguments (as in
# "arg1=foo&arg2=bar"), or top-level JSON object arguments.
#
# params: a list of parameter names to grab. The code assumes that all supplied
#         parametes are required.
# returns: a tuple of paramater values, having the same number of elements
#          as `params`.
# aborts with HTTP 415: if request contains neither JSON nor form data.
# aborts with HTTP 400: if a supplied parameter doesn't appear in the request.
def parse_request(*params):
    values = []
    requestArray = None
    if request.json:
        requestArray = request.json
    elif request.form:
        requestArray = request.form
    elif request.args:
        requestArray = request.args
    else:
        print("Request must be sent as a JSON body, query string, or www-form arguments")
        abort(415) # Unsupported Media Type

    for param in params:
        if not param in requestArray:
            print(f"Missing required argument {param}")
            abort(400) # Bad request (missing required argument)
        values.append(requestArray[param])

    if len(values) == 1:
        return values[0]
    else:
        return values
