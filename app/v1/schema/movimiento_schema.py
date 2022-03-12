from datetime import datetime
from xmlrpc.client import Boolean
from pydantic import BaseModel
from pydantic import Field

date = datetime.now()

class MovimientoDetailModel(BaseModel):
    id: int = Field(
        ...,
        example=4
    ),
    movimiento: int = Field(
        ...,
        example=2
    ),
    tipo: Boolean = Field(
        ...,
        example=True
    ),
    importe: float = Field(
        ...,
        example=123.32
    )
    importe_total: float = Field( 
        None,  
        example=123.32
    )