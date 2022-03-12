import peewee
import os
import requests

from app.v1.utils.db import db
from .client_model import Client

class Cuenta(peewee.Model):
    cliente = peewee.ForeignKeyField(Client, backref= 'cuentas')
    saldo_disponible = peewee.CharField(null=False)

    class Meta:
        database = db


    def get_total_usd (self):
        api_url = os.getenv('DOLAR_ENDPOINT')
        response = requests.get(api_url)
        res_json = response.json()
        for item in res_json:
            if (item["casa"]["nombre"]) == "Dolar Bolsa":
                item["casa"]["venta"]=item["casa"]["venta"].replace(',', '.')
                saldo_convertido = float(self.saldo_disponible) / float(item["casa"]["venta"])
                return saldo_convertido
                
        
        return None
        
