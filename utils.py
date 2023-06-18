import sqlite3
import string
import random


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits

    result = ''
    # breakpoint()
    for _ in range(length):
        result += random.choice(chars)

    return result


def commit_sql(sql):
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    cur.execute(sql)

    con.commit()

    con.close()
