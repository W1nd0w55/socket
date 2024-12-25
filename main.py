import socket, accounts, symbols, page

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
            try: client_socket.send(page.load_site(data))
            except TypeError: pass
            try: client_socket.shutdown(socket.SHUT_WR)
            except OSError: pass
    except KeyboardInterrupt: server.close()

if __name__ == '__main__': main()
