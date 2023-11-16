import pandas as pd

from leitor_de_dados import LeitorDeDados

df = pd.DataFrame()
df = LeitorDeDados(df).get_dados_cor_raca_csv()


class MatriculasCorRacaBahia:

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

        for c in range(len(self.df)):
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
                    dependencia_administrativa['Privada']['Não declarada'] += self.df['Matrículas'][c]

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

    def get_porcentagem_matriculas_dependencia_administrativa(self):

        matriculas_dependencia_administrativa = self.get_matriculas_dependencia_administrativa()

        porcentagem_matriculas_dependencia_administrativa = {
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

        for dependencia_administrativa in matriculas_dependencia_administrativa:
            for cor_raca in matriculas_dependencia_administrativa[dependencia_administrativa]:
                porcentagem_matriculas_dependencia_administrativa[dependencia_administrativa][cor_raca] = round((
                                                                                                                        matriculas_dependencia_administrativa[
                                                                                                                            dependencia_administrativa][
                                                                                                                            cor_raca] / sum(
                                                                                                                    matriculas_dependencia_administrativa[
                                                                                                                        dependencia_administrativa].values())) * 100,
                                                                                                                2)

        for dependencia_administrativa in porcentagem_matriculas_dependencia_administrativa:
            for raca_cor in porcentagem_matriculas_dependencia_administrativa[dependencia_administrativa]:
                porcentagem_matriculas_dependencia_administrativa[dependencia_administrativa][raca_cor] = str(
                    porcentagem_matriculas_dependencia_administrativa[dependencia_administrativa][raca_cor]) + '%'

        return porcentagem_matriculas_dependencia_administrativa

    def get_total_matriculas_por_raca(self):

        total_matriculas_por_raca = {
            'Branca': 0,
            'Preta': 0,
            'Parda': 0,
            'Amarela': 0,
            'Indígena': 0,
            'Não declarada': 0
        }

        for c in range(len(self.df)):
            if self.df['Categoria 1'][c] == 'Branca':
                total_matriculas_por_raca['Branca'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Preta':
                total_matriculas_por_raca['Preta'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Parda':
                total_matriculas_por_raca['Parda'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Amarela':
                total_matriculas_por_raca['Amarela'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Indígena':
                total_matriculas_por_raca['Indígena'] += self.df['Matrículas'][c]
            elif self.df['Categoria 1'][c] == 'Não declarada':
                total_matriculas_por_raca['Não declarada'] += self.df['Matrículas'][c]

        return total_matriculas_por_raca

    def get_matriculas_raca_porcentagem_total(self):
        matriculas_por_raca_porcentagem = {}
        matriculas_por_raca = self.get_total_matriculas_por_raca()
        total_matriculas = sum(matriculas_por_raca.values())

        for c in matriculas_por_raca:
            matriculas_por_raca_porcentagem[c] = round((matriculas_por_raca[c] / total_matriculas) * 100, 2)

        for c in matriculas_por_raca_porcentagem:
            matriculas_por_raca_porcentagem[c] = str(matriculas_por_raca_porcentagem[c]) + '%'

        return matriculas_por_raca_porcentagem


matriculas = MatriculasCorRacaBahia(df)

print(matriculas.get_total_matriculas_por_raca())
