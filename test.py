
import string
letters_guessed = "abc"
available = ""
for letter in string.ascii_lowercase:
    if letter not in letters_guessed:
        available += letter

print(available)