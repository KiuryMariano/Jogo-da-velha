import random
from verifica_vencedor import verifica_vencedor

# Função para a jogada da IA
def jogada_ia(tabuleiro):
    # Tenta encontrar uma jogada que vença a partida para a IA
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = "O"
                if verifica_vencedor(tabuleiro, "O"):
                    return
                tabuleiro[i][j] = " "
    # Tenta encontrar uma jogada que bloqueie a vitória do jogador
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = "X"
                if verifica_vencedor(tabuleiro, "X"):
                    tabuleiro[i][j] = "O"
                    return
                tabuleiro[i][j] = " "
    # Se não houver jogadas vencedoras ou bloqueadoras, joga aleatoriamente
    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if tabuleiro[i][j] == " ":
            tabuleiro[i][j] = "O"
            break
