import tkinter as tk

window = tk.Tk()
window.geometry("900x900")

window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize=85)
window.columnconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize=85)

#Subroutine to show main menu screen
def main_menu_sub():
    pokedex_menu.pack_forget()
    main_menu.pack()
#subroutine to show the pokedex 
def show_dex_sub():
    main_menu.pack_forget()
    pokedex_menu.pack()
#subroutine to show teams menu
def show_teams_sub():
    main_menu.pack_forget()
    show_teams_menu.pack()
#subroutine to show Login menu
def login_sub():
    main_menu.pack_forget()
    login_menu.pack()


##Main menu frame ######################################################
main_menu = tk.Frame()

#see pokedex button
see_dex = tk.Button(master=main_menu, text = "See Pokedex", fg="black", command=show_dex_sub)
see_dex.grid(row=3, column=1, padx=5)

#see teams button
see_teams = tk.Button(master=main_menu, text = "See teams from anime", fg="black", command= show_teams_sub)
see_teams.grid(row=3, column=4,  padx=5)

#Login button
team_builder = tk.Button(master=main_menu, text = "Login", fg="black", command= login_sub)
team_builder.grid(row=3, column=7, padx=5)
#########################################################################

##Pokedex menu frame #######################################################
pokedex_menu = tk.Frame()

#Back to menu button
back = tk.Button(master=pokedex_menu, text="Back", fg="Black", command=main_menu_sub)
back.grid(row=0, column=0, padx= 5, pady=5, sticky='nw')

# Loop for part of pokedex select



##See teams ############################################################################
show_teams_menu = tk.Frame()

#select person whos team




##Login ##########################################
login_menu = tk.Frame()












main_menu.pack()

window.mainloop()