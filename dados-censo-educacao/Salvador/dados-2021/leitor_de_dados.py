import os
import pandas as pd

caminho_arquivo_csv = os.path.join('dados', 'matriculas-faixa_etaria-salvador.csv')

class LeitorDeDados:
    def __init__(self, df):
        self.df = df
    
    
    def get_dados_faixa_etaria_csv(self):
        
        #df_faixa_etaria = pd.read_csv('/home/lasid-rafael/Documentos/educacao/dados-matriculas-eja/dados-censo-educacao/Salvador/dados-2021/matriculas-faixa_etaria-salvador.csv', sep=';')
        
        df_faixa_etaria = pd.read_csv(caminho_arquivo_csv, sep=';')
        
        return df_faixa_etaria
    
    def get_dados_raca_cor_csv(self):

        df_raca = pd.read_csv('/home/lasid-rafael/Documentos/educacao/dados-matriculas-eja/dados-censo-educacao/Salvador/dados-2021/matriculas-raca-cor-salvador.csv', sep=';')
        
        return df_raca
    
    def get_dados_sexo_csv(self):
        
        df_sexo = pd.read_csv('/home/lasid-rafael/Documentos/educacao/dados-matriculas-eja/dados-censo-educacao/Salvador/dados-2021/matriculas-sexo-salvador.csv' , sep=';')
        
        return df_sexo

print(os.getcwd())
    
    