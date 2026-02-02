from datetime import datetime
# Note: the module name is psycopg, not psycopg3
import psycopg

from db_util import get_connection, initialize_table

def main():
    # Connect to an existing database
    with get_connection() as conn:
        initialize_table(conn)
        
        # Open a cursor to perform database operations
        # マップ型で取得する。
        with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
            
            #--------------------------------------
            # こっちはロールバック

            # insert
            cur.execute(
                "INSERT INTO test_table (name, created_at) VALUES (%(name)s , %(created_at)s )",
                {"name": "helloA", "created_at": datetime.now()})

            conn.rollback()

            #--------------------------------------
            # こっちはコミット
            
            # insert
            cur.execute(
                "INSERT INTO test_table (name, created_at) VALUES (%(name)s , %(created_at)s )",
                {"name": "helloB", "created_at": datetime.now()})
            
            conn.commit()


if __name__ == "__main__":
    main()

