
from pydantic import BaseModel
from pydantic import Field

class CuentaModel(BaseModel):
    id: int = Field(
        ...,
        example=3
    ),
    cliente: int = Field(
        ...,
        example=3
    ),
    saldo_disponible: float = Field(
        ...,
        example=123.321
    ),
    saldo_convertido: float = Field(
        None,
        example=123.321
    )