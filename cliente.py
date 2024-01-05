from funcoes import show_reservation, euros, conta, load, save, limpar_tela,espera_utilizador,pedir_data_valida
from datetime import datetime,date

def make_reservation(user):
    listReservations = load("reservation.json")
    nome = input("Introduza o seu nome: ")
    nif = pedir_nif()
    # Verificação da data que nao pode ser numa quarta feira
    data = pedir_data(user["email"])
    print("Horario: 18:00h as 00:00h")
    #hora = input("Introduza a hora prevista de chegada no formato hh:mm: ")
    hora = pedir_horas()
    adultos = pedir_numero("Quantos adultos são: ")
    criancas = pedir_numero("Quantas criancas sao: ")    
    reserva = {"nome": nome, "nif": nif, "data": data, "hora": hora,
               "adultos": adultos, "criancas": criancas, "email": user["email"]}
    listReservations += [reserva]
    show_reservation(reserva, False)
    print("       Dados de faturação:")
    print()
    print("Nome: " + nome + " com NIF:" + nif)
    print("\nTotal a pagar:" +
          euros(conta(reserva['adultos'], reserva['criancas'])))
    confirmacao = input("Deseja confirmar a reserva? s/n: ")
    if confirmacao.lower() == "s":
        save(listReservations, "reservation.json")


def verificacao_do_dia ():
    diaFechado = 2
    diaAtual = datetime.now()
    if diaAtual.weekday() == diaFechado:
        print("Restaurante fechado")
    else:
        print("data valida")

    
def pedir_horas():
    hora_introduzida = ""
    while True:
        hora_introduzida = input("Introduza a hora prevista de chegada no formato hh:mm: ")

        partes = hora_introduzida.split(':')    
        if len(partes) == 2:
            hora, minutos = partes
            if hora.isdigit() and minutos.isdigit():
                if 18 <= int(hora) <= 23 and 0 <= int(minutos) <= 59:
                    return hora_introduzida
        
        print("Formato de hora inválido. Por favor, introduza novamente.\n")
        
def pedir_nif():
    nif = ""
    while True:
        nif = input("Introduza o seu NIF: ")
        if nif.isdigit() and len(nif) == 9:
            return nif

        print("Formato de NIF inválido. Por favor, introduza novamente.\n")

def pedir_data(email):
    listReservations = load("reservation.json")
    pedenovamente = True
    data = ""
    while pedenovamente == True:
        data = pedir_data_valida()
        #data = input("Introduza outra data no formato aaaa-mm-dd: ")
        valido = True
        for reserva in listReservations:
            if data == reserva["data"] and email == reserva["email"]: 
                print("Ja existe uma marcação para esta data\n")
               
                valido = False
                break   
        if valido == True:
            pedenovamente = False
    return data

def pedir_numero(dados):
    numero = 0
    while True:
        numero = input(dados)
        if numero.isdigit():
            return int(numero)
        print(" Valores inválidos. Por favor, introduza novamente.\n")


def menu_client(user):
    while True:
        limpar_tela()
        print("\nMenu do Cliente:")
        print("1-Marcar Refeição")
        print("2-Ver Historico")
        print("3-Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            make_reservation(user)
        elif opcao == "2":
            show_client_history(user)
        elif opcao == "3":
            break
        else:
            print("Opção invalida")


def show_client_history(user):
    listReservations = load("reservation.json")

    for reserva in listReservations:
        if reserva["email"] == user["email"]:
            show_reservation(reserva, True)
    espera_utilizador()