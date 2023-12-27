import json
from funcoes import load, show_reservation, conta, euros


def menu_admin(admin):
    while True:
        print("\nMenu do Administrador:")
        print("1. Definições")
        print("2. Dias Fechados")
        print("3. Extrato de reservas por dia")  # mostrar as reservas feitas
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("\nPreço por Adulto: 25")
            print("Preço por Criança: 12.5")
            print("Ocupação Máxima: 64")
            print("Número de Mesas: 16")
            print("Dia de Folga: Quarta-Feira")
            input("Prima uma tecla qualquer para voltar")
            # o programa devia voltar para cima a mostrar o menu de admin

        elif opcao == '2':
            show_close_days()
        elif opcao == '3':
            total_close_day()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")
# faz print das datas em que o rstaurante esta fechado


def show_close_days():
    days = load("closedays.json")
    print()
    for dia in days:
        print(dia)
    input("Prima uma tecla qualquer para voltar")


def total_close_day():
    reservas = load("reservation.json")
    print()
    data = input("Introduza o dia que deseja ver: ")
    temreserva = False
    print("\nReservas adicionadas no dia " + data)
    print()
    for reserva in reservas:
        if data == reserva["data"]:
            show_reservation(reserva, True)
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

    for reserva in reservas:
        if reserva["data"] == data:
            total += conta(reserva["adultos"], reserva["criancas"])
            totalpessoas += reserva["adultos"] + reserva["criancas"]
            totaladultos += reserva["adultos"]
            totalcriancas += reserva["criancas"]
    print("Estatistica")
    print("Total faturado: " + euros(total))
    print("\nTotal de adultos: " + str(totaladultos))
    print("\nTotal de criancas: " + str(totalcriancas))
    print("\nTotal de pessoas: " + str(totalpessoas))
    input("Prima uma tecla qualquer para voltar")
    # vai as reservas e ve quantos adultos e crianças foram e soma tudo


def view_closing_days(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)
