import postlogin, js2py

def load_site(request_data):
    # define the status codes
    status_OK = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
    status_400 = 'HTTP/1.1 400 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
    status_401 = 'HTTP/1.1 401 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
    status_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
    status_418 = 'HTTP/1.1 418 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
    try:
        path = request_data.split(' ')[1]
        return messages(status_OK, status_400, status_401, request_data.split('\r\n')[20].split('&'))
    except IndexError: pass
    try:
        # show whatever page the client requests
        with open('views'+path, 'rb') as file: response = file.read()
        return status_OK + response
    except UnboundLocalError: pass
    except FileNotFoundError:
        # return 404 page
        with open('status/error/404.html', 'rb') as err: response = err.read()
        return status_404 + response
    except IsADirectoryError:
    # is there a http error code for 'Is a Directory'?
        with open('status/error/isadirectory.html', 'rb') as err: response = err.read()
        return status_418 + response

def messages(status_OK, status_400, status_401, filtered_data):
    # change page after signup
    if filtered_data[0] == 'method=sign_up':
        if filtered_data[1] == 'username=' or filtered_data[2] == 'password=' or filtered_data[3] == 'email=':
            with open('status/error/signup_400.html', 'rb') as err: response = err.read()
            return status_400 + response
        with open('status/signup_success.html', 'rb') as success: response = success.read()
        return status_OK + response
        # change page after login
    elif filtered_data[0] == 'method=login_name':
        if postlogin.username():
            with open('status/username_success.html', 'rb') as success: response = success.read()
            return status_OK + response
        elif filtered_data[1] == 'username=' or filtered_data[2] == 'password=':
            with open('status/error/username_400.html', 'rb') as err: response = err.read()
            return status_400 + response
        else:
            with open('status/username_failed.html', 'rb') as fail: response = fail.read()
            return status_401 + response
    elif filtered_data[0] == 'method=login_email':
        if postlogin.username():
            with open('status/email_success.html', 'rb') as success: response = success.read()
            return status_OK + response
        elif filtered_data[1] == 'email=' or filtered_data[2] == 'password=':
            with open('status/error/email_400.html', 'rb') as err: response = err.read()
            return status_400 + response
        else:
            with open('status/email_failed.html', 'rb') as fail: response = fail.read()
            return status_401 + response
