from funcoes import load, adicionar_usuario
from admin import menu_admin
from cliente import menu_client


def login():
    email = input("Introduza o seu email:")
    users = load("users.json")
    userlogado = None
    # se existe - mete na variavel user
    for user in users:
        if email == user["email"]:
            userlogado = user
    if userlogado == None:
        userlogado = adicionar_usuario(email, users)
    if userlogado["permission"] == "cliente":
        menu_client(userlogado)
    else:
        palavraPass = ""
        while palavraPass != userlogado["password"]:
            palavraPass = input("Introdua a sua palavra pass:")
            # vai verificar se a palavra pass introduzida é igual a que está guardada na lista de utilizadores em Admin
            if palavraPass == userlogado["password"]:
                menu_admin(userlogado)
            else:
                print("Palavra pass errada tente novamente")

        # adiciona o email a lista de users e ve se é admin ou cliente
# print(euros(1))
login()

# adicionar_usuario(listUsers)
# create_menu(user)                NAO EXISTE
# make_reservation(user)
# show_history(user)
# fatura(user)
# menu_admin(user)
# show_close_days()
# total_close_day()
# view_closing_days("close_days.json")
# print(close_days(admin):)
