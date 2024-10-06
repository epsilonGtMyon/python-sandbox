from contextlib import closing
from sqlite_connection import get_connection

# DDLの実行や初期データなど

with get_connection() as con:
    with closing(con.cursor()) as cursor:
        # schema
        cursor.execute(
            """
create table EMP(
     EMP_ID   integer
    ,FAMILY_NAME   text
    ,FIRST_NAME    text
    ,BIKO          text
    ,constraint PK_EMP primary key(
       EMP_ID                   
    )       
)
        """
        )

        # data
        cursor.execute(
            "insert into EMP(EMP_ID, FAMILY_NAME, FIRST_NAME) VALUES(1, '田中', '一郎')"
        )
        cursor.execute(
            "insert into EMP(EMP_ID, FAMILY_NAME, FIRST_NAME) VALUES(2, '山本', '二郎')"
        )
        cursor.execute(
            "insert into EMP(EMP_ID, FAMILY_NAME, FIRST_NAME) VALUES(3, '中田', '三郎')"
        )
        cursor.execute(
            "insert into EMP(EMP_ID, FAMILY_NAME, FIRST_NAME) VALUES(4, '佐藤', '孝')"
        )
        cursor.execute(
            "insert into EMP(EMP_ID, FAMILY_NAME, FIRST_NAME) VALUES(5, '伊藤', '浩二')"
        )
        cursor.execute(
            "insert into EMP(EMP_ID, FAMILY_NAME, FIRST_NAME) VALUES(6, '山下', '博司')"
        )

        pass
