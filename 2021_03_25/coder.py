ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class Coder():
    def __init__(self, key):
        self.key = key
 
    def decrypt(self, msg):
        return self._encode(self.key, ALPHABET, msg)
    
    def crypt(self, msg):
        return self._encode(ALPHABET, self.key, msg)

    def _encode(self, alphabet, key, msg):
        result = ''
        mapping = dict(zip(alphabet, key))
        for caracter in msg:
            result += mapping.get(caracter)
        return result
