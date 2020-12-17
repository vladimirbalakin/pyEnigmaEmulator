from base import decode


def RUN():
    word = input("Type you message: ").lower()
    coded = decode(word)
    print("Your secret message : ", coded)


if __name__ == '__main__':
    RUN()
