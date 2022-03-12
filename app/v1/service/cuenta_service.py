
from fastapi import HTTPException, status

from app.v1.model.cuenta_model import Cuenta as CuentaModel

from app.v1.schema import cuenta_schema

def get_cuenta(cuenta_id: int):
    cuenta = CuentaModel.filter(CuentaModel.id == cuenta_id).first()
    if not cuenta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cuenta no existe"
        )
    
    cuenta.saldo_convertido = cuenta.get_total_usd()
    print(cuenta)
    return cuenta_schema.CuentaModel(
        id = cuenta.id,
        cliente = cuenta.cliente.id,
        saldo_disponible = cuenta.saldo_disponible,
        saldo_convertido = cuenta.saldo_convertido
    )
