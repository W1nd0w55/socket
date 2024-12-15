import socket, accounts, symbols

def main():
    try:
        # create socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 80))
        #server.bind(('172.16.0.2', 80))
        server.listen(1000)
        while 1:
            # client-server interactions
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            try: accounts.main(symbols.decode(data.split('\r\n')[20]))
            except IndexError: pass
            response = load_site(data)
            try: client_socket.send(response)
            except TypeError: pass
            try: client_socket.shutdown(socket.SHUT_WR)
            except OSError: pass
    except KeyboardInterrupt: server.close()

def load_site(request_data):
    # define the status codes
    HDRS_OK = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
    try: path = request_data.split(' ')[1]
    except IndexError: pass
    try:
        # show whatever page the client requests
        with open('views'+path, 'rb') as file: response = file.read()
        return HDRS_OK + response
    except UnboundLocalError: pass
    except FileNotFoundError:
        # return 404 page
        with open('views/error/404', 'rb') as err: response = err.read()
        return HDRS_404 + response
    except IsADirectoryError:
        # is there an http error code for 'Is a Directory'?
        with open('views/error/isadirectory', 'rb') as err: response = err.read()
        return HDRS_OK + response

if __name__ == '__main__': main()
