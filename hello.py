from flask import Flask, request
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

model_pred = open('train_model.pkl', 'rb')
clf =  pickle.load(model_pred)

# create a prediction for model trained for loan prediction 
@app.route('/pred', methods = ['POST'])
def pred():
    loan_req = request.get_json()
    # convert string to number (label encoding)
    if loan_req['gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    if loan_req['credit_history'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1
    ApplicantIncome = loan_req['applicant_income']
    LoanAmount = loan_req['loan_amount']

    prediction = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    if prediction == 0:
        pred = 'rejected'
    else :
        pred = 'approved'
    
    return {'loan_approval_status': pred}

    #input for post request in postman with format for pred endpoint
    '''{
    "gender" : "Male",
    "married" : "Unmarried",
    "credit_history" : "Unclear Debts",
    "applicant_income" : 50000,
    "loan_amount" : 5000
    }
    '''