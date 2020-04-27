import socket
import argparse

def argv():
    # Create parser
    arg_parser = argparse.ArgumentParser()
    # Add arguments
    arg_parser.add_argument('-p', '--port', help='Specify port to connect to')
    # Return parsed arguments
    return arg_parser.parse_args()

    
# Create a TCP/IP socket
args = argv()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', int(args.port))
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)
try:

    # Send data
    message = b'E11000000000DA7A0000000501020304050B1E00000000'
    print ( 'sending "%s"' % message)
    sock.sendall(message)

    # Look for the response

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(4096)
        amount_received += len(data)
        print ( 'received "%s"' % data)

finally:
    print ('closing socket')
    sock.close()