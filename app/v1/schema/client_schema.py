from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class ClientModel(BaseModel):
    id: int = Field(
        ...,
        example=3
    ),
    email: EmailStr = Field(
        ...,
        example="myemail@devs.com"
    )
    nombre: str = Field(
        ...,
        min_length=5,
        max_length=50,
        example="Mari@ Perez"
    )