import socket
import argparse
from utils.parser import Parser
import utils.JSON as JSON
import os.path
import json
from utils import colors


def argv():
    # Create parser
    arg_parser = argparse.ArgumentParser()
    # Add arguments
    arg_parser.add_argument('-p', '--port', help='Specify port to connect to')
    arg_parser.add_argument('-r', '--replay', help='Replay blob history file')
    # Return parsed arguments
    return arg_parser.parse_args()


def get_type(blob_type):
    # get blob type
    if blob_type == 'E110':
        return 'Hello'
    elif blob_type == 'DA7A':
        return 'Data'
    else:
        return 'Goodbye'


def replay(file):
    # read file from history folder
    if os.path.isfile('history/' + file):
        with open('history/' + file) as json_file:
            data = json.load(json_file)
            print(colors.Green, 'TLV blob received on', data['timestamp'].split('@')[0], 'at',
                  data['timestamp'].split('@')[1], ':')
            for blob in data['data']:
                print(colors.Blue, data['client']['ip'], ']:[', data['client']['port'], ']', colors.White,
                      get_type(blob['type']), '] [', blob['length'], ']', blob['value'])
    else:
        # if file is not found
        print("File doesn't exist, use a valid file name")

    



####################################################################################################

def main():
    args = argv()

    if args.replay:
        replay(args.replay)
    else:
        # Create a TCP/IP socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = ('localhost', int(args.port))
        print(colors.Green + "Server Starting on: ", server_address)
        server.bind(server_address)

        # Listen for incoming connections
        server.listen(5)

        while True:
            # Wait for a connection
            print(colors.Blue + 'waiting for a connection' + colors.White)
            connection, client_address = server.accept()
            try:
                print(colors.Green + 'connection from ', client_address[0], 'on Port ', client_address[0])

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(4096)

                    if data:
                        p = Parser(data)
                        tlv_blob = p.parse()
                        p.print_parsed_data(tlv_blob, client_address)
                        JSON.write_json(tlv_blob, client_address)

                        # print('sending data back to the client')
                        connection.sendall(data)
                    else:
                        print(colors.Red + 'no more data from', client_address)
                        break

            finally:
                # Clean up the connection
                connection.close()


if __name__ == "__main__":
    main()
