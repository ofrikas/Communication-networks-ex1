import sys
import socket
import time

def main():
    if len(sys.argv) != 5:
        print("Usage: resolver.py [myPort] [parentIP] [parentPort] [x]")
        return

    # Parse the command line arguments
    my_port = int(sys.argv[1])
    parent_ip = sys.argv[2]
    parent_port = int(sys.argv[3])
    cache_duration = int(sys.argv[4])

    # Create a UDP socket af_inet is the address family, and sock_dgram is the socket type for UDP
    resolver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    resolver_socket.bind(('', my_port))

    # Cache to store domain responses
    cache = {}

    try:
        while True:
            # Receive a query from a client
            query, client_address = resolver_socket.recvfrom(1024)
            domain = query.decode().strip()

            # Check if the domain or its suffixes are in the cache
            current_time = time.time()
            response = None
            domain_parts = domain.split('.')
            
            for i in range(len(domain_parts)):
                suffix = '.'.join(domain_parts[i:])
                if i != 0:
                    suffix = '.' + suffix
                if suffix in cache and current_time - cache[suffix]['timestamp'] < cache_duration:
                    response = cache[suffix]['response']
                    response_parts = response.decode().split(',')
                    ip_port = response_parts[1].split(':')
                    parent_ip = ip_port[0]
                    parent_port = int(ip_port[1])
                    domain = response_parts[0].strip()
                    break

            if response is None or response.decode().endswith("NS\n") or response.decode().endswith("NS"):
                # Forward the query to the parent server
                resolver_socket.sendto(query, (parent_ip, parent_port))
                response, _ = resolver_socket.recvfrom(1024)
                
                # Handle the case where the response ends with "NS" 
                while response.decode().endswith("NS\n") or response.decode().endswith("NS"):
                    
                    # Extract the IP and port of the new parent server
                    response_parts = response.decode().split(',')
                    ip_port = response_parts[1].split(':')
                    parent_ip = ip_port[0]
                    parent_port = int(ip_port[1])
                    domain = response_parts[0].strip()
                    current_time = time.time()

                    # Cache the response
                    cache[domain] = {
                        'response': response,
                        'timestamp': current_time
                    }
        
                    # Check if the domain or its suffixes are in the cache
                    response = None
                    domain_parts = domain.split('.')
                    
                    for i in range(len(domain_parts)):
                        suffix = '.'.join(domain_parts[i:])
                        if i != 0:
                            suffix = '.' + suffix
                        if suffix in cache and current_time - cache[suffix]['timestamp'] < cache_duration:
                            response = cache[suffix]['response']
                            response_parts = response.decode().split(',')
                            ip_port = response_parts[1].split(':')
                            parent_ip = ip_port[0]
                            parent_port = int(ip_port[1])
                            domain = response_parts[0].strip()
                            break
                    
                    # Forward the query to the new parent server
                    resolver_socket.sendto(query, (parent_ip, parent_port))
                    response, _ = resolver_socket.recvfrom(1024)                    

                # Cache the response
                cache[query.decode()] = {
                    'response': response,
                    'timestamp': current_time
                }

            # Send the response to the client
            resolver_socket.sendto(response, client_address)

    except KeyboardInterrupt:
        print("\nResolver terminated.")
    finally:
        resolver_socket.close()

if __name__ == "__main__":
    main()