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
    

def login(users):
    email = input("Introduza o seu email:")
    for user in users:
        if str(email) == users["email"]:
            print(create_menu)
        if email == "admin@gmail.com":
            palavraPass = input("Introdua a sua palavra pass:")
            #vai verificar se a palavra pass introduzida é igual a que está guardada na lista de utilizadores em Admin
            if palavraPass not in {"password"}: 
                print("Palavra pass errada tente novamente")
            if palavraPass == user["password"]:
                print(menu_admin)
    if email not in users:
        adicionar_usuario
        #adiciona o email a lista de users e v~e se é admin ou cliente

def adicionar_usuario(users):
    novo_email = input("Introduza o novo email:")
    nova_senha = input("Introduza a nova senha:")
    for user in users:
        if user["email"] == novo_email:
            print("Este email já está registrado. Tente novamente.")
            return
        
    novo_usuario = {"email": novo_email, "password": nova_senha}
    users.append(novo_usuario)
    print("Utilizador registrado com sucesso!")    

    
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
        print("2-Ver Historico")
        print("3-Sair")

        opcao = input("Escolha uma opção")
        if opcao == "1":
            make_reservation
        elif opcao == "2":
            see_historic
        elif opcao == "3":
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
            view_closing_days(admin)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")
#faz print das datas em que o rstaurante esta fechado 
def close_days(admin):
   load("close_days.json")
print(close_days)

#def view_closing_days(filename):
    #mostra o ficheiro dos dias fecho    