import matriculas_salvador_sexo

matriculas_sexo = matriculas_salvador_sexo.MatriculasSalvadorSexo(df=matriculas_salvador_sexo.df)

#função transforma get_matriculas_por_sexo() em forma de tabela.
def get_matriculas_por_sexo_tabela():
    matriculas_por_sexo = matriculas_sexo.get_matriculas_por_sexo()
    
    print('Total de matrículas por sexo:')
    print('Feminino:')
    for c in matriculas_por_sexo['Feminino']:
        print(f'{c}: {matriculas_por_sexo["Feminino"][c]}')
    
    print('\nMasculino:')
    for c in matriculas_por_sexo['Masculino']:
        print(f'{c}: {matriculas_por_sexo["Masculino"][c]}')
        
#função transforma get_matriculas_por_sexo_porcentagem() em forma de tabela.
def get_matriculas_por_sexo_porcentagem_tabela():
    matriculas_por_sexo_porcentagem = matriculas_sexo.get_matriculas_por_sexo_porcentagem()
    
    print('Percentual de matrículas por sexo:')
    print('Feminino:')
    for c in matriculas_por_sexo_porcentagem['Feminino']:
        print(f'{c}: {matriculas_por_sexo_porcentagem["Feminino"][c]}')
    
    print('\nMasculino:')
    for c in matriculas_por_sexo_porcentagem['Masculino']:
        print(f'{c}: {matriculas_por_sexo_porcentagem["Masculino"][c]}')

get_matriculas_por_sexo_porcentagem_tabela()
print('------------------------------------')
get_matriculas_por_sexo_tabela()