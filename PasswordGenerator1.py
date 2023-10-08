import string
from random import *
characters = string.punctuation + string.ascii_lowercase + string.digits + string.ascii_uppercase
password = "".join(choice(characters)for x in range (randint(8,25)))
print (password)
