from __future__ import print_function
import math 

class LowpassFilter(object):

    def __init__(self,freq_cutoff):
        self.value = None
        self.freq_cutoff = freq_cutoff 

    def update(self,data,dt):
        if self.value is not None:
            tau = 1.0/(2*math.pi*self.freq_cutoff)
            alpha = dt/(dt  + tau)
            self.value = (1-alpha)*self.value + alpha*data
        else:
            self.value = data

