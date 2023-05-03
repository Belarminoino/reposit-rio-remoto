# Define posições
def define_posicoes (linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        posicoes.append([linha, coluna])
        if tamanho > 1:
            for i in range(1, tamanho):
                posicoes.append([linha + i, coluna])
    
    elif orientacao == 'horizontal':
        posicoes.append([linha, coluna])
        if tamanho > 1:
            for i in range(1, tamanho):
                posicoes.append([linha, coluna + i])
    return posicoes

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes_navio:
        linha, coluna = posicao
        if linha < 0 or coluna < 0 or linha > 9 or coluna > 9:
            return False
        for navio in frota.values():
            for pos in navio:
                if posicao in pos:
                    return False
    return True