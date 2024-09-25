# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

notas = 0

for i in range(5):
    nota = float(input("Digite as notas de 5 alunos: "))

    if nota >= 7:
        notas += 1

    print("Alunos aprovados: ", notas)

