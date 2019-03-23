class Caesar:


    def __init__(self):
        self.message = input("Enter message ")
        self.rotation = int(input("Enter rotation amount"))

    def alphabet_position(self):
        input = self.message

message = Caesar()
print(message.alphabet_position())