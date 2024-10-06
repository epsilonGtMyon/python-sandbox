from contextlib import closing

from sqlite_connection import get_connection

# SELECTの実行

print("1.----------")
with get_connection() as con:
    with closing(con.cursor()) as cursor:
        param1 = {"emp_id": 2}
        # 逐次フェッチ
        emps = cursor.execute(
            """
select
   EMP_ID
  ,FAMILY_NAME
  ,FIRST_NAME
  ,BIKO
  ,FAMILY_NAME || FIRST_NAME as FULL_NAME
from
   EMP
where
   EMP_ID > :emp_id
order by
   EMP_ID desc
                       """,
            param1,
        )

        for emp in emps:
            print(emp)


print("2.----------")
with get_connection() as con:
    with closing(con.cursor()) as cursor:
        param1 = {"emp_id": 2}
        cursor.execute(
            """
select
   EMP_ID
  ,FAMILY_NAME
  ,FIRST_NAME
  ,BIKO
  ,FAMILY_NAME || FIRST_NAME as FULL_NAME
from
   EMP
where
   EMP_ID > :emp_id
order by
   EMP_ID desc
                       """,
            param1,
        )

        # 全件フェッチ
        emps = cursor.fetchall()
        for emp in emps:
            print(emp)


