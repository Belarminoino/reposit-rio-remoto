# Define posições
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

# Faz Jogada
def faz_jogada (tabuleiro,linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna]= 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna]= '-'
    return tabuleiro

# valida posicao

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


p = True
l = True
#precisa por a frota
tamanhos = {
        "porta-aviões": 4,
        "navio-tanque": 3,
        "contratorpedeiro": 2,
        "submarino": 1,
    }

while p:

    barco = input('Qual barco?')
    if barco == 'porta-aviões':
        print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
    elif barco == 'navio-tanque':
        print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
    elif barco == 'contratorpedeiro':
        print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
    elif barco == 'submarino':
        print('Insira as informações referentes ao navio submarino que possui tamanho 1')

    while l:
        linha = int(input('Qual a linha?'))
        coluna = int(input('Qual a coluna?'))
        if barco != 'submarino':
            orientacao = int(input('Qual orientação?')) # so poder ser 1 ou 2
            if posicao_valida(FROTA, linha,coluna,orientacao,tamanhos):
                z = define_posicoes(linha,coluna,orientacao,tamanhos)
                b = preenche_frota(frota,linha,coluna,orientacao,tamanhos)
            else:
                print('Esta posição não está válida!')
                l = True
        elif barco == 'submarino':
                orientacao = 1
            if posicao_valida(FROTA, linha,coluna,orientacao,tamanhos):
                z = define_posicoes(linha,coluna,orientacao,tamanhos)
                b = preenche_frota(frota,linha,coluna,orientacao,tamanhos)
            else:
                print('Esta posição não está válida!')
                l = True


    



