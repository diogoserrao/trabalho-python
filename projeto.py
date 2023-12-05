import json


informacao = int(input("Administrador pressione 1\nCliente pressione 2\nnº:"))

def autenticacao(informacao):
    if informacao == 1:
        email = input("Introduza o seu email:")
        senha = input("Introduza a sua senha:")
    elif informacao == 2:
        email2= input("Introduza o seu email:")

    return informacao

print(autenticacao(informacao))

