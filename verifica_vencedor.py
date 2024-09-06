# Função para verificar se há um vencedor
def verifica_vencedor(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        # Checa se todas as células de uma linha ou coluna são iguais ao jogador
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False