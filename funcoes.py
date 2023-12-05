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
    
userFilename = "users.json"

listUsers = load(userFilename)
print(listUsers)

for user in listUsers:
    if user['permission'] == 'admin':
        print("Admin")
    else:
        print("client")

'''
def credenciais(email,senha):
    email = input("Introduza o seu email:")
    senha = input("Introduza a sua senha:")
    if senha != senhaoficial or email != emailoficial:
        print("As credenciais de acesso estão erradas\nTente novamente:")
        credenciais(email,senha)

print(credenciais(emailoficial,senhaoficial))

def autenticacao(informacao):
    if informacao == 1:
        credenciais
        
    elif informacao == 2:

        email2= input("Introduza o seu email:")

    else:
        print("Opção Invalida")

    return informacao

print(autenticacao(informacao))

opcao = int(input("1-Marcar Refeição\n2-Ver Historico\n3-Sair\nIndique a opção desejada: "))
print(opcao)

def menu (opcao):
    if opcao == 1:
        data = input("Intoduza a Data: ")
        horario = input("Introduza a Data: ")
        hora = input("Introduza a Hora prevista de chegada: ")
    
    if opcao == 2 :
        #se nao tiver nenhuma reserva feita tem que guardar num ficheiro

    if opcao == 3:
        print("Tenha um Bom Dia")
    else:
        print("Opção Invalida")

print(menu(opcao))

def reservas(data,horario,hora):
    pass
'''