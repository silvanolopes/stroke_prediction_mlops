"""
Creator: Ivanovitch Silva
Date: 26 April. 2022
Script that POSTS to the API using the requests 
module and returns both the result of 
model inference and the status code
"""
import requests
import json
# import pprint

person = {
        "gender": 'Male',
        "age": 67.0,
        "hypertension": 0,
        "heart_disease": 1,
        "ever_married": 'Yes',
        "work_type": 'Private',
        "Residence_type": 'Urban',
        "avg_glucose_level": 228.69,
        "bmi": 36.6,
        "smoking_status": 'formerly smoked',
    }

#url = "https://decision-tree-high-income-app.herokuapp.com"
url = "http://127.0.0.1:8000"
response = requests.post(f"{url}/predict",
                         json=person)

print(f"Request: {url}/predict")
print(f"Person: \n gender: {person['gender']}\n age: {person['age']}\n"\
      f" hypertension: {person['hypertension']}\n heart_disease: {person['heart_disease']}\n"\
      f" ever_married: {person['ever_married']}\n"\
      f" work_type: {person['work_type']}\n"\
      f" Residence_type: {person['Residence_type']}\n"\
      f" avg_glucose_level: {person['avg_glucose_level']}\n"\
      f" bmi: {person['bmi']}\n"\
      f" smoking_status: {person['smoking_status']}\n"\
     )
print(f"Result of model inference: {response.json()}")
print(f"Status code: {response.status_code}")