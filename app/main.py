import socket  # noqa: F401


def create_message(id):
    id_bytes=id.to_bytes(4,byteorder="big")
    # Message length is 8 bytes (4 bytes for the message length itself, 4 bytes for correlation ID)
    message_length = (len(id_bytes) + 4).to_bytes(4, byteorder="big")
    
    # Return the full message (message length + correlation ID)
    return message_length + id_bytes

def handle_client(client):
    client.recv(1024)
    client.sendall(create_message(7))
    client.close()

def main():
    server = socket.create_server(("localhost", 9092))  # Removed reuse_port=True for simplicity
    server.listen(1)  #Ensure the server is listening for connections
    
    while True:
        client, addr = server.accept()  # Accept connection
        handle_client(client)  # Handle the connected client

if __name__ == "__main__":
    main()
