from __future__ import absolute_import, division, print_function
from six import integer_types

from nacl import exceptions as exc
from nacl._sodium import ffi, lib
from nacl.exceptions import ensure

crypto_stream_chacha20_KEYBYTES = lib.crypto_stream_chacha20_keybytes()
crypto_stream_chacha20_NONCEBYTES = lib.crypto_stream_chacha20_noncebytes()
crypto_stream_chacha20_MESSAGEBYTES_MAX = lib.crypto_stream_chacha20_messagebytes_max()
crypto_stream_chacha20_ietf_KEYBYTES = lib.crypto_stream_chacha20_ietf_keybytes()
crypto_stream_chacha20_ietf_NONCEBYTES = lib.crypto_stream_chacha20_ietf_noncebytes()
crypto_stream_chacha20_ietf_MESSAGEBYTES = lib.crypto_stream_chacha20_ietf_messagebytes_max()

def crypto_stream_chacha20_keygen():
    outbuf = ffi.new("unsigned char[]", crypto_stream_chacha20_KEYBYTES)
    lib.crypto_stream_chacha20_keygen(outbuf)
    return ffi.buffer(outbuf, crypto_stream_chacha20_KEYBYTES)[:]

def crypto_stream_chacha20_xor(message, nonce, key):
    ensure(isinstance(message, bytes), raising=exc.TypeError)
    ensure(isinstance(nonce, bytes), raising=exc.TypeError)
    ensure(isinstance(key, bytes), raising=exc.TypeError)

    outlen = len(message)
    outbuf = ffi.new("unsigned char[]", outlen)
    ret = lib.crypto_stream_chacha20_xor(outbuf, message, outlen, nonce, key)

    ensure(ret == 0, 'Unexpected failure in key derivation',
           raising=exc.RuntimeError)

    return ffi.buffer(outbuf, outlen)[:]

def crypto_stream_chacha20_xor_ic(message, nonce, ic, key):
    ensure(isinstance(message, bytes), raising=exc.TypeError)
    ensure(isinstance(nonce, bytes), raising=exc.TypeError)
    ensure(isinstance(key, bytes), raising=exc.TypeError)
    ensure(isinstance(ic, integer_types), raising=exc.TypeError)
    
    outlen = len(message)
    outbuf = ffi.new("unsigned char[]", outlen)
    
    ret = lib.crypto_stream_chacha20_xor_ic(outbuf, message, outlen, nonce, ic,
                                            key)
    ensure(ret == 0, 'Unexpected failure in key derivation',
           raising=exc.RuntimeError)
    return ffi.buffer(outbuf, outlen)[:]