keyword:

## Transport layer

### Multiplexing and Demultiplexing

1. UDP(user datagram protocols)
    1. two tuple
    2. dest IP, dest Port

2. TCP(transmission connection protocols)
    1. four tuples
    2. dest IP and Port, source IP and Port

###  UDP

1. UDP features
    1. Best effort
    2. connectionless
    3. stateless
        1. no congestion control
    4. small packet header:
        UDP 8B of header
2. UDP segment structure
    1. check sum
        1. add the total sum of the bit and with its supplement(if the last addition had overflow, which was wrapped around)
        2. check whether all bits are equal to 1.

### RDT ( reliable data transfer)

1. RDT1.0
2. RDT2.0(over a channel with bit errors)
    1. ARQ protocols
        1. error detection
        2. receiver feedback
        3. retransmission
    2. drawback
        1. do not consider the possibility that ACK or NAK packet may be corrupted
    3. RDT2.1
        1. sequence number
    4. RDT2.2
        2. no NAK
3. RDT3.0(over a lossy channel with bit errors)
    1. countdown timer 
    2. efficiency:U = $\frac{L/R}{RTT+L/R}$
4. Pipelined RDT
    1. Efficiency: U = $\frac{N*L/R}{RTT+L/R}$
    2. method:
        1. GO back N
            1. N is the window size (k is the number of bits in packet sequence, N = 2^k - 1)
            2. one timer
            3. no buffer, no receiver window
        2. selective repeat
            1. each packet should have a timer
            2. should have buffer
            3. sender window size <= 1/2 of sequence number space
                1. receiver can not judge whether it is the new packet or it is the retransmisssion
### TCP

32-bit sequence number field
1. segment structure
    1. source port number + destination port number (each 16 bits)
    2. sequence number field ( 32 bits)
        1. byte-stream number of the first byte in the segment
    3. acknowledgment number field ( 32 bits )
        1. the sequence number of the next expecting byte 
        2. provide the cumulative acknowledgment ( GBN )
        3. in practice, method of selective repeat is usual
    4. checksum ( 16 bits) + urgent data pointer
    5. header length( 4 bits ) and flags + receiver window field( 16 bits) 
    ( minimize header: 5*32/8 = 20B)

    MSS ( maximum segment size ) = 1460B = MTU (maximum transmission unit = 1500) - IP header(20) - TCP header(20)

2. Round-trip time estimation and timeout
    1. 