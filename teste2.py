import json

def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)


lista = [
    {'email' : 'aaa@aa.aa', 'password' : '', 'permission' : 'client'},
    {'email' : 'bbb@bb.bb', 'password' : 'bbbb', 'permission' : 'admin'}
]

save_data(lista, "users.json")