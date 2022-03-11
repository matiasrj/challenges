import peewee

from app.v1.utils.db import db

class Client(peewee.Model):
    email = peewee.CharField(unique=True)
    nombre = peewee.CharField(unique=True)

    class Meta:
        database = db