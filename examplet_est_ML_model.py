import numpy as np
import pytest

for i in range(1e2):
    gender = np.random.choice("Male", "Female")
    marrage_status =  np.random.choice('Married', "Unmarried")
    applicant_incoem = np.random.choice(1, 1e6)
    loan_amount = np.random.choice(1, 1e6)
    credit_history = np.random.choice("Unclear debits", "Cleared debits", "No debits")
 

# Get data from above loop and create a dataframe out it
# send those data for prediction for the model which is created
