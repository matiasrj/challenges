import peewee
import datetime
from app.v1.utils.db import db
from .client_model import Client

class Movimiento(peewee.Model):
    fecha = peewee.DateTimeField (default=datetime.datetime.now())
    cliente = peewee.ForeignKeyField(Client, backref= 'movimientos')

    class Meta:
        database = db
