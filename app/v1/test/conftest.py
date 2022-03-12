import os
os.environ['RUN_ENV'] = 'test'

from app.v1.model import client_model,cuenta_model,movimiento_detalle_model,movimiento_model
from app.v1.utils.settings import Settings

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

settings = Settings()

def postgresql_connection():
    dbname =settings.db_name
    user= settings.db_user
    password = settings.db_pass
    strconfig = f"dbname='{dbname}' user='{user}' password='{password}'"
    print(strconfig)

    con = psycopg2.connect(dbname="test_bd_challenge", user="root", password="root")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return con

def delete_database():

    if not settings.db_name.startswith("test_"):
        raise Exception(f'Invalid name for database = {settings.db_name}')

    sql_drop_db = f"DROP DATABASE IF EXISTS {settings.db_name}"
    con = postgresql_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE  pg_stat_activity.datname = '{settings.db_name}' AND pid <> pg_backend_pid();")
    cursor.execute(sql_drop_db)
    con.close()

def create_database():
    pass
    sql_create_db = f"CREATE DATABASE {settings.db_name} WITH OWNER = root ENCODING = 'UTF8' CONNECTION LIMIT = -1;"

    con = postgresql_connection()
    cursor = con.cursor()
    # cursor.execute(sql_create_db)
    con.close()

def pytest_sessionstart(session):

    delete_database()
    create_database()

    from app.v1.utils.db import db

    with db:
        db.create_tables([client_model.Client, cuenta_model.Cuenta, movimiento_detalle_model.MovimientoDetalle, movimiento_model.Movimiento])


def pytest_sessionfinish(session, exitstatus):
    delete_database()
    pass