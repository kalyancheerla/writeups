import socket
from time import sleep

HOST = 'misc.bcactf.com'  # The server's hostname or IP address
PORT = 49156        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    findstr = 'er "'
    i = 1
    while True:
        try:
            #sleep(1)
            reply = s.recv(1024)
            if not reply:
                break
            freply = "\n".join(reply.decode().splitlines())
            print(f"recvd [{i}]:\n{freply}")

            result = freply.find(findstr)
            #print(result)
            #print(findstr)
            if (result != -1):
                #print(freply[result:])
                firstkey = freply[result + len(findstr)]
                #print(f'{firstkey}')
                s.send(bytes(firstkey, 'utf-8'))

            #s.send(bytes('\n', 'utf-8'))

        except KeyboardInterrupt:
            print("bye")
            break
        i += 1
    s.close()

