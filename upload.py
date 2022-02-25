import psycopg2
from . import settings

def create_table():
    conn = psycopg2.connect(dbname="algomost", user=settings.DB_USER, password=settings.DB_PASS)
    cur = conn.cursor()
    sql = open('./create.sql').read()

    cur.execute(sql)
    conn.commit()
