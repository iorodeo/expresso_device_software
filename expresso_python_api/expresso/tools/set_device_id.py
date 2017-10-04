from __future__ import print_function
from expresso.libs.expresso_serial import ExpressoSerial
import sys

port = sys.argv[1]
number = int(sys.argv[2])

print()
print('setting device ID')
print('  port    = {0}'.format(port))
print('  number  = {0}'.format(number))
print()

dev = ExpressoSerial(port,checkId=False)
dev.setDeviceId(number)

print('fetching device ID')
dev_id = dev.getDeviceId()
print('  device ID =  {0}'.format(dev_id))
print()






