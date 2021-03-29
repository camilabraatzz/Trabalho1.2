#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numero = int(input("Digite o tamanho do conjunto: "))
maior = None
menor = None

for i in range(numero):
    x = float(input('Digite um número entre 0 e 1000: '))
    while not 0 < x < 1000:
        x = float(input('O número digitado é maior que 1000, tente novamente'))
    else:
        maior = maior if maior != None and maior > x else x
        menor = menor if menor != None and menor < x else x

print(f'O maior valor digitado foi {maior} e o menor foi {menor}')