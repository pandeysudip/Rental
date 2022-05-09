import joblib
import numpy as np


# defing model to predict based on our saved model

def loading_model(variables):
    if variables[0] == '' or variables[1] == '' or variables[2] == '':
        return "Please enter the above information first and click submit. "
    else:
        # using standardscaler for transformation
        scaler = joblib.load('scaler.pkl')
        if not 'StandardScaler()':
            return 'Standarderror'
        test_data = scaler.transform([variables])
        if not test_data[0][0]:
            return 'test_data error'
        trained_model = joblib.load('model.pkl')
        prediction = trained_model.predict(test_data)
        if not prediction:
            return 'Prediction Error'

        if prediction == 1:
            return "Based on your above input- 'Tenant is good renter!!!!!!' "
        else:
            return "Based on your above input: 'Tenant is high risk for renting your property!!!!!'"

