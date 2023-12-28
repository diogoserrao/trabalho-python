from login import login
from funcoes import limpar_tela
from admin import menu_admin
from cliente import menu_client

while True:
    limpar_tela()
    user = login()

    if user["permission"] == "admin":
        menu_admin()
    else:
        menu_client(user)

