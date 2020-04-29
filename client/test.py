from client import CLIENT
import argparse
from threading import Thread

def argv():
    # Create parser
    arg_parser = argparse.ArgumentParser()
    # Add arguments
    arg_parser.add_argument('-t', '--test', help='Specify which test to run')
    arg_parser.add_argument('-p', '--port', help='Specify port to connect to')
    

    # Return parsed arguments
    return arg_parser.parse_args()

def test1(port):
    client1= CLIENT(b'E11000000000DA7A0000000501020304050B1E00000000',port)
    client1.send()

def test2(port):
    for test in range (0,50):
        print('test ', test)
        client1= CLIENT(b'E11000000000DA7A0000000501020304050B1E00000000',port)
        client1.send()
def test4(port):
    msg=b'E11000000000DA7A000003E8'
    for i in range(0,500):
        msg+=b'01'
    msg+=b'0B1E00000000'
    print('data length: ',len(msg))
    client1= CLIENT(msg,port)
    client1.send()



def main():
    args = argv()

    if args.test == 'test1':
        #test1 : test simple client connecting and sending binary string
        test1(args.port)
    if args.test == 'test2':
        #test2 : test a big number of connections 
        test2(args.port)

    if args.test == 'test3':
        #test3 a big number of simultanious connections
        for i in range (0,50):
            Thread(target = test1(args.port)).start()

    if args.test == 'test4':
        #test2 : test sending big data
        test4(args.port)


if __name__ == "__main__":
    main()
