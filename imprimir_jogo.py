# Função para imprimir o tabuleiro
def imprimir_jogo(tabuleiro):
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        # Imprime uma linha separadora
        if i < 2:
            print("-" * 9)  # Linha de separação entre as linhas do tabuleiro
    print('\n')