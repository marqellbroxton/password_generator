import random

ucLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lcLetters = ucLetters.lower()
numbers = "0123456789"
special_characters = "()[]{};:.-_/\\?+*#$%^&@!"

upper, lower, nums, syms = True, True, True, True

field = ""

if upper:
    field += ucLetters
if lower:
    field += lcLetters
if nums:
    field += numbers
if syms:
    field += special_characters

pw_length = 12
display = 5

for x in range(display):
    password = "".join(random.sample(field, pw_length))
    print(password)



