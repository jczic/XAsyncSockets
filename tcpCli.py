
from   XAsyncSockets import XAsyncSocketsPool, XAsyncTCPClient, XClosedReason
import time

def _onTCPClientFailsToConnect(xAsyncTCPClient) :
    print("On TCP Client Fails To Connect")

def _onTCPClientConnected(xAsyncTCPClient) :
    print("On TCP Client Connected")
    xAsyncTCPClient.AsyncSendData( data          = b'Hello World',
                                   onDataSent    = _onTCPClientDataSent,
                                   onDataSentArg = 'test' )
    xAsyncTCPClient.AsyncRecvData(onDataRecv=_onTCPClientDataRecv)

def _onTCPClientDataSent(xAsyncTCPClient, arg) :
    print("On TCP Client Data Sent (%s)" % arg)

def _onTCPClientDataRecv(xAsyncTCPClient, data, arg) :
    print("On TCP Client Data Recv (%s bytes) : %s" % (len(data), data.tobytes()))
    xAsyncTCPClient.AsyncRecvData(onDataRecv=_onTCPClientDataRecv)

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

countClosed = 0

pool    = XAsyncSocketsPool()
srvAddr = ('127.0.0.1', 12345)

for i in range(100) :
    cli = XAsyncTCPClient.Create(pool, srvAddr)
    if cli :
        print("Client %s created" % (i+1))
        cli.OnFailsToConnect = _onTCPClientFailsToConnect
        cli.OnConnected      = _onTCPClientConnected
        cli.OnClosed         = _onTCPClientClosed
    else :
        print("Error to create client %s..." % (i+1))

pool.AsyncWaitEvents(threadsCount=1)
time.sleep(7)
pool.StopWaitEvents()
