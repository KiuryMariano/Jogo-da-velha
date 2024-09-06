# Função para verificar se o tabuleiro está cheio
def verifica_empate(tabuleiro):
    # Verifica se todas as células estão preenchidas
    return all(cell != " " for row in tabuleiro for cell in row)
