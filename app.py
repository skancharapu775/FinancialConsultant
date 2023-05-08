#boilerplate for testing
from flask import Flask, request, send_file
from flask_cors import CORS
import json
from consultant import *

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


# flask function that SENDS data to the client
@app.route('/members')
def members ():
    return {"members": ["Member1", "Member2", "Member3"]}


# chat requests
@app.route('/consultant', methods=['GET', 'POST'])
def consultant ():

    if request.method == "POST":
        return ('', 204)
      
    if request.method == "GET":
        return


@app.route('/pdf', methods=['GET'])
def pdf():

    if request.method == 'GET':
        with open('Financial_Plan.pdf', 'rb') as static_file:
            # Generate plan for finances (Generate pdf report)
            return send_file('Financial_Plan.pdf')
    
    
if __name__ == '__main__':
    app.run(debug=True)