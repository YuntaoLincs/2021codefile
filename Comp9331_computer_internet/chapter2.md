keyword: client-server, socket, IP address, port number, transport-layer protocol, TCP, UDP, application-layer protocols, HTTP, DNS

1. socket can be regarded as an API between application and internet(or transport layer protocol).

2. port number: 80 web server.

## Transport-layer Protocol

3. transport-layer protocol
    1. requirement: reliable data transfer, Throughput, timing(layout), security

4. TCP service:
    1.  connection-oriented service
    2.  reliable data transfer service
    3. congestion control
(TLS can be regarded as an enhanced TCP for security)

5. UDP service:
    1. connectionless, no handshaking
    2. unreliable data transfer
    3. no congestion control

## Application-layer Protocols

6. application-layer protocols
    1. types of message exchanged, request and response
    2. syntax of message
    3. semantics of fields
    4. rules

7. types of application-layer protocols
    1. Web: http
    2. E-mail
    3. DNS
    4. P2P file sharing
    5. video streaming

8. Web: http(hyperText Transfer Protocol)
    1. a base HTML file and several referenced objects
    2. url(universal resource locator), two components: hostname of server and object's path name
    3. stateless protocol

9. Non-persistent HTTP
    1. Initiate a TCP connection to the server on a port number 80
    2. Client send a request message to server via its socket
    3. Server receives the request message, send the response message
    4. Server process tells TCP to close the TCP connection 
    5. Client receives the response message. TCP connection terminates

    Shortcoming:
    1. Connection established too much and need to save TCP buffers and variables which place a heavy burden on Web server.
    2. High delay 


    Q1. 描述RTT(round-trip time)以及非持久性连接的时延
        the response time of requesting a HTML file: two RTT + propagation time
10. Persistent HTTP

11. HTTP message format
    1. request message
        1. request line: method field, URL field, HTTP version field
        (first line)
            > GET / kurose_ross/interactive/index.php HTTP/1.1
        2. header line:  
            > Host: gaia.cs.umass.edu
            > Connection: close
            > User-agent:
            > Accept-language:
        3. Blank line
        4. Entity body(when use GET method, such place should be empty. Only use POST method )
            using the GET method may put the entity body into the URL
    2. Response message:
        1. status line: 
            1. protocol version
            2. status code
            3. corresponding status message
        2. header line
            1. Date: the time when you get the response message
            2. Server
            3. Last-Modified: the time when object was created or modified
            4. Content-Length
            5. Content-Type
        3. entity body
    3. supply material: 
        method:
        1. GET
        2. POST
        3. HEAD
        4. PUT
        5. DELETE
        state code
        1. 200 ok
        2. 301 Moved permanently
        3. 400 bad request
        4. 404 not found
        5. 408 time out
        5. 505 http version not supported
    4. Cookie 

    5. Web cache
        
    6. HTTP 2.0(需要从英文版书籍中完善)
12. DNS(domain name system)
    1. main task: translate hostnames to IP addresses
    2. Definition: 
        1. a distributed database
        2. an application-layer protocol
    3. port number: 53
    4. using UDP 
    5. other tasks: 
        1. host aliasing
        2. mail server aliasing
        3. load distribution

13. DNS: distributed database
    1. not a centralized design
        1. a single point of failure
        2. Traffic volume
        3. Distant centralized database
        4. Maintenance
    2. distributed, hierarchical database
        1. root DNS servers, top-level domain(TLD), authoritative DNS servers, local DNS server
        2. process of querying DNS message(待完善)
        3. DNS caching(待完善)
        4. DNS record
            1. resource record(RR)(待完善)
                TTL( time to live of resource record)
            2. DNS message format(待完善)
            3. 
    
14. Socket programming with UDP(待完善)
15. Socket programming with TCP(待完善)
