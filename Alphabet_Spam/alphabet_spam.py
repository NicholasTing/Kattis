word = input()

white = 0
lower = 0
upper = 0
symbols = 0

for letter in word:
    if letter == '_':
        white += 1

    elif letter.islower():
        lower += 1

    elif letter.isupper():
        upper += 1

    else:
        symbols += 1

total = white + lower + upper + symbols

print(white/total)
print(lower/total)
print(upper/total)
print(symbols/total)
