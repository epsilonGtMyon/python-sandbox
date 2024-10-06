

import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_connection():
  con = sqlite3.connect("./db/sandbox.db", autocommit=False) 
  # sqlite3で結果を辞書にマッピングしたい
  con.row_factory = dict_factory
  return con