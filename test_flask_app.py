import pytest
from hello import app

@pytest.fixture # setup for testing and teardown after testing completed
def client():
    return app.test_client()

''' fixture --> This is a special decorator in pytest that tells the testing framework that the function below 
it is a fixture. A fixture is a way to create a setup for your tests and teardown after testing.
'''
# fixture is kind of pre-requesties needed to run in application like open brwoser and login as setup. 
# then reset to original state to continure testing. as every testing to be done from home page
'''
Setup: Open the browser and log in to the application.
Test: Perform various test actions, such as navigating to different pages, filling out forms, etc.
Teardown: Log out and close the browser to reset the environment.
'''

'''test_client(): This test_client simulates a web client without need to run app in server, 
allowing you to send HTTP requests to your application and receive responses without needing to run the server.'''
import numpy as np
def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200, 'the status code is not 200'
    assert response.json == {'message': 'Pinging model application'}, "wrong message"

def test_predict(client):
    test_data={'gender':"Male", 'married':"Unmarried",'credit_history' : "Unclear Debts",
               'applicant_income':100000,'loan_amount':2000000}
    response = client.post('/pred', json=test_data)
    assert response.status_code == 200, 'the status code is not 200'
    assert response.json == {'loan_approval_status': "rejected"}, "The message was not as expected"

def test_dynamic_pred(client):
    for _ in range(100):
        gender = np.random.choice(["Male", "Female"])
        married =  np.random.choice(['Married', "Unmarried"])
        applicant_income = np.random.randint(1, int(1e5))
        loan_amount = np.random.randint(1, 100000)
        credit_history = np.random.choice(["Unclear debits", "Cleared debits", "No debits"])
        test_data = {'gender': gender, 'married': married ,'credit_history' :credit_history,
               'applicant_income':applicant_income,'loan_amount':loan_amount}
        response = client.post('/pred', json=test_data)
        assert response.status_code == 200, 'the status code is not 200'
        assert 'loan_approval_status' in response.json, "The message was not as expected"