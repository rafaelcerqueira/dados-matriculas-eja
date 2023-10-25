import pandas as pd

df = pd.read_csv('/home/rafael/Documents/EJA/dados-censo-educacao/Salvador/dados-2022/matriculas-faixa_etaria-salvador.csv', sep=';')

class MatriculasSalvadorFaixaEtaria:
    
    def __init__(self, df):
        self.df = df
    
    
    #a função retorna um dicionário com a faixa etária com chave e 'Matrículas' como valor.
    def get_matriculas_faixa_etaria(self):
        
        #Dicionários aninhados.
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
        
        #o loop percorre o dataframe e adiciona os valores as chaves em cada dicionário equivalente.
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
    
    #a função que retorna o total de matrículas por faixa etária em cada dependência administrativa.
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
    
    #chama o método get_matriculas_faixa_etaria() e retorna a porcentagem de cada faixa etária em cada dependência administrativa.
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
            
        #adiciona o simbolo de porcentagem ao final de cada valor.
        for c in total_matriculas_faixa_etaria_porcentagem['Estadual']:
            total_matriculas_faixa_etaria_porcentagem['Estadual'][c] = str(total_matriculas_faixa_etaria_porcentagem['Estadual'][c]) + '%'
            
        return total_matriculas_faixa_etaria_porcentagem
    

#instancia a classe
matriculas_faixa_etaria = MatriculasSalvadorFaixaEtaria(df)

#imprime os resultados
print("Matrículas por faixa etária em cada dependência administrativa:", matriculas_faixa_etaria.get_matriculas_faixa_etaria())
print('--------------------------')
print("Todal de matrículas por dependência administrativa:", matriculas_faixa_etaria.get_total_matriculas_faixa_etaria())
print('--------------------------')
print("Porcentagem das matrículas por faixas etárias em cada dependência administrativa: ", matriculas_faixa_etaria.get_total_matriculas_faixa_etaria_porcentagem())
