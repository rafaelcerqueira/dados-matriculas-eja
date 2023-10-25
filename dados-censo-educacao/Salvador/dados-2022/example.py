'''        
    def get_matriculas_feminino(self):
        matriculas_feminino = {}
        for c in range(len(self.df)):
            if self.df['Categoria 1'][c] == 'Feminino':
                matriculas_feminino[self.df['Categoria 2'][c]] = self.df['Matrículas'][c]
        return matriculas_feminino
    
    def get_matriculas_masculino(self):
        matriculas_masculino = {}
        for c in range(len(self.df)):
            if self.df['Categoria 1'][c] == 'Masculino':
                matriculas_masculino[self.df['Categoria 2'][c]] = self.df['Matrículas'][c]
        return matriculas_masculino
    
    def get_total_feminino(self):
        matriculas_feminino = self.get_matriculas_feminino()
        total_feminino = sum(matriculas_feminino.values())
        return total_feminino
    
    def get_total_masculino(self):
        matriculas_masculino = self.get_matriculas_masculino()
        total_masculino = sum(matriculas_masculino.values())
        return total_masculino
    
    #total de matrículas dos alunos do sexo feminino e masculino
    def get_total_matriculas(self):
        total_matriculas = self.get_total_feminino() + self.get_total_masculino()
        return total_matriculas

    #Total de matrículas por Categoria 2, de acordo com sexo feminino
    def get_total_matriculas_categoria_2_feminino(self):
        matriculas_categoria_2_feminino = {}
        for c in range(len(self.df)):
            if self.df['Categoria 1'][c] == 'Feminino':
                matriculas_categoria_2_feminino[self.df['Categoria 2'][c]] = self.df['Matrículas'][c]
        return matriculas_categoria_2_feminino
    
    #Total de matrículas por Categoria 2, de acordo com sexo masculino
    def get_total_matriculas_categoria_2_masculino(self):
        matriculas_categoria_2_masculino = {}
        for c in range(len(self.df)):
            if self.df['Categoria 1'][c] == 'Masculino':
                matriculas_categoria_2_masculino[self.df['Categoria 2'][c]] = self.df['Matrículas'][c]
        return matriculas_categoria_2_masculino
    
    #percentual de matrículas do sexo feminino.
    def get_percentual_matriculas_feminino(self):
        percentual_matriculas_feminino = (self.get_total_feminino() / self.get_total_matriculas()) * 100  
        #arredondando o valor para duas casas decimais
        percentual_matriculas_feminino = round(percentual_matriculas_feminino, 2)
        return percentual_matriculas_feminino
    
    #percentual de matrículas do sexo masculino.
    def get_percentual_matriculas_masculino(self):
        percentual_matriculas_masculino = (self.get_total_masculino() / self.get_total_matriculas()) * 100
        #arredondando o valor para duas casas decimais
        percentual_matriculas_masculino = round(percentual_matriculas_masculino, 2)
        return percentual_matriculas_masculino
    
    #função que chama o método get_matriculas_feminino() e get_matriculas_masculino()
    def get_total_matriculas_categoria_2(self):
        matriculas_categoria_2 = {}
        matriculas_categoria_2.update(self.get_matriculas_feminino())
        matriculas_categoria_2.update(self.get_matriculas_masculino())
        
            
    
    
    
#instaciando a classe
matriculas = MatriculasSalvadorSexo(df=df)

#função que retorna o total de matrículas por sexo feminino em forma de tabela.
def imprime_tabela_matriculas_feminino():
    
    print('O total de matrículas do sexo feminino em Salvador é de:')
    #loop que percorre o dicionário matriculas_feminino e imprime o total de matrículas por sexo feminino em forma de tabela.
    for c in matriculas.get_matriculas_feminino():
        print(c, matriculas.get_matriculas_feminino()[c])

def imprime_tabela_matriculas_masculino():
    print('O total de matrículas do sexo masculino em Salvador é de:')
    #loop que percorre o dicionário matriculas_masculino e imprime o total de matrículas por sexo masculino em forma de tabela.
    for c in matriculas.get_matriculas_masculino():
        print(c, matriculas.get_matriculas_masculino()[c])

def imprime_tabela_percentual_matriculas():
    #loop percorre o dicionário matriculas_feminino e imprime o percentual de matrículas por sexo feminino em forma de tabela.
    print('O percentual de matrículas do sexo feminino em Salvador é de:')
    for c in matriculas.get_matriculas_feminino():
        print(c, matriculas.get_matriculas_feminino()[c] / matriculas.get_total_matriculas() * 100)
        


#mostra o total de matrículas por sexo feminino:
print('Masculino:', matriculas.get_matriculas_masculino())
print('Feminino:', matriculas.get_matriculas_feminino())
print('------------------------------------------------------------------------------------------------------------------')
print("O total de matrículas por sexo feminino em Salvador, no ano de 2022, é de:", matriculas.get_total_feminino())
print("O total de matrículas por sexo masculino em Salvador, no ano de 2022, é de:", matriculas.get_total_masculino())
print("O total de matrículas em Salvador, no ano de 2022, é de:", matriculas.get_total_matriculas())

        
'''