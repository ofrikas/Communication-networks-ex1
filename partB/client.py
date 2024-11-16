import sys
import socket

def main():
    # Check if the user entered the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: client.py [serverIP] [serverPort]")
        return

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    # Create a UDP socket, Af.Intent is the address family, and SOCK_DGRAM is the socket type for UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # Read domain name from user
            domain = input("Enter domain name: ")

            # Send the domain name to the resolver server
            client_socket.sendto(domain.encode(), (server_ip, server_port))

            # Receive the response from the server
            response, _ = client_socket.recvfrom(1024)
        

            # Print the response
            if response.decode() == "non-existent domain":
                print("non-existent domain")
            else:
                print(response.decode().split(',')[1].strip())
        
    # print the response and close the socket
    except KeyboardInterrupt:
        print("\nClient terminated.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()