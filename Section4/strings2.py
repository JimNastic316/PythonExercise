number = '412-848-9999923423,32423$-189'
separators = ''

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = ''.join(char if char not in separators else ' ' for char in number).split()
print([int(val) for val in values])
