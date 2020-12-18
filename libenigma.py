class Rotor:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'
    shift = 0
    need_to_turn_next_rotor = False

    def __init__(self, shift_):
        self.shift = shift_

    def shift_rotor(self) -> None:
        """Check that rotor's shift is correct or if it is wrong fixed it."""
        if self.shift > 25:
            self.shift %= 26
            self.need_to_turn_next_rotor = True

    def turn_rotor(self) -> None:
        """It turn current rotor."""
        self.shift += 1
        self.shift_rotor()

    def decode(self, letter) -> str:
        """Emulate electric signal in current rotor. Direction of signal - to reflector."""
        number_of_letter_in_alphabet = (ord(letter) - ord('a') + self.shift) % 26
        self.shift_rotor()
        return self.cipher[number_of_letter_in_alphabet]

    def encode(self, letter) -> str:
        """Emulate electric signal in current rotor. Direction of signal - from reflector."""
        number_of_letter_in_alphabet = (ord(letter) - ord('a') - self.shift) % 26
        self.shift_rotor()
        return self.cipher[number_of_letter_in_alphabet]


class Reflector:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'fvpjiaoyedrzxwgctkuqsbnmhl'

    def decode(self, letter) -> str:
        number_of_letter_in_alphabet = ord(letter) - ord('a')
        return self.cipher[number_of_letter_in_alphabet]


class Plugboard:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'qbcdefghijklmnoparstuvwxyz'

    def decode(self, letter) -> str:
        number_of_letter_in_alphabet = ord(letter) - ord('a')
        return self.cipher[number_of_letter_in_alphabet]


class Enigma:
    reflector = Reflector
    plugboard = Plugboard

    def __init__(self, n, shifts):
        self.rotors = []
        for i in range(n):
            self.rotors.append(Rotor(shifts[i]))

    def forward(self, h):
        """emulate electric signal from first rotor to reflector"""
        for i in range(len(self.rotors)):
            h = self.rotors[i].decode(h)
        return h

    def backward(self, h):
        """emulate electric signal from reflector to first rotor"""
        for i in range(len(self.rotors)):
            h = self.rotors[i].encode(h)
        return h

    def decode(self, word):
        """word must in lower case. function return coded word by enigma."""
        coded = ""
        for i in word:
            if not (ord('a') <= ord(i) <= ord('z')):
                coded += i
                continue
            h = i
            self.rotors[0].turn_rotor()
            for j in range(len(self.rotors)):
                if self.rotors[j].need_to_turn_next_rotor and j < len(self.rotors) - 1:
                    self.rotors[j + 1].turn_rotor()
                    self.rotors[j].need_to_turn_next_rotor = False
                else:
                    break
            h = self.plugboard.decode(self.plugboard, h)
            h = self.forward(h)
            h = self.reflector.decode(self.reflector, h)
            h = self.backward(h)
            h = self.plugboard.decode(self.plugboard, h)
            coded += h
        return coded
