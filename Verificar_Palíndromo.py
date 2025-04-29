word = input("Digite uma palavra: ").lower()
if word == word[::-1]:
    print(f"A palavra {word} é um palíndromo!")
else:
    print(f"A palavra {word} não é um palíndromo.")