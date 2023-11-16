import pandas as pd

from leitor_de_dados import LeitorDeDados

df = pd.DataFrame()
df = LeitorDeDados(df).get_dados_faixa_etaria_csv()


class MatriculasFaixaEtariaBahia:

    def __init__(self, df):
        self.df = df

    def get_matriculas_faixa_etaria_dependencia_administrativa(self):

        matriculas_faixa_etaria_dependencia_administrativa = {
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
                matriculas_faixa_etaria_dependencia_administrativa['Estadual'][self.df['Categoria 1'][c]] = self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Municipal':
                matriculas_faixa_etaria_dependencia_administrativa['Municipal'][self.df['Categoria 1'][c]] = self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Privada':
                matriculas_faixa_etaria_dependencia_administrativa['Privada'][self.df['Categoria 1'][c]] = self.df['Matrículas'][c]
            elif self.df['Categoria 2'][c] == 'Federal':
                matriculas_faixa_etaria_dependencia_administrativa['Federal'][self.df['Categoria 1'][c]] = self.df['Matrículas'][c]

        return matriculas_faixa_etaria_dependencia_administrativa

    def get_total_matriculas(self):
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

    def get_percentual_matriculas_faixa_etaria_dependencia_adm(self):

        matriculas_faixa_etaria = self.get_matriculas_faixa_etaria_dependencia_administrativa()
        total_matriculas_faixa_etaria = self.get_total_matriculas()

        percentual_matriculas_faixa_etaria_dependencia_adm = {
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
            percentual_matriculas_faixa_etaria_dependencia_adm['Estadual'][c] = round(
                matriculas_faixa_etaria['Estadual'][c] / total_matriculas_faixa_etaria['Estadual'] * 100, 2)

        for c in matriculas_faixa_etaria['Municipal']:
            percentual_matriculas_faixa_etaria_dependencia_adm['Municipal'][c] = round(
                matriculas_faixa_etaria['Municipal'][c] / total_matriculas_faixa_etaria['Municipal'] * 100, 2)

        for c in matriculas_faixa_etaria['Privada']:
            percentual_matriculas_faixa_etaria_dependencia_adm['Privada'][c] = round(
                matriculas_faixa_etaria['Privada'][c] / total_matriculas_faixa_etaria['Privada'] * 100, 2)

        for c in matriculas_faixa_etaria['Federal']:
            percentual_matriculas_faixa_etaria_dependencia_adm['Federal'][c] = round(
                matriculas_faixa_etaria['Federal'][c] / total_matriculas_faixa_etaria['Federal'] * 100, 2)

        # adiciona símbolo de porcentagem
        for c in percentual_matriculas_faixa_etaria_dependencia_adm['Estadual']:
            percentual_matriculas_faixa_etaria_dependencia_adm['Estadual'][c] = str(
                percentual_matriculas_faixa_etaria_dependencia_adm['Estadual'][c]) + '%'

        for c in percentual_matriculas_faixa_etaria_dependencia_adm['Municipal']:
            percentual_matriculas_faixa_etaria_dependencia_adm['Municipal'][c] = str(
                percentual_matriculas_faixa_etaria_dependencia_adm['Municipal'][c]) + '%'

        for c in percentual_matriculas_faixa_etaria_dependencia_adm['Privada']:
            percentual_matriculas_faixa_etaria_dependencia_adm['Privada'][c] = str(
                percentual_matriculas_faixa_etaria_dependencia_adm['Privada'][c]) + '%'

        for c in percentual_matriculas_faixa_etaria_dependencia_adm['Federal']:
            percentual_matriculas_faixa_etaria_dependencia_adm['Federal'][c] = str(
                percentual_matriculas_faixa_etaria_dependencia_adm['Federal'][c]) + '%'

        return percentual_matriculas_faixa_etaria_dependencia_adm

    def get_total_matriculas_faixa_etaria(self):

        tota_matriculas = self.get_matriculas_faixa_etaria_dependencia_administrativa()

        total_matriculas_faixa_etaria = {
            'Até 14 anos': 0,
            '15 a 17 anos': 0,
            '18 a 19 anos': 0,
            '20 a 24 anos': 0,
            '25 a 29 anos': 0,
            '30 a 34 anos': 0,
            '35 a 39 anos': 0,
            '40 anos ou mais': 0,
        }

        for c in tota_matriculas['Estadual']:
            total_matriculas_faixa_etaria[c] += tota_matriculas['Estadual'][c]
        for c in tota_matriculas['Municipal']:
            total_matriculas_faixa_etaria[c] += tota_matriculas['Municipal'][c]
        for c in tota_matriculas['Privada']:
            total_matriculas_faixa_etaria[c] += tota_matriculas['Privada'][c]
        for c in tota_matriculas['Federal']:
            total_matriculas_faixa_etaria[c] += tota_matriculas['Federal'][c]

        return total_matriculas_faixa_etaria

    def get_percentual_matriculas_faixa_etaria(self):

        percentual_matriculas_faixa_etaria = {
            'Até 14 anos': 0,
            '15 a 17 anos': 0,
            '18 a 19 anos': 0,
            '20 a 24 anos': 0,
            '25 a 29 anos': 0,
            '30 a 34 anos': 0,
            '35 a 39 anos': 0,
            '40 anos ou mais': 0,
        }

        total_matriculas_faixa_etaria = self.get_total_matriculas_faixa_etaria()

        for c in total_matriculas_faixa_etaria:
            percentual_matriculas_faixa_etaria[c] = round(
                total_matriculas_faixa_etaria[c] / sum(total_matriculas_faixa_etaria.values()) * 100, 2)

        # adiciona símbolo de porcentagem
        for c in percentual_matriculas_faixa_etaria:
            percentual_matriculas_faixa_etaria[c] = str(
                percentual_matriculas_faixa_etaria[c]) + '%'

        return percentual_matriculas_faixa_etaria


matriculas = MatriculasFaixaEtariaBahia(df)

print(matriculas.get_total_matriculas_faixa_etaria())