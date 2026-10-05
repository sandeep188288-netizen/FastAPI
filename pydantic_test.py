# parameter to kitne bhi ho skte hai ,baar baar likhenge kya ? [this problem is type validation]
'''def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("inserted into database")

    else:
        raise TypeError("Incorrect dataa type")

insert_patient_data("sandeep", 20) 
'''

#---------------------------------------------------------
'''
def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        if age <= 0:
            raise ValueError("Age cannot be zero or negative")
        else:
            print(name)
            print(age)
            print("inserted into database")

    else:
        raise TypeError("Incorrect dataa type")

insert_patient_data("sandeep", 20)
'''

#---------------------------------------------------------

# pydantic library is used to solve the above problems

'''
Pydantic => works in three main steps:

1. Define a Pydantic model that represents the ideal schema of the data.
   • This includes the expected fields, their types, and validation constraints
     (e.g., gt=0 for positive numbers).

2. Instantiate the model with raw input data (usually a dictionary or JSON-like structure).
   • Pydantic will automatically validate the data and coerce it into the correct Python
     types (if possible).
   • If the data doesn't meet the model's requirements, Pydantic raises a ValidationError.

3. Pass the validated model object to functions or use it throughout your codebase.
   • This ensures that every part of your program works with clean, type-safe,
     and logically valid data.
     
'''
# basis use of pydantic we can create a model and validate the data before inserting into database or updating into database
'''
from pydantic import BaseModel 
class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted into database") 

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated into database")

patient_info = {'name': 'sandeep', 'age': 21}

patient1 = Patient(**patient_info)  # unpacking the dictionary into the Patient model

update_patient_data(patient1)  # passing the validated model to the function
'''

# --------------------------------------------------------------------------------


from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='Name of hte patient', description='Give the name of the oatient in less than 50 chars', example=['Sandeep', 'Riju'])]  
    age: int
    email: EmailStr
    Linkedin_url: AnyUrl
    weight: Annotated[float, Field(gt=0, strict=True)]  # gt=0 => greater than 0, strict=True => only float type allowed, not str
    # married: bool
    married: Annotated[bool, Field(default=None, description='Is the patient married or not', example=False)]  
    # allergies: List[str]    # List[str] => allergies khud me ek list ho aur uske andar ke elements str type ke ho
    # allergies: Optional[List[str]] = None # Optional[List[str]] => allergies khud me ek list ho aur uske andar ke elements str type ke ho, agar allergies ka data nahi aaya to default value None ho jaayegi  
    allergies: Optional[List[str]] = Field(max_lenght=5)
    allergies: Annotated[Optional[List[str]], Field(default=None, max_lenght=5)]
    contact_details: Dict[str, str] # Dict[str, str] => contact_details khud me ek dictionary ho aur uske andar ke keys str type ke ho aur values bhi str type ke ho 

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted into database") 

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.Linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated into database")

patient_info = {'name': 'sandeep', 'age': 21, 'email': 'sandeep@gmail.com', 'Linkedin_url': 'http://linkedin.com/1322', 'weight': 65.5, 'married': False, 'contact_details': {'phone': '1234567890'}}

patient1 = Patient(**patient_info)  

update_patient_data(patient1)


