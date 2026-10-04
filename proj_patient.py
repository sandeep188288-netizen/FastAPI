from fastapi import FastAPI, Path, HTTPException, Query
# path function => used to enhance the readability + client ko padh k samajh me aayega ki ye parameter kya expect krr raha hai.
# HTTPException => used to return error message with status code(eg: 404, 500, etc) to the client.
# Query => query parametre are optional parameters that can be passed in the URL after the ? symbol. They are used to filter or sort the data returned by the API.
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

@app1.get("/patient/{patient_id}")      # let patient_id = P001
def view_patient(patient_id: str = Path(..., description = "ID of the patient in the DB", example='P001')):
# path function => used to enhance the readability + client ko padh k samajh me aayega ki ye parameter kya expect krr raha hai.
# ... => Iska matlab parameter required hai. , description => parameter ka description, example => parameter ka example

    #load all teh patients
    data = load_data()

# agar mera data me patient_id present hoga to uska data return kardo otherwise error message return kardo
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'Patient not found')

@app1.get("/sort")
def sort_patients(sort_by: str = Query(..., description = 'Sort on the basis of height, weight or bmi'), order: str = Query('asc', description = 'sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code = 400, detail = 'Invalid order select between asc and decs')

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = dict(sorted(data.items(), key=lambda x: x[1].get(sort_by, 0), reverse=sort_order))

    return sorted_data

