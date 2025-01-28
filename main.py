import tkinter as tk

window = tk.Tk()
window.geometry("910x910")

window.rowconfigure([0,1,2,3,4,5,6], minsize=120)
window.columnconfigure([0,1,2,3,4,5,6], minsize=120)

#Subroutine to show main menu screen
def main_menu_sub():
    pokedex_menu.grid_remove()
    show_teams_menu.grid_remove()
    login_menu.grid_remove()
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



#login button ###
login_button = tk.Button(master=login_menu, text="Login", fg="black",height=6,width=12,command=login_sub)
login_button.grid(row=3,column=8,padx=5,pady=5)






main_menu.grid()

window.mainloop()