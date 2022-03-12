from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from pathlib import Path

from app.v1.schema import movimiento_schema
from app.v1.service import movimiento_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/movimiento")



@router.post(
    "/",
    tags=["movimientos"],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_db)],
    summary="Create a new transfer"
)
def create_movimiento(client_id: int, movimiento: movimiento_schema.MovimientoDetailModel = Body(...) ):
    """
    ## Create a new movimiento in the app

    ### Args
    The app can recive next fields into a JSON
    - movimiento: Unique movimiento
    - tipo: tipo
    - importe: importe
    ### Returns
    - Movimiento: Movimiento info
    """
    

    return movimiento_service.create_movimiento(client_id,movimiento)

@router.get(
    "/",
    tags=["movimientos"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="List of  movimientos"
)
def list_movimientos(client_id:int):
    """
    ## return list of movimientos in the app

    ### Args
    The app can recive next fields into a JSON
    ### Returns
    - movimientos: Movimientos info
    """
    return movimiento_service.list_movimientos(client_id)

@router.get(
    "/{mov_id}",
    tags=["movimientos"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Detail of movimientos"
)
def get_movimiento(client_id:int, mov_id:int):
    """
    ## return detail of mov in the app

    ### Args
    The app can recive next fields into a JSON
    ### Returns
    - movimiento: Movimiento info
    """
    return movimiento_service.get_movimiento(client_id, mov_id)
