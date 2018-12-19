
from   XAsyncSockets import XAsyncSocketsPool, XAsyncTCPServer, XClosedReason
import time

def _onTCPSrvClientAccepted(xAsyncTCPServer, xAsyncTCPClient) :
    global countAccepted
    countAccepted += 1
    print('%s) On TCP Server Client Accepted' % countAccepted)
    xAsyncTCPClient.OnClosed = _onTCPClientClosed
    xAsyncTCPClient.AsyncRecvData( onDataRecv    = _onTCPClientDataRecv,
                                   onDataRecvArg = 'test',
                                   timeoutSec    = 1 )

def _onTCPSrvClosed(xAsyncTCPServer, closedReason) :
    print("On TCP Server Closed")

def _onTCPClientDataRecv(xAsyncTCPClient, data, arg) :
    global countRecv
    countRecv += 1
    print( "%s) On TCP Client Data Recv (%s bytes) : %s" \
           % (countRecv, len(data), data.tobytes()) )
    xAsyncTCPClient.AsyncRecvData(onDataRecv=_onTCPClientDataRecv, timeoutSec=2)

def _onTCPClientClosed(xAsyncTCPClient, closedReason) :
    global countClosed
    countClosed += 1
    if closedReason == XClosedReason.Error :
        reason = "error"
    elif closedReason == XClosedReason.ClosedByHost :
        reason = "closed by host"
    elif closedReason == XClosedReason.ClosedByPeer :
        reason = "closed by peer"
    elif closedReason == XClosedReason.Timeout :
        reason = "timeout"
    else :
        reason = "???"
    print("%s) On TCP Client Closed (%s)" % (countClosed, reason))

countAccepted = 0
countRecv     = 0
countClosed   = 0
 
pool    = XAsyncSocketsPool()
srvAddr = ('0.0.0.0', 12345)

srv                  = XAsyncTCPServer.Create(pool, srvAddr)
srv.OnClientAccepted = _onTCPSrvClientAccepted
srv.OnClosed         = _onTCPSrvClosed

pool.AsyncWaitEvents(threadsCount=1)

while True :
    time.sleep(1)
