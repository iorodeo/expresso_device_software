from __future__ import print_function
import serial
import time
import numpy

ARRAY_SZ = 768
NUM_CHANNELS = 5
MAX_ERROR_CNT = 10

# Serial Command Ids
CMD_SET_MODE = 0
CMD_GET_MODE = 1
CMD_GET_CHANNEL = 2
CMD_GET_LEVEL = 3
CMD_GET_LEVELS = 4
CMD_GET_PIXEL_DATA = 5
CMD_GET_WORKING_BUFFER = 6
CMD_GET_DEVICE_ID = 7
CMD_GET_DEVICE_NUMBER = 8
CMD_SET_DEVICE_NUMBER = 9
CMD_UNSET_NORM_CONST = 10
CMD_SET_NORM_CONST_FROM_BUFFER = 11
CMD_SET_NORM_CONST_FROM_FLASK = 12
CMD_SET_CHANNEL = 13

# Operating modes
MODE_STOPPED = 0
MODE_SINGLE_CHANNEL = 1
MODE_MULTI_CHANNEL = 2

SUCCESS_CHR = '0' 

class ArrayReader(serial.Serial):

    def __init__(self, port):
        super(ArrayReader,self).__init__(port, baudrate=3000000, timeout=1)
        time.sleep(2.0)
        self.emptyBuffer()

    def getMode(self):
        """
        Returns the operating mode of the device
        """
        cmd = self.makeCommand(CMD_GET_MODE)
        self.write(cmd)
        line = self.readline()
        if line.startswith(SUCCESS_CHR):
            line = line.rsplit()
            mode = int(line[1])
            return mode
        else:
            raise IOError, 'unable to get mode'

    def getChannel(self):
        """
        Returns the single channel mode channel setting from the device.
        """
        cmd = self.makeCommand(CMD_GET_CHANNEL)
        self.write(cmd)
        line = self.readline()
        if not line.startswith(SUCCESS_CHR):
            raise IOError, 'unable to get channel'
        line = line.rsplit()
        chan = int(line[1])
        return chan

    def setMode(self, *args):
        """
        Sets the operating mode of the device.  For single channel mode can also set the 
        current channel setting. 
        """
        if len(args) ==  1:
            mode = args[0]
            cmd = self.makeCommand(CMD_SET_MODE, mode)
        else:
            mode = args[0]
            chan = args[1]
            cmd = self.makeCommand(CMD_SET_MODE, mode, chan)
        self.write(cmd)
        line = self.readline()
        if not line.startswith(SUCCESS_CHR):
            raise IOError, 'unable to set mode' 

    def setModeStopped(self):
        """
        Sets the operating mode of the device to stopped.
        """
        self.setMode(MODE_STOPPED)

    def setModeSingleChannel(self,chan=None):
        """
        Sets the operating mode of the device to single channel.
        """
        if chan == None:
            self.setMode(MODE_SINGLE_CHANNEL)
        else:
            self.setMode(MODE_SINGLE_CHANNEL, chan)

    def setModeMultiChannel(self):
        """
        Sets the mode of the device to multi channel
        """
        self.setMode(MODE_MULTI_CHANNEL)

    def setChannel(self,chan):
        """
        Sets the device's single channel mode channel setting. 
        """
        cmd = self.makeCommand(CMD_SET_CHANNEL,chan)
        self.write(cmd)
        line=self.readline()
        if not line.startswith(SUCCESS_CHR):
            raise IOError, 'unable to set channel' 

    def getPixelData(self):
        """
        Returns the fluid level and the array of pixel values from the device.
        """
        cmd = self.makeCommand(CMD_GET_PIXEL_DATA)
        self.write(cmd)

        line=self.readline()
        if not line.startswith(SUCCESS_CHR):
            raise IOError, 'unable to read pixel data'
        line = line.split()
        level = float(line[1])

        data = []
        errorCnt = 0
        while len(data) < ARRAY_SZ:
            byte = self.read(1)
            try:
                data.append(ord(byte))
            except TypeError, e:
                errorCnt += 1
            if errorCnt >= MAX_ERROR_CNT:
                raise IOError, 'error reading pixel values'
        return level, numpy.array(data)

    def getLevel(self,chan=None):
        """
        Get the level for the specified channel. If chan=None then the level
        for the currently selected channel (in single channel mode)  is returned.  
        Otherwise the level for the channel specified by chan is returned. 
        """
        chan = self.getChannel()
        cmd = self.makeCommand(CMD_GET_LEVEL,chan)
        self.write(cmd)
        line = self.readline()
        if not line.startswith(SUCCESS_CHR):
            raise IOError, 'unable to get level'
        line = line.rsplit()
        level = float(line[1])
        return level
    
    def getLevels(self):
        """
        Get levels for all channels. 
        """
        cmd = self.makeCommand(CMD_GET_LEVELS)
        self.write(cmd)
        line = self.readline()
        if not line.startswith(SUCCESS_CHR):
            raise IOError, 'unable to get levels'
        line = line.rsplit()
        levels = [float(x) for x in line]
        return levels

    def emptyBuffer(self):
        """
        Empty the serial input buffer.
        """
        while self.inWaiting() > 0:
            self.read()

    def makeCommand(self,*args):
        """
        Packs arguments into a command string suitable for sending to the 
        device.
        """
        args = map(str,args)
        cmd = ','.join(args)
        cmd =  '[{0}]'.format(cmd)
        return cmd

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    dev = ArrayReader('/dev/ttyACM0')

    if 0:
        mode = dev.getMode()
        print('mode', mode)
    if 0:
        chan = dev.getChannel()
        print('channel', chan)
    if 0:
        mode = dev.getMode()
        print('original mode:', mode)

        print('setting single channel mode')
        dev.setMode(MODE_SINGLE_CHANNEL)
        mode = dev.getMode()
        chan = dev.getChannel()
        print('mode = ', mode)
        print('chan =', chan)

        print('setting single channel mode + channel = 1')
        dev.setMode(MODE_SINGLE_CHANNEL, 1)
        mode = dev.getMode()
        chan = dev.getChannel()
        print('mode = ', mode)
        print('chan =', chan)

        print('setting single channel mode + channel = 0')
        dev.setMode(MODE_SINGLE_CHANNEL, 0)
        mode = dev.getMode()
        chan = dev.getChannel()
        print('mode = ', mode)
        print('chan =', chan)

        print('setting multi channel mode')
        dev.setMode(MODE_MULTI_CHANNEL)
        mode = dev.getMode()
        print('mode = ', mode)

        print('returning to mode stopped')
        dev.setMode(MODE_STOPPED)
        mode = dev.getMode()
        print('mode = ', mode)

    if 0:
        for i in range(NUM_CHANNELS) + [0]:
            print('setting channel to {0}'.format(i))
            dev.setChannel(i)
            chan = dev.getChannel()
            print('chan = {0}'.format(chan))

    if 0:
        dev.setMode(MODE_SINGLE_CHANNEL)
        mode = dev.getMode()
        print('mode = ', mode)

        level, data = dev.getPixelData()
        print(level)
        print(data.shape)

        dev.setMode(MODE_STOPPED)
        mode = dev.getMode()
        print('mode = ', mode)

    if 0:

        dev.setMode(MODE_SINGLE_CHANNEL,0)
        mode = dev.getMode()
        chan = dev.getChannel()
        print('mode = ', mode)
        print('chan =', chan)

        level = dev.getLevel()
        print('level = ', level)

        dev.setMode(MODE_STOPPED)
        mode = dev.getMode()
        print('mode = ', mode)

    if 1:
        dev.setMode(MODE_MULTI_CHANNEL)
        mode = dev.getMode()
        print('mode = ', mode)

        levels = dev.getLevels()
        print('levels', levels)
        
        dev.setMode(MODE_STOPPED)
        mode = dev.getMode()
        print('mode = ', mode)




