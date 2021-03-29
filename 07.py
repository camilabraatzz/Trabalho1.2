# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'O número {num} é divisível por {i}')
        contador += 1

print(f'O número {num} foi divisível {contador} vezes!')

print('O número é primo') if contador == 2 else print('O número não é primo')
