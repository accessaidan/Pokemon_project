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
    global username
    new_username = txt_new_username.get()
    new_password = txt_new_password.get()
    conf_password = txt_conf_password.get()

    if new_username == "" or new_password == "":
        empty_inputs = tk.Toplevel(window)
        empty_inputs.title("ERROR")
        empty_inputs.geometry('250x50')
        lbl_must_input = tk.Label(empty_inputs, text="You must fill the boxs", foreground='black').pack()
        lbl_can_close = tk.Label(empty_inputs, text="You may now close this window and try again", foreground='black').pack()
    else:
        ### reads cvs 
        user_data = pd.read_csv('user_data.csv')

        #check if passwords match and username doesnt already exist
        if new_username in user_data["username"].values or new_password != conf_password:
            reg_fail= tk.Toplevel(window)
            reg_fail.title("ERROR")
            reg_fail.geometry('350x50')
            lbl_reg_fail = tk.Label(reg_fail, text="Either that username already exists or the passwords do not match", foreground='black').pack()
            lbl_can_close = tk.Label(reg_fail, text="You may now close this window and try again", foreground='black').pack()
        else:
            registration_success = tk.Toplevel(window)
            registration_success.title("SUCCESS")
            registration_success.geometry('250x50')
            lbl_registration_success = tk.Label(registration_success, text="registration successful", foreground='black').pack()
            lbl_can_close = tk.Label(registration_success, text="You may now close this window and continue", foreground='black').pack()
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
            user_data.to_csv('user_data.csv', index=False)
            main_menu_sub()


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
    global username
    username_input = txt_username.get()
    password_input = txt_password.get()
    if username_input == "" or password_input == "":
        empty_inputs = tk.Toplevel(window)
        empty_inputs.title("ERROR")
        empty_inputs.geometry('250x50')
        lbl_must_input = tk.Label(empty_inputs, text="You must fill the boxs", foreground='black').pack()
        lbl_can_close = tk.Label(empty_inputs, text="You may now close this window and try again", foreground='black').pack()
    else:
        ###reads csv
        user_data = pd.read_csv('user_data.csv')
        
        if username_input in user_data["username"].values:
            if password_input in user_data["password"].values: ########################### Does not fucking work
                login_success = tk.Toplevel(window)
                login_success.title("SUCCESS")
                login_success.geometry('250x50')
                lbl_login_success = tk.Label(login_success, text="login success", foreground='black').pack()
                lbl_can_close = tk.Label(login_success, text="You may now close this window and continue", foreground='black').pack()
                username = username_input
                main_menu_sub()
            else:
                wrong_password = tk.Toplevel(window)
                wrong_password.title("ERROR")
                wrong_password.geometry('250x50')
                lbl_wrong_password = tk.Label(wrong_password, text="That password does not match your username", foreground='black').pack()
                lbl_can_close = tk.Label(wrong_password, text="You may now close this window and try again", foreground='black').pack()
        else:
            wrong_username = tk.Toplevel(window)
            wrong_username.title("ERROR")
            wrong_username.geometry('250x50')
            lbl_wrong_username = tk.Label(wrong_username, text="That username does not exist", foreground='black').pack()
            lbl_can_close = tk.Label(wrong_username, text="You may now close this window and try again", foreground='black').pack()

#main menu subroutine 
def main_menu_sub():
    global username
    frm_login.pack_forget()
    frm_register.pack_forget()
    frm_main_menu.pack()
#back to menu button
def back_to_menu_sub():
    frm_profile_menu.pack_forget()
    frm_main_menu.pack()

#subroutine for profile menu
def profile_sub():                      
    frm_main_menu.pack_forget()
    frm_profile_menu.pack()
# subroutine for logging out
def log_out_sub():
    frm_profile_menu.pack_forget()
    frm_reg_or_log.pack()
#subroutine for checking deleting account
def delete_account_sub():
    delete_account_confirm = tk.Toplevel(window)
    delete_account_confirm.title("DELETE ACCOUNT")
    delete_account_confirm.geometry('250x50')
    lbl_must_input = tk.Label(delete_account_confirm, text="Are you SURE you want to DELETE your account", foreground='black').pack()
    btn_can_close = tk.Button(delete_account_confirm, text="DELETE ACCOUNT", foreground='black', command= delete_account_function_sub).pack()
#subroutine to actually delete account
def delete_account_function_sub():
    global username
    user_data = pd.read_csv('user_data.csv')
    user_data = user_data[user_data.username!= username]
    user_data.to_csv('user_data.csv', index=False)
    frm_profile_menu.pack_forget()
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

#profile button
profile = tk.Button(frm_main_menu, text=('profile'), fg='black',height=6, width=12, command= profile_sub)
profile.place(x=785,y=5)
#########################################################################


#Profile menu frame
frm_profile_menu = tk.Frame(window, width=910, height=910)
#logout button
log_out = tk.Button(frm_profile_menu, text = "log out", fg="black",height=6,width=12, command=log_out_sub)
log_out.place(x= 265, y=265)


#see team button
see_team = tk.Button(frm_profile_menu, text = "View your team", fg="black",height=6,width=12 )
see_team.place(x=395, y= 265)

#delete account button
delete_account = tk.Button(frm_profile_menu, text = "Delete account", fg="black",height=6,width=12, command= delete_account_sub )
delete_account.place(x= 525, y=265)

#Back to menu button
back = tk.Button(frm_profile_menu, text="Back to menu", fg="Black",height=6,width=12,command=back_to_menu_sub)
back.place(x= 5, y=5 )

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
