# -*- coding: utf-8 -*-

import pandas as pd

'''df = pd.read_csv('/home/rafael/Documents/EJA/dados-censo-educacao/Salvador/dados-2022/matriculas-raca-cor-salvador.csv', sep=';')
'''

from leitor_de_dados import LeitorDeDados
df = pd.DataFrame()
df = LeitorDeDados(df).get_dados_raca_cor_csv()

class MatriculasSalvadorRaca:
    
    def __init__(self, df):
        self.df = df
    
    def get_matriculas_dependencia_administrativa(self):
        
        dependencia_administrativa = {
            'Estadual': {
                'Branca': 0,
                'Preta': 0,
                'Parda': 0,
                'Amarela': 0,
                'Indígena': 0,
                'Não declarada': 0
            },
            'Municipal': {
                'Branca': 0,
                'Preta': 0,
                'Parda': 0,
                'Amarela': 0,
                'Indígena': 0,
                'Não declarada': 0
            },
            'Privada': {
                'Branca': 0,
                'Preta': 0,
                'Parda': 0,
                'Amarela': 0,
                'Indígena': 0,
                'Não declarada': 0
            },
            'Federal': {
                'Branca': 0,
                'Preta': 0,
                'Parda': 0,
                'Amarela': 0,
                'Indígena': 0,
                'Não declarada': 0
            }     
            
        }
        
        #cria um loop que percorre o dataframe
        for c in range(len(self.df)):
            
        #para cada linha do dataframe, verifica se a 'Categoria 2' é igual a 'Estadual', 'Municipal', 'Privada' ou 'Federal'
            if self.df['Categoria 2'][c] == 'Estadual':
                if self.df['Categoria 1'][c] == 'Branca':
                    dependencia_administrativa['Estadual']['Branca'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Preta':
                    dependencia_administrativa['Estadual']['Preta'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Parda':
                    dependencia_administrativa['Estadual']['Parda'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Amarela':
                    dependencia_administrativa['Estadual']['Amarela'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Indígena':
                    dependencia_administrativa['Estadual']['Indígena'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Não declarada':
                    dependencia_administrativa['Estadual']['Não declarada'] += self.df['Matrículas'][c]
                
            elif self.df['Categoria 2'][c] == 'Municipal':
                if self.df['Categoria 1'][c] == 'Branca':
                    dependencia_administrativa['Municipal']['Branca'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Preta':
                    dependencia_administrativa['Municipal']['Preta'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Parda':
                    dependencia_administrativa['Municipal']['Parda'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Amarela':
                    dependencia_administrativa['Municipal']['Amarela'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Indígena':
                    dependencia_administrativa['Municipal']['Indígena'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Não declarada':
                    dependencia_administrativa['Municipal']['Não declarada'] += self.df['Matrículas'][c]
                    
            elif self.df['Categoria 2'][c] == 'Privada':
                if self.df['Categoria 1'][c] == 'Branca':
                    dependencia_administrativa['Privada']['Branca'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Preta':
                    dependencia_administrativa['Privada']['Preta'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Parda':
                    dependencia_administrativa['Privada']['Parda'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Amarela':
                    dependencia_administrativa['Privada']['Amarela'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Indígena':
                    dependencia_administrativa['Privada']['Indígena'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Não declarada':
                    dependencia_administrativa['Estadual']['Não declarada'] += self.df['Matrículas'][c]
                    
            elif self.df['Categoria 2'][c] == 'Federal':
                if self.df['Categoria 1'][c] == 'Branca':
                    dependencia_administrativa['Federal']['Branca'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Preta':
                    dependencia_administrativa['Federal']['Preta'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Parda':
                    dependencia_administrativa['Federal']['Parda'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Amarela':
                    dependencia_administrativa['Federal']['Amarela'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Indígena':
                    dependencia_administrativa['Federal']['Indígena'] += self.df['Matrículas'][c]
                elif self.df['Categoria 1'][c] == 'Não declarada':
                    dependencia_administrativa['Federal']['Não declarada'] += self.df['Matrículas'][c]
                    
        return dependencia_administrativa
    
    
    #total de matriculas por raça/cor.
    def get_total_matriculas_por_raca(self):
        
        matriculas_por_raca = {
            'Branca': 0,
            'Preta': 0,
            'Parda': 0,
            'Amarela': 0,
            'Indígena': 0,
            'Não declarada': 0
        }
        
        for c in range(len(self.df)):
            if self.df['Categoria 1'][c] == 'Branca':
                matriculas_por_raca['Branca'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Preta':
                matriculas_por_raca['Preta'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Parda':
                matriculas_por_raca['Parda'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Amarela':
                matriculas_por_raca['Amarela'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Indígena':
                matriculas_por_raca['Indígena'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Não declarada':
                matriculas_por_raca['Não declarada'] += self.df['Matrículas'][c]
                
        return matriculas_por_raca
    
    #percentual de matrículas por raça/cor por dependência administrativa.
    def get_porcentagem_matriculas_por_raca_e_dependencia_administrativa(self):
            
        dependencia_administrativa = self.get_matriculas_dependencia_administrativa()
        matriculas_por_raca_por_dependencia_administrativa = {
            'Estadual': {
                'Branca': 0,
                'Preta': 0,
                'Parda': 0,
                'Amarela': 0,
                'Indígena': 0,
                'Não declarada': 0
            },
            'Municipal': {
                'Branca': 0,
                'Preta': 0,
                'Parda': 0,
                'Amarela': 0,
                'Indígena': 0,
                'Não declarada': 0
            },
            'Privada': {
                'Branca': 0,
                'Preta': 0,
                'Parda': 0,
                'Amarela': 0,
                'Indígena': 0,
                'Não declarada': 0
            },
            'Federal': {
                'Branca': 0,
                'Preta': 0,
                'Parda': 0,
                'Amarela': 0,
                'Indígena': 0,
                'Não declarada': 0
            }     
            
        }
        
        for c in dependencia_administrativa:
            for c2 in dependencia_administrativa[c]:
                matriculas_por_raca_por_dependencia_administrativa[c][c2] = round((dependencia_administrativa[c][c2] / sum(dependencia_administrativa[c].values())) * 100, 2)
                
        #adiciona o simbolo de porcentagem ao final de cada valor.
        for c in matriculas_por_raca_por_dependencia_administrativa:
            for c2 in matriculas_por_raca_por_dependencia_administrativa[c]:
                matriculas_por_raca_por_dependencia_administrativa[c][c2] = str(matriculas_por_raca_por_dependencia_administrativa[c][c2]) + '%'
                
        return matriculas_por_raca_por_dependencia_administrativa
    
    #percentual total de matrículas por raça/cor.
    def get_matriculas_raca_porcentagem_total(self):
        matriculas_por_raca_porcentagem = {}
        matriculas_por_raca = self.get_total_matriculas_por_raca()
        total_matriculas = sum(matriculas_por_raca.values())
        
        for c in matriculas_por_raca:
            matriculas_por_raca_porcentagem[c] = round((matriculas_por_raca[c] / total_matriculas) * 100, 2)
            
        #adiciona o simbolo de porcentagem ao final de cada valor.
        for c in matriculas_por_raca_porcentagem:
            matriculas_por_raca_porcentagem[c] = str(matriculas_por_raca_porcentagem[c]) + '%'
            
        return matriculas_por_raca_porcentagem
    
   

matriculas = MatriculasSalvadorRaca(df=df)

print("Porcentagem de matrículas por raça:", matriculas.get_porcentagem_matriculas_por_raca_e_dependencia_administrativa())

