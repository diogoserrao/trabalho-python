import json
from funcoes import load, show_reservation, conta, euros, espera_utilizador, save, limpar_tela, pedir_data_valida


def menu_admin():
    while True:
        limpar_tela()
        print("\nMenu do Administrador:")
        print("1. Definições")
        print("2. Dias Fechados")
        print("3. Extrato de reservas por dia")  # mostrar as reservas feitas
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            show_definitions()
            espera_utilizador()
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

def show_definitions():
    defenicoes = load("definitions.json")
    print("\nPreço por Adulto: " + str(defenicoes["preco_adulto"]))
    print("Preço por Criança: " + str(defenicoes["preco_crianca"]))
    print("Ocupação Máxima: " + str(defenicoes["ocupacao_maxima"]))
    print("Número de Mesas: " + str(defenicoes["numero_mesas"]))
    print("Dia de Folga: " + defenicoes["dia_folga"])

def show_close_days():
    days = load("closedays.json")
    print()
    for dia in days:
        print(dia)
    resposta = input("Deseja acrescentar agluma data? s/n: ")
    if resposta.lower() == "s":
        data_adicionada = pedir_data_valida()
        days += [data_adicionada]
        save(days,"closedays.json")

    espera_utilizador()



def total_close_day():
    reservas = load("reservation.json")
    print()
    data = pedir_data_valida()
    temreserva = False
    print("\nReservas adicionadas no dia " + data)
    print()
    for reserva in reservas:
        if data == reserva["data"]:
            show_reservation(reserva, True)
            temreserva = True
    estatistica(data)         
    if temreserva == False:
        print("Não existe nenhuma reserva para esta data")
        print()
    espera_utilizador()


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
    # vai as reservas e ve quantos adultos e crianças foram e soma tudo


def view_closing_days(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)
