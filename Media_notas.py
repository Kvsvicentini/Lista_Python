grades = []
for i in range(1, 4):
    grade = float(input("Digite a sua nota: "))
    grades.append(grade)
average = sum(grades) / len(grades)
print(f"Sua média de notas foi: {average:.2f}")
if (average >= 7):
    print(f"Aluno aprovado com a média de {average:.2f}")
else:
    print(f"Aluno reprovado com a média de {average:.2f}")