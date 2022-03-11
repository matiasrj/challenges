from app.v1.model.client_model import Client
from app.v1.model.cuenta_model import Cuenta
from app.v1.model.movimiento import Movimiento
from app.v1.model.movimiento_detalle import MovimientoDetalle

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([Client, Cuenta, Movimiento, MovimientoDetalle])