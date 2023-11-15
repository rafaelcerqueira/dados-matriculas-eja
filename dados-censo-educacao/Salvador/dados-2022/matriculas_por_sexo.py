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
    
    def get_matriculas_por_sexo_por_dependencia_administrativa(self):
        
        # acessa o dicionario matriculas_feminino e matriculas_masculino em get_matriculas_por_sexo()
        matriculas_por_sexo = self.get_matriculas_por_sexo()
        
        # cria um dicionario para armazenar as matriculas de cada sexo por dependencia administrativa
        matriculas_por_sexo_por_dependencia_administrativa = {
            'Estadual': {
                'Feminino': 0,
                'Masculino': 0
            },
            'Municipal': {
                'Feminino': 0,
                'Masculino': 0
            },
            'Privada': {
                'Feminino': 0,
                'Masculino': 0
            },
            'Federal': {
                'Feminino': 0,
                'Masculino': 0
            }
        }
        
       # percorre o dicionario matriculas_feminino e verifica se a categoria é estadual, municipal, privada ou federal
         # se for estadual, municipal, privada ou federal, soma a quantidade de matriculas de cada sexo
        for sexo in matriculas_por_sexo:
            for categoria in matriculas_por_sexo[sexo]:
                if categoria == 'Estadual':
                    matriculas_por_sexo_por_dependencia_administrativa['Estadual'][sexo] += round(matriculas_por_sexo[sexo][categoria], 2)
                elif categoria == 'Municipal':
                    matriculas_por_sexo_por_dependencia_administrativa['Municipal'][sexo] += round(matriculas_por_sexo[sexo][categoria], 2)
                elif categoria == 'Privada':
                    matriculas_por_sexo_por_dependencia_administrativa['Privada'][sexo] += round(matriculas_por_sexo[sexo][categoria], 2)
                elif categoria == 'Federal':
                    matriculas_por_sexo_por_dependencia_administrativa['Federal'][sexo] += round(matriculas_por_sexo[sexo][categoria], 2)
            
                
        return matriculas_por_sexo_por_dependencia_administrativa
    
    def get_percentual_por_sexo_dependencia_administrativa(self):
        
        # acessa o dicionario matriculas_por_sexo_por_dependencia_administrativa
        matriculas_por_sexo_por_dependencia_administrativa = self.get_matriculas_por_sexo_por_dependencia_administrativa()
        
        # cria um dicionario para armazenar o percentual de matriculas de cada sexo por dependencia administrativa
        percentual_por_sexo_dependencia_administrativa = {
            'Estadual': {
                'Feminino': 0,
                'Masculino': 0
            },
            'Municipal': {
                'Feminino': 0,
                'Masculino': 0
            },
            'Privada': {
                'Feminino': 0,
                'Masculino': 0
            },
            'Federal': {
                'Feminino': 0,
                'Masculino': 0
            }
        }

        # percorre o dicionario matriculas_por_sexo_por_dependencia_administrativa
        for categoria in matriculas_por_sexo_por_dependencia_administrativa:
            # soma a quantidade de matriculas de cada sexo
            total = matriculas_por_sexo_por_dependencia_administrativa[categoria]['Feminino'] + matriculas_por_sexo_por_dependencia_administrativa[categoria]['Masculino']
            # calcula o total de matriculas feminino, divide pelo total de matriculas e multiplica por 100
            percentual_por_sexo_dependencia_administrativa[categoria]['Feminino'] = round((matriculas_por_sexo_por_dependencia_administrativa[categoria]['Feminino'] / total) * 100, 2)
            # calcula o total de matriculas masculino, divide pelo total de matriculas e multiplica por 100
            percentual_por_sexo_dependencia_administrativa[categoria]['Masculino'] = round((matriculas_por_sexo_por_dependencia_administrativa[categoria]['Masculino'] / total) * 100, 2)
            # adiciona os valores em percentual_por_sexo_dependencia_administrativa
            percentual_por_sexo_dependencia_administrativa[categoria]['Feminino'] = str(percentual_por_sexo_dependencia_administrativa[categoria]['Feminino']) + '%'
            percentual_por_sexo_dependencia_administrativa[categoria]['Masculino'] = str(percentual_por_sexo_dependencia_administrativa[categoria]['Masculino']) + '%'            
                
        return percentual_por_sexo_dependencia_administrativa
    
    def get_percentual_total_por_sexo(self):
        
        total_matriculas_por_sexo = self.get_total_matriculas_por_sexo()
        
        percentual_total_por_sexo = {
            'Feminino': 0,
            'Masculino': 0
        }
        
        total = total_matriculas_por_sexo['Feminino'] + total_matriculas_por_sexo['Masculino']
        percentual_total_por_sexo['Feminino'] = round((total_matriculas_por_sexo['Feminino'] / total) * 100, 2)
        percentual_total_por_sexo['Masculino'] = round((total_matriculas_por_sexo['Masculino'] / total) * 100, 2)
        percentual_total_por_sexo['Feminino'] = str(percentual_total_por_sexo['Feminino']) + '%'
        percentual_total_por_sexo['Masculino'] = str(percentual_total_por_sexo['Masculino']) + '%'
        
        return percentual_total_por_sexo
    
    
matriculas = MatriculasSalvadorSexo(df=df)

print('--------------------------------------------------------------')
print(matriculas.get_matriculas_por_sexo())
print('--------------------------------------------------------------')
print(matriculas.get_total_matriculas_por_sexo())
print('--------------------------------------------------------------')
print(matriculas.get_matriculas_por_sexo_por_dependencia_administrativa())
print('--------------------------------------------------------------')
print(matriculas.get_percentual_por_sexo_dependencia_administrativa())
print('--------------------------------------------------------------')
print(matriculas.get_percentual_total_por_sexo())
print('--------------------------------------------------------------')

