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
    

    
def make_reservation(user):
    
    data = input("Introduza a data no formato aaaa-mm-dd: ")
    hora = input("Horário previsto: ")
    dia = input("Introduza a hora prevista de chegada no formato hh:mm: ")
    #se não estiver sobreposta pergunta quantas pessoas são
    #if True :
        #pessoas = input("Indique o numero de pessoas (max 12): ")
        #criancas = input("INdique o numero de crianças: ")
   

def see_historic(user):
    try:
        with open("historico.json", 'w') as f:
            data =json.historico(f)
    except:
        print("\nErro: não foi possível abrir o ficheiro")
        return[]
    else:
        return data
    
def create_menu(user):
    while True:
        print("\nMenu do Cliente:")
        print("1-Marcar Refeição")
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

def fatura(user):
    nome = input("indique o seu nome: ")
    nif = input("Introduza o seu NIF: ")


def menu_admin(admin):
     while True:
        print("\nMenu do Administrador:")
        print("1. Definições")
        print("2. Fecho do dia")
        print("3. Extrato de reservas por dia")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
           print("Preço por Adulto: 25")
           print("Preço por Criança: 12.5")
           print("Ocupação Máxima: 64")
           print("Número de Mesas: 16")
           print("Dia de Folga: Quarta-Feira")
           print("Prima uma tecla qualquer para voltar")
           #o programa devia voltar para cima a mostrar o menu de admin

        elif opcao == '2':
            close_day(admin)
        elif opcao == '3':
            view_last_closing_days(admin)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")
#faz print das datas em que o rstaurante esta fechado 
def close_days(admin):
   load("close_days.json")
print(close_days)

    
       