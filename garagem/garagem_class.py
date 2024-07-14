class Carro:
    nome =''
    cor=''
    potencia = int
    fabricante = ''
    ano = int
    nome_dono = ''


brasilia = Carro()

brasilia.nome = 'Brasilia'
brasilia.cor = 'branca'
brasilia.potencia = 120
brasilia.fabricante = 'VW'
brasilia.ano = 1981
brasilia.nome_dono = 'Gustavo'



#-----------------------------------------------------

#class Devices:
    #self é mesma coisa que o this do js etc...
#    def __init__(self, id):
#        self.id = id
#        self.descricao = ''
#        self.processador = ''
#        self.ip = ''
    
#    def __str__(self): #quando alguem chamar a classe em questao, e quiser exibir, vai aparecer esse conteudo
#        return self.descricao


#irrigacao = Devices('0x01')
#irrigacao.processador = 'esp32'
#irrigacao.descricao = 'controlador irrigacao 4 saidas wi-fi'


#----------------------------------------------------
from tuning_class import Tuning


class Garagem:
    carros = []

    def __init__(self, nome, marca, ano,chassis,funcionando):
        self._nome = nome.title() #deixa primeira letra letra maiuscula
        self._marca = marca.upper() #deixa tudo maiusculo
        self._ano = ano
        self._funcionando = funcionando
        self._numero_chassis = chassis #usar undeline antes, como convencao para mostra rque é um valor privado
        self._potencia = None
        Garagem.carros.append(self)

    def listar_carros():
        print('Sua garagem tem os seguintes carros:')
        print(f'{'Nome'.ljust(20)} | {'Marca'.ljust(20)} | {'Ano'.ljust(10)} | Status')
        print('-'*100)
        for carro in Garagem.carros:
            print(f'{carro._nome.ljust(20)} | {carro._marca.ljust(20)} | {str(carro._ano).ljust(10)} | atualmente ele(a) está {carro.get_funcionando.ljust(15)}')
    


    @property
    def get_funcionando(self):  # acessa a variável interna e formata a saída
        return 'funcionando' if self._funcionando else 'estragado'

    def alterar_funcionamento(self, state):
        self._funcionando = state

    def definir_potencia(self, potencia):
        if self._potencia is None:
            self._potencia = Tuning(potencia)
        else:
            self._potencia.atualizar_potencia(potencia)  # Supondo que Tuning tenha um método para atualizar a potência

    @property
    def tipo_preparacao(self):
        if self._potencia is None:
            return f'{self._nome} potencia nao definida'
        
        if  self._potencia.cv_atual < 100:
            return f'{self._nome} -> {self._potencia.cv_atual}cv -> Perde até pra 1.0'
        elif self._potencia.cv_atual >= 100 and self._potencia.cv_atual < 200:
            return f'{self._nome} -> {self._potencia.cv_atual}cv -> Dá pra se divertir'
        elif self._potencia.cv_atual >= 200:
            return f'{self._nome} -> {self._potencia.cv_atual}cv -> motor forte'
        else:
            return 'potencia nao definida'
    
#brasilia = Garagem('brasilia', 'Vw', 1981, 123456,True)
#brasilia.alterar_funcionamento(True)
#Garagem.listar_carros()