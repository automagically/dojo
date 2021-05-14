
from coder import Coder

def test_key_is_alphabet_decode_msg():
    key = 'abcdefghijklmnopqrstuvwxyz'
    coder = Coder(key)
    ciphertext = 'test'
    plaintext = 'test'
    assert coder.decrypt(ciphertext) == plaintext

def test_decode_msg_a_equals_b():
    key = 'bacdefghijklmnopqrstuvwxyz'
    coder = Coder(key)
    ciphertext = 'abnbnb'
    plaintext = 'banana'
    assert coder.decrypt(ciphertext) == plaintext

def test_decode_msg_a_equals_at():
    key = '@bcdefghijklmnopqrstuvwxyz'
    coder = Coder(key)
    plaintext = 'banana'
    ciphertext = 'b@n@n@'
    assert coder.decrypt(ciphertext) == plaintext

def test_decode_msg_random_key():
    #     'abcdefghijklmnopqrstuvwxyz'
    key = '!)"(£*%&><@abcdefghijklmno'
    coder = Coder(key)
    plaintext = 'calendario'
    ciphertext = '"!a£c(!g>d'
    assert coder.decrypt(ciphertext) == plaintext

def test_code_msg_no_changes():
    key = 'abcdefghijklmnopqrstuvwxyz'
    coder = Coder(key)
    ciphertext = 'banana'
    plaintext = 'banana'
    assert coder.crypt(plaintext) == ciphertext

def test_code_msg_one_letter_different():
    key = 'abcdefghijklmnopq$stuvwxyz'
    coder = Coder(key)
    plaintext = 'door'
    ciphertext = 'doo$'
    assert coder.crypt(plaintext) == ciphertext

def test_code_msg_random_key():
    key = '!)"(£*%&><@abcdefghijklmno'
    coder = Coder(key)
    plaintext = 'calendario'
    ciphertext = '"!a£c(!g>d'
    assert coder.crypt(plaintext) == ciphertext

def test_code_msg_ceasar_chiper():
    key = 'bcdefghijklmnopqrstuvwxyza'
    coder = Coder(key)
    ciphertext = 'cbobob'
    plaintext = 'banana'
    assert coder.crypt(plaintext) == ciphertext