from flask import Flask
import pickle

# instance of flask and holds name of module
app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def ping():
    return {'message': 'Pinging model application'}

@app.route('/ratio', methods = ['GET'])
def ratio():
    return {'message': 'hello world'}


# run above code in terminal and use this code to run flask --app hello.py run
# open this link http://127.0.0.1:5000 available in terminal 
# in browser url needs to modified at end with /ping --> http://127.0.0.1:5000/ping -> to make run ping function