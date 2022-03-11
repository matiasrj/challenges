
from fastapi import HTTPException, status

from app.v1.model.client_model import Client as ClientModel
from app.v1.model.cuenta_model import Cuenta as CuentaModel

from app.v1.schema import client_schema


def create_client(client: client_schema.ClientModel):


    get_client = ClientModel.filter((ClientModel.email == client.email) | (ClientModel.nombre == client.nombre)).first()
    if get_client:
        msg = "Email ya registrado."
        if get_client.nombre == client.nombre:
            msg = "nombre de usuario ya registrado."
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_client = ClientModel(
        nombre=client.nombre,
        email=client.email,
    )

    db_client.save()

    return client_schema.ClientModel(
        id = db_client.id,
        nombre = db_client.nombre,
        email = db_client.email
    )

def put_client(client_id, client : client_schema.ClientModel):
        client_old = ClientModel.filter(ClientModel.id == client_id).first()

        if not client_old:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente no existe"
            )

        #Debe ser posible optimizar.
        client_old.nombre= client.nombre
        client_old.email = client.email
        client_old.save()
        return client_schema.ClientModel(
            id = client_old.id,
            nombre = client_old.nombre,
            email = client_old.email,
        )

def list_client():
    clients = ClientModel.select()
    print (clients.sql())
    list_clients = []
    for client in clients:
        list_clients.append(
            client_schema.ClientModel(
                id = client.id,
                nombre = client.nombre,
                email = client.email
            )
        )

    return ({"status_code":status.HTTP_200_OK,
            'clients' : list_clients})

def get_client(client_id: int):
    client = ClientModel.filter(ClientModel.id == client_id).first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no existe"
        )

    return client_schema.ClientModel(
        id = client.id,
        nombre = client.nombre,
        email = client.email,
    )

def delete_client(client_id: int):
    client = ClientModel.filter(ClientModel.id == client_id).first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no existe"
        )

    client.delete_instance()

    return ({"status_code":status.HTTP_200_OK,
    "msg": 'Cliente borrado con exito'})


def get_cuenta(client_id: int):
    cuenta = CuentaModel.filter(CuentaModel.cliente_id == client_id).first()

    if not cuenta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cuenta no existe para el cliente"
        )

    return ({"status_code":status.HTTP_200_OK,
            "saldo" : cuenta.saldo_disponible})
