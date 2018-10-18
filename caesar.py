import string
from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    new_text = ""
    for char in text:
        new_char = rotate_character(char, rot)
        new_text += str(new_char)

    return new_text

def main():
    input_text = ("Hello World!")
    input_rot = 5

    print(encrypt(input_text, input_rot))

if __name__ == "__main__":
     main()