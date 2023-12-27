import json


def load(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except:
        print("\nErro: não foi possível abrir o ficheiro")
        return []
    else:
        return data


def save(lista, filename):
    try:
        with open(filename, "w") as f:
            json.dump(lista, f, indent=4)
    except:
        print("\n nao foi possivel abrir o ficheiro")


def adicionar_usuario(email, users):
    user = {"email": email, "password": "", "permission": "cliente"}
    users += [user]
    save(users, "users.json")
    return user


def show_reservation(reserva, show_total):
    print(100 * "*")
    print()
    print("Data: " + reserva['data'], "\tHora: " + reserva['hora'])
    print()
    totalpessoas = reserva['adultos'] + reserva['criancas']
    print("Adultos: " + str(reserva['adultos']), "\tCrianças: " + str(
        reserva['criancas']), "\tTotal de pessoas: " + str(totalpessoas))
    print("Nome: " + reserva['nome'], "\tNIF: " + reserva['nif'])
    print()
    if show_total == True:
        print("Total a pagar: " +
              euros(conta(reserva['adultos'], reserva['criancas'])))
        print()


def euros(valor):
    return "%.2f" % valor + "€"


def conta(adultos, criancas):
    adultostemp = 0
    criancastemp = 0
    adultostemp = adultos * 25
    criancastemp = criancas * 12.5
    return adultostemp + criancastemp
