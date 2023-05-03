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

# definindo dicionário da frota
embarcacoes = {'porta-aviões': 4, 'navio-tanque': 3, 'contratorpedeiro': 2, 'submarino': 1}

frota = {'porta-aviões': [], 'navio-tanque': [], 'contratorpedeiro': [], 'submarino': []}

for nome in ['porta-aviões', 'navio-tanque', 'navio-tanque', 'contratorpedeiro', 'contratorpedeiro', 'contratorpedeiro', 'submarino', 'submarino', 'submarino', 'submarino']:
    tamanho = embarcacoes[nome]
    print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
    while True:
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if nome != "submarino":
            orientacao = int(input("[1] Vertical [2] Horizontal >"))
            posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
            
        else:
            posicoes = [linha, coluna]
            orientacao = None
            
        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            frota[nome].append(posicoes)
            break
            
            
        else:
            print("Esta posição não está válida!")

print(frota) 