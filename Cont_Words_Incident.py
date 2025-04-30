sentence = input("Digite uma frase: ").lower()
words = sentence.split()
incident = {}
for word in words:
    incident[word] = incident.get(word, 0) + 1
print("Ocorrências das palavras:")
for word, amount in incident.items():
    print(f"{word}: {amount}")