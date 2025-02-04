import tkinter as tk
import pandas as pd
import os

global username
username = ""

window = tk.Tk()
window.geometry("910x910")

window.rowconfigure([0,1,2,3,4,5,6], minsize=120)
window.columnconfigure([0,1,2,3,4,5,6], minsize=120)

#Subroutines changing GUI ###################################################################
#reigster button on login screen pressed
def reg_button_press():
    frm_reg_or_log.pack_forget()
    frm_login.pack_forget()
    frm_register.pack()
##login button pressed in register
def log_in_reg_sub():
    frm_register.pack_forget()
    frm_login.pack()
##register submit button pressed
def check_new_user():
    new_username = txt_new_username.get()
    new_password = txt_new_password.get()
    conf_password = txt_conf_password.get()

    if new_username == "" or new_password == "":
        print("You must fill the boxs")
    else:
        ### reads cvs 
        user_data = pd.read_csv('user_data.csv')

        #check if passwords match and username doesnt already exist
        if new_username in user_data["username"].values or new_password != conf_password:
            print("Sorry either that username already exists or the passwords do not match")
        else:
            print("New user accepted")
            adding_data = (
                {
                    "username":new_username,
                    "password":new_password,
                    "poke1":0,
                    "poke2":0,
                    "poke3":0,
                    "poke4":0,
                    "poke5":0,
                    "poke6":0,
                }
            )
            user_data.loc[len(user_data)] = adding_data
            global username
            username = new_username
            
            main_menu_sub(username)




##Login button pressed
def login_button_press():
    frm_reg_or_log.pack_forget()
    frm_register.pack_forget()
    frm_login.pack()
#register button pressed in login
def reg_button_in_login_pressed():
    frm_login.pack_forget()
    frm_register.pack()
#login submitt button pressed
def check_user_pass():
    username_input = txt_username.get()
    password_input = txt_password.get()
    if username_input == "" or password_input == "":
        print("You must enter a username and password")
    else:
    ###reads csv
        user_data = pd.read_csv('user_data.csv')
        if username_input in user_data["username"]:##################################################Doesnt work and i dont know why
                needed_password = user_data[user_data['username']== username_input, 'password'] #####Might not work havent been able to test
                if password_input == needed_password:
                    print("Login success")
                    username = username_input
                    main_menu_sub(username)
        else:
            print("Login fail")

#main menu subroutine 
def main_menu_sub(username):
    frm_pokedex_menu.pack_forget()
    frm_register.pack_forget()
    frm_main_menu.pack()
# subroutine for logging out
def log_out_sub():
    frm_main_menu.pack_forget()
    frm_reg_or_log.pack()





############################Start of Tkinter stuff ###########################
#Login screen #######################################################
frm_reg_or_log = tk.Frame(window, width=910, height=910)

#Register button
btn_register= tk.Button(frm_reg_or_log, text="Register", fg="Black",height=6,width=12, command=reg_button_press)
btn_register.place(x=265, y=135)

##register button functions
##Shows username, password, confirm password
##makes frame
frm_register = tk.Frame(window, width=910, height=910)

## keeping register button
btn_register= tk.Button(frm_register, text="Register", fg="Black",height=6,width=12, command=reg_button_press)
btn_register.place(x=265, y=135)
##keeping login button
btn_login= tk.Button(frm_register, text="Login", fg="Black",height=6,width=12,command=log_in_reg_sub)
btn_login.place(x=525, y=135)
##username label and inoput
lbl_new_username = tk.Label(frm_register, text= 'Enter username',foreground='black', height=6, width=12)
lbl_new_username.place(x=265, y=225)
txt_new_username = tk.Entry(frm_register, textvariable='Enter username', foreground='black')
txt_new_username.place(x= 385, y=265)
##Password label and input
lbl_new_password = tk.Label(frm_register, text= 'Enter password',foreground='black', height=6, width=12)
lbl_new_password.place(x=265, y=285)
txt_new_password = tk.Entry(frm_register, textvariable='Enter password', foreground='white')
txt_new_password.place(x= 385, y=325)
##Confirm Password label and input
lbl_conf_password = tk.Label(frm_register, text= 'Confirm password',foreground='black', height=6, width=16)
lbl_conf_password.place(x=260, y=345)
txt_conf_password = tk.Entry(frm_register, textvariable='Confirm password', foreground='white')
txt_conf_password.place(x= 385, y=385)
##New user submit button
btn_new_submit = tk.Button(frm_register, text='submit', fg='black', height=5,width=12, command=check_new_user)
btn_new_submit.place(x=395,y=525)

#Login button
btn_login= tk.Button(frm_reg_or_log, text="Login", fg="Black",height=6,width=12,command=login_button_press)
btn_login.place(x=525, y=135)

##login frame
frm_login = tk.Frame(window, width=910, height=910)

##keeping register button
btn_register= tk.Button(frm_login, text="Register", fg="Black",height=6,width=12, command=reg_button_in_login_pressed)
btn_register.place(x=265, y=135)
##keeping login button
btn_login= tk.Button(frm_login, text="Login", fg="Black",height=6,width=12,)
btn_login.place(x=525, y=135)
##username label and inoput
lbl_username = tk.Label(frm_login, text= 'Enter username',foreground='black', height=6, width=12)
lbl_username.place(x=525, y=225)
txt_username = tk.Entry(frm_login, textvariable='Enter username', foreground='black')
txt_username.place(x= 385, y=265)
##Password label and input
lbl_password = tk.Label(frm_login, text= 'Enter password',foreground='black', height=6, width=12)
lbl_password.place(x=525, y=285)
txt_password = tk.Entry(frm_login, textvariable='Enter password', foreground='white')
txt_password.place(x= 385, y=325)
##login submit button
btn_new_submit = tk.Button(frm_login, text='submit', fg='black', height=5,width=12, command=check_user_pass)
btn_new_submit.place(x=395,y=525)


################    need to fix the login function ######################
################    Apart from that above this is done ##################







##Main menu frame ######################################################
frm_main_menu = tk.Frame(window, width=910, height=910)


#see pokedex button
see_dex = tk.Button(frm_main_menu, text = "See Pokedex", fg="black",height=6,width=12)
see_dex.place(x= 265, y=265)

#see teams button
see_teams = tk.Button(frm_main_menu, text = "See teams \n from anime", fg="black",height=6,width=12 )
see_teams.place(x=395, y= 265)

#team builder button
team_builder = tk.Button(frm_main_menu, text = "Make a team", fg="black",height=6,width=12 )
team_builder.place(x= 525, y=265)

#Logout button
log_out = tk.Button(frm_main_menu, text=(username, '\n log out'), fg='black',height=6, width=12, command= log_out_sub)
log_out.place(x=785,y=5)
#########################################################################








##Pokedex menu frame #######################################################
frm_pokedex_menu = tk.Frame(window, width=910, height=910)


#Back to menu button
back = tk.Button(frm_pokedex_menu, text="Back to menu", fg="Black",height=6,width=12)
back.place(x= 5, y=5 )

# Loop for part of pokedex select









##See teams ############################################################################
frm_show_teams_menu = tk.Frame(window, width=910, height=910)


#back to menu button
back = tk.Button(frm_show_teams_menu, text="Back to menu", fg="Black",height=6,width=12)
back.place(x= 5, y=5 )
#select person whos team












##Make a team ##########################################








frm_reg_or_log.pack()

window.mainloop()
