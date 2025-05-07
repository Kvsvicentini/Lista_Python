import random
import string
def password_generator(password_size):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(password_size))
    return password

#Exemplo de uso:
password_size = int(input("Digite o tamanho da senha que você deseja: "))
print(f"A senha gerada foi: {password_generator(password_size)}")