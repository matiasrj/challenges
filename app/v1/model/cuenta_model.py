import peewee

from app.v1.utils.db import db
from .client_model import Client

class Cuenta(peewee.Model):
    cliente = peewee.ForeignKeyField(Client, backref= 'cuentas')
    saldo_disponible = peewee.CharField(null=False)

    class Meta:
        database = db