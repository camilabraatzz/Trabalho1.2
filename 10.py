# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Digite a quantidade de eleitores'))
candidatoA = 0
candidatoB = 0
candidatoC = 0
vencedor = str
for n in range(eleitores):
    voto = int(input('Digite seu candidato\n 1 - Candidato A\n 2 - Cadndidato B \n 3 - Candidato C\n'))
    if voto == 1:
        candidatoA += 1
    elif voto == 2:
        candidatoB += 1
    elif voto == 3:
        candidatoC += 1
    else:
        voto = int(input('Digite novamente\n 1 - Candidato A\n 2 - Cadndidato B \n 3 - Candidato C\n'))

if candidatoA > candidatoB and candidatoA > candidatoC:
    vencedor = 'Candidato A'
elif candidatoB > candidatoA and candidatoB > candidatoC:
    vencedor = 'Candidato B'
elif candidatoC > candidatoB and candidatoC > candidatoA:
    vencedor = 'Candidato C'
elif candidatoA == candidatoB and candidatoA == candidatoC:
    vencedor = 'Nenhum, houve um empate'
print('O vencedor foi', vencedor)
