from random import randint
import sys, traceback, threading, socket

from RtpPacket import RtpPacket

# server state
STATE = {
    'INIT': 0,
    'OK': 1,
    'PLAYING': 2,
}

# process vided stream
class Streaming:
    count = 1

    def __init__(self, path):
        self.path = path

        try:
            self.file = open(path, 'rb')
        except:
            raise IOError

        self.currentFrame = 0

    def getCurrentFrame(self):
        return self.currentFrame

    def getPath(self):
        return self.path

    def getFiel(self):
        return self.file

    def getNextFrame(self): 
        self.count += 1
        path = 'img/' + str(self.count) + '.jpg'
        print(path)
        try:
            self.file = open(path, 'rb')
        except:
            self.count = 1
            self.file = open('img/1.jpg', 'rb')

        data = self.file.read()
        self.currentFrame += 1

        return data


# process server
class Server:
    clientInfo = {}

    state = STATE['INIT']
    
    def __init__(self, clientInfo):
        self.clientInfo = clientInfo
    
    # 多client连接
    def processThreads(self):
        threading.Thread(target=self.getRequest).start()

    def getRequest(self):
        sk = self.clientInfo['rtspSocket'][0]

        while 1:
            data = sk.recv(1024).decode()

            if data:
                print('Recv:', data)
                self.processRequest(data)

    def processRequest(self, data): 
        dataList = data.split('\n')

        param = dataList[0]
        seq = dataList[1]
        addr = dataList[2]

        paramList = param.split(' ')
        seqList = seq.split(' ')
        addrList = addr.split(' ')

        kind = paramList[0]
        path = paramList[1]

        # state setup
        if kind == 'SETUP': 
            # msg
            print ('SETUP...')

            # get videostream
            try: 
                self.clientInfo['videoStream'] = Streaming(path)
                
                # set state
                self.state = STATE['OK']

            except IOError: 
                print ("Error: 404 not found.")

            # set session
            self.clientInfo['session'] = randint(100000, 999999)

            # response msg
            response = 'RTSP/1.0 200 OK\nCSeq: ' + \
                seqList[1] + \
                '\nSession: ' + \
                str(self.clientInfo['session'])
            sk = self.clientInfo['rtspSocket'][0]
            sk.send(response.encode())

            self.clientInfo['rtpPort'] = addrList[3]

        # state play
        elif kind == 'PLAY':
            if self.state == STATE['OK']:
                # msg
                print ('PLAY...')
                
                # set state
                self.state = STATE['PLAYING']

                # create sk
                self.clientInfo['rtpSocket'] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                # response msg
                response = 'RTSP/1.0 200 OK\nCSeq: ' + \
                    seqList[1] + \
                    '\nSession: ' + \
                    str(self.clientInfo['session'])
                sk = self.clientInfo['rtspSocket'][0]
                sk.send(response.encode())

                # process thread
                self.clientInfo['event'] = threading.Event()
                self.clientInfo['worker'] = threading.Thread(target=self.sendPacket)
                self.clientInfo['worker'].start()

        # state pause
        elif kind == 'PAUSE':
            if self.state == STATE['PLAYING']:
                # msg
                print ('PAUSE...') 

                # set state
                self.state = STATE['OK']

                # process
                self.clientInfo['event'].set()

                # response msg
                response = 'RTSP/1.0 200 OK\nCSeq: ' + \
                    seqList[1] + \
                    '\nSession: ' + \
                    str(self.clientInfo['session'])
                sk = self.clientInfo['rtspSocket'][0]
                sk.send(response.encode())

        elif kind == 'TEARDOWN':
            # msg
            print ('TEARDOWN...')

            # process
            self.clientInfo['event'].set()

            # response msg
            response = 'RTSP/1.0 200 OK\nCSeq: ' + \
                seqList[1] + \
                '\nSession: ' + \
                str(self.clientInfo['session'])
            sk = self.clientInfo['rtspSocket'][0]
            sk.send(response.encode())

            # close sk
            self.clientInfo['rtpSocket'].close()

        else:
            print ('Error: Wrong kind.')

    def sendPacket(self): 
        while 1:
            # set interval
            self.clientInfo['event'].wait(0.5)

            # break if pause or teardown
            if self.clientInfo['event'].isSet():
                break

            # get next frame
            frame = self.clientInfo['videoStream'].getNextFrame()

            if frame: 
                # get current frame
                currentFrame = self.clientInfo['videoStream'].getCurrentFrame()

                try: 
                    # get addr
                    ip = self.clientInfo['rtspSocket'][1][0]
                    port = int(self.clientInfo['rtpPort'])
                    self.clientInfo['rtpSocket'].sendto(self.setPacket(frame, currentFrame), (ip, port))

                except: 
                    print('Error: Connecting failed.')

    def setPacket(self, frame, currentFrame):
        # set packet
        rtpPacket = RtpPacket()
        rtpPacket.encode(2, 0, 0, 0, currentFrame, 0, 26, 0, frame)
        
        return rtpPacket.getPacket()


if __name__ == "__main__":
    try: 
        port = int(sys.argv[1])

    except: 
        print('Please add param [port]')
    
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('', port))
    sk.listen(5) 

    while 1: 
        clientInfo = {}
        clientInfo['rtspSocket'] = sk.accept()
        Server(clientInfo).processThreads()
