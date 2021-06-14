# Welcome to the Casino
**Category :** misc

## Description :
Can you get three-of-a-kind on this slot machine? Let's find out!

## Solution :
This is a challenge where you have to connect to a given host & port with netcat for a tcp connection. And provide the requested letter to start the spinning.

I created a small python script to connect automatically and provide input. Please find it below.
```
$ cat connect.py
import socket
from time import sleep

HOST = 'misc.bcactf.com'  # The server's hostname or IP address
PORT = 49156        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # anything near can be used like 'Enter the letter "' 
    # but I got better results like this.
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
```

Above script only makes a single connection to the host but we need to make multiple connections. So I just did a simple shell multithreading like below. (here output for each connection is stored in *\<num\>.txt* file.)

```
$ for i in {1..500}; do python3 connect.py >"${i}.txt" & done
```
But this got me several failed connections. Where the program stays up trying to listen from the host but the host doesn't respond.

```
# lists no. of empty files
$ for i in *.txt; do if [ ! -s "$i" ]; then echo $i; fi; done | wc -l
368
# lists no. of jobs that are still running.
$ jobs | wc -l
368
# kill all my remaining jobs
$ kill $(jobs -p)
# grep the congrats files
$ grep -i cong -A 20 *.txt | vi -
```
But from the successful connection outputs, I found different prizes like *zstegasaurus plushie*, *MISSINGNO* and *respect*.

Instead of trying to pop multiple connections at the same instant, I added a little delay so that I can limit my failed connections, pop a new connection by sleeping a second.
```
$ for i in {1..500}; do sleep 1;python3 connect.py >"${i}.txt" & done
```
I got lucky this time, as I got no failed connections and finally the **grand prize** flag.
```
recvd [35]:
Congratulations! You won the grand prize!
recvd [36]:

recvd [37]:
It's a flag!
recvd [38]:

recvd [39]:

recvd [40]:
   .^.
  (( ))
   |#|_______________________________
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#|'""""""""""""""""""""""""""""""'
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|

recvd [41]:
bcactf{y0u_g0t_1ucKy_af23dd97g64n}
recvd [42]:


recvd [43]:
Come back next time!
recvd [44]:
```

Note: added the output file 394.txt where flag is present.

# Flag :
bcactf{y0u_g0t_1ucKy_af23dd97g64n}
