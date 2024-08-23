# Jogo da Velha com Inteligência Artificial

## Descrição do Projeto

Este projeto consiste em um jogo da velha onde o usuário joga contra um agente inteligente. O objetivo principal é desenvolver um programa que implemente a lógica do jogo, permitindo que o usuário jogue interativamente com o computador. A IA foi projetada para tomar decisões inteligentes com base nos movimentos do jogador, ao invés de realizar jogadas aleatórias.

### Descrição da Atividade

Desenvolva um programa para que tenha um agente inteligente para jogar um jogo, mas não é qualquer jogo. Deverá ser o jogo da velha. A ideia é você implementar de acordo com seu conhecimento em qualquer linguagem que desejar. O jogo deverá interagir com o usuário, de forma a jogar automaticamente, de acordo com os movimentos do humano que estiver jogando com o computador. Utilize os recursos que desejar, considerando movimentos inteligentes e não aleatórios.

## Funcionalidades

- **Jogador vs Computador**: O jogador humano joga contra o computador.
- **Movimentos Inteligentes**: A IA do jogo toma decisões inteligentes, tentando vencer ou bloquear o jogador com base nos movimentos atuais no tabuleiro.
- **Verificação de Vitória**: O jogo verifica se há um vencedor após cada jogada.
- **Verificação de Empate**: O jogo também verifica se houve um empate, ou seja, se todas as posições do tabuleiro estão preenchidas sem um vencedor.
- **Interação com o Usuário**: O jogo interage com o usuário pedindo que ele insira as coordenadas para sua jogada.

## Estrutura do Código

- **imprimir_tabuleiro(tabuleiro)**: Função que imprime o tabuleiro do jogo no console.
- **verificar_vencedor(tabuleiro, jogador)**: Função que verifica se o jogador (X ou O) venceu a partida.
- **verificar_empate(tabuleiro)**: Função que verifica se houve um empate.
- **jogada_jogador(tabuleiro)**: Função que permite ao jogador humano fazer sua jogada, escolhendo a linha e a coluna no tabuleiro.
- **jogada_ia(tabuleiro)**: Função que define a jogada da IA, com uma lógica que tenta vencer ou bloquear o jogador humano.
- **jogar()**: Função principal que inicia e gerencia o fluxo do jogo, alternando as jogadas entre o jogador humano e a IA até que haja um vencedor ou um empate.

## Como Rodar o Jogo

1. **Requisitos**: Você precisa ter Python instalado no seu computador.

2. **Execução**:
    - Clone este repositório ou copie o código em um arquivo `.py`.
    - Abra o terminal ou prompt de comando no diretório onde o arquivo está localizado.
    - Execute o comando `python nome_do_arquivo.py` (substitua `nome_do_arquivo` pelo nome do seu arquivo).

3. **Jogue**:
    - Siga as instruções exibidas no terminal para jogar contra o computador.
    - Insira as coordenadas para as suas jogadas e tente vencer a IA!

## Exemplo de Uso

```bash
Escolha a linha (1, 2, 3): 1
Escolha a coluna (1, 2, 3): 1
 X |   |  
---------
   |   |  
---------
   |   |  
