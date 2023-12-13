from funcoes import login,load,create_menu,make_reservation,close_days






listUsers = load( "users.json")
print(listUsers)

user = login(listUsers)
print(login)
print(create_menu(user))
print(make_reservation(user))
#print(close_days(admin):)
