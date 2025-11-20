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


# FUNC PARA TRANSFORMAR DICTS E LISTS EM SERIES E DEPOIS EM DATAFRAMES
def trasnformar_series_em_df(valor, colunas=[]):
    df = pd.Series(valor)
    return pd.DataFrame(df, columns=[colunas]).sort_values(by=colunas, ascending=False)

# RETORNAR O DECK VENCEDOR OU AMBOS OS DECK EM FORMA DE DICIONARIO

''''
    Função que retorna 2 possíveis resultados:
        Um dicionário com todos os decks vencedores

        Um dicionário com ambos os decks

    Oque cada parâmetro faz:
      tipo - 1 para utilizar a func que retorna apenas os decks vencedores e 2 para utilizar a func que retorna ambos os decks
      df - recebe o dataframe com os decks para que se possa pegar os dados
      axis - escolhe o axis, se irá pegar por coluna ou linha
'''
def retorna_deck_venc_ou_ambos(tipo, df, axis):
    if tipo == 1:
        df_intermedi = df.apply(func_verificar_vencedor, axis=axis)
        return df_intermedi.to_dict()
    elif tipo == 2:
        df_intermedi = df.apply(contar_cartas_por_linhas, axis=axis)
        return df_intermedi.to_dict()