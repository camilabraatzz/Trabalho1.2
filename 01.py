#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Fatorial de: "))
resultado = 1
string = f'{numero}! = '
for n in range(numero, 0, -1):
    resultado *= n
    string = string + str(n) + '.'
print(f'{string} = {resultado}')