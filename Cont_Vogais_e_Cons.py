def cont_letters(sentence):
    vowels = 'aeiouãõ'
    sentence = sentence.lower()
    num_vowels = num_consonant = 0
    for letter in sentence:
        if (letter.isalpha()):
            if (letter in vowels):
                num_vowels += 1
            else:
                num_consonant += 1
    return num_vowels, num_consonant
sentence = input("Digite uma frase: ")
num_vowels, num_consonant = cont_letters(sentence)
print(f"O número de vogais é {num_vowels} e o número de consoantes é {num_consonant}")