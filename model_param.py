import joblib
import numpy as np


# defing model to predict based on our saved model

def loading_model(variables):
    if variables[0] == '' or variables[1] == '' or variables[2] == '' or variables[3] == '':
        return "Please enter the above information first and click submit. "
    else:
        Age = variables[0]
        Rent_Amount = variables[1]
        Payment_Amount = variables[2]
        Payment_Date = variables[3]
        final_variables = [Age, Rent_Amount,
                           Payment_Amount, Payment_Date]
        # using standardscaler for transformation
        scaler = joblib.load('scaler.pkl')
        X_scaler = scaler.transform([final_variables])

        test_data = scaler.transform(X_scaler)
        trained_model = joblib.load('model.pkl')
        prediction = trained_model.predict(test_data)
        if prediction == [1]:
            return "Based on your input- 'Tenants is good renter' "
        else:
            return "Based on your input- 'Tenants is high risk'"
