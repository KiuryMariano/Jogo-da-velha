import random

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("-" * 9)
    
    print('\n')

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

# Função para verificar se o tabuleiro está cheio (empate)
def verificar_empate(tabuleiro):
    return all([cell != " " for row in tabuleiro for cell in row])

# Função para a jogada do jogador
def jogada_jogador(tabuleiro):
    while True:
        try:
            linha = int(input("Escolha a linha (1, 2, 3): ")) - 1
            coluna = int(input("Escolha a coluna (1, 2, 3): ")) - 1
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "X"
                break
            else:
                print("Posição já ocupada, escolha outra.")
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.")

# Função para a jogada da IA
def jogada_ia(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = "O"
                if verificar_vencedor(tabuleiro, "O"):
                    return
                else:
                    tabuleiro[i][j] = " "
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = "X"
                if verificar_vencedor(tabuleiro, "X"):
                    tabuleiro[i][j] = "O"
                    return
                else:
                    tabuleiro[i][j] = " "
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if tabuleiro[i][j] == " ":
            tabuleiro[i][j] = "O"
            break

# Função principal para rodar o jogo
def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    imprimir_tabuleiro(tabuleiro)

    while True:
        jogada_jogador(tabuleiro)
        imprimir_tabuleiro(tabuleiro)
        if verificar_vencedor(tabuleiro, "X"):
            print("Você venceu!")
            break
        if verificar_empate(tabuleiro):
            print("Empate!")
            break

        jogada_ia(tabuleiro)
        imprimir_tabuleiro(tabuleiro)
        if verificar_vencedor(tabuleiro, "O"):
            print("Você perdeu!")
            break
        if verificar_empate(tabuleiro):
            print("Empate!")
            break

# Iniciar o jogo
jogar()
