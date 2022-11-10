import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

digits = 267

screen = 1

while screen == 1:
    sequence = ''
    for i in range(digits):
        sequence += ''.join(secrets.choice(alphabet))

    print(sequence)