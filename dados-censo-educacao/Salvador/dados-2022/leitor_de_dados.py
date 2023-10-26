import pandas as pd


#Classe que lê os dados dos arquivos csv e os armazena em um dataframe.
class LeitorDeDados:
        
    def __init__(self, df):
        self.df = df
        
    def get_dados_faixa_etaria_csv(self):
            
        df_faixa_etaria = pd.read_csv('/home/lasid-rafael/Documentos/educacao/dados-matriculas-eja/dados-censo-educacao/Salvador/dados-2022/matriculas-faixa_etaria-salvador.csv', sep=';')
        
        return df_faixa_etaria

    def get_dados_raca_cor_csv(self):

        df_raca = pd.read_csv('/home/lasid-rafael/Documentos/educacao/dados-matriculas-eja/dados-censo-educacao/Salvador/dados-2022/matriculas-raca-cor-salvador.csv', sep=';')
        
        return df_raca

    def get_dados_sexo_csv(self):
        
        df_sexo = pd.read_csv('/home/lasid-rafael/Documentos/educacao/dados-matriculas-eja/dados-censo-educacao/Salvador/dados-2022/matriculas-sexo-salvador.csv')
        
        return df_sexo
    

