import socket, threading, sys, traceback, os, tkinter, time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel

from PIL import Image, ImageTk, ImageFile

from RtpPacket import RtpPacket

ImageFile.LOAD_TRUNCATED_IMAGES = True

RECV_SIZE = 20480 + 16
HIGHT = 500
CACHE_FILE_NAME = "tmp-"
CACHE_FILE_EXT = ".jpg"

class QLabel(QLabel):
    def keyPressEvent(self, event): 
        # escape full screen
        if event.key() == QtCore.Qt.Key_Escape: 
            global ui
            global client

            # avoid crash
            client.pauseMovie()
            time.sleep(1)

            page_main.label_display.setWindowFlags(Qt.Widget)
            page_main.label_display.showNormal()

            client.playMovie()

        # fullscreen pause and play
        if event.key() == QtCore.Qt.Key_Space: 
            # pause
            if client.state == client.PLAYING:
                client.pauseMovie()

            # play
            elif client.state == client.READY:
                client.playMovie()

        # if event.key() == QtCore.Qt.Key_Left: 
        #     if client.state == client.PLAYING or client.state == client.READY:
        #         if (client.page_main.scrollLine.value() - 3 > 0):
        #             client.page_main.scrollLine.setValue(client.page_main.scrollLine.value() - 3)
        #             client.relocatePosition = client.page_main.scrollLine.value()
        #     client.sendRtspRequest(client.RELOCATE)

        # if event.key() == QtCore.Qt.Key_Right: 
        #     if client.state == client.PLAYING or client.state == client.READY:
        #         if (client.page_main.scrollLine.value() + 3 < 100):
        #             client.page_main.scrollLine.setValue(client.page_main.scrollLine.value() + 3)
        #             client.relocatePosition = client.page_main.scrollLine.value()
        #     client.sendRtspRequest(client.RELOCATE)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(6, 1, 791, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_title.setText("")
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.label_display = QLabel(self.verticalLayoutWidget)
        self.label_display.setText("")
        self.label_display.setObjectName("label_display")
        self.verticalLayout.addWidget(self.label_display)
        self.label_subtitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_subtitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_subtitle.setText("")
        self.label_subtitle.setObjectName("label_subtitle")
        self.verticalLayout.addWidget(self.label_subtitle)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.scrollLine = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.scrollLine.setOrientation(QtCore.Qt.Horizontal)
        self.scrollLine.setObjectName("scrollLine")
        self.verticalLayout.addWidget(self.scrollLine)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_setup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_setup.setObjectName("btn_setup")
        self.horizontalLayout.addWidget(self.btn_setup)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btn_play = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.btn_pause = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_pause.setObjectName("btn_pause")
        self.horizontalLayout.addWidget(self.btn_pause)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.btn_teardown = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_teardown.setObjectName("btn_teardown")
        self.horizontalLayout.addWidget(self.btn_teardown)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.btn_fullscreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_fullscreen.setObjectName("btn_fullscreen")
        self.horizontalLayout.addWidget(self.btn_fullscreen)
        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 7)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 7)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 7)
        self.horizontalLayout.setStretch(7, 1)
        self.horizontalLayout.setStretch(8, 7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 30)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_slower = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_slower.setObjectName("btn_slower")
        self.horizontalLayout_5.addWidget(self.btn_slower)
        self.btn_faster = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_faster.setObjectName("btn_faster")
        self.horizontalLayout_5.addWidget(self.btn_faster)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 34)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 60)
        self.verticalLayout_2.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_setup.setText(_translate("MainWindow", "Setup"))
        self.btn_play.setText(_translate("MainWindow", "Play"))
        self.btn_pause.setText(_translate("MainWindow", "Pause"))
        self.btn_teardown.setText(_translate("MainWindow", "Teardown"))
        self.btn_fullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.label_2.setText(_translate("MainWindow", "视频"))
        self.label_3.setText(_translate("MainWindow", "倍速调整"))
        self.btn_slower.setText(_translate("MainWindow", "0.5"))
        self.btn_faster.setText(_translate("MainWindow", "2.0"))


class Client:
    INIT = 0
    READY = 1
    PLAYING = 2
    state = INIT
    
    SETUP = 0
    PLAY = 1
    PAUSE = 2
    TEARDOWN = 3
    FASTER = 4
    SLOWER = 5
    RELOCATE = 6
    
    # init
    def __init__(self, serveraddr, serverport, rtpport, filename, page):
        self.page_main = page
        self.state == self.READY
        self.serverAddr = serveraddr
        self.serverPort = int(serverport)
        self.rtpPort = int(rtpport)
        self.fileName = filename
        self.rtspSeq = 0
        self.sessionId = 0
        self.relocatePosition = 0
        self.requestSent = -1
        self.teardownAcked = 0
        self.connectToServer()
        self.frameNbr = 0

    # handle fullscreen
    def setFull(self):
        if self.state == self.PLAYING or self.state == self.READY:
            self.pauseMovie()
            time.sleep(1)
            self.page_main.label_display.setWindowFlags(Qt.Window)
            self.page_main.label_display.showFullScreen()
            self.playMovie()

    # handle relocate
    def relocateMovie(self):
        if self.state == self.PLAYING or self.state == self.READY:
            self.relocatePosition = self.page_main.scrollLine.value()
            self.sendRtspRequest(self.RELOCATE)

    # handle faster
    def fasterMovie(self):
        if self.state == self.PLAYING or self.state == self.READY:
            self.sendRtspRequest(self.FASTER)

    # handle slower
    def slowerMovie(self):
        if self.state == self.PLAYING or self.state == self.READY:
            self.sendRtspRequest(self.SLOWER)

    # handle setup
    def setupMovie(self):
        if self.state == self.INIT:
            self.sendRtspRequest(self.SETUP)
    
    # handle teardown
    def exitClient(self):
        self.sendRtspRequest(self.TEARDOWN)
        os.remove(CACHE_FILE_NAME + str(self.sessionId) + CACHE_FILE_EXT) # Delete tmp img
        sys.exit(0) # Exit

    # handle pause
    def pauseMovie(self):
        if self.state == self.PLAYING:
            self.sendRtspRequest(self.PAUSE)
    
    # handle play
    def playMovie(self):
        if self.state == self.READY:
            threading.Thread(target=self.listenRtp).start()
            self.playEvent = threading.Event()
            self.playEvent.clear()
            self.sendRtspRequest(self.PLAY)
    
    # get rtp packet
    def listenRtp(self):
        while 1:
            try:
                cachename = CACHE_FILE_NAME + str(self.sessionId) + CACHE_FILE_EXT
                file = open(cachename, "wb+")
                while 1:
                    data = self.rtpSocket.recv(RECV_SIZE)

                    if data:
                        rtpPacket = RtpPacket()
                        rtpPacket.decode(data)
                        self.page_main.scrollLine.setValue(rtpPacket.getPot())

                        currFrameNbr = rtpPacket.seqNum()
                        file.write(rtpPacket.getPayload())
                        print("FrameNo:", currFrameNbr)

                        # if new frame
                        if currFrameNbr > self.frameNbr and rtpPacket.getIfEnd():
                            self.frameNbr = currFrameNbr
                            self.updateMovie(cachename)
                            file.close()
                            break
            except:
                # pause or teardown
                if self.playEvent.isSet(): 
                    break

                print('Error: Frame receiving failed!')

                if self.teardownAcked == 1:
                    self.rtpSocket.shutdown(socket.SHUT_RDWR)
                    self.rtpSocket.close()
                    break

    # write cutframe to local
    def writeFrame(self):
        cachename = CACHE_FILE_NAME + str(self.sessionId) + CACHE_FILE_EXT
        file = open(cachename, "wb")
        for item in self.cutFrameList:
            file.write(item)
        file.close()
        
        return cachename

    # get new frame
    def updateMovie(self, imageFile):
        pixmap = QtGui.QPixmap(imageFile)
        self.page_main.label_display.setPixmap(pixmap)
        self.page_main.label_display.setScaledContents(True)
    
    # connect
    def connectToServer(self):
        self.rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.rtspSocket.connect((self.serverAddr, self.serverPort))
        
        except:
            print('Error: Connect to', self.serverAddr, ':', self.serverPort, 'failed')
            sys.exit(0) # exit
    
    # send rtsp request
    def sendRtspRequest(self, requestCode):
        # Setup
        if requestCode == self.SETUP and self.state == self.INIT:
            threading.Thread(target=self.recvRtspReply).start()
            # Update RTSP sequence number.
            self.rtspSeq += 1
            
            # Write the RTSP request to be sent.
            request = 'SETUP ' + self.fileName + ' RTSP/1.0\nCSeq: ' + str(self.rtspSeq) + '\nTransport: RTP/UDP; client_port= ' + str(self.rtpPort)
            
            # Keep track of the sent request.
            self.requestSent = self.SETUP 
        
        # Play
        elif requestCode == self.PLAY and self.state == self.READY:
            self.rtspSeq += 1
            request = 'PLAY ' + self.fileName + ' RTSP/1.0\nCSeq: ' + str(self.rtspSeq) + '\nSession: ' + str(self.sessionId)
            self.requestSent = self.PLAY
        
        # Pause
        elif requestCode == self.PAUSE and self.state == self.PLAYING:
            self.rtspSeq += 1
            request = 'PAUSE ' + self.fileName + ' RTSP/1.0\nCSeq: ' + str(self.rtspSeq) + '\nSession: ' + str(self.sessionId)
            self.requestSent = self.PAUSE
            
        # Teardown
        elif requestCode == self.TEARDOWN and not self.state == self.INIT:
            self.rtspSeq += 1
            request = 'TEARDOWN ' + self.fileName + ' RTSP/1.0\nCSeq: ' + str(self.rtspSeq) + '\nSession: ' + str(self.sessionId)
            self.requestSent = self.TEARDOWN
        
        # Faster
        elif requestCode == self.FASTER and (self.state == self.PLAYING or self.state == self.READY):
            self.rtspSeq += 1
            request = 'FASTER ' + self.fileName + ' RTSP/1.0\nCSeq: ' + str(self.rtspSeq) + '\nSession: ' + str(self.sessionId)
            self.requestSent = self.FASTER
        
        # Slower
        elif requestCode == self.SLOWER and (self.state == self.PLAYING or self.state == self.READY):
            self.rtspSeq += 1
            request = 'SLOWER ' + self.fileName + ' RTSP/1.0\nCSeq: ' + str(self.rtspSeq) + '\nSession: ' + str(self.sessionId) 
            self.requestSent = self.SLOWER

        # Relocate
        elif requestCode == self.RELOCATE and (self.state == self.PLAYING or self.state == self.READY):
            self.rtspSeq += 1
            request = 'RELOCATE ' + str(self.relocatePosition / 100) + ' RTSP/1.0\nCSeq: ' + str(self.rtspSeq) + '\nSession: ' + str(self.sessionId)
            self.requestSent = self.RELOCATE

        else:
            return
        
        self.rtspSocket.send(request.encode())
        
        print('Data:', '\n', request)
    
    # get rtsp reply
    def recvRtspReply(self):
        while True:
            reply = self.rtspSocket.recv(1024)
            
            if reply: 
                self.parseRtspReply(reply.decode("utf-8"))

            # teardown
            if self.requestSent == self.TEARDOWN:
                self.rtspSocket.shutdown(socket.SHUT_RDWR)
                self.rtspSocket.close()
                break
    
    def parseRtspReply(self, data):
        # get line
        lines = str(data).split('\n')
        seqNum = int(lines[1].split(' ')[1])
        
        if seqNum == self.rtspSeq:
            session = int(lines[2].split(' ')[1])
            # set session
            if self.sessionId == 0:
                self.sessionId = session
            
            # check session
            if self.sessionId == session:
                if int(lines[0].split(' ')[1]) == 200:
                    # state setup
                    if self.requestSent == self.SETUP:
                        self.state = self.READY
                        self.openRtpPort()
                    
                    # state play
                    elif self.requestSent == self.PLAY:
                        self.state = self.PLAYING

                    # state pause
                    elif self.requestSent == self.PAUSE:
                        self.state = self.READY
                        self.playEvent.set()

                    # state teardown
                    elif self.requestSent == self.TEARDOWN:
                        self.state = self.INIT
                        self.teardownAcked = 1 
    
    # set rtp port
    def openRtpPort(self):
        self.rtpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # timeout flag
        self.rtpSocket.settimeout(0.5)
        
        try:
            # bind
            self.rtpSocket.bind(("", self.rtpPort))
        except:
            print('Error: bind to', self.rtpPort, 'failed')
            sys.exit(0) # exit


if __name__ == "__main__": 
    # get params
    try:
        serverAddr = sys.argv[1]
        serverPort = sys.argv[2]
        rtpPort = sys.argv[3]
        fileName = sys.argv[4]

    except:
        print ("Error: Wrong params.") 
        sys.exit(0) # exit

    # init ui
    page_main = Ui_MainWindow()
    app = QtWidgets.QApplication(sys.argv)
    page_tmp = QMainWindow()
    page_main.setupUi(page_tmp)

    # init client
    client = Client(serverAddr, serverPort, rtpPort, fileName, page_main)

    # init signal
    page_main.label_title.setText(fileName)
    page_main.listWidget.addItem(fileName)
    page_main.btn_setup.clicked.connect(lambda: client.setupMovie())
    page_main.btn_play.clicked.connect(lambda: client.playMovie())
    page_main.btn_pause.clicked.connect(lambda: client.pauseMovie())
    page_main.btn_teardown.clicked.connect(lambda: client.exitClient())
    page_main.btn_faster.clicked.connect(lambda: client.fasterMovie())
    page_main.btn_slower.clicked.connect(lambda: client.slowerMovie())
    page_main.btn_fullscreen.clicked.connect(lambda: client.setFull())
    page_main.scrollLine.sliderMoved.connect(lambda: client.relocateMovie())

    page_tmp.show()
    sys.exit(app.exec_())