
from datetime import datetime
from fastapi import HTTPException, status

from app.v1.model.client_model import Client as ClientModel
from app.v1.model.cuenta_model import Cuenta as CuentaModel
from app.v1.model.movimiento_model import Movimiento as MovimientoModel

from app.v1.schema import movimiento_schema
from app.v1.schema.movimiento_schema import MovimientoDetailModel
from app.v1.model.movimiento_detalle_model import MovimientoDetalle
from app.v1.model.cuenta_model import Cuenta


def create_movimiento(client_id:int , movimiento_detalle: movimiento_schema.MovimientoDetailModel):
    # return ('hola desde router movimiento')

    client_cuenta = CuentaModel.filter( CuentaModel.id == client_id).first()
    if  not client_cuenta :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no posee cuenta asociada"
        )
    
    # Check que egreso menor a saldo disponible . False = Egreso
    if movimiento_detalle.tipo == False:
        if (float(movimiento_detalle.importe) > float(client_cuenta.saldo_disponible)):
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="saldo insuficiente"
        )
        # Egreso
        client_cuenta.saldo_disponible = float(client_cuenta.saldo_disponible) - float(movimiento_detalle.importe)
    else:    
        # ingreso
        client_cuenta.saldo_disponible = float(client_cuenta.saldo_disponible) + float(movimiento_detalle.importe)
    #guardo instancia.
    client_cuenta.save()

    mov_db = MovimientoModel.create(cliente=client_id)
    movimiento_detalle.movimiento = mov_db

    movimiento_detalle_db =MovimientoDetalle.create(tipo = movimiento_detalle.tipo,
                                                    movimiento = movimiento_detalle.movimiento,
                                                    importe = movimiento_detalle.importe
                                                    )
    movimiento_detalle_db.save()

    importe_total = float(movimiento_detalle_db.get_total())
    
    return  movimiento_schema.MovimientoDetailModel(
        id = movimiento_detalle_db.id,
        tipo = movimiento_detalle_db.tipo,
        importe = movimiento_detalle_db.importe ,
        movimiento= movimiento_detalle_db.movimiento.id,
        importe_total=importe_total)

def delete_movimiento(client_id: int, mov_id: int):
    # Busco cliente
    client = ClientModel.filter(ClientModel.id == client_id).first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no existe"
        )

    movimiento = MovimientoModel.filter( MovimientoModel.id == mov_id).first()
    if not movimiento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movimiento no existe"
        )  

    #Consulto movimiento detalle para identificar su importe.
    movimiento_detalle = MovimientoDetalle.filter(MovimientoDetalle.movimiento_id == mov_id).first()
    if not movimiento_detalle:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Movimiento detalle no existe"
        )  

    #Consulto cuenta par aver si tiene saldo suficiente.
    cuenta_cliente = CuentaModel.filter(CuentaModel.cliente_id == client_id ).first()
    if not cuenta_cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cuenta cliente no existe"
        )  

    
    # Realizo Eliminación.
    if movimiento_detalle.tipo:
        # Si fué un ingreso:
        if float(cuenta_cliente.saldo_disponible)  >= float(movimiento_detalle.importe):
            cuenta_cliente.saldo_disponible = float(cuenta_cliente.saldo_disponible) - float(movimiento_detalle.importe)
        # No puedo eliminar el ingreso, quedaría saldo negativo.
        else:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se puede revertir la operacion en este momento. Saldo insuficimente"
            ) 
    else:
        # Fue egreso
            cuenta_cliente.saldo_disponible = float(cuenta_cliente.saldo_disponible) + float(movimiento_detalle.importe)


    movimiento_detalle.delete_instance()
    movimiento.delete_instance()
    cuenta_cliente.save()

    return ({"status_code":status.HTTP_200_OK,
    "msg": 'Movimient eliminado con exito'})


def get_cuenta(client_id: int):
    cuenta = CuentaModel.filter(CuentaModel.cliente_id == client_id).first()

    if not cuenta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cuenta no existe para el cliente"
        )

    return ({"status_code":status.HTTP_200_OK,
            "saldo" : cuenta.saldo_disponible})
   
    
def list_movimientos(client_id:int):
    movimientos = MovimientoModel.filter(MovimientoModel.cliente ==client_id )
    list_movs = []
    for mov in movimientos:
        detalle = MovimientoDetalle.filter(MovimientoDetalle.movimiento == mov.id)
        for det in detalle:
            list_movs.append(   
                det.__data__
            )

    return ({"status_code":status.HTTP_200_OK,
            'clients' : list_movs})

def get_movimiento(client_id:int, mov_id : int):
    movimiento_ob = MovimientoModel.select().where(MovimientoModel.id== mov_id, MovimientoModel.cliente == client_id).first()

    mov_detalle = MovimientoDetalle.select().where(MovimientoDetalle.movimiento == movimiento_ob.id).first()
    if not mov_detalle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="movimiento no disponible"
        )

    resp = movimiento_schema.MovimientoDetailModel(id = mov_detalle.id,
                                                    movimiento =movimiento_ob.id,
                                                    tipo= mov_detalle.tipo,
                                                    importe= mov_detalle.importe,
                                                    )

    # resp='asd'
    return ({"status_code":status.HTTP_200_OK,
            'movimiento' : resp})