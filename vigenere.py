import string
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    message = ''
    rot_list = []
    stop = 0
    x = 0
    for char in key:
        rot_list.append(alphabet_position(char))
    while stop < len(text):
        for char in text:

            if x >= len(rot_list):
                x = 0

            if string.punctuation.find(char) > -1:
                message += char
            elif char == " ":
                message += char
            else:
                message += rotate_character(char, rot_list[x])
                stop += 1
                x += 1

        return message

def main():
    text = input('Type a message: ')
    key = input('Encryption key: ')
    print(encrypt(text, key))


if __name__ == "__main__":
    main()


def encrypt(text, key):
    message = ''
    rot_list = []
    x = 0

    for char in text:
        while len(rot_list) < len(key):
            for chars in key:
                rot_list.append(alphabet_position(chars))
        if x > len(rot_list)-1:
            x = 0

        if char in string.ascii_letters is False:
            message += char
        else:
            message += rotate_character(char, rot_list[x])
            x += 1
    return message
