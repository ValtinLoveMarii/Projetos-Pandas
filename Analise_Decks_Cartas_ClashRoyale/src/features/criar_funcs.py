import pandas as pd

# FUNÇÃO QUE RETORNA O DECK VENCEDOR
def func_verificar_vencedor(valor):
    if valor['Deck Vencedor'] == 1:
        return valor['p1_1': 'p1_8'].to_list()
    elif valor['Deck Vencedor'] == 2:
        return valor['p2_1': 'p2_8'].to_list()
    else:
        print('DEU ERRO OU EMPATE(ERRO ENT)')

# FUNÇÃO PARA CRIAR UM LISTA, ONDE SE TERÁ O NÚMERO DE CARTAS POR LINHAS, NO FINAL TENDO OS DADOS COMPLETOS DE CADA LINHA (COM OS 2 DEKCS SENDO CONTADOS)
def contar_cartas_por_linhas(valor):
    return valor['p1_1': 'p2_8'].to_list()