def alphabet_position(letter):
    alphabet ="abcdefghijklmnopqrstuvwxyz" #Lists alphabet for a key
    lower_letter = letter.lower()   #Makes any input lowercase.
    return alphabet.index(lower_letter) #Returns the position of input as a number.

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        a = alphabet_position(char)
        a = str((a + rot) % 26)            #needs modulo
        a = (alphabet[a])
        if char.isupper():
            a = a.title()
        return a
    else:
       return char