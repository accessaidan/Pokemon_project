import tkinter as tk
import pandas as pd
import os

window = tk.Tk()
window.geometry("910x910")

window.rowconfigure([0,1,2,3,4,5,6], minsize=120)
window.columnconfigure([0,1,2,3,4,5,6], minsize=120)

#Subroutine to show main menu screen
def main_menu_sub():
    pokedex_menu.grid_remove()
    show_teams_menu.grid_remove()
    login_menu.grid_remove()
    new_account_frame.grid_remove()
    main_menu.grid()
#subroutine to show the pokedex 
def show_dex_sub():
    main_menu.grid_remove()
    pokedex_menu.grid()
#subroutine to show teams menu
def show_teams_sub():
    main_menu.grid_remove()
    show_teams_menu.grid()
#subroutine to show Login menu
def login_menu_sub():
    main_menu.grid_remove()
    login_menu.grid()
#subroutine to make new account
def new_account_sub():
    login_button.grid_forget()
    new_account_frame.grid()
#subroutine to login to account
def login_sub():
    new_account.grid_forget()



##Main menu frame ######################################################
main_menu = tk.Frame()

#see pokedex button
see_dex = tk.Button(master=main_menu, text = "See Pokedex", fg="black",height=6,width=12, command=show_dex_sub)
see_dex.grid(row=3, column=1, padx=5)


#see teams button
see_teams = tk.Button(master=main_menu, text = "See teams \n from anime", fg="black",height=6,width=12, command= show_teams_sub)
see_teams.grid(row=3, column=3,  padx=5)

#Login button
team_builder = tk.Button(master=main_menu, text = "Login", fg="black",height=6,width=12, command= login_menu_sub)
team_builder.grid(row=3, column=5, padx=5)
#########################################################################

##Pokedex menu frame #######################################################
pokedex_menu = tk.Frame()

#Back to menu button
back = tk.Button(master=pokedex_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.grid(row=0, column=0, padx= 5, pady=5, sticky='nw')

# Loop for part of pokedex select



##See teams ############################################################################
show_teams_menu = tk.Frame()

#back to menu button
back = tk.Button(master=show_teams_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.grid(row=0, column=0, padx= 5, pady=5, sticky='nw')
#select person whos team




##Login ##########################################
login_menu = tk.Frame()

#Back to menu button
back = tk.Button(master=login_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.grid(row=0, column=0, padx= 5, pady=5, sticky='nw')
#make a new account button ###
new_account = tk.Button(master=login_menu, text="Register", fg="black",height=6,width=12,command= new_account_sub)
new_account.grid(row=3, column=3,padx=5,pady=5)

#frame with inputs for new account
new_account_frame = tk.Frame()
#entry box for new username
username_label = tk.Label(master= new_account_frame, text="Username: ", fg="black", width=12)
username_label.grid(row=4,column=2,pady=5)
username_input = tk.Entry(master= new_account_frame, textvariable="Username", fg="black", width=24)
username_input.grid(row=4,column=3,pady=5) 
password_label = tk.Label(master= new_account_frame, text="Password: ", fg="black", width=12)
password_label.grid(row=5,column=2,pady=5)
password_input = tk.Entry(master= new_account_frame, textvariable="password", fg="black", width=24)
password_input.grid(row=5,column=3,pady=5)


#login button ###
login_button = tk.Button(master=login_menu, text="Login", fg="black", height=6, width=12 ,command=login_sub)
login_button.grid(row=3,column=8,padx=5,pady=5)

user_data = pd.read_csv("user_data.csv")

main_menu.grid()

window.mainloop()   