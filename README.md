# Rental Prediction
The website is deployed to Heroku at: https://rental-pred.herokuapp.com/index.html

In this project, studied the monthly rental payment information and built a machine learning model that predict the risk of renting the tenants.

## Background
Used the dataset that contains monthly rental information like rent amount, payment amount, age, payment date and other information to build the machine learning models. Created a web application for house owners to mimimize their risk factor while renting the property using the monthly rental information dataset.House owners also can click their zipcode to see the average monthly rent rate in that area. 

## Resoruces
* Monthly rental payment information for a set of renters in San Diego, CA.

## Preprocessing: 
### Scaling the data
Used `StandardScaler` to scale the training and testing sets. 
### Converting categorical data to numeric
* Used `pd.get_dummies()` to convert the House Zipcode  data to numeric. 
* Used scikit-learn label encoder to for target vector

## Model Building
Created different classification models to predict patient’s risk of developing lung cancer. Different models are:
* Logistic Regression
* Stochastic Gradient Descent Classifier
* Decision Tree Classifier
* Random Forest Classifier
* Extremely Random Trees
* AdaBoost Classifier
* Gradient Boosting Classifier

## Tuning hyperparamaters for all model
* Grid Search CV
* Randomized Search CV

## Comparing real and predicted value using sample test set

![Images/landingResize.png](Images/comp1.png)


## Productionization
Used Flask templating to create a website to predict tenant rental risk factor. The saved model is used for the prediction.

To begin tentants monthly rental information need to enter. 
The best model predict a tenant's risk levl (Low, High). 


The website is deployed to Heroku at: https://rental-pred.herokuapp.com/index.html

![Images6.png](Images/hero1.png)
