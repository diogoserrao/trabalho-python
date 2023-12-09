import json



def load(filename):
    try:
        with open(filename, 'r') as f:
            data =json.load(f)
    except:
        print("\nErro: não foi possível abrir o ficheiro")
        return[]
    else:
        return data
    
def make_reservaton(user):
    data = input("Introduza a data no formato aaaa-mm-dd: ")
    hora = input("Horário previsto: ")
    dia = input("Introduza a hora prevista de chegada no formato hh:mm: ")
    #se não estiver sobreposta pergunta quantas pessoas são
    if True :
        pessoas = input("Indique o numero de pessoas (max 12): ")
        criancas = input("INdique o numero de crianças: ")
   

def see_historic(user):
    try:
        with open("historico.json", 'r') as f:
            data =json.historico(f)
    except:
        print("\nErro: não foi possível abrir o ficheiro")
        return[]
    else:
        return data
    
def create_menu(user):
    while True:
        print("\nMarcar Refeição")
        print("Ver Historico")
        print("Sair")

        opcao = input("Escolha uma opção")
        if opcao == 1:
            print(make_reservaton)
        elif opcao == 2:
            print(see_historic)
        elif opcao == 3:
            break
        else:
            print("Opção invalida")    
