import pandas as pd

url = 'https://raw.githubusercontent.com/rafaelcerqueira/dados-eja-matriculas/main/Bahia'

class LeitorDeDados:

    def __init__(self, df):
        self.df = df

    def get_dados_faixa_etaria_csv(self):

        df_faixa_etaria = pd.read_csv(url + '/dados-2020/matriculas-faixa_etaria-bahia.csv', sep=';')

        return df_faixa_etaria

    def get_dados_cor_raca_csv(self):

        df_raca_cor = pd.read_csv(url + '/dados-2020/matriculas-cor_raca-bahia.csv', sep=';')

        return df_raca_cor

    def get_dados_sexo_csv(self):

        df_sexo = pd.read_csv(url + '/dados-2020/matriculas-sexo-bahia.csv', sep=';')

        return df_sexo



