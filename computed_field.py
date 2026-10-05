#  model validator -> operates on whole pydantic model

from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str 
    age: int
    email: EmailStr
    weight: float   # kg
    height: float   # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 

    @computed_field
    @property
    def calculated_bmi(self) -> float:
        bmi = self.weight/(self.height**2),2
        return bmi
     
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI', patient.calculated_bmi)
    print("updated into database")

patient_info = {'name': 'sandeep', 'age': 65, 'email': 'sandeep@hdfc.com', 'weight': 65.5, 'height': 1.57, 'married': False, 'allergies': ['dust', 'smoke'], 'contact_details': {'phone': '1234567890', 'emergency': '9876543210'}}

patient1 = Patient(**patient_info)  # validation -> type coercion

update_patient_data(patient1)