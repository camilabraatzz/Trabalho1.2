# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1
    else:
        print(f'O número {num} é divisível por {i}')

print("O número é primo") if contador == 2 else print("O número não é primo")
