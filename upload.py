import psycopg2
import settings
import os
import uuid

conn = psycopg2.connect(dbname=settings.DB_NAME, user=settings.DB_USER, password=settings.DB_PASS, host=settings.DB_HOST, port=settings.DB_PORT)
cur = conn.cursor()

def create_table():
    
    sql = """
        CREATE TABLE IF NOT EXISTS file_store (
            id SERIAL PRIMARY KEY,
            file_name VARCHAR(255) NOT NULL,
            file_data BYTEA
        );
    """

    cur.execute(sql)
    conn.commit()


def upload(file_path=None):
    file_path = os.path.abspath('./tmp' if file_path is None else file_path)
    
    file_name = os.path.basename(file_path)
    tmp_file_name = str(uuid.uuid4()) + file_name

    data_sql = """
        SHOW data_directory;
    """

    cur.execute(data_sql)
    data_directory = cur.fetchone()[0]

    tmp_file_path = os.path.join(data_directory, tmp_file_name)

    tmp = open(tmp_file_path, 'wb')
    f = open(file_path, 'rb')
    tmp.write(f.read())
    f.close()
    tmp.close()

    sql = """
        INSERT INTO file_store (file_name) VALUES (%s) RETURNING id;
    """

    cur.execute(sql, (file_name,))
    file_id = cur.fetchone()[0]

    upload_sql = """
        UPDATE file_store SET file_data = pg_read_binary_file(%s)::bytea WHERE id = %s;
    """

    cur.execute(upload_sql, (tmp_file_name, file_id))
    conn.commit()

    os.remove(os.path.join(data_directory, tmp_file_name))

if __name__ == '__main__':
    create_table()
    upload()