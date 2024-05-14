# Questão 4: Lógica de Programação
# Desenvolva um trecho de código (Em qualquer linguagem, mas preferencialmente JavaScript)
# para verificar se pacientes devem ser encaminhados para urgência ou emergência.
# Requisitos:
# 1. Defina uma coleção de objetos representando pacientes, com os seguintes atributos:
# “nome”, “idade” e “condição”
# 2. Escreva um método que identifique na coleção, segundo o critério a seguir, se o
# paciente deve ser encaminhado para urgência ou emergência:
# a. Pacientes com dores agudas no peito, fraturas expostas, acidentes de trânsito,
# ferimentos à bala ou com idade superior a 70 anos devem ser encaminhados
# para emergência.
# b. Pacientes com fraturas não expostas, cólicas renais, luxações e torções devem
# ser encaminhados para urgência.

#OBS minha linguagem atual


import os

class Paciente:
    def __init__ (self):
        self._nome = None
        self._idade = None
        self._condicao = None

    def avaliacao(self):
        if (self._idade >= 70):
            return "Paciente encaminhado para EMERGENCIA"
        
        if (self._condicao == "dores agudas no peito" or self._condicao == "fraturas expostas" or self._condicao == "acidentes de trânsito" or self._condicao =="ferimentos à bala"):
            return "Paciente encaminhado para EMERGENCIA"
        elif (self._condicao == "fraturas não expostas" or self._condicao == "cólicas renais" or self._condicao == "luxações" or self._condicao == "torções"):
            
            return "Paciente encaminhado para Urgencia"

    @property
    def atribui_nome(self):
        return self._nome
    
    @atribui_nome.setter
    def atribui_nome(self, nome):
        self._nome = nome
    
    @property
    def atribui_idade(self):
        return self._idade
    
    @atribui_idade.setter
    def atribui_idade(self, idade):
        self._idade = idade
    
    @property
    def atribui_condicao(self):
        return self._condicao
    
    @atribui_condicao.setter
    def atribui_condicao(self, condicao):
        self._condicao = condicao
    
def recebe_condicao():
    print("1- dores agudas no peito")
    print("2- fraturas expostas")
    print("3- fraturas não expostas")
    print("4- acidentes de trânsito")
    print("5- ferimentos à bala")
    print("6- cólicas renais")
    print("7- luxações")
    print("8- torções")
    condicao = input("Selecione a condição do paciente: ")

    if condicao == "1":
        os.system('cls')
        return "dores agudas no peito"
    elif condicao == "2":
        os.system('cls')
        return "fraturas expostas"
    elif condicao == "3":
        os.system('cls')
        return "fraturas não expostas"
    elif condicao == "4":
        os.system('cls')
        return "acidentes de trânsito"
    elif condicao == "5":
        os.system('cls')
        return "ferimentos à bala"
    elif condicao == "6":
        os.system('cls')
        return "cólicas renais"
    elif condicao == "7":
        os.system('cls')
        return "luxações"
    elif condicao == "8":
        os.system('cls')
        return "torções"
    else:
        os.system('cls')
        return "Condição Inválida"


while(True):
    paciente = Paciente()
    paciente.atribui_nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    idade = int(idade)
    paciente.atribui_idade = idade
    condicao = recebe_condicao()
    paciente.atribui_condicao = condicao



    print(paciente._nome)      
    print(paciente._idade)
    print(paciente._condicao)
    print(paciente.avaliacao())
    
    opcao = input("\nDigite s para sair ou qualquer tecla para continuar: ")
    os.system('cls')
    
    if opcao == 's':
        break



