import XAsyncSockets

def _onUDPDatagramRecv(xAsyncUDPDatagram, remoteAddr, datagram) :
    print('On UDP Datagram Recv (%s:%s) :' % remoteAddr)
    print(bytes(datagram))

xAsyncSocketsPool = XAsyncSockets.XAsyncSocketsPool()
localAddr         = ('0.0.0.0', 12345)
xAsyncUDPDatagram = XAsyncSockets.XAsyncUDPDatagram. \
                    Create(xAsyncSocketsPool, localAddr)
if xAsyncUDPDatagram :
    xAsyncUDPDatagram.OnRecv = _onUDPDatagramRecv
    print("LocalAddr : %s:%s" % xAsyncUDPDatagram.LocalAddr)

xAsyncSocketsPool.AsyncWaitEvents()
