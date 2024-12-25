import sqlconnect, symbols

def main(user_data):
    # checking the method and running account scripts
    if user_data.split('&')[0] == 'method=sign_up': sign_up(user_data)
    elif user_data.split('&')[0] == 'method=login_name': name_login(user_data)
    elif user_data.split('&')[0] == 'method=login_email': email_login(user_data)

def sign_up(user_data):
    # for signing up
    username = user_data.split('&')[1].replace('username=', '')
    password = str(symbols.sha256_hash(user_data.split('&')[2].replace('password=', '')))
    email = user_data.split('&')[3].replace('email=', '')
    sqlconnect.sign_up(sqlconnect.connection, username, password, email)

def name_login(user_data):
    # for logging in with the username
    username = user_data.split('&')[1].replace('username=', '')
    password = str(symbols.sha256_hash(user_data.split('&')[2].replace('password=', '')))
    sqlconnect.name_login(sqlconnect.connection, username, password)

def email_login(user_data):
    # for logging in with the email
    email = user_data.split('&')[1].replace('email=', '')
    password = str(symbols.sha256_hash(user_data.split('&')[2].replace('password=', '')))
    sqlconnect.email_login(sqlconnect.connection, email, password)
