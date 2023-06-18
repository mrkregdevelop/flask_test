import sqlite3

from flask import Flask, request

from utils import generate_password, commit_sql

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def password():
    length = request.args.get('length', '10')

    if length.isdigit():
        length = int(length)
    else:
        return f'Invalid length value: {length}'

    if length > 100:
        return 'Length should be less than 100'

    return generate_password(length)


@app.route('/email/create')
def email_create():
    email = request.args['email']

    sql = f"""
    INSERT INTO Emails (EmailValue)
    VALUES ('{email}');
    """
    commit_sql(sql)

    return 'email_create'


@app.route('/email/read')
def email_read():
    ordering = request.args.get('ordering')

    con = sqlite3.connect("example.db")
    cur = con.cursor()

    if ordering:
        direction = 'DESC' if ordering.startswith('-') else 'ASC'
        field = ordering.strip('-')

        sql = f"""
            SELECT * FROM Emails ORDER BY {field} {direction};
            """
    else:
        sql = f"""
            SELECT * FROM Emails;
            """

    cur.execute(sql)

    result = cur.fetchall()

    con.close()
    return str(result)


@app.route('/email/update')
def email_update():
    email = request.args['email']
    email_id = request.args['email_id']

    sql = f"""
    UPDATE Emails
    SET EmailValue = '{email}'
    WHERE EmailId = {email_id};
    """
    commit_sql(sql)

    return 'email_update'


@app.route('/email/delete')
def email_delete():
    email_id = request.args['email_id']

    sql = f"""
    DELETE FROM Emails
    WHERE EmailId = {email_id};
    """

    commit_sql(sql)
    return 'email_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


'''
http:// 127.0.0.1 :5000 /hello ?name=John&email=sjjsjd

1. PROTOCOL - http/s, ftp, smtp

2. DOMAIN - 127.0.0.1 localhost

x.x.x.x

[0-255].[0-255].[0-255].[0-255]

3.47.127.43
78.145.24.78
255.255.255.255
0.0.0.0
78.145.24.78.124
78.145.24
256.0.123.56

IPv4

IPv6

3. PORT :5000
https - 443
http - 80

4. PATH /hello/world

5. QUERY PARAMETERS

CRUD
C - Create
R - Read
U - Update
D - Delete

'''

print(1)
print('HOMEWORK')
