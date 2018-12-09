import XAsyncSockets

def _onUDPDatagramFailsToSend(xAsyncUDPDatagram, datagram, remoteAddr) :
    print('On UDP Datagram Fails To Send')

def _onUDPDatagramOnCanSend(xAsyncUDPDatagram) :
    print("On UDP Datagram Can Send")
    xAsyncUDPDatagram.AsyncSendDatagram(b'Hello Wolrd', ('127.0.0.1', 12345))

xAsyncSocketsPool = XAsyncSockets.XAsyncSocketsPool()
xAsyncUDPDatagram = XAsyncSockets.XAsyncUDPDatagram. \
                    Create(xAsyncSocketsPool)
if xAsyncUDPDatagram :
	xAsyncUDPDatagram.OnFailsToSend = _onUDPDatagramFailsToSend
	xAsyncUDPDatagram.OnCanSend     = _onUDPDatagramOnCanSend

xAsyncSocketsPool.AsyncWaitEvents()
