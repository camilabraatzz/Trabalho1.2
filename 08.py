# Faça um programa que calcule o mostre a média aritmética de N notas.

qt_notas = int(input('Digite a quantidade de notas que você deseja digitar\n'))
soma = 0
for n in range(qt_notas):
    nota = float(input('Digite a nota:\n'))
    soma += nota
media = soma / qt_notas
print('A média das notas digitadas foi de:', media)
