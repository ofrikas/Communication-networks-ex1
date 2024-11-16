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

    try:
        while True:
            client_data, client_address = server_socket.recvfrom(1024)
            print(f"Connection from {client_address}")
            domain = client_data.decode().strip()
            
            isDomainFound = False
            # Check if the domain is in the list of domains
            for line in lines:
                lineInfo = line.split(',')
                if domain.lower() == lineInfo[0]:
                    isDomainFound = True
                    server_socket.sendto(line.encode(), client_address)
                    break
                
            if not isDomainFound:
                # Check if the domain's suffix is in the list of domains
                for line in lines:
                    lineInfo = line.split(',')
                    if domain.lower().endswith(lineInfo[0])  and lineInfo[2].strip() == "NS":
                        isDomainFound = True
                        server_socket.sendto(line.encode(), client_address)
                        break
                
            if not isDomainFound:
                server_socket.sendto("non-existent domain".encode(), client_address)
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()