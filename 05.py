# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um número inteiro '))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'Múltiplo de: {i}')
        contador += 1
print('O número é primo' if contador == 2 else 'O número não é primo')
