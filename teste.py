import json
from datetime import datetime, timedelta

# Função para carregar dados dos arquivos JSON para listas de dicionários
def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

# Função para salvar dados em arquivos JSON
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

# Função de autenticação
def authenticate_user(user_type):
    users = load_data('users.json')
    email = input('Digite seu email: ')
    
    for user in users:
        if user['email'] == email and (user_type == 'admin' and user['is_admin'] or user_type == 'client'):
            if user_type == 'admin':
                password = input('Digite sua senha: ')
                if user['password'] == password:
                    return user
            else:
                return user
    
    if user_type == 'admin':
        print('Credenciais inválidas para administrador.')
    else:
        print('Usuário não registrado. Registrando...')
        user = {'email': email, 'is_admin': False}
        users.append(user)
        save_data(users, 'users.json')
    
    return user

# Função para realizar uma reserva
def make_reservation(client):
    # Implemente a lógica para fazer uma reserva aqui
    pass

# Função para ver o histórico de reservas
def view_reservation_history(client):
    # Implemente a lógica para visualizar o histórico de reservas aqui
    pass

# Função principal para clientes
def client_menu(client):
    while True:
        print("\nMenu do Cliente:")
        print("1. Efetuar uma reserva")
        print("2. Ver histórico de reservas")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            make_reservation(client)
        elif choice == '2':
            view_reservation_history(client)
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

# ... (código anterior)

if __name__ == "__main__":
    # Carregar dados dos arquivos JSON para listas de dicionários
    definitions = load_data('definitions.json')
    users = load_data('users.json')
    closedays = load_data('closedays.json')
    meals = load_data('meals.json')

    # Autenticação do usuário
    user_type = input("Digite 'client' para cliente ou 'admin' para administrador: ")
    if user_type == 'client':
        client = authenticate_user('client')
        client_menu(client)
    elif user_type == 'admin':
        admin = authenticate_user('admin')
        admin_menu(admin)
    else:
        print("Tipo de usuário inválido.")  

# ... (código anterior)

if __name__ == "__main__":
    # Carregar dados dos arquivos JSON para listas de dicionários
    definitions = load_data('definitions.json')
    users = load_data('users.json')
    closedays = load_data('closedays.json')
    meals = load_data('meals.json')

    # Autenticação do usuário
    user_type = input("Digite 'client' para cliente ou 'admin' para administrador: ")
    if user_type == 'client':
        client = authenticate_user('client')
        client_menu(client)
    elif user_type == 'admin':
        admin = authenticate_user('admin')
        admin_menu(admin)
    else:
        print("Tipo de usuário inválido.")

# ... (código anterior)

if __name__ == "__main__":
    # Carregar dados dos arquivos JSON para listas de dicionários
    definitions = load_data('definitions.json')
    users = load_data('users.json')
    closedays = load_data('closedays.json')
    meals = load_data('meals.json')

    # Autenticação do usuário
    user_type = input("Digite 'client' para cliente ou 'admin' para administrador: ")
    if user_type == 'client':
        client = authenticate_user('client')
        client_menu(client)
    elif user_type == 'admin':
        admin = authenticate_user('admin')
        admin_menu(admin)
    else:
        print("Tipo de usuário inválido.")

# Função para adicionar fecho do dia
def add_closing_day(admin):
    # Implemente a lógica para adicionar o fecho do dia aqui
    pass

# Função para ver os últimos fechos do dia
def view_last_closing_days(admin):
    # Implemente a lógica para visualizar os últimos fechos do dia aqui
    pass

# Função para extrato de reservas por dia
def extract_reservations_by_day(admin):
    # Implemente a lógica para extrato de reservas por dia aqui
    pass

# Função principal para administradores
def admin_menu(admin):
    while True:
        print("\nMenu do Administrador:")
        print("1. Definições")
        print("2. Fecho do dia")
        print("3. Extrato de reservas por dia")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            # Implemente a lógica para as definições aqui
            pass
        elif choice == '2':
            add_closing_day(admin)
        elif choice == '3':
            view_last_closing_days(admin)
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    # Carregar dados dos arquivos JSON para listas de dicionários
    definitions = load_data('definitions.json')
    users = load_data('users.json')
    closedays = load_data('closedays.json')
    meals = load_data('meals.json')

    # Autenticação do usuário
    user_type = input("Digite 'client' para cliente ou 'admin' para administrador: ")
    if user_type == 'client':
        client = authenticate_user('client')
        client_menu(client)
    elif user_type == 'admin':
        admin = authenticate_user('admin')
        admin_menu(admin)
    else:
        print("Tipo de usuário inválido.")