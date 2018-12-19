import XAsyncSockets

def _onUDPDatagramDataRecv(xAsyncUDPDatagram, remoteAddr, datagram) :
    print('On UDP Datagram Data Recv (%s:%s) :' % remoteAddr)
    print(bytes(datagram))

xAsyncSocketsPool = XAsyncSockets.XAsyncSocketsPool()
localAddr         = ('0.0.0.0', 12345)
xAsyncUDPDatagram = XAsyncSockets.XAsyncUDPDatagram. \
                    Create(xAsyncSocketsPool, localAddr)
if xAsyncUDPDatagram :
    xAsyncUDPDatagram.OnDataRecv = _onUDPDatagramDataRecv
    print("LocalAddr : %s:%s" % xAsyncUDPDatagram.LocalAddr)

xAsyncSocketsPool.AsyncWaitEvents()
