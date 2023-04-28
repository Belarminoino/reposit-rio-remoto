def afundados(frota, tabuleiro):
    num_afundados = 0
    for embarcacao, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                if tabuleiro[linha][coluna] != 'X':
                    break
            else:
                num_afundados += 1
    return num_afundados
