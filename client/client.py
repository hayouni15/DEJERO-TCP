import socket
import argparse

class CLIENT:

    def __init__(self, message,port):
        self.message = message
        self.port = port


    def send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', int(self.port))
        print ('connecting to %s port %s' % server_address)
        sock.connect(server_address)
        try:
            # Send data
            message=self.message
            print ( 'sending "%s"' % message)
            sock.sendall(message)

            # Look for the response

            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(1024)
                amount_received += len(data)
                print ( 'received "%s"' % data)

        finally:
            print ('closing socket')
            sock.close()