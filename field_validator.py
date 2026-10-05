# field validator -> always a classmethod and operate on a single field, can be used for validation and transformation of a field

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str 
    age: int
    email: EmailStr
    weight: float 
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gamil.com
        
        domain_name = value.split('@')[-1]  # gmail.com
        if domain_name not in valid_domains:
            raise ValueError("Invalid email domain")

        return value
    
    # for transformation
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    # mode = before => give values before type coercion, mode = after => give values after type coercion
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Invalid age, should be between 0 and 100")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated into database")

patient_info = {'name': 'sandeep', 'age': 21, 'email': 'sandeep@hdfc.com', 'weight': 65.5, 'married': False, 'allergies': ['dust', 'smoke'], 'contact_details': {'phone': '1234567890'}}

patient1 = Patient(**patient_info)  # validation -> type coercion

update_patient_data(patient1)