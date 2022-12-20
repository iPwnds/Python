import secrets
import string
import pyfiglet
import colorama

colorama.init()

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

digits = 236

screen = 10000

while screen > 0:
    sequence = ''
    for i in range(digits):
        sequence += ''.join(secrets.choice(alphabet))

    print(sequence)
    screen = screen -1

access = pyfiglet.figlet_format("Access Granted")
print(colorama.Fore.GREEN + access)

colorama.deinit()