import psycopg2
import settings

def create_table():
    conn = psycopg2.connect(dbname="algomost", user=settings.DB_USER, password=settings.DB_PASS, host=settings.DB_HOST, port=settings.DB_PORT)
    cur = conn.cursor()
    sql = open('./create.sql').read()

    cur.execute(sql)
    conn.commit()


if __name__ == '__main__':
    create_table()