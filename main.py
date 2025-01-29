import tkinter as tk
import pandas as pd
import os

window = tk.Tk()
window.geometry("910x910")

window.rowconfigure([0,1,2,3,4,5,6], minsize=120)
window.columnconfigure([0,1,2,3,4,5,6], minsize=120)

#Subroutine to show main menu screen
def main_menu_sub():
    pokedex_menu.pack_forget()
    show_teams_menu.pack_forget()
    login_menu.pack_forget()
    new_account_frame.pack_forget()
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
def login_menu_sub():
    main_menu.pack_forget()
    login_menu.pack()
#subroutine to make new account
def new_account_sub():
    login_button.pack_forget()
    new_account_frame.pack()
#subroutine to login to account
def login_sub():
    new_account.pack_forget()
def check_new_user():
    username = username_input.get()
    password = password_input.get()
    confirm_password = confirm_password_input.get()
    if username in user_data:
        alert_window = tk.Tk()
        alert_label = tk.Label(text= "That username has already been used")


##Main menu frame ######################################################
main_menu = tk.Frame(window, width=910, height=910)
main_menu.pack()

#see pokedex button
see_dex = tk.Button(main_menu, text = "See Pokedex", fg="black",height=6,width=12, command=show_dex_sub)
see_dex.place(x= 265, y=265)


#see teams button
see_teams = tk.Button(main_menu, text = "See teams \n from anime", fg="black",height=6,width=12, command= show_teams_sub)
see_teams.place(x=395, y= 265)

#Login button
team_builder = tk.Button(main_menu, text = "Make a team", fg="black",height=6,width=12, command= login_menu_sub)
team_builder.place(x= 525, y=265)
#########################################################################

##Pokedex menu frame #######################################################
pokedex_menu = tk.Frame(window, width=910, height=910)
pokedex_menu.pack()

#Back to menu button
back = tk.Button(pokedex_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.place(x= 5, y=5 )

# Loop for part of pokedex select



##See teams ############################################################################
show_teams_menu = tk.Frame(window, width=910, height=910)
show_teams_menu.pack()

#back to menu button
back = tk.Button(master=show_teams_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.place(x= 5, y=5 )
#select person whos team




##Make a team ##########################################
login_menu = tk.Frame(window, width=910, height=910)
login_menu.pack()

#Back to menu button
back = tk.Button(master=login_menu, text="Back", fg="Black",height=6,width=12, command=main_menu_sub)
back.place(x= 5, y=5 )

#make a new account button ###
new_account = tk.Button(master=login_menu, text="Register", fg="black",height=6,width=12,command= new_account_sub)
new_account.place(x= 265, y=265)

#frame with inputs for new account
new_account_frame = tk.Frame(window, width=910, height=910)
new_account_frame.pack()
#entry box for new username, password and confirm password
username_label = tk.Label(master= new_account_frame, text="Username: ", fg="black", width=12)
username_label.place(x= 265,y= 395)
username_input = tk.Entry(master= new_account_frame, textvariable="Username", fg="black", width=24)
username_input.place(x= 395, y= 395) 
password_label = tk.Label(master= new_account_frame, text="Password: ", fg="black", width=12)
password_label.place(x= 265, y= 525)
password_input = tk.Entry(master= new_account_frame, textvariable="password", fg="black", width=24)
password_input.place(x= 395, y= 525)
confirm_password_label = tk.Label(master= new_account_frame, text="confirm Password: ", fg="black", width=12)
confirm_password_label.place(x= 265, y= 655)
confirm_password_input = tk.Entry(master= new_account_frame, textvariable="confirm password", fg="black", width=24)
confirm_password_input.place(x=395, y=655)

submit_button = tk.Button(master=new_account_frame, text="submit", command= check_new_user )
submit_button.place(x=395, y=785)




#login button ###
login_button = tk.Button(master=login_menu, text="Login", fg="black", height=6, width=12 ,command=login_sub)
login_button.place(x= 525, y=265)

user_data = pd.read_csv("user_data.csv")

main_menu.pack()

window.mainloop()