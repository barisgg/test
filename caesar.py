import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    message = ''
    x = list(string.punctuation)
    for char in text:
        try:
            if char == " ":
                message += char
            else:
                message += rotate_character(char, rot)
        except ValueError:
            message += char
    return message


def main():
    text = input('Type a message: ')
    rot =  int(input('Rotate by: '))
    print(encrypt(text,rot))

if __name__ == "__main__":
    main()
