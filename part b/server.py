import socket
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python server.py [myPort] [zoneFileName.txt]")
        sys.exit(1)

    myPort = int(sys.argv[1])
    zoneFileName = sys.argv[2]

    # Read the lines from the text file and store them in a list
    try:
        with open(zoneFileName, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {zoneFileName} not found.")
        sys.exit(1)

    # Create a socket and bind it to the specified port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', myPort))
    print(f"Server listening on port {myPort}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        client_socket.sendall(b"Hello, you are connected to the server.\n")
        domain = client_socket.recv(1024).decode().strip()
        
        isDomainFound = False
        for line in lines:
            lineDomain = line.split(',')[0]
            if domain == lineDomain:
                isDomainFound = True
                client_socket.sendall(line.encode())
                client_socket.close()
                break
            
        if not isDomainFound:
            client_socket.sendall("non-existent domain".encode())       
            client_socket.close()

if __name__ == "__main__":
    main()