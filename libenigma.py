class Rotor:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'
    shift = 0
    need_to_turn_next_rotor = False

    def __init__(self, shift_):
        self.shift = shift_

    def shift_rotor(self):
        self.shift += 1
        if self.shift > 25:
            self.shift %= 26
            self.need_to_turn_next_rotor = True

    def decode(self, letter):
        number_of_letter_in_alphabet = ord(letter) - 'a'
        self.shift_rotor()
        return self.cipher[number_of_letter_in_alphabet]


class Reflector:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'fvpjiaoyedrzxwgctkuqsbnmhl'

    def decode(self, letter):
        number_of_letter_in_alphabet = ord(letter) - 'a'
        return self.cipher[number_of_letter_in_alphabet]


class Plugboard:
    normal, cipher = 'abcdefghijklmnopqrstuvwxyz', 'qbcdefghijklmnoparstuvwxyz'

    def decode(self, letter):
        number_of_letter_in_alphabet = ord(letter) - 'a'
        return self.cipher[number_of_letter_in_alphabet]
