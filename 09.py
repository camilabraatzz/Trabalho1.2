# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
# verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

qt_pessoas = int(input('Digite o quantidade de pessoas da turma\n'))
soma = 0
for n in range(qt_pessoas):
    idade = int(input('Digite sua idade'))
    soma += idade
media = soma / qt_pessoas
if 0 > media < 25:
    print('Turma de Jovens, média de idade: ', media)
elif media < 60:
    print('Turma de Adultos, média de idade: ', media)
else:
    print('Turma de Idosos, média de idade: ', media)

