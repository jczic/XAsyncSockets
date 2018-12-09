
from   XAsyncSockets import XAsyncSocketsPool, XAsyncTCPClient, XClosedReason
import time

def _onTCPClientFailsToConnect(xAsyncTCPClient) :
    print("On TCP Client Fails To Connect")

def _onTCPClientConnected(xAsyncTCPClient) :
    print("On TCP Client Connected")
    xAsyncTCPClient.AsyncSendData(b'Hello World')
    xAsyncTCPClient.AsyncRecvData()

def _onTCPClientLineRecv(xAsyncTCPClient, line) :
    print("On TCP Client Line Recv : %s" % line)
    xAsyncTCPClient.AsyncRecvLine()

def _onTCPClientDataRecv(xAsyncTCPClient, data) :
    global countRecv
    countRecv += 1
    print( "%s) On TCP Client Data Recv (%s bytes) : %s" \
           % (countRecv, len(data), data.tobytes()) )
    xAsyncTCPClient.AsyncRecvData()

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

countRecv   = 0
countClosed = 0

pool    = XAsyncSocketsPool()
srvAddr = ('127.0.0.1', 12345)

for i in range(100) :
    cli = XAsyncTCPClient.Create(pool, srvAddr)
    if cli :
        print("Client %s created" % (i+1))
        cli.OnFailsToConnect = _onTCPClientFailsToConnect
        cli.OnConnected      = _onTCPClientConnected
        cli.OnLineRecv       = _onTCPClientLineRecv
        cli.OnDataRecv       = _onTCPClientDataRecv
        cli.OnCanSend        = _onTCPClientCanSend
        cli.OnClosed         = _onTCPClientClosed
    else :
        print("Error to create client %s..." % (i+1))

pool.AsyncWaitEvents(threadsCount=1)
time.sleep(7)
pool.StopWaitEvents()
