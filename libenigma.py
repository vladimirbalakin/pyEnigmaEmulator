class Rotor:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'
    shift = 0
    need_to_turn_next_rotor = False

    def __init__(self, shift_):
        self.shift = shift_

    def shift_rotor(self):
        if self.shift > 25:
            self.shift %= 26
            self.need_to_turn_next_rotor = True

    def turn_rotor(self):
        self.shift += 1
        self.shift_rotor()

    def decode(self, letter):
        number_of_letter_in_alphabet = (ord(letter) - ord('a') + self.shift) % 26
        self.shift_rotor()
        return self.cipher[number_of_letter_in_alphabet]

    def encode(self, letter):
        number_of_letter_in_alphabet = (ord(letter) - ord('a') - self.shift) % 26
        self.shift_rotor()
        return self.cipher[number_of_letter_in_alphabet]


class Reflector:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'fvpjiaoyedrzxwgctkuqsbnmhl'

    def decode(self, letter):
        number_of_letter_in_alphabet = ord(letter) - ord('a')
        return self.cipher[number_of_letter_in_alphabet]


class Plugboard:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'qbcdefghijklmnoparstuvwxyz'

    def decode(self, letter):
        number_of_letter_in_alphabet = ord(letter) - ord('a')
        return self.cipher[number_of_letter_in_alphabet]
