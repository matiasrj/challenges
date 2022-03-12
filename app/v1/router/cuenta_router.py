from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from pathlib import Path

from app.v1.service import cuenta_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1/cuenta")

@router.get(
    "/{cuenta_id}",
    tags=["movimientos"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Detail of movimientos"
)
def get_movimiento(cuenta_id:int):
    """
    ## return detail of cuenta in the app

    ### Args
    The app can recive next fields into a JSON
    ### Returns
    - cuenta: Cuenta info
    """
    return cuenta_service.get_cuenta(cuenta_id)


