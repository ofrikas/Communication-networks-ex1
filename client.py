import socket
# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send data
s.sendto(b'Ofri Kastenbaum and Oran Zafrani', ('127.0.0.1', 12345))
# Receive response
data, addr = s.recvfrom(1024)
print(str(data), addr)
s.close()