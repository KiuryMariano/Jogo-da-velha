# Função para a jogada do jogador
def jogada_jogador(tabuleiro):

    while True:
        try:
            # Solicita ao jogador a linha e a coluna para a jogada
            linha = int(input("Escolha a linha (1, 2, 3): ")) - 1
            coluna = int(input("Escolha a coluna (1, 2, 3): ")) - 1
            # Verifica se a entrada está dentro do intervalo permitido e se a célula está vazia
            if 0 <= linha < 3 and 0 <= coluna < 3:
                if tabuleiro[linha][coluna] == " ":
                    # Marca a célula com 'X' se estiver vazia
                    tabuleiro[linha][coluna] = "X"
                    break
                else:
                    print("Posição já ocupada, escolha outra.")
            else:
                print("Escolha inválida. Linha e coluna devem ser entre 1 e 3.")
        except ValueError:
            # Trata erros de conversão de entrada
            print("Entrada inválida. Tente novamente.")
