import pymysql, postlogin

# create a connection
conn = pymysql.connect (host='172.16.2.3',
                        database='db1',
                        port=3306,
                        user='admin',
                        password='Sql@5325')

def sign_up(conn, username, password_hash, email):
    try:
        with conn.cursor() as cur:
            # pass the data into SQL
            query = 'INSERT INTO accounts(username, password, email, role) VALUES("'+username+'", "'+password_hash+'", "'+email+'", "user");'
            cur.execute(query)
        conn.commit()
    finally: conn.close()

def name_login(conn, username, password_hash):
    try:
        with conn.cursor() as cur:
            # search the DB for an account with that username and password
            query = 'SELECT * FROM accounts WHERE username = "'+username+'" AND password = "'+password_hash+'";'
            cur.execute(query)
            # pass the output to postlogin script
            postlogin.sql_output = cur.fetchone()
            print(postlogin.username(), postlogin.admin())
            # TODO: delete this ^
        conn.commit()
    except pymysql.err.InterfaceError: pass
    finally: cur.close()

def email_login(conn, email, password_hash):
    try:
        with conn.cursor() as cur:
            # search the DB for an account with that email and password
            query = 'SELECT * FROM accounts WHERE email = "'+email+'" AND password = "'+password_hash+'"'
            cur.execute(query)
            # pass the output to postlogin script
            postlogin.sql_output = cur.fetchone()
            print(postlogin.username(), postlogin.admin())
            # TODO: delete this ^
        conn.commit()
    except pymysql.err.InterfaceError: pass
    finally: cur.close()
