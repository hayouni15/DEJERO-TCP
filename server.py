import socket

import argparse
from utils.parser import Parser
import utils.JSON as JSON


def argv():
    # Create parser
    arg_parser = argparse.ArgumentParser()

    # Add arguments
    arg_parser.add_argument('-p', '--port', help='Specify port to connect to')
    arg_parser.add_argument('-r', '--replay', help='Replay history')

    # Return parsed arguments
    return arg_parser.parse_args()


####################################################################################################

def main():

    args = argv()

    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('localhost', int(args.port))
    print("Server Starting on: ", server_address)
    server.bind(server_address)

    # Listen for incoming connections
    server.listen(5)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = server.accept()
        try:
            print('connection from ', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(4096)

                if data:
                    p = Parser(data)
                    TLV_blob = p.parse()
                    p.print_parsed_data(TLV_blob, client_address)
                    JSON.write_json(TLV_blob, client_address)

                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no more data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    main()

