"""
File: caesar.py
Name: Leticia
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program presents the caesar cipher concept allowing
    users enter a secret number and a ciphered string to decode.
    """
    n = int(input("Secret number: "))
    new_index = shift_index(n)
    ciphered_string = input("What's the ciphered string?").upper()
    deciphered_string = decipher(ciphered_string, new_index)
    print("The deciphered string is:", deciphered_string)


def shift_index(n):
    ans = ""
    if n < 0 or n > 25:
        return 'Error'
    else:
        ans += ALPHABET[(26-n):]+ALPHABET[:(26-n)]
    return ans


def decipher(ciphered_string, new_index):
    deciphered_string = ""
    for ch in ciphered_string:
        if ch in ALPHABET:
            original_index = (new_index.find(ch) + len(ALPHABET)) % len(ALPHABET)
            original_ch = ALPHABET[original_index]
            deciphered_string += original_ch
        else:
            deciphered_string += ch
            # Non-alphabetic characters input are retained in the deciphered string
    return deciphered_string


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
