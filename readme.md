# TCP 

This project is an implementation of a TCP listening socket bound to an IP address and and a port number provided by the user as a command-line argument.

# Test

Start the server:
```sh
$ python server.py -p 10000
```
expected output:
>Server Starting on:  ('', 10000)

>waiting for a connection

connecting from client and sending data:
in a new terminal, change directory to client folder :
```sh
$ cd client
```
connect on the same port and perform one of the following built in tests:
## test1 : test simple client connecting and sending data
```sh
$ python test.py -p 10000 -t test1
```
expected output:
>connection from  127.0.0.1 on Port  56805

>[ 127.0.0.1 : 56805 ] [Hello]  [ 0 ]  []

>[ 127.0.0.1 : 56805 ] [Data]  [ 5 ]  ['0x01', '0x02', '0x03', '0x04', '0x05']

>[ 127.0.0.1 : 56805 ] [Goodbye]  [ 0 ]  []

>no more data from ('127.0.0.1', 56805)

>waiting for a connection
## test2 : test a big number of connections
```sh
$ python test.py -p 10000 -t test2
```
## test3 : test simultanious connections
```sh
$ python test.py -p 10000 -t test3
```
## test4 :  test sending big data
```sh
$ python test.py -p 10000 -t test4
```




# History

server.py saves the received message in Json format in the history folder:

```json
{
    "timestamp": "04-27-2020@09-35-08",
    "client": 
    {
        "ip": "127.0.0.1",
        "port": 56619
    },
    "data": 
    [
        {
        "type": "E110",
        "length": 0,
        "value": []
        },
        {
        "type": "DA7A",
        "length": 5,
        "value": [
        "0x01",
        "0x02",
        "0x03",
        "0x04",
        "0x05"
        ]
        },
        {
        "type": "0B1E",
        "length": 0,
        "value": []
        }
    ]
}
```
to replay hisotory , specify file from the history directory using the -r argument as follows:
```sh
$ python server.py -r 04-27-2020@09-35-08.json
```
