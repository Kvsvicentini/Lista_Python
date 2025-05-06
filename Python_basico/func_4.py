def cont_vowels(word):
    vowels = "aááâãeéèêiíìîoóòôõuúùû"
    cont = 0
    for letter in word:
        if letter in vowels:
            cont += 1
    return cont

#Exemplo de uso:
word = input("Digite uma palavra: ")
print(f"Existem {cont_vowels(word)} vogais na palavra {word}")