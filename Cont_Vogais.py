print("Vamos contar vogais em uma palavra")
word = input("Digite uma palavra: ").lower()
vowels = "aeiouãõ"
cont = 0
for letter in word:
    if letter in vowels:
        cont += 1
print(f"Número de vogais na palavra é: {cont}")