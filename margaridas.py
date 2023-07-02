linhas, colunas, linhas_lote, colunas_lote = map(int, input().split())
matriz = []
lista_pos = [0, 0]
maximo = -1
soma = 0

for i in range(linhas):
    matriz.append(list(map(int, input().split())))
    
for j in range(linhas//linhas_lote):
    lista_pos[1] = 0
    for k in range(colunas//colunas_lote):
        soma = 0
        for l in range(linhas_lote):
            soma += sum(matriz[lista_pos[0]+l][lista_pos[1]:lista_pos[1]+colunas_lote])
        if soma > maximo:
            maximo = soma
        lista_pos[1] += colunas_lote
    lista_pos[0] += linhas_lote

print(maximo)