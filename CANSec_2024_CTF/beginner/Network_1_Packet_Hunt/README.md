# Network 1: Packet Hunt
**Points**: 25

## Description
We've intercepted a network capture file network\_file.pcap, and it’s up to you to find the hidden flag. Somewhere in the traffic, among all the noise of typical web activity, is your target. Use a network analysis tool to dig through the packets and uncover the flag. The challenge isn’t just spotting the flag—it’s figuring out where it’s been hidden in plain sight.

Hint: There are a couple of fake flags in this file. However, once found, they will get you closer to the actual flag.

## Writeup
This is a simple packet analysis challenge but the provide pcap file is huge. So, immediately I fired-up the wireshark app to understand the network packets.

As this is a simple beginner challenge and the file is huge, I immediately went for filtering the http packets.
```
Wireshark filter: http
```
And found many modified HTTP GET requests being sent using cURL. So, I filtered for POST and GET requests first (not responses).
```
Wireshark filter: http.request.method == "POST" || http.request.method == "GET"
```
POST requests were simply chrome verifying cert signature using OCSP. Also, I found .goog is a domain level TLD dedicated for Google.

GET requests is where the fake flags started apprearing and many had CTF in them. So, I immediately searched for strings containing CTF in them using Wireshark search (CTRL+F). Tweaked the options to `Packet bytes`, `String` and Non case-sensitive and found few hits. After looking through them I found 3 CTF flags where are as below,
```
CTF{GaLvANiZ4D}
CTF{sQu1R4}
CTF{sTe4L}
```
I tried all three of them separately with and without CTF blocks as flag structure is not disclosed. My final try on piecing them together as `GaLvANiZ4D sQu1R4 sTe4L` worked.

# Flag
GaLvANiZ4D sQu1R4 sTe4L
