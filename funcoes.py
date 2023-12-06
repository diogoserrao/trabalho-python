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

def see_historic(user):
    
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
            
        else:
            print("Opção invalida")    
