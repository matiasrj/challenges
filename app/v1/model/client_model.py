import peewee

from app.v1.utils.db import db

class Client(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    nombre = peewee.CharField(unique=True, index=True)

    class Meta:
        database = db