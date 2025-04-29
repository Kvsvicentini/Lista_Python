import string
def strong_password(password):
    return (
        len(password) >= 8 and
        any(caracter.islower() for caracter in password) and
        any(caracter.isupper() for caracter in password) and
        any(caracter.isdigit() for caracter in password) and
        any(caracter in string.punctuation for caracter in password)
    )
password = input("Digite uma senha: ")
if strong_password(password):
    print(f"A senha é forte")
else:
    print("A senha é fraca")