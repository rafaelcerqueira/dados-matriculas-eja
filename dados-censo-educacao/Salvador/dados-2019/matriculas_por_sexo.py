import pandas as pd

from leitor_de_dados import LeitorDeDados
df = pd.DataFrame()
df = LeitorDeDados(df).get_dados_sexo_csv()

class MatriculasSalvadorSexo:
    
    def __init__(self, df):
        self.df = df
    
    def get_matriculas_por_sexo(self):
        
        matriculas_feminino = {
            'Estadual': 0,
            'Municipal': 0,
            'Privada': 0,
            'Federal': 0
        }
        
        matriculas_masculino = {
            'Estadual': 0,
            'Municipal': 0,
            'Privada': 0,
            'Federal': 0
        }
        
        for c in range(len(self.df)):
            if self.df['Categoria 2'][c] == 'Estadual':
                if self.df['Categoria 1'][c] == 'Feminino':
                    matriculas_feminino['Estadual'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Masculino':
                    matriculas_masculino['Estadual'] += self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Municipal':
                if self.df['Categoria 1'][c] == 'Feminino':
                    matriculas_feminino['Municipal'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Masculino':
                    matriculas_masculino['Municipal'] += self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Privada':
                if self.df['Categoria 1'][c] == 'Feminino':
                    matriculas_feminino['Privada'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Masculino':
                    matriculas_masculino['Privada'] += self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Federal':
                if self.df['Categoria 1'][c] == 'Feminino':
                    matriculas_feminino['Federal'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Masculino':
                    matriculas_masculino['Federal'] += self.df['Matrículas'][c]
        
        return {'Feminino': matriculas_feminino, 'Masculino': matriculas_masculino}
    
    def get_total_matriculas_por_sexo(self):
        
        total_matriculas_por_sexo = {
            'Feminino': 0,
            'Masculino': 0
        }
        
        for c in range(len(self.df)):
            if self.df['Categoria 1'][c] == 'Feminino':
                total_matriculas_por_sexo['Feminino'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Masculino':
                total_matriculas_por_sexo['Masculino'] += self.df['Matrículas'][c]
        
        return total_matriculas_por_sexo
    
    def get_matriculas_por_sexo_porcentagem(self):
        
        matriculas_por_sexo = self.get_matriculas_por_sexo()
        
        matriculas_por_sexo_porcentagem = {
            'Feminino': {
                'Estadual': 0,
                'Municipal': 0,
                'Privada': 0,
                'Federal': 0
            },
            'Masculino': {
                'Estadual': 0,
                'Municipal': 0,
                'Privada': 0,
                'Federal': 0
            }
        }
        
        for sexo in matriculas_por_sexo:
            for categoria in matriculas_por_sexo[sexo]:
                matriculas_por_sexo_porcentagem[sexo][categoria] = round((matriculas_por_sexo[sexo][categoria] / self.get_total_matriculas_por_sexo()[sexo]) * 100, 2)
         
        #adiciona símbolo de porcentagem
        for sexo in matriculas_por_sexo_porcentagem:
            for categoria in matriculas_por_sexo_porcentagem[sexo]:
                matriculas_por_sexo_porcentagem[sexo][categoria] = str(matriculas_por_sexo_porcentagem[sexo][categoria]) + '%'        
                
        return matriculas_por_sexo_porcentagem
        
matriculas = MatriculasSalvadorSexo(df)

print(matriculas.get_matriculas_por_sexo_porcentagem())
    