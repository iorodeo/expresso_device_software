import time
import scipy
import matplotlib.pylab as pylab
from array_reader import ArrayReader
import sys 
reader = ArrayReader(port='/dev/ttyACM0',baudrate=3000000,timeout=1)

#def dgaussian(x,sigma):
#    value = -x/(scipy.sqrt(2*scipy.pi)*sigma**3)
#    value *= scipy.exp((-x**2)/(2*sigma**2))
#    return value 
#
#def dgaussian_filt_coeff(w):
#    sigma = float(w)/4
#    n = int(w)/2
#    x = scipy.arange(-n,n+1,dtype=scipy.float64)
#    y = dgaussian(x,sigma)
#    return y
#
#filt_coeff = dgaussian_filt_coeff(21)
#pylab.plot(filt_coeff)
#pylab.show()

testSingleChannel = True
testMultiChannel = False
CHNL_1 = 0
CHNL_2 = 1
CHNL_3 = 2
CHNL_4 = 3
CHNL_5 = 4
pylab.ion()

i = 0
config = { 
        'modeSingleChannel' : True,
        'modeMultiChannel'  : False,
        'channel'           : 1,
        } 
while 1:
    # Single-channel mode
    if config['modeSingleChannel']:
        channel = config['channel']
        if i==0:
            rsp = reader.setMode(1,channel)
        t0 = time.time()
        level, data = reader.getPixelData()
        t1 = time.time()
        dt = t1-t0
        print(dt)

        if data is None:
            continue
        print i, ": ", level
        #edge_data = scipy.convolve(data,filt_coeff,mode='valid')
        #edge_data = 20*edge_data
        if i==0:
            pylab.figure(1)
            #pylab.subplot(211)
            h_line, = pylab.plot(data,linewidth=2)
            h_level, = pylab.plot([0],[0],'ro')
            h_level.set_visible(False)
            pylab.grid('on')
            pylab.ylim(0,256)
            #pylab.ylim(100,150)
            pylab.xlim(0,768)
            pylab.xlabel('pixel')
            pylab.ylabel('intensity')
            #pylab.subplot(212)
            #h_edge, = pylab.plot(edge_data,linewidth=2)
        else:
            h_line.set_ydata(data)
            #h_edge.set_ydata(edge_data)
            if level >= 0:
                level = int(level)
                h_level.set_xdata([level])
                h_level.set_ydata([data[level]])
                h_level.set_visible(True)
            else:
                h_level.set_visible(False)
        pylab.draw()

    # Multi-channel mode
    if config['modeMultiChannel']:
        if i==0:
            rsp = reader.setMode(2)
        levels = reader.getLevels()
        print i, ": ", levels

    i += 1
