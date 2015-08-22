
def mk_test_hex(n_chars, filler='badbeefdeadfeed'):
    assert len(filler) == 15
    assert n_chars <= 256
    return ''.join([
        (hex(i/16)[2] if i % 16 == 0 else filler[(i%16)-1]) 
            for i in range(n_chars)
    ])
