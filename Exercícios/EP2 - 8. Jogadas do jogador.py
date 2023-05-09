# Define posições
def define_posicoes (linha,coluna,orientacao,tamanho):
    posicoes = []
    if orientacao == 1:
        posicoes.append([linha,coluna])
        if tamanho > 1:
            for i in range(1, tamanho):
                posicoes.append([linha + i,coluna])
    
    elif orientacao == 2:
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

def posiciona_frota(frota):
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for posicao in frota.values():
        for p in posicao:
            for local in p:
                tabuleiro[local[0]][local[1]] = 1
    return tabuleiro
# Faz Jogada

def faz_jogada (tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna]= 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna]= '-'
    return tabuleiro

# Quantas embarcações afundadas?
def afundados(frota, tabuleiro):
    num_afundados = 0
    for posicoes in frota.values():
        for posicao in posicoes:
            for linha, coluna in posicao:
                if tabuleiro[linha][coluna] != 'X':
                    break
            else:
                num_afundados += 1
    return num_afundados

# definindo dicionário da frota
embarcacoes = {'porta-aviões': 4, 'navio-tanque': 3, 'contratorpedeiro': 2, 'submarino': 1}

frota = {'porta-aviões': [], 'navio-tanque': [], 'contratorpedeiro': [], 'submarino': []}

for nome in ['porta-aviões', 'navio-tanque', 'navio-tanque', 'contratorpedeiro', 'contratorpedeiro', 'contratorpedeiro', 'submarino', 'submarino', 'submarino', 'submarino']:
    tamanho = embarcacoes[nome]
    
    while True:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if nome != "submarino":
            orientacao = int(input("[1] Vertical [2] Horizontal >"))
            posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
            
        else:
            posicoes = [linha, coluna]
            orientacao = 1
            
        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota=  preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            break
            
            
        else:
            print("Esta posição não está válida!")



#Jogadas do Jogador
frota_oponente = {'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],'navio-tanque': [[[6, 0], [6, 1], [6, 2]],[[4, 3], [5, 3], [6, 3]]],'contratorpedeiro': [[[1, 6], [1, 7]],[[0, 5], [1, 5]],[[3, 6], [3, 7]]],'submarino': [[[2, 7]],[[0, 6]],[[9, 7]],[[7, 6]]]}


# Tabuleiros
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
# loop jogando
jogando = True
ja_perguntou = []

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
    
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))
    pergunta_ataque = True
    while pergunta_ataque:
        pergunta_linha_ataque = True
        while pergunta_linha_ataque:
            linha_atacar = int(input('Qual linha você deseja atacar? '))
            if linha_atacar < 0 or linha_atacar > 9 or linha_atacar == '':
                print('Linha inválida!')
            else:
                pergunta_linha_ataque = False

        pergunta_coluna_ataque = True
        while pergunta_coluna_ataque:
            coluna_atacar = int(input('Qual coluna você deseja atacar? '))
            if coluna_atacar < 0 or coluna_atacar > 9 or coluna_atacar=='':
                print('Coluna inválida!')
            else:
                pergunta_coluna_ataque = False
        coordenada = [linha_atacar,coluna_atacar]
        if coordenada not in ja_perguntou:
            ja_perguntou.append(coordenada)
            # Atualiza tabuleiro do oponente
            tabuleiro_oponente = faz_jogada(tabuleiro_oponente,linha_atacar,coluna_atacar)
            pergunta_ataque = False   
        else:
            print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_atacar,coluna_atacar))

    ganhou_jogador = afundados(frota_oponente,tabuleiro_oponente) 
    if ganhou_jogador == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False