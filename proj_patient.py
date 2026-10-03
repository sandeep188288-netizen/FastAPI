from fastapi import FastAPI
import json

app1 = FastAPI()     #object

def load_data():        #helper function to load data from patients.json
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app1.get("/")
def hello():
    return {'message': 'Patient Management System API'}


@app1.get("/about")
def about():
    return {'message': 'A fully functional API to manage your patients records'}


@app1.get("/view")
def view_patients():
    data = load_data()

    return data 