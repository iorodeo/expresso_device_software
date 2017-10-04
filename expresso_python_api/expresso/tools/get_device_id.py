from __future__ import print_function
from expresso.libs.expresso_serial import ExpressoSerial
import sys

port = sys.argv[1]
dev = ExpressoSerial(port,checkId=False)

print()
print('fetching device ID')
dev_id = dev.getDeviceId()
print('  device ID =  {0}'.format(dev_id))
print()






