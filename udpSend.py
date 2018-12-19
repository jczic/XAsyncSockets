import XAsyncSockets

def _onUDPDatagramFailsToSend(xAsyncUDPDatagram, datagram, remoteAddr) :
    print('On UDP Datagram Fails To Send')

def _onUDPDatagramDataSent(xAsyncUDPDatagram, arg) :
    print("On UDP Datagram Data Sent (%s)" % arg)
    xAsyncUDPDatagram.AsyncSendDatagram(b'NEXT', ('127.0.0.1', 12345))

xAsyncSocketsPool = XAsyncSockets.XAsyncSocketsPool()
xAsyncUDPDatagram = XAsyncSockets.XAsyncUDPDatagram. \
                    Create(xAsyncSocketsPool)
if xAsyncUDPDatagram :
	xAsyncUDPDatagram.OnFailsToSend = _onUDPDatagramFailsToSend
	xAsyncUDPDatagram.OnDataSent    = _onUDPDatagramDataSent
	xAsyncUDPDatagram.AsyncSendDatagram( datagram      = b'START',
		                                 remoteAddr    = ('127.0.0.1', 12345),
		                                 onDataSent    = _onUDPDatagramDataSent,
		                                 onDataSentArg = 'test' )

xAsyncSocketsPool.AsyncWaitEvents()
