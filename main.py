import tkinter as tk
import pandas as pd
import os

window = tk.Tk()
window.geometry("910x910")

window.rowconfigure([0,1,2,3,4,5,6], minsize=120)
window.columnconfigure([0,1,2,3,4,5,6], minsize=120)

#Subroutine to show main menu screen
def main_menu_sub():
    frm_pokedex_menu.pack_forget()
    frm_show_teams_menu.pack_forget()
    frm_login_menu.pack_forget()
    frm_register.forget()

    frm_main_menu.pack()
#subroutine to show the pokedex 
def show_dex_sub():
    frm_main_menu.pack_forget()
    frm_pokedex_menu.pack()
#subroutine to show teams menu
def show_teams_sub():
    frm_main_menu.pack_forget()
    frm_show_teams_menu.pack()
#subroutine to show Login menu
def login_menu_sub():
    frm_main_menu.pack_forget()
    frm_login_menu.pack()

#subroutine to make new account
def new_user_sub():
    print("1")
    btn_login.forget()
    print("2")
    frm_register.pack()
    print("3")
#subroutine to login to account








##Main menu frame ######################################################
frm_main_menu = tk.Frame(window, width=910, height=910)
frm_main_menu.pack()

#see pokedex button
see_dex = tk.Button(frm_main_menu, text = "See Pokedex", fg="black",height=6,width=12, command=show_dex_sub)
see_dex.place(x= 265, y=265)


#see teams button
see_teams = tk.Button(frm_main_menu, text = "See teams \n from anime", fg="black",height=6,width=12, command= show_teams_sub)
see_teams.place(x=395, y= 265)

#Login button
team_builder = tk.Button(frm_main_menu, text = "Make a team", fg="black",height=6,width=12, command= login_menu_sub)
team_builder.place(x= 525, y=265)
#########################################################################








##Pokedex menu frame #######################################################
frm_pokedex_menu = tk.Frame(window, width=910, height=910)
frm_pokedex_menu.pack()

#Back to menu button
back = tk.Button(frm_pokedex_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.place(x= 5, y=5 )

# Loop for part of pokedex select









##See teams ############################################################################
frm_show_teams_menu = tk.Frame(window, width=910, height=910)
frm_show_teams_menu.pack()

#back to menu button
back = tk.Button(frm_show_teams_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.place(x= 5, y=5 )
#select person whos team












##Make a team ##########################################
frm_login_menu = tk.Frame(window, width=910, height=910)
frm_login_menu.pack()

#Back to menu button
back = tk.Button(frm_login_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.place(x= 5, y=5 )

#Register button
btn_register= tk.Button(frm_login_menu, text="Register", fg="Black",height=6,width=12, command=new_user_sub)
btn_register.place(x=265, y=265)

##register button functions
##Shows username, password, confirm password
##makes frame
frm_register = tk.Frame(window, width=910, height=910)
frm_register.pack()

lbl_new_username = tk.Label(frm_register, textvariable= 'Enter username', height=3, width=24)
lbl_new_username.place(x=265, y=395)


#Login button
btn_login= tk.Button(frm_login_menu, text="Login", fg="Black",height=6,width=12,)
btn_login.place(x=525, y=265)





user_data = pd.read_csv("user_data.csv")

frm_main_menu.pack()

window.mainloop()