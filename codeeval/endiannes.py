__author__ = 'Hinshitsu-IT'

import sys
if sys.byteorder:
    print('LittleEndian')
else:
    print('BigEndian')