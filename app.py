#boilerplate for testing
from flask import Flask, request, send_file
from flask_cors import CORS
import json
from consultant import generate_fresponse
from report import generate_pdf

app = Flask(__name__)
CORS(app)
#api = Api(app)


# # flask function that SENDS data to the client
# @app.route('/members')
# def members ():
#     return {"members": ["Member1", "Member2", "Member3"]}


# chat requests
@app.route('/consultant', methods=['GET', 'POST'])
def consultant ():
    if request.method == "POST":
        input = request.json['input']
        print(input)

        response = generate_fresponse(input)
        generate_pdf(response)

        return (response)
      
    if request.method == "GET":
        return(response)


@app.route('/pdf', methods=['GET'])
def pdf():

    if request.method == 'GET':
        with open('Financial_Plan.pdf', 'rb') as static_file:
            # Generate plan for finances (Generate pdf report)
            return send_file('Financial_Plan.pdf')
    
    
if __name__ == '__main__':
    app.run(debug=True)