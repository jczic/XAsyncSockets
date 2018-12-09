## XAsyncSockets is a little but full Python library of managed asynchronous sockets.

![HC²](hc2.png "HC²")

#### Very easy to integrate and very light with one file only :
- `"XAsyncSockets.py"`

#### XAsyncSockets features :
- Managed asynchronous sockets (in pool)
- Works directly with I/O
- Supports very large number of simultaneous pending connections
- Supports concurrent synchronous processing operations if necessary (threaded)
- Implementation of TCP server
- Implementation of TCP client
- Implementation of UDP datagrams sender/receiver
- TCP client can event after a specified size of data or a text line received
- The reasons of TCP client closures are returned
- Really robust, very fast and easy to use

### *XAsyncSockets* classes :

| Class name | Description |
| - | - |
| XAsyncSocketsPool | Managed pool of 'XAsyncSocket' objects |
| XClosedReason | Enumerator of 'XAsyncSocket' closing reasons |
| XAsyncSocket | Abstract class of managed asynchronous sockets |
| XAsyncTCPServer | TCP server implementation of 'XAsyncSocket' |
| XAsyncTCPClient | TCP client implementation of 'XAsyncSocket' |
| XAsyncUDPDatagram | UDP sender/recever implementation of 'XAsyncSocket' |
| XBufferSlot | Managed buffer |
| XBufferSlots | Managed buffers collection |

### *XAsyncSockets* exceptions :

| Class name | Description |
| - | - |
| XAsyncSocketsPoolException | Exception class for 'XAsyncSocketsPool' |
| XAsyncSocketException | Exception class for 'XAsyncSocket' |
| XAsyncTCPServerException | Exception class for 'XAsyncTCPServer' |
| XAsyncTCPClientException | Exception class for 'XAsyncTCPClient' |
| XAsyncUDPDatagramException | Exception class for 'XAsyncUDPDatagram' |

### *XAsyncSocketsPool* class details :

| Method | Arguments |
| - | - |
| Constructor | None |
| AsyncWaitEvents | `threadsCount=0` (int) |
| StopWaitEvents | None |

( Do not call directly the methods `AddAsyncSocket`, `RemoveAsyncSocket`, `NotifyNextReadyForReading` and `NotifyNextReadyForWriting` )

### *XClosedReason* class details :

| Static variable | Value |
| - | - |
| Error | 0x00 |
| ClosedByHost | 0x01 |
| ClosedByPeer | 0x02 |
| Timeout | 0x03 |

### *XAsyncSocket* class details :

| Method | Arguments |
| - | - |
| GetAsyncSocketsPool | None |
| GetSocketObj | None |
| Close | None |

| Property | Details |
| - | - | - |
| OnClosed | Get or set an event of type f(closedReason) |
| State | Get or set object |

### *XAsyncTCPServer* class details :

| Method | Arguments |
| - | - |
| Create (static) | `asyncSocketsPool`, `srvAddr` (tuple of ip and port), `srvBacklog=256` (int), `recvBufSlots=None` |

| Property | Details |
| - | - | - |
| SrvAddr | Tuple of ip and port |
| OnClientAccepted | Get or set an event of type f(xAsyncTCPServer, xAsyncTCPClient) |

### *XAsyncTCPClient* class details :

| Method | Arguments |
| - | - |
| Create (static) | `asyncSocketsPool`, `srvAddr`, `connectTimeout=5`(int), `recvbufLen=4096`(int) |
| AsyncRecvLine | `timeoutSec=None` (int) |
| AsyncRecvData | `size=None` (int), `timeoutSec=None` (int) |
| AsyncSendData | `data` (bytes or buffer protocol) |

| Property | Details |
| - | - | - |
| SrvAddr | Tuple of ip and port |
| CliAddr | Tuple of ip and port |
| OnFailsToConnect | Get or set an event of type f(xAsyncTCPClient) |
| OnConnected | Get or set an event of type f(xAsyncTCPClient) |
| OnLineRecv | Get or set an event of type f(xAsyncTCPClient, line) |
| OnDataRecv | Get or set an event of type f(xAsyncTCPClient, data) |
| OnCanSend | Get or set an event of type f(xAsyncTCPClient) |

### *XAsyncUDPDatagram* class details :

| Method | Arguments |
| - | - |
| Create (static) | `asyncSocketsPool`, `localAddr=None` (tuple of ip and port), `recvbufLen=4096`(int), `broadcast=False`(bool) |
| AsyncSendDatagram | `datagram` (bytes or buffer protocol), `remoteAddr` (tuple of ip and port) |

| Property | Details |
| - | - | - |
| LocalAddr | Tuple of ip and port |
| OnRecv | Get or set an event of type f(xAsyncUDPDatagram, remoteAddr, datagram) |
| OnFailsToSend | Get or set an event of type f(xAsyncUDPDatagram, datagram, remoteAddr) |
| OnCanSend | Get or set an event of type f(xAsyncUDPDatagram) |

### *XBufferSlot* class details :

| Method | Arguments |
| - | - |
| Constructor | `size` (int), `keepAlloc=True`(bool) |

| Property | Details |
| - | - | - |
| Available | Get or set the availability of the slot |
| Size | Get the buffer size of the slot |
| Buffer | Get the buffer of the slot |

### *XBufferSlots* class details :

| Method | Arguments |
| - | - |
| Constructor | `slotsCount`(int), `slotsSize`(int), `keepAlloc=True`(bool) |
| GetAvailableSlot | None |

| Property | Details |
| - | - | - |
| SlotsCount | Get the number of slots |
| SlotsSize | Get the buffer size of each slots |
| Slots | Get the list of slots |

### By JC`zic for [HC²](https://www.hc2.fr) ;')

*Keep it simple, stupid* :+1:
