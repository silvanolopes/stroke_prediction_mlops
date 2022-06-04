"""
Creator: Ivanovitch Silva
Date: 18 April 2022
API testing
"""
from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an instance with a low income
def test_get_inference_stroke():

    person = {
        "gender": 'Female',
        "age": 45.0,
        "hypertension": 0,
        "heart_disease": 0,
        "ever_married": 'Yes',
        "work_type": 'Private',
        "Residence_type": 'Urban',
        "avg_glucose_level": 97.95,
        "bmi": 24.5,
        "smoking_status": 'Unknown',
    }

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "Non-Stroke"

# a unit test that tests the status code and response 
# for an instance with a high income
def test_get_inference_stroke():

    person = {
        "gender": 'Male',
        "age": 74.0,
        "hypertension": 1,
        "heart_disease": 1,
        "ever_married": 'Yes',
        "work_type": 'Private',
        "Residence_type": 'Rural',
        "avg_glucose_level": 70.09,
        "bmi": 27.4,
        "smoking_status": 'never smoked',
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "Stroke"