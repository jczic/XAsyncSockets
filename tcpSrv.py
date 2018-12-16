
from   XAsyncSockets import XAsyncSocketsPool, XAsyncTCPServer, XClosedReason
import time

def _onTCPSrvClientAccepted(xAsyncTCPServer, xAsyncTCPClient) :
    global countAccepted
    countAccepted += 1
    print('%s) On TCP Server Client Accepted' % countAccepted)
    xAsyncTCPClient.OnFailsToConnect = _onTCPClientFailsToConnect
    xAsyncTCPClient.OnLineRecv       = _onTCPClientLineRecv
    xAsyncTCPClient.OnDataRecv       = _onTCPClientDataRecv
    xAsyncTCPClient.OnCanSend        = _onTCPClientCanSend
    xAsyncTCPClient.OnClosed         = _onTCPClientClosed
    xAsyncTCPClient.AsyncRecvData(timeoutSec=1)

def _onTCPSrvClosed(xAsyncTCPServer, closedReason) :
    print("On TCP Server Closed")

def _onTCPClientFailsToConnect(xAsyncTCPClient) :
    print("On TCP Client Fails To Connect")

def _onTCPClientLineRecv(xAsyncTCPClient, line) :
    print("On TCP Client Line Recv : %s" % line)
    xAsyncTCPClient.AsyncRecvLine(timeoutSec=2)

def _onTCPClientDataRecv(xAsyncTCPClient, data) :
    global countRecv
    countRecv += 1
    print( "%s) On TCP Client Data Recv (%s bytes) : %s" \
           % (countRecv, len(data), data.tobytes()) )
    xAsyncTCPClient.AsyncRecvData(timeoutSec=2)

def _onTCPClientCanSend(xAsyncTCPClient) :
    print("On TCP Client Can Send")

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
