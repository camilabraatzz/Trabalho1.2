#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numero = int(input("Digite o tamanho do conjunto: "))
maior = None
menor = None
for i in range(numero):
   x = float(input("Digite um número: "))
   maior = maior if maior != None and maior > x else x
   menor = menor if menor != None and menor < x else x

print(f'O maior valor digitado foi {maior} e o menor foi {menor}')