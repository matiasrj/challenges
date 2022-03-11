import black
import peewee
from app.v1.model.movimiento import Movimiento

from app.v1.utils.db import db

class MovimientoDetalle(peewee.Model):
    movimiento = peewee.ForeignKeyField(Movimiento, backref= 'movimientos_detalles')
    tipo = peewee.BooleanField()
    importe = peewee.FloatField(null=False)

    class Meta:
        database = db
