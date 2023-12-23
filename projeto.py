from funcoes import login,adicionar_usuario,load,create_menu,make_reservation,see_historic,fatura,menu_admin,close_days,view_closing_days,conta






listUsers = load("users.json")
#print(listUsers)
user = listUsers[0]
# user = login(listUsers)
# admin = login(listUsers)
# login(listUsers)
# adicionar_usuario(listUsers)
#create_menu(user)
#make_reservation(user)
see_historic(user)
#print(conta(2,2))
# fatura(user)
# menu_admin(admin)
# close_days(admin)
# view_closing_days("close_days.json")
#print(close_days(admin):)
