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
        2. selective repeat
### TCP

1. 