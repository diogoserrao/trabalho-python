from funcoes import login,adicionar_usuario,load,create_menu,make_reservation, show_history,fatura,menu_admin,close_days,view_closing_days,conta






listUsers = load("users.json")
#print(listUsers)
user = listUsers[0]
#user = login(listUsers)
#admin = login(listUsers)
login()
# adicionar_usuario(listUsers)
#create_menu(user)
#make_reservation(user)
#show_history(user)
# fatura(user)
# menu_admin(admin)
# close_days(admin)
# view_closing_days("close_days.json")
#print(close_days(admin):)
