# B6 Prog01: Remove spaces at the beginning w/o using lstrip()

"""
PSEUDOCODE

user input
use for loop to eliminate space
print output
"""

index = 0
user = input("Enter word/s: ")

for x in user:
    if x == " ":
        index += 1
    else:
        break

print(user[index:])