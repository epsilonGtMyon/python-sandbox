from contextlib import closing
from sqlite_connection import get_connection

# トランザクションなど

with get_connection() as con:
    with closing(con.cursor()) as cursor:

        try:
            # query1
            param1 = {
                "emp_id": 7,
                "family_name": "織田",
                "first_name": "信長",
                "biko": None,
            }
            cursor.execute(
                "insert into EMP(EMP_ID, FAMILY_NAME, FIRST_NAME, BIKO) VALUES(:emp_id, :family_name, :first_name, :biko)",
                param1,
            )

            # query2
            param2 = {
                "emp_id": 8,
                "family_name": "豊臣",
                "first_name": "秀吉",
                "biko": None,
            }
            cursor.execute(
                "insert into EMP(EMP_ID, FAMILY_NAME, FIRST_NAME, BIKO) VALUES(:emp_id, :family_name, :first_name, :biko)",
                param2,
            )

            # query3
            param3 = {
                "emp_id": 5,
                "biko": "更新されたデータ",
            }
            cursor.execute(
                "update EMP set BIKO = :biko where EMP_ID = :emp_id",
                param3,
            )

            con.commit()
        except Exception as e:
            con.rollback()
            raise
