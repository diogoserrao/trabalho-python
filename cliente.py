from funcoes import show_reservation, euros, conta, load, save


def make_reservation(user):
    nome = input("Introduza o seu nome: ")
    nif = input("Introduza o seu NIF: ")
    data = input("Introduza a data no formato aaaa-mm-dd: ")
    print("Horario: 18:00h as 23:00")
    hora = input("Introduza a hora prevista de chegada no formato hh:mm: ")
    adultos = int(input("Quantos adultos são: "))
    criancas = int(input("Quantas crianças são: "))
    # validar hora
    listReservations = load("reservation.json")
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
