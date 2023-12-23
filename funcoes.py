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
    
def save(lista,filename):
    try:
        with open(filename,"w") as f:
            json.dump(lista,f,indent=4)
    except:
        print("\n nao foi possivel abrir o ficheiro")       
    else:
        print("\nFicheiro escrito com sucesso!")

def login():
    email = input("Introduza o seu email:")
    users = load("users.json")
    userlogado = None
    # se existe - mete na variavel user
    for user in users:
        if email == user["email"]:
            userlogado = user 
    if userlogado == None :
        userlogado = adicionar_usuario(email,users)


    create_menu(userlogado)
    # if user["email"] == "admin@gmail.com":
    #     palavraPass = input("Introdua a sua palavra pass:")
    #     #vai verificar se a palavra pass introduzida é igual a que está guardada na lista de utilizadores em Admin
    #     if palavraPass not in {"password"}: 
    #         print("Palavra pass errada tente novamente")
    #     if palavraPass == user["password"]:
    #         print(menu_admin)

        #adiciona o email a lista de users e ve se é admin ou cliente
    
def adicionar_usuario(email,users):
    user = {"email":email,"password":"","permission":"cliente"}
    users += [user]
    save(users,"users.json")
    return user

def make_reservation(user):
    nome = input("Introduza o seu nome: ")
    nif = input("Introduza o seu NIF: ")
    data = input("Introduza a data no formato aaaa-mm-dd: ")
    print("Horario: 18:00h as 23:00")
    hora= input("Introduza a hora prevista de chegada no formato hh:mm: ")
    adultos = int(input ("Quantos adultos são: "))
    criancas = int(input ("Quantas crianças são: "))
    #validar hora
    listReservations = load("reservation.json")
    reserva = [{"nome":nome,"nif":nif,"data":data,"hora":hora,"adultos":adultos,"criancas":criancas}]
    listReservations += reserva
    save(listReservations,"reservation.json")

def show_history(user):
    listReservations = load("reservation.json")
    print(listReservations)
    for reserva in listReservations:
        print(100 * "*")
        print()
        print("Data: " + reserva['data'],"\tHora: " + reserva['hora'])
        print()
        totalpessoas = reserva['adultos'] + reserva['criancas']
        print("Adultos: "+ str(reserva['adultos']),"\tCrianças: " + str(reserva['criancas']),"\tTotal de pessoas: " + str(totalpessoas) )
        print("Nome: " + reserva['nome'], "\tNIF: "+ reserva['nif'])
        print()
        print("Total a pagar:" + str(conta(reserva['adultos'],reserva['criancas'])))
        print()
    
def conta(adultos,criancas):
    adultostemp = 0
    criancastemp = 0
    adultostemp = adultos * 25
    criancastemp = criancas * 12
    return adultostemp + criancastemp

def create_menu(user):
    while True:
        print("\nMenu do Cliente:")
        print("1-Marcar Refeição")
        print("2-Ver Historico")
        print("3-Sair")

        opcao = input("Escolha uma opção")
        if opcao == "1":
            make_reservation(user)
        elif opcao == "2":
            show_history(user)
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
            total_close_day(admin)
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

def  total_close_day(adultos,criancas,admin):
    adultostemp = 0
    criancatemp = 0
    adultostemp += adultos
    criancatemp += criancas

#vai as reservas e v~e quantos adultos e crianças foram e soma tudo 

def view_closing_days(data,file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

    lista = [
    {'dia' : '1 de janeiro'},
    {'dia' : '25 de abril'},
    {'dia' : '25 de dezembro'}
    ]
#por mais dias
    save_data(lista, "close_days.json")
#mostra o ficheiro dos dias fecho    