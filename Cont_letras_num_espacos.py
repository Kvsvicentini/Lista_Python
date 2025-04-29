text = input("Digite um texto: ")
letters = num = spaces = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        num += 1
    elif char.isspace():
        spaces += 1
print(f"A quantidade de letras são: {letters}")
print(f"A quantidade de números são: {num}")
print(f"A quantidade de espaços são: {spaces}")