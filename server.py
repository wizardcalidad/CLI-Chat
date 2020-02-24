import socket

def server_program():
    #get the host name
    host = '0.0.0.0'   #socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    #configure how many ckients
    server_socket.listen(2)
    conn, address = server_socket.accept()#accept new connection
    print("Connection from: " + str(address))
    while True:
        #receive data streams,
        data = conn.recv(1024).decode()
        if not data:
            #if data is not received
            break
        print("from connected user: "+ str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()

server_program()