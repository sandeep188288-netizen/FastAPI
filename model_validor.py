#  model validator -> operates on whole pydantic model

from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str 
    age: int
    email: EmailStr
    weight: float 
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):     # model-> all fields of the model
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 years and must have an emergency contact")
        return model
        
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated into database")

patient_info = {'name': 'sandeep', 'age': 65, 'email': 'sandeep@hdfc.com', 'weight': 65.5, 'married': False, 'allergies': ['dust', 'smoke'], 'contact_details': {'phone': '1234567890', 'emergency': '9876543210'}}

patient1 = Patient(**patient_info)  # validation -> type coercion

update_patient_data(patient1)