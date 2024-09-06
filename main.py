# -*- coding: utf-8 -*-
"""
Jogo da Velha em Python

Autores:
- Leonardo Paes
- Kiury Mariano

Descrição:
Este é um jogo da velha simples implementado em Python. O jogo permite que um jogador jogue contra uma IA.
O tabuleiro é exibido após cada jogada, e o jogo continua até que haja um vencedor ou empate.
A IA utiliza uma estratégia básica para determinar suas jogadas.

Boa sorte e divirta-se jogando!

Versão: 1.0
"""

from imprimir_jogo import imprimir_jogo
from verifica_vencedor import verifica_vencedor
from verifica_empate import verifica_empate
from jogada_jogador import jogada_jogador
from jogada_ia import jogada_ia

# Função principal para rodar o jogo
def jogar():
    # Inicializa o tabuleiro com espaços vazios
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    imprimir_jogo(tabuleiro)

    while True:
        # Jogada do jogador
        jogada_jogador(tabuleiro)
        imprimir_jogo(tabuleiro)
        # Verifica se o jogador venceu ou se houve empate
        if verifica_vencedor(tabuleiro, "X"):
            print("Você venceu!")
            break
        if verifica_empate(tabuleiro):
            print("Empate!")
            break

        # Jogada da IA
        jogada_ia(tabuleiro)
        imprimir_jogo(tabuleiro)
        # Verifica se a IA venceu ou se houve empate
        if verifica_vencedor(tabuleiro, "O"):
            print("Você perdeu!")
            break
        if verifica_empate(tabuleiro):
            print("Empate!")
            break

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
