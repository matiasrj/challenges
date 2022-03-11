from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from pathlib import Path

from app.v1.schema import client_schema
from app.v1.service import client_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1/client")

@router.post(
    "/",
    tags=["clients"],
    status_code=status.HTTP_201_CREATED,
    response_model=client_schema.ClientModel,
    dependencies=[Depends(get_db)],
    summary="Create a new client"
)
def create_client(user: client_schema.ClientModel = Body(...)):
    """
    ## Create a new client in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    ### Returns
    - client: Client info
    """
    return client_service.create_client(user)

@router.put(
    "/{client_id}",
    tags=["clients"],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_db)],
    summary="Create a new client"
)
def put_client( client_id: int ,client_instance: client_schema.ClientModel = Body(...)):
    """
    ## Create a new client in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    ### Returns
    - client: Client info
    """
    return client_service.put_client(client_id,client_instance)


@router.get(
    "/",
    tags=["clients"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="List of  clients"
)
def list_client():
    """
    ## return list of clients in the app

    ### Args
    The app can recive next fields into a JSON
    ### Returns
    - client: Client info
    """
    return client_service.list_client()


@router.get(
    "/{client_id}",
    tags=["clients"],
    status_code=status.HTTP_200_OK,
    response_model=client_schema.ClientModel,
    dependencies=[Depends(get_db)],
    summary="Detail of client"
)
def get_client ( client_id: int ):
    return client_service.get_client ( client_id )


@router.delete(
    "/{client_id}",
    tags=["clients"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_client(client_id: int):
    return client_service.delete_client(client_id)


@router.get(
    "/{client_id}/saldo",
    tags=["clientes"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Saldo de cuenta"
)
def get_cuenta ( client_id: int ):
    return client_service.get_cuenta ( client_id )

