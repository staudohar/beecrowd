linhas, colunas, linhas_lote, colunas_lote = map(int, input().split())
matriz = []
maximo = -1
soma = 0

for i in range(linhas):
    matriz.append(list(map(int, input().split())))
    

for k in range(colunas - (colunas_lote - 1)):
    soma = 0
    for j in range(linhas):
        if j >= linhas_lote:
            soma -= sum(matriz[j-(linhas_lote)][k:k+colunas_lote])

        soma += sum(matriz[j][k:k+colunas_lote])
        if soma > maximo:
            maximo = soma

print(maximo)