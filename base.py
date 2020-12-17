from libenigma import Rotor, Reflector, Plugboard

rotors = [Rotor(0) for i in range(3)]
refl = Reflector
plug = Plugboard


def forward(h):
    for i in range(len(rotors)):
        h = rotors[i].decode(h)
    return h


def backward(h):
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
        # if rotors[0].need_to_turn_next_rotor and i < len(rotors) - 1:
        #    rotors[i + 1].turn_rotor()
        #    rotors[i].need_to_turn_next_rotor = False
        h = plug.decode(plug, h)
        h = forward(h)
        h = refl.decode(refl, h)
        h = backward(h)
        h = plug.decode(plug, h)
        coded += h
    return coded
