from flask import Flask, render_template, request, redirect

import pandas as pd

import pickle

import numpy as np

app=Flask(__name__)

model = pickle.load(open("LinearRegressionModel.pkl", 'rb'))
car = pd.read_csv("cleaned car.csv")

@app.route('/')
def index():
    # retreving the companies , car, years , fule_type  for getting categories

    companies = sorted(car['company'].unique())
    car_model = sorted(car['name'].unique())
    year = sorted(car['year'].unique(),  reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    companies.insert(0, "Select comapny")

    return render_template('index.html', companies=companies, car_models=car_model,
                            years=year, fuel_types=fuel_type)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))
    # print(company, car_model, fuel_type, kms_driven);

    prediction = model.predict(pd.DataFrame([[car_model, company, year,kms_driven,fuel_type]], 
                                            columns=['name','company','year','kms_driven', 'fuel_type'] ))
    
    print(prediction[0])

    return prediction[0]

if __name__=="__main__":
    app.run(debug=True)