import string

import string


def alphabet_position(letter):

    return int(string.ascii_lowercase.index(letter))


def rotate_character(char, rot):
    index = alphabet_position(char)
    y = index + rot

    if y >= 25:
        if char.islower() is True:
            return string.ascii_lowercase[y % 26]
        if char.isupper() is True:
            return string.ascii_uppercase[y % 26]
    elif y <= 24:
        if char.islower() is True:
            return string.ascii_lowercase[y]
        elif char.isupper() is True:
            return string.ascii_uppercase[y]
