
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address  # nested model

address_dict = {'city': 'maihar', 'state': 'madhya pradesh', 'pin': '485771'}

address1 = Address(**address_dict)

patient_dict = {'name': 'sandeep', 'gender': 'male', 'age': 21, 'address': address1}

patient1 = Patient(**patient_dict)

# temp = patient1.model_dump()    # pura output dictionay me dedega
temp = patient1.model_dump(include=['name', 'gender'])  # similarly for exclude also
# temp = patient1.model_dump_json()       # for json 

print(temp)
print(type(temp))