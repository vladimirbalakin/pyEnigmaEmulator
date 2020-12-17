from libenigma import Rotor, Reflector, Plugboard

rotors = [Rotor(0) for i in range(10)]
reflector = Reflector
plugboard = Plugboard


def forward(h):
    """emulate electric signal from first rotor to reflector"""
    for i in range(len(rotors)):
        h = rotors[i].decode(h)
    return h


def backward(h):
    """emulate electric signal from reflector to first rotor"""
    for i in range(len(rotors)):
        h = rotors[i].encode(h)
    return h


def decode(word):
    """word must in lower case. function return coded word by enigma."""
    coded = ""
    for i in word:
        if not(ord('a') <= ord(i) <= ord('z')):
            coded += i
            continue
        h = i
        rotors[0].turn_rotor()
        for j in range(len(rotors)):
            if rotors[j].need_to_turn_next_rotor and j < len(rotors) - 1:
                rotors[j + 1].turn_rotor()
                rotors[j].need_to_turn_next_rotor = False
            else:
                break
        h = plugboard.decode(plugboard, h)
        h = forward(h)
        h = reflector.decode(reflector, h)
        h = backward(h)
        h = plugboard.decode(plugboard, h)
        coded += h
    return coded
