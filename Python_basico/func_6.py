def check_palindromes(text):
    clean_text = ''.join(x.lower() for x in text if x.isalnum())
    return clean_text == clean_text[::-1]

#Exemplo de uso
text = input("Digite uma palavra ou frase: ")
print("A palavra digitada é um palíndromo" if check_palindromes(text) else "A palavra digitada não é um palíndromo")