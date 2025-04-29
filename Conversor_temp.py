'''
celsius = float(input("Digite a temperatura em °C: "))
fahrenheit =(celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")
'''
#Exemplo do chatgpt
def converter_temperatura(valor, origem, destino):
    # Primeiro, converte tudo para Celsius
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5/9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        return "Unidade de origem inválida."

    # Agora, converte de Celsius para o destino
    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9/5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return "Unidade de destino inválida."


print("=== Conversor de Temperaturas ===")
valor = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

resultado = converter_temperatura(valor, origem, destino)

if isinstance(resultado, str):
    print("Erro:", resultado)
else:
    print(f"{valor}°{origem} equivale a {resultado:.2f}°{destino}")