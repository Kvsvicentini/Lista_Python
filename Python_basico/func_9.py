def ATM(value):
    banknotes = [2, 5, 10, 20, 50, 100, 200]
    result = {}
    for banknote in banknotes:
        amount = value // banknote
        if amount:
            result[banknote] = amount
            value %= banknote
    return result

#Exemplo de uso:
value = int(input("Digite um valor para saque: "))
for banknote, amount in ATM(value).items():
    print(f"Você sacou {amount} nota(s) de R${banknote}")