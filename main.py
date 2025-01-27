import tkinter as tk

window = tk.Tk()
window.geometry("900x900")

window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize=85)
window.columnconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize=85)
def main_menu_sub():
    pokedex_menu.pack_forget()
    main_menu.pack()

def show_dex_sub():
    main_menu.pack_forget()
    pokedex_menu.pack()


##Main menu frame ######################################################
main_menu = tk.Frame()

#see pokedex button
see_dex = tk.Button(master=main_menu, text = "See Pokedex", fg="black", command=show_dex_sub)
see_dex.grid(row=3, column=1, padx=5)

#team builder button
team_builder = tk.Button(master=main_menu, text = "Make your team", fg="black")
team_builder.grid(row=3, column=4, padx=5)

#see teams button
see_teams = tk.Button(master=main_menu, text = "See teams from anime", fg="black")
see_teams.grid(row=3, column=7,  padx=5)

#########################################################################

##Pokedex menu frame #######################################################
pokedex_menu = tk.Frame()

#Back to menu button
back = tk.Button(master=pokedex_menu, text="Back", fg="Black", command=main_menu_sub)
back.grid(row=0, column=0, padx= 5, pady=5, sticky='nw')

main_menu.pack()

window.mainloop()