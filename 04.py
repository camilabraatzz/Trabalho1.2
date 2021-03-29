#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    numero = int(input('Digite um número inteiro'))
    while not 0 <= numero <= 16:
        numero = int(input('O número deve estar entre 0 e 16, digite novamente: '))
    else:
        resultado = 1
        for n in range(1, numero + 1):
            resultado *= n
        print(resultado)
