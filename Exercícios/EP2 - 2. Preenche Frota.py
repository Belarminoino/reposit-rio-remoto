# Define Posições

def define_posicoes (linha,coluna,orientacao,tamanho):
    posicoes = []
    if orientacao == "vertical":
        posicoes.append([linha,coluna])
        if tamanho > 1:
            for i in range(1, tamanho):
                posicoes.append([linha + i,coluna])
    
    elif orientacao == 'horizontal':
        posicoes.append([linha,coluna])
        if tamanho > 1:
            for i in range(1, tamanho):
                posicoes.append([linha,coluna + i])
    return posicoes

# Preenche Frota
def preenche_frota (frota,nome,linha,coluna,orientacao,tamanho):
    if nome not in frota.keys():
        frota[nome] = [define_posicoes(linha,coluna,orientacao,tamanho)]
    else:
        frota[nome].append(define_posicoes(linha,coluna,orientacao,tamanho))
    return frota