print("--------------------------------------------------------------------------------------------------------------------------------------")
print("Vamos ler dois números realizar três operaçõe matemáticas e mostrar os resultados se a soma dos valores originais for menor que 20")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
calc_1 = num_1 + num_2
if (calc_1 < 20):
    calc_2 = num_1 * 10
    calc_3   = num_2 * 10
    print(f"Os resultados das operações são {calc_2} e {calc_3}")


