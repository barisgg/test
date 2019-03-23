import string


class Caesar:

    def __init__(self):
        self.lower = list(string.ascii_lowercase)
        self.upper = list(string.ascii_uppercase)
        self.punctuation = string.punctuation
        self.rotate_character()

def alphabet_position(letter):
    x = letter.lower()
    alphabet = string.ascii_lowercase
    return int(alphabet.index(x))

def rotate_character(self):
        
        rot = int(input("Enter rotation amount: "))
        
        while True:
            x = ''
            message = input("Enter message: ")
            for l in message:
                try:
                    temp = ''
                    temp += l

                    if l == " " or self.punctuation.find(temp) is True:
                        x += l

                    if l.isupper() is True:
                        index = self.alphabet_position(l)
                        letter = self.upper[index + rot]
                        x += letter
                    if l.islower() is True:
                        index = self.alphabet_position(l)
                        letter = self.lower[index + rot]
                        x += letter

                except IndexError:
                    if l.isupper() is True:
                        index = self.alphabet_position(l)
                        letter = self.upper[(index+rot) % 26]
                        x += letter
                    if l.islower() is True:
                        index = self.alphabet_position(l)
                        letter = self.lower[(index+rot) % 26]
                        x += letter
            print(x)
            
            if input("Do you have another message (yes/no): ") == 'no':
                return False
            else:
                continue
        

Caesar()
