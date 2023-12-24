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
    if userlogado["permission"] == "cliente":
        menu_client(userlogado)
    else:
        palavraPass = ""
        while palavraPass != userlogado["password"]:
            palavraPass = input("Introdua a sua palavra pass:")
            #vai verificar se a palavra pass introduzida é igual a que está guardada na lista de utilizadores em Admin
            if palavraPass == userlogado["password"]: 
                menu_admin(userlogado)
            else: 
                print("Palavra pass errada tente novamente")


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
        show_reservation(reserva)

def show_reservation(reserva):
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

def menu_client(user):
    while True:
        print("\nMenu do Cliente:")
        print("1-Marcar Refeição")
        print("2-Ver Historico")
        print("3-Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            make_reservation(user)
        elif opcao == "2":
            show_history(user)
        elif opcao == "3":
            break
        else:
            print("Opção invalida")  

#def fatura(user):
    #nome = input("indique o seu nome: ")
    #nif = input("Introduza o seu NIF: ")

def menu_admin(admin):
     while True:
        print("\nMenu do Administrador:")
        print("1. Definições")
        print("2. Dias Fechados")
        print("3. Extrato de reservas por dia")  #mostrar as reservas feitas 
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
           print("\nPreço por Adulto: 25")
           print("Preço por Criança: 12.5")
           print("Ocupação Máxima: 64")
           print("Número de Mesas: 16")
           print("Dia de Folga: Quarta-Feira")
           input("Prima uma tecla qualquer para voltar")
           #o programa devia voltar para cima a mostrar o menu de admin

        elif opcao == '2':
            show_close_days()  
        elif opcao == '3':
            total_close_day()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")
#faz print das datas em que o rstaurante esta fechado 
            
def show_close_days():
    days = load("closedays.json")
    print()
    for dia in days:
        print(dia)
    input("Prima uma tecla qualquer para voltar")
    
def  total_close_day():
    reservas = load("reservation.json")
    print()
    data = input("Introduza o dia que deseja ver: ")
    temreserva = False
    print("\nReservas adicionadas no dia "+ data)
    print()
    for reserva in reservas:
        if data == reserva["data"]:
            show_reservation(reserva)
            estatistica(data)
            temreserva = True
    if temreserva == False:
        print("Não existe nenhuma reserva para esta data")
        print()    
    input("Prima uma tecla qualquer para voltar")

def estatistica(data):
    reservas = load("reservation.json") 
    total = 0
    totalpessoas = 0
    totaladultos = 0
    totalcriancas = 0
   
    for reserva in reservas :
        if reserva["data"] == data:
            total += conta(reserva["adultos"], reserva["criancas"]) 
            totalpessoas += reserva["adultos"] + reserva["criancas"]
            totaladultos += reserva["adultos"]
            totalcriancas += reserva["criancas"]
    print("Estatistica")
    print("Total faturado: "+ str(total))
    print("\nTotal de adultos: "+ str(totaladultos))
    print("\nTotal de criancas: "+ str(totalcriancas))
    print("\nTotal de pessoas: "+ str(totalpessoas))
    input("Prima uma tecla qualquer para voltar")
    #vai as reservas e ve quantos adultos e crianças foram e soma tudo 

def view_closing_days(data,file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

    