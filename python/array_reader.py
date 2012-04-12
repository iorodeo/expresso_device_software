import time
import serial
import struct
import numpy
import sys

NUM_CHANNELS = 5
ARRAY_SZ = 768
INWAITING_DT = 0.05
BUF_EMPTY_NUM = 3
BUF_EMPTY_DT = 0.01
CMD_SET_MODE = 0
CMD_GET_MODE = 1
CMD_GET_CHANNEL = 2
CMD_GET_LEVEL = 3
CMD_GET_LEVELS = 4
CMD_GET_PIXEL_DATA = 5
MODE_STOPPED = 0
MODE_SINGLE_CHANNEL = 1
MODE_MULTI_CHANNEL = 2

class ArrayReader(serial.Serial):

    def __init__(self,**kwargs):
        super(ArrayReader,self).__init__(**kwargs)
        time.sleep(2.0)
        print "Initializing..."
        self.emptyBuffer()

    def setMode(self, *args):
        mode = args[0]
        if (mode == MODE_SINGLE_CHANNEL):
            cmd = self.makeCommand(CMD_SET_MODE,mode,args[1])
        else:
            cmd = self.makeCommand(CMD_SET_MODE,mode)
        self.write(cmd)
        if (self.readline().startswith('0')):
            print "Mode set"
            return 0
        else:
            print "Could not set mode"
            sys.exit()

    def getMode(self):
        cmd = self.makeCommand(CMD_GET_MODE)
        self.write(cmd)

    def getChannel(self):
        cmd = self.makeCommand(CMD_GET_CHANNEL)
        self.write(cmd)
        line=self.readline()
        if (line.startswith('0')):
            chan = line.split(' ',1)[1]
            chan = int(chan.rsplit()[0])
        else:
            chan = -1
            print "Could not get channel"
        return chan

    def getPixelData(self):
        cmd = self.makeCommand(CMD_GET_PIXEL_DATA)
        self.write(cmd)

        line=self.readline()
        line = line.split(' ')
        rsp = line[0]
        level = float(line[1])

        data = []
        # TODO: Error checking
        while len(data) < ARRAY_SZ:
            byte = self.read(1)
            data.append(ord(byte))
        return level, numpy.array(data)

    def getLevel(self):
        chan = self.getChannel()
        cmd = self.makeCommand(CMD_GET_LEVEL,chan)
        self.write(cmd)
        line=self.readline()
        if (line.startswith('0')):
            level = line.split(' ',1)[1]
            level = float(level.rsplit()[0])
        else:
            level = -1
            print "Could not get level"
        return level
    
    def getLevels(self):
        cmd = self.makeCommand(CMD_GET_LEVELS)
        self.write(cmd)
        line=self.readline()
        if (line.startswith('0')):
            levels = line.split(' ',1)[1]
        else:
            levels = -1
            print "Could not get levels"
        levels = levels.rsplit()
        try:
            levels = [float(x) for x in levels]
        except ValueError:
            levels = None
        return levels

    def emptyBuffer(self):
        """
        Empty the serial input buffer.
        """
        #for i in range(0,BUF_EMPTY_NUM):
        #    self.flushInput()
        #    time.sleep(BUF_EMPTY_DT)
        while self.inWaiting() > 0:
            self.read()

    def getFakeData(self):
        fakeData = 800*numpy.ones((ARRAY_SZ,))
        fakeData[:200] = 0.0*fakeData[:200]
        return fakeData

    def makeCommand(self,*args):
        cmd='\['
        cnt=1
        for a in args:
            cmd+=str(a)
            if cnt < len(args):
                cnt+=1
                cmd+=','
        cmd+='\]'
        return cmd
