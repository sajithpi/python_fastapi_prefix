from pydantic import BaseModel
class user_data(BaseModel):
    username:str
    email:str
    class config:
        orm_mode = True