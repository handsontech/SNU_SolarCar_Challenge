import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5005

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

print(f"Server listening on {SERVER_PORT}...")

try:
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")
        
        try:
            while True:
                data = client_socket.recv(1024)
                if not data: break
                
                decoded_data = data.decode('utf-8').strip()
                print(f"Received: {decoded_data}")
                
        except Exception as e:
            print(f"Client error: {e}")
        finally:
            client_socket.close()
            print("Connection closed")

except KeyboardInterrupt:
    print("Server stopping")
finally:
    server_socket.close()