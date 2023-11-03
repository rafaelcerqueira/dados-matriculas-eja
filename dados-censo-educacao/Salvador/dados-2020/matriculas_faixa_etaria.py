import pandas as pd

from leitor_de_dados import LeitorDeDados
df = pd.DataFrame()
df = LeitorDeDados(df).get_dados_faixa_etaria_csv()

class MatriculasSalvadorFaixaEtaria:
    
    def __init__ (self, df):
        self.df = df
        
    def get_matriculas_faixa_etaria(self):
            
        matriculas_faixa_etaria = {
            'Estadual': {
            
            },
            'Municipal': {
                
            },
            'Privada': {
                
            },
            'Federal': {
                
            }
        }
        
        for c in range(len(self.df)):
            if self.df['Categoria 2'][c] == 'Estadual':
                matriculas_faixa_etaria['Estadual'][self.df['Categoria 1'][c]] = self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Municipal':
                matriculas_faixa_etaria['Municipal'][self.df['Categoria 1'][c]] = self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Privada':
                matriculas_faixa_etaria['Privada'][self.df['Categoria 1'][c]] = self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Federal':
                matriculas_faixa_etaria['Federal'][self.df['Categoria 1'][c]] = self.df['Matrículas'][c]
                
        return matriculas_faixa_etaria
    
    def get_total_matriculas_faixa_etaria(self):
        total_matriculas_faixa_etaria = {
            'Estadual': 0,
            'Municipal': 0,
            'Privada': 0,
            'Federal': 0
        }
        
        for c in range(len(self.df)):
            if self.df['Categoria 2'][c] == 'Estadual':
                total_matriculas_faixa_etaria['Estadual'] += self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Municipal':
                total_matriculas_faixa_etaria['Municipal'] += self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Privada':
                total_matriculas_faixa_etaria['Privada'] += self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Federal':
                total_matriculas_faixa_etaria['Federal'] += self.df['Matrículas'][c]
        
        return total_matriculas_faixa_etaria
    
    def get_total_matriculas_faixa_etaria_porcentagem(self):
        matriculas_faixa_etaria = self.get_matriculas_faixa_etaria()
        total_matriculas_faixa_etaria = self.get_total_matriculas_faixa_etaria()
        
        total_matriculas_faixa_etaria_porcentagem = {
            'Estadual': {
            
            },
            'Municipal': {
                
            },
            'Privada': {
                
            },
            'Federal': {
                
            }
        }
        
        for c in matriculas_faixa_etaria['Estadual']:
            total_matriculas_faixa_etaria_porcentagem['Estadual'][c] = round((matriculas_faixa_etaria['Estadual'][c] / total_matriculas_faixa_etaria['Estadual']) * 100, 2)

        for c in matriculas_faixa_etaria['Municipal']:
            total_matriculas_faixa_etaria_porcentagem['Municipal'][c] = round((matriculas_faixa_etaria['Municipal'][c] / total_matriculas_faixa_etaria['Municipal']) * 100, 2)
        
        for c in matriculas_faixa_etaria['Privada']:
            total_matriculas_faixa_etaria_porcentagem['Privada'][c] = round((matriculas_faixa_etaria['Privada'][c] / total_matriculas_faixa_etaria['Privada']) * 100, 2)
        
        for c in matriculas_faixa_etaria['Federal']:
            total_matriculas_faixa_etaria_porcentagem['Federal'][c] = round((matriculas_faixa_etaria['Federal'][c] / total_matriculas_faixa_etaria['Federal']) * 100, 2)
        
        #adiciona símbolo de porcentagem
        for c in total_matriculas_faixa_etaria_porcentagem['Estadual']:
            total_matriculas_faixa_etaria_porcentagem['Estadual'][c] = str(total_matriculas_faixa_etaria_porcentagem['Estadual'][c]) + '%'
        for c in total_matriculas_faixa_etaria_porcentagem['Municipal']:
            total_matriculas_faixa_etaria_porcentagem['Municipal'][c] = str(total_matriculas_faixa_etaria_porcentagem['Municipal'][c]) + '%'
        for c in total_matriculas_faixa_etaria_porcentagem['Privada']:
            total_matriculas_faixa_etaria_porcentagem['Privada'][c] = str(total_matriculas_faixa_etaria_porcentagem['Privada'][c]) + '%'
        for c in total_matriculas_faixa_etaria_porcentagem['Federal']:
            total_matriculas_faixa_etaria_porcentagem['Federal'][c] = str(total_matriculas_faixa_etaria_porcentagem['Federal'][c]) + '%'
        
        return total_matriculas_faixa_etaria_porcentagem
    
    
    
    
matriculas = MatriculasSalvadorFaixaEtaria(df)

print(matriculas.get_total_matriculas_faixa_etaria_porcentagem())