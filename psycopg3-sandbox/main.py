from datetime import datetime
# Note: the module name is psycopg, not psycopg3
import psycopg

def main():
    # Connect to an existing database
    with psycopg.connect("dbname=test_db user=test_user password=test_user host=localhost port=5432") as conn:
        
        # Open a cursor to perform database operations
        # マップ型で取得する。
        with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:

            # insert
            cur.execute(
                "INSERT INTO test_table (name, created_at) VALUES (%(name)s , %(created_at)s )",
                {"name": "hello", "created_at": datetime.now()})
            
            
            # select
            cur.execute("SELECT id, name, created_at FROM test_table")
            for row in cur:  # 自動でfetchone()相当
                print(f"ID: {row['id']}, Name: {row['name']}, Time: {row['created_at']}")



if __name__ == "__main__":
    main()

