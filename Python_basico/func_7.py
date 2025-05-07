def check_approval(grades):
    sum_grades = sum(grades)
    number_grades = len(grades)
    grades_average = sum_grades / number_grades
    return grades_average

#Exemplo de uso:
cont = 0
student_name = input("Digite o nome do aluno: ")
while cont != 4:
    grades = [float(input("Digite uma nota: "))]
    cont += 1
if check_approval(grades) >= 6:
    print(f"O aluno {student_name} foi aprovado com a média de {check_approval(grades)}")
else:
    print(f"O aluno {student_name} foi reprovado com a média de {check_approval(grades)}")