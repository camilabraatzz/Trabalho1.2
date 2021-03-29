# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qt_cds = int(input('Digite a quantidade de CDs'))
soma = 0
for n in range(qt_cds):
    valor_cd = float(input('Digite o valor dos CDs'))
    soma += valor_cd
media = soma / qt_cds
print('A media gasta na coleção de CDs é de: ', media)
