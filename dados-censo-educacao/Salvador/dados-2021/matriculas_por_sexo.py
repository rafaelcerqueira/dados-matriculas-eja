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
    
    #mostra a porcentagem de matrículas de cada sexo por dependência administrativa.
    def get_matriculas_por_sexo_porcentagem(self):
        total_matriculas_por_sexo = self.get_total_matriculas_por_sexo()
        matriculas_por_sexo = self.get_matriculas_por_sexo()
        
        total_matriculas_por_sexo_porcentagem = {
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
        
        for c in matriculas_por_sexo['Feminino']:
            total_matriculas_por_sexo_porcentagem['Feminino'][c] = (matriculas_por_sexo['Feminino'][c] / total_matriculas_por_sexo['Feminino']) * 100
            total_matriculas_por_sexo_porcentagem['Feminino'][c] = round(total_matriculas_por_sexo_porcentagem['Feminino'][c], 2)
            
        for c in matriculas_por_sexo['Masculino']:
            total_matriculas_por_sexo_porcentagem['Masculino'][c] = (matriculas_por_sexo['Masculino'][c] / total_matriculas_por_sexo['Masculino']) * 100
            total_matriculas_por_sexo_porcentagem['Masculino'][c] = round(total_matriculas_por_sexo_porcentagem['Masculino'][c], 2)
        
        
        #adiciona o simbolo de porcentagem ao final de cada valor.
        for c in total_matriculas_por_sexo_porcentagem['Feminino']:
            total_matriculas_por_sexo_porcentagem['Feminino'][c] = str(total_matriculas_por_sexo_porcentagem['Feminino'][c]) + '%'
        
        for c in total_matriculas_por_sexo_porcentagem['Masculino']:
            total_matriculas_por_sexo_porcentagem['Masculino'][c] = str(total_matriculas_por_sexo_porcentagem['Masculino'][c]) + '%'
            
        return total_matriculas_por_sexo_porcentagem
    
    #mostra a porcentagem total de matrículas de cada sexo.
    def get_matriculas_por_sexo_porcentagem_total(self):
        total_matriculas_por_sexo = self.get_total_matriculas_por_sexo()
        
        total_matriculas_por_sexo_porcentagem_total = {
            'Feminino': 0,
            'Masculino': 0
        }
        
        for c in total_matriculas_por_sexo:
            total_matriculas_por_sexo_porcentagem_total[c] = (total_matriculas_por_sexo[c] / sum(total_matriculas_por_sexo.values())) * 100
            total_matriculas_por_sexo_porcentagem_total[c] = round(total_matriculas_por_sexo_porcentagem_total[c], 2)
        
        #adiciona o simbolo de porcentagem ao final de cada valor.
        for c in total_matriculas_por_sexo_porcentagem_total:
            total_matriculas_por_sexo_porcentagem_total[c] = str(total_matriculas_por_sexo_porcentagem_total[c]) + '%'
            
        return total_matriculas_por_sexo_porcentagem_total
    
    

matriculas = MatriculasSalvadorSexo(df)
print(matriculas.get_total_matriculas_por_sexo())
                    