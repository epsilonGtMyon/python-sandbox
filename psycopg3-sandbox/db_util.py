from datetime import datetime
import psycopg

def get_connection() -> psycopg.Connection:
    """
    コネクションを取得
    """
    return psycopg.connect("dbname=test_db user=test_user password=test_user host=localhost port=5432")



def initialize_table(conn: psycopg.Connection):
    """
    テーブルデータの初期化
    """
    with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
        # delete all records
        cur.execute("DELETE FROM test_table")

        # insert many
        cur.executemany(
            "INSERT INTO test_table (name, created_at) VALUES (%(name)s , %(created_at)s )",
            [
                {"name": "hello1", "created_at": datetime.now()},
                {"name": "hello2", "created_at": datetime.now()},
                {"name": "hello3", "created_at": datetime.now()}
            ])
        conn.commit()
