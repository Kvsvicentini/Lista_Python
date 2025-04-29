def gerar_chave():
    """
    Gera uma chave para criptografia e descriptografia
    onde cada letra do alfabeto é substituída por outra.
    """
    import string
    import random

    alfabeto = string.ascii_lowercase  # Letras de 'a' a 'z'
    chave = list(alfabeto)
    random.shuffle(chave)  # Embaralha a chave
    return dict(zip(alfabeto, chave)), dict(zip(chave, alfabeto))


def criptografar(mensagem, chave):
    """
    Criptografa a mensagem usando a chave fornecida.
    """
    criptografada = ""
    for char in mensagem.lower():
        if char in chave:
            criptografada += chave[char]
        else:
            criptografada += char  # Não altera caracteres não alfabéticos
    return criptografada


def descriptografar(mensagem, chave_reversa):
    """
    Descriptografa a mensagem usando a chave reversa fornecida.
    """
    descriptografada = ""
    for char in mensagem.lower():
        if char in chave_reversa:
            descriptografada += chave_reversa[char]
        else:
            descriptografada += char
    return descriptografada


# Uso do programa
mensagem_original = input("Digite a mensagem a ser criptografada: ")
chave, chave_reversa = gerar_chave()

# Criptografar
mensagem_criptografada = criptografar(mensagem_original, chave)
print(f"Mensagem Criptografada: {mensagem_criptografada}")

# Descriptografar
mensagem_decifrada = descriptografar(mensagem_criptografada, chave_reversa)
print(f"Mensagem Decifrada: {mensagem_decifrada}")
