import peewee
from app.v1.model.movimiento_model import Movimiento

from app.v1.utils.db import db
from app.v1.model.cuenta_model import Cuenta as CuentaModel

class MovimientoDetalle(peewee.Model):
    movimiento = peewee.ForeignKeyField(Movimiento, backref= 'movimientos_detalles')
    tipo = peewee.BooleanField()
    importe = peewee.FloatField(null=False)

    class Meta:
        database = db



    def get_total (self):
        client =self.movimiento.cliente 
        cuenta = CuentaModel.filter(CuentaModel.cliente == client.id).first()
        # if self.tipo :
        #     importe_total = float(cuenta.saldo_disponible) + self.importe
        # else:
        #     importe_total = float(cuenta.saldo_disponible) - self.importe
        return cuenta.saldo_disponible
        
