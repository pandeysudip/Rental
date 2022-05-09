# Rental Prediction
The website is deployed to Heroku at: https://rental-pred.herokuapp.com/index.html

In this project, studied the monthly rental payment information and built a machine learning model that predict the risk level of tenant's.

## Background
Used the dataset that contains monthly rental information like rent amount, payment amount, age, payment date and other information and build the machine learning models. Created a web application for house owners to mimimize their risk factor while renting the property using the monthly rental information data. House owners also can click their zipcode to see the average monthly rent rate in that area. 

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
* `Logistic Regression`
* `Stochastic Gradient Descent Classifier`
* `Decision Tree Classifier`
* `Random Forest Classifier`
* `Extremely Random Trees`
* `AdaBoost Classifier`
* `Gradient Boosting Classifier`

## Tuning hyperparamaters for all model
* `Grid Search CV`
* `Randomized Search CV`

## Comparision of real and predicted value using sample test set

![Images/landingResize.png](Images/comp1.png)


## Productionization
Different languages and tools were used to build the machichine learning web app.
* `HTML`
* `CSS`
* `Javascript`
* `Bootstrap`
* `Git`
* `Flask`
* `Heroku`
The machine learning model are saved as a pickle file to used for the prediction.
Used `Flask` servers to interact with our `Machine Learning model` and then connect the model with a web application. Deployed the flask machine learning web-app in Heroku Cloud Platform.

 The website has a differnt pages:
* `Home` User can enter the information to predict the tenant's risk factor.
To use the website applicatin tentants monthly rental information need to enter. 
Our model predict a tenant's risk levl (Low, High). 
* `Plots` Differnt plots of the studied data can be found inside this section.
* `Maps ` User can also enter the zipcode to view the average rent in that area with the google maps.
* `Model ` Different models performances metrics 
* `Data` Cleaned data used for the studied in the table format
* `Contact` Contact information


The website is deployed to Heroku at: https://rental-pred.herokuapp.com/index.html

![Images6.png](Images/hero1.png)
