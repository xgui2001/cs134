"""The basis for building objects that can encode and decode messages.

   Typical usage:
   >>> coder = CaesarCipher(7)  # any particular cipher
   >>> coder.encode('Hello, world.')
   'OLSSVDVYSK'
   >>> coder.decode('OLSSVDVYSK')
   'HELLOWORLD'
"""
__all__ = [ 'CaesarCipher', 'Cipher','Rot13','Vigenere' ]


class Cipher(object):
    """The base class/interface for all Cipher classes."""

    __slots__ = []

    def __init__(self):
        """Trivial base class initialization."""
        pass

    def encode(self,sourceString):
        """Placeholder for encode method in subclasses."""
        return sourceString

    def decode(self,sourceString):
        """Placeholder for encode method in subclasses."""
        return sourceString

    # here down: private utility methods, available to subclasses:
    def _normalize(self,sourceString):
        """Normalize by eliminating non-letters, then upper-casing.
        >>> coder = Cipher()
        >>> coder._normalize('Hello, world.')
        'HELLOWORLD'
        """
        return ''.join([c.upper() for c in sourceString if c.isalpha()])

    def _a2i(self,a):
        assert a.isalpha() and len(a) == 1
        return (ord(a) & 31)-1

    def _i2a(self,i):
        return 'abcdefghijklmnopqrstuvwxyz'[i%26]

    def _i2A(self,i):
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i%26]

    def _rotate(self, c, n):
        """Rotate letters n steps around alphabet; other chars unchanged.

        >>> coder = Cipher()
        >>> coder._rotate('m',4)
        'q'
        >>> coder._rotate('!',4)
        '!'
        """
        assert len(c) == 1
        if c.isalpha():
            newCode = (self._a2i(c)+n)%26
            c = self._i2a(newCode) if c.islower() else self._i2A(newCode)
        return c

    def __str__(self):
        """Convert cipher to a string."""
        return "<a simple cipher>"

    def __repr__(self):
        """Generate representation of Cipher."""
        return "Cipher()"

class CaesarCipher(Cipher):
    """Encode messages using rotation."""
    __slots__ = ['_n']

    def __init__(self,n):
        """Construct a rotation-by-n encode/decode."""
        super().__init__()
        self._n = n%26

    def encode(self,sourceString):
        """Encode by rotating characters of sourceString forward
        by a constant."""
        coded = ''
        for c in self._normalize(sourceString):
            coded += self._rotate(c,self._n)  # encoding: map forward
        return coded

    def decode(self,sourceString):
        """Decode by rotating characters of sourceString backward by a constant.

        >>> coder = CaesarCipher(15)
        >>> plaintext = coder.decode(open('story.txt').read())
        >>> plaintext.count('AMHERST')
        4
        """
        coded = ''
        for c in self._normalize(sourceString):
            coded += self._rotate(c,-self._n) # decoding: map backward
        return coded

    def __repr__(self):
        """Representation of the CaesarCipher."""
        return "CaesarCipher({})".format(n)

class Rot13(CaesarCipher):
    """Rotating messages by 13 characters."""

    def __init__(self):
        """Calls its superclass initializer with a fixed value of 13.

        >>> code2 = 'How are you?'
        >>> coder = Rot13()
        >>> coder.encode(code2)
        'Ubj ner lbh?'
        """
        super().__init__(13)

    def _normalize(self, sourceString):
        """Normalizing without remmoving punctation or change case."""
        return sourceString

    def __repr__(self):
        """Representation of Rot13."""
        return "Rot13()"

class Vigenere(Cipher):
    """Encode messages using a set amount of rotation based on a key.""" 
    __slots__ = ['_key']

    def __init__(self,key):
        """Normalize the key to all uppercase letters.

        >>> code = open('cia.txt').read()[:51]
        >>> coder = Vigenere('SANBORN')
        >>> code
        'KAACCIAKKEZDKBKIFBGTHDPGVFVYGCNUSUBFTUFUIBMNQTCWPAA'
        >>> coder.decode(code)
        'SANBORNSKRYPTOSISASCULPTURELOCATEDONTHEGROUNDSOFCIA'
        >>> coder
        Vigenere('SANBORN')
        """
        super().__init__()
        self._key = self._normalize(key)

    def encode(self, sourceString):
        """Encode by rotating characters of sourceString forward based on values corresponding to alphabets in key.

        >>> vCoder = Vigenere('Williams')
        >>> vCoder.encode('purple cows')
        'LCCATEOGSA'
        """
        normalized = self._normalize(sourceString) # normalize the sourceString
        shift = []
        shiftLength = len(self._key)
        counter = 0
        encoded = ''
        for k in self._key:
            shift.append(self._a2i(k)) # compile the values corresponding to alphabets in the key
        for n in normalized:
            e = self._rotate(n, shift[counter%shiftLength]) # rotate the normalized sourceString forward by the compiled values of key
            encoded += e
            counter += 1
        return encoded
            
    def decode(self,sourceString):
        """Decode by by rotating characters of sourceString backward based on values corresponding to alphabets in key.

        >>> vCoder = Vigenere('Williams')
        >>> vCoder.encode('purple cows')
        'LCCATEOGSA'
        >>> vCoder.decode('lccateogsa')
        'PURPLECOWS'
        """
        normalized = self._normalize(sourceString)
        shift = []
        shiftLength = len(self._key)
        counter = 0
        decoded = ''
        for k in self._key:
            shift.append(self._a2i(k))
        for n in normalized:
            e = self._rotate(n, -shift[counter%shiftLength]) # rotate the normalized sourceString backward by the compiled values of key
            decoded += e
            counter += 1
        return decoded

    def __repr__(self):
        """Representation of the class Vigenere."""
        return "Vigenere('{}')".format(self._key)

          
def test():
    """Perform doctests."""
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test()
    coder = CaesarCipher(7) # use other ciphers!
    coder = Rot13()
    coder = Vigenere('Williams')
    encoding = coder.encode('Hello, world')
    decoding = coder.decode(encoding)
    #print(decoding)
