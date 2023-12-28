from funcoes import load, adicionar_usuario


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
        return userlogado
    else:
        palavraPass = ""
        while palavraPass != userlogado["password"]:
            palavraPass = input("Introdua a sua palavra pass:")
            # vai verificar se a palavra pass introduzida é igual a que está guardada na lista de utilizadores em Admin
            if palavraPass == userlogado["password"]:
                return userlogado
            else:
                print("Palavra pass errada tente novamente")
