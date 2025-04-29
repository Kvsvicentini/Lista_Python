def convert_money(value, rate, for_coin):
    if for_coin:
        return value / rate
    else:
        return value * rate
value = float(input("Digite o valor: "))
rate = float(input("Digite a taxa: "))
mode = input("Converter para a moeda desejada? s/n: ").lower() == 's'
result = convert_money(value, rate, mode)
print(f"O valor é: {result:.2f}")