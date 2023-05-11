#boilerplate for testing
from flask import Flask, request, send_file
from flask_cors import CORS
import json
from consultant import generate_fresponse
from report import generate_pdf

app = Flask(__name__)
CORS(app)

#api = Api(app)
response = ""


# # flask function that SENDS data to the client
# @app.route('/members')
# def members ():
#     return {"members": ["Member1", "Member2", "Member3"]}


# chat requests
@app.route('/consultant', methods=['GET', 'POST'])
def consultant ():
    global response

    if request.method == "POST":
        # Get user response from json
        input = request.json['input']
        print(input)

        # Generate model response
        response = generate_fresponse(input)
       
        # Create PDF on disk
        generate_pdf(response)

        # Return text response to frontend for display
        return (response)
      
    if request.method == "GET":
        return(response)


@app.route('/pdf', methods=['GET'])
def pdf():

    if request.method == 'GET':
        with open('Financial_Plan.pdf', 'rb') as static_file:
            
            # Show user pdf version of GPT response
            return send_file('Financial_Plan.pdf')
    
if __name__ == '__main__':
    app.run(debug=True)