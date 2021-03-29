# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

qt_turmas = int(input('Digite a quantidade de turmas'))
soma = 0
for n in range(qt_turmas):
    qt_alunos = int(input('Digite a quantidade de alunos'))
    while qt_alunos > 40:
        qt_alunos = int(input('Número de alunos deve ser menor ou igual a 40, digite novamente'))
    soma += qt_alunos
media = soma / qt_turmas
print('A média de alunos é igual a:', media)