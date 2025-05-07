def words_cont(text):
    words = text.lower().split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

#Exemplo de uso:
text = input("Digite uma frase: ")
result = words_cont(text)
print("As palavras são e suas quantidades são:")
for word, amount in result.items():
    print(f"A palavra '{word}' aparece: {amount}")