'''
from lib2to3.pgen2.pgen import DFAState
import sys

#adicionando o caminho do módulo 'matriculas_salvador' ao sys.path
sys.path.append('/home/rafael/Documents/EJA/dados-censo-educacao/Salvador/dados-2022')

import matriculas_salvador_sexo


#instanciando a classe
matriculas = matriculas_salvador_sexo.MatriculasSalvadorSexo(df=matriculas_salvador_sexo.df)

#mostra o total de matrículas por sexo feminino
print("O total de matrículas por sexo feminino em Salvador, no ano de 2022, é de:", matriculas.get_total_feminino())

#mostra o total de matrículas por sexo masculino
print("O total de matrículas por sexo masculino em Salvador, no ano de 2022, é de:", matriculas.get_total_masculino())

#imprime o total de matrículas de ambos os sexos
print("O total de matrículas em Salvador, no ano de 2022, é de:", matriculas.get_total_matriculas())

#imprime o total de matrículas por categoria 2, de acordo com o sexo feminino
print("O total de matrículas do sexo feminino por dependência administrativa em Salvador, no ano de 2022, é de:", matriculas.get_total_matriculas_categoria_2_feminino())

#imprime o total de matrículas por categoria 2, de acordo com o sexo masculino
print("O total de matrículas do sexo masculino por dependência administrativa em Salvador, no ano de 2022, é de:", matriculas.get_total_matriculas_categoria_2_masculino())

#imprime o percentual de matrículas do sexo feminino
print("O percentual de matrículas do sexo feminino em Salvador, no ano de 2022, é de:", matriculas.get_percentual_matriculas_feminino(), "%")

#imprime o percentual de matrículas do sexo masculino
print("O percentual de matrículas do sexo masculino em Salvador, no ano de 2022, é de:", 100 - matriculas.get_percentual_matriculas_feminino(), "%") 

'''