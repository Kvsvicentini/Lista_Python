def sao_anagramas(word_1, word_2):
    return sorted(word_1.lower()) == sorted(word_2.lower())
word_1 = input("Digite a primeira palavra: ")
word_2 = input("Digite a segunda palavra: ")
if sao_anagramas(word_1, word_2):
    print("São anagramas!")
else:
    print("Não são anagramas.")