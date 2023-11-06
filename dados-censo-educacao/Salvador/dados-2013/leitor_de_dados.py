import pandas as pd

url = 'https://raw.githubusercontent.com/rafaelcerqueira/dados-eja-matriculas/main/Salvador'


class LeitorDeDados:
    
    def __init__(self, df):
        self.df = df
    
    def get_dados_faixa_etaria_csv(self):
        
        df_faixa_etaria = pd.read_csv(url + '/dados-2013/matriculas-faixa_etaria-salvador.csv', sep=';')

        return df_faixa_etaria
    
    def get_dados_raca_cor_csv(self):
        
        df_raca_cor = pd.read_csv(url + '/dados-2013/matriculas-cor_raca-salvador.csv', sep=';')
        
        return df_raca_cor
    
    def get_dados_sexo_csv(self):
        
        df_sexo = pd.read_csv(url + '/dados-2013/matriculas-sexo-salvador.csv', sep=';')
        
        return df_sexo
    