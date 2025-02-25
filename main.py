import tkinter as tk
import pandas as pd
import os
import requests
from PIL import Image, ImageTk
import io

global username
username = ""

window = tk.Tk()
#window.geometry("910x910")

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
    frm_show_teams_menu.pack_forget()
    frm_pokedex_menu.pack_forget()
    frm_make_team.pack_forget()
    frm_pokedex_menu.pack_forget()
    frm_main_menu.pack()

#subroutine for profile menu
def profile_sub():                      
    frm_main_menu.pack_forget()
    frm_show_teams_menu.pack_forget()
    frm_make_team.pack_forget()
    frm_pokedex_menu.pack_forget()
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


##Buttons for functions in main menu
#subroutine to see poekdex
def see_dex_sub():
    frm_main_menu.pack_forget()
    frm_pokedex_menu.pack()

#subroutie for seeing teams from the anime
def see_teams_sub():
    frm_main_menu.pack_forget()
    frm_show_teams_menu.pack()
##showing team
def show_team_sub(character):
    global username
    user_data = pd.read_csv('user_data.csv')

    if character == "user":
        character_name = username
        poke1 = user_data.loc[user_data['username'] == username, 'poke1'].values[0]
        poke2 = user_data.loc[user_data['username'] == username, 'poke2'].values[0]
        poke3 = user_data.loc[user_data['username'] == username, 'poke3'].values[0]
        poke4 = user_data.loc[user_data['username'] == username, 'poke4'].values[0]
        poke5 = user_data.loc[user_data['username'] == username, 'poke5'].values[0]
        poke6 = user_data.loc[user_data['username'] == username, 'poke6'].values[0]

    elif character == "brock":
        character_name = "brock"
        poke1 = 208
        poke2 = 205
        poke3 = 272
        poke4 = 259
        poke5 = 453
        poke6 = 242
    
    elif character == "misty":
        character_name = "misty"
        poke1 = 175
        poke2 = 54
        poke3 = 118
        poke4 = 120
        poke5 = 121
        poke6 = 186
    ## new window opens to see team chosen
    show_team_window = tk.Toplevel(window)
    show_team_window.geometry('910x910')
    show_team_window.title(character_name + "'s Team")
    
    


    #pokemon 1
    poke_sprite = fetch_pokemon_sprite(poke1)

    btn_poke1 = tk.Button(show_team_window, image=(poke_sprite), fg="black",height=120,width=120)
    btn_poke1.image = poke_sprite
    btn_poke1.place(x= 135, y=265)

    #pokemon 2
    poke_sprite = fetch_pokemon_sprite(poke2)

    btn_poke2 = tk.Button(show_team_window, image=(poke_sprite), fg="black",height=120,width=120)
    btn_poke2.image = poke_sprite
    btn_poke2.place(x= 395, y=265)

    #pokemon 3
    poke_sprite = fetch_pokemon_sprite(poke3)

    btn_poke3 = tk.Button(show_team_window, image=(poke_sprite), fg="black",height=120,width=120)
    btn_poke3.image = poke_sprite
    btn_poke3.place(x= 655, y=265)
    
    #pokemon 4
    poke_sprite = fetch_pokemon_sprite(poke4)

    btn_poke4 = tk.Button(show_team_window, image=(poke_sprite), fg="black",height=120,width=120)
    btn_poke4.image = poke_sprite
    btn_poke4.place(x= 135, y=525)

    #pokemon 5
    poke_sprite = fetch_pokemon_sprite(poke5)

    btn_poke5 = tk.Button(show_team_window, image=(poke_sprite), fg="black",height=120,width=120)
    btn_poke5.image = poke_sprite
    btn_poke5.place(x= 395, y=525)

    #pokemon 6
    poke_sprite = fetch_pokemon_sprite(poke6)

    btn_poke6 = tk.Button(show_team_window, image=(poke_sprite), fg="black",height=120,width=120)
    btn_poke6.image = poke_sprite
    btn_poke6.place(x= 655, y=525)


#subrtoutine to make a team
def team_builder_sub():
    frm_main_menu.pack_forget()
    frm_make_team.pack()

#subroutine to see if inputted pokemon exists 
def check_pokemon_sub():
    pokemon = txt_make_team.get()



    try: 
        pokemon_id = pokemon
        poke_sprite = fetch_pokemon_sprite(pokemon_id)

        inputted_pokemon_window = tk.Toplevel(window)
        inputted_pokemon_window.geometry('240x240')

        btn_poke = tk.Button(inputted_pokemon_window, image=(poke_sprite), fg="black",height=120,width=120)
        btn_poke.image = poke_sprite
        btn_poke.place(x= 60, y=0)
        flag = False
        #add_to_team(pokemon_id, inputted_pokemon_window)
    

    except:
        try:
            pokemon_id = fetch_pokemon_id(pokemon.lower())
            poke_sprite = fetch_pokemon_sprite(pokemon_id)

            inputted_pokemon_window = tk.Toplevel(window)
            inputted_pokemon_window.geometry('240x240')

            btn_poke = tk.Button(inputted_pokemon_window, image=(poke_sprite), fg="black",height=120,width=120)
            btn_poke.image = poke_sprite
            btn_poke.place(x= 60, y=0)
            flag = False
            #add_to_team(pokemon_id, inputted_pokemon_window)

        except:
            inputted_pokemon_window = tk.Toplevel(window)
            inputted_pokemon_window.geometry('240x50')
            btn_invalid_pokemon = tk.Label(inputted_pokemon_window, text="Invalid Pokemon", fg="black")
            btn_invalid_pokemon.place(x= 30, y=0)
            flag = True
    
    if flag == False:   #add to team button doesnt work if invalid pokemon is entered
        #button to add to team
        btn_add_to_team = tk.Button(inputted_pokemon_window, text="Add to team", fg="black",background="green",
                                     height=6, width=12, command= lambda: select_remove_pokemon_sub(pokemon_id))
        btn_add_to_team.place(x= 10, y=125)
        #btn to not add to team
        btn_not_add_to_team = tk.Button(inputted_pokemon_window, text="dont add to team", fg="black",background="red", height=6, width=12)
        btn_not_add_to_team.place(x= 130, y=125)


#subroutine to select which pokemon to revove from team
def select_remove_pokemon_sub(pokemon_id):
    select_pokemon_remove_window = tk.Toplevel(window)
    select_pokemon_remove_window.geometry('910x910')

    global username
    user_data = pd.read_csv('user_data.csv')


    poke1 = user_data.loc[user_data['username'] == username, 'poke1'].values[0]
    poke2 = user_data.loc[user_data['username'] == username, 'poke2'].values[0]
    poke3 = user_data.loc[user_data['username'] == username, 'poke3'].values[0]
    poke4 = user_data.loc[user_data['username'] == username, 'poke4'].values[0]
    poke5 = user_data.loc[user_data['username'] == username, 'poke5'].values[0]
    poke6 = user_data.loc[user_data['username'] == username, 'poke6'].values[0]

    #pokemon 1
    poke_sprite = fetch_pokemon_sprite(poke1)

    btn_poke1 = tk.Button(select_pokemon_remove_window, image=(poke_sprite), fg="black",height=120,width=120, 
                          command= lambda: replace_pokemon(pokemon_id, poke1, "poke1"))
    btn_poke1.image = poke_sprite
    btn_poke1.place(x= 135, y=265)

    #pokemon 2
    poke_sprite = fetch_pokemon_sprite(poke2)

    btn_poke2 = tk.Button(select_pokemon_remove_window, image=(poke_sprite), fg="black",height=120,width=120, 
                          command= lambda: replace_pokemon(pokemon_id, poke2, "poke2"))
    btn_poke2.image = poke_sprite
    btn_poke2.place(x= 395, y=265)

    #pokemon 3
    poke_sprite = fetch_pokemon_sprite(poke3)

    btn_poke3 = tk.Button(select_pokemon_remove_window, image=(poke_sprite), fg="black",height=120,width=120, 
                          command= lambda: replace_pokemon(pokemon_id, poke3, "poke3"))
    btn_poke3.image = poke_sprite
    btn_poke3.place(x= 655, y=265)
    
    #pokemon 4
    poke_sprite = fetch_pokemon_sprite(poke4)

    btn_poke4 = tk.Button(select_pokemon_remove_window, image=(poke_sprite), fg="black",height=120,width=120, 
                          command= lambda: replace_pokemon(pokemon_id, poke4, "poke4"))
    btn_poke4.image = poke_sprite
    btn_poke4.place(x= 135, y=525)

    #pokemon 5
    poke_sprite = fetch_pokemon_sprite(poke5)

    btn_poke5 = tk.Button(select_pokemon_remove_window, image=(poke_sprite), fg="black",height=120,width=120, 
                          command= lambda: replace_pokemon(pokemon_id, poke5, "poke5"))
    btn_poke5.image = poke_sprite
    btn_poke5.place(x= 395, y=525)

    #pokemon 6
    poke_sprite = fetch_pokemon_sprite(poke6)

    btn_poke6 = tk.Button(select_pokemon_remove_window, image=(poke_sprite), fg="black",height=120,width=120, 
                          command= lambda: replace_pokemon(pokemon_id, poke6, "poke6"))
    btn_poke6.image = poke_sprite
    btn_poke6.place(x= 655, y=525)
    #label instructinh user
    lbl_instruct = tk.Label(select_pokemon_remove_window, text="Select which Pokemon to remove from your team:", fg="black")
    lbl_instruct.place(x= 335, y=5)

#subroutine to replace pokemon
def replace_pokemon(pokemon_id, existing_pokemon, placement):
    global username
    user_data = pd.read_csv('user_data.csv')
    user_data.loc[user_data['username'] == username, placement] = str(pokemon_id)
    
    user_data.to_csv('user_data.csv')

#subroutine where pokemon sprite is fetched
def fetch_pokemon_sprite(pokemon_id):
    url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
    response = requests.get(url)
    poke_image_data = response.content
    poke_sprite = Image.open(io.BytesIO(poke_image_data))
    poke_sprite = ImageTk.PhotoImage(poke_sprite)

    

    return poke_sprite
#subroutine to get the pokemon id from its name
def fetch_pokemon_id(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    pokemon_data = response.json()
    pokemon_id = pokemon_data['id']
    
    return pokemon_id

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


##Main menu frame ######################################################
frm_main_menu = tk.Frame(window, width=910, height=910)


#see pokedex button
see_dex = tk.Button(frm_main_menu, text = "See Pokedex", fg="black",height=6,width=12, command= see_dex_sub)
see_dex.place(x= 265, y=265)

#see teams button
see_teams = tk.Button(frm_main_menu, text = "See teams \n from anime", fg="black",height=6,width=12,command= see_teams_sub) 
see_teams.place(x=395, y= 265)

#team builder button
team_builder = tk.Button(frm_main_menu, text = "Make a team", fg="black",height=6,width=12, command= team_builder_sub)
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
see_team = tk.Button(frm_profile_menu, text = "View your team", fg="black",height=6,width=12, command=lambda: show_team_sub("user") )
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
back = tk.Button(frm_pokedex_menu, text="Back to menu", fg="Black",height=6,width=12, command=back_to_menu_sub)
back.place(x= 5, y=5 )
#profile button
#profile button
profile = tk.Button(frm_pokedex_menu, text=('profile'), fg='black',height=6, width=12, command= profile_sub)
profile.place(x=785,y=5)
# Loop for part of pokedex select









##See teams ############################################################################
frm_show_teams_menu = tk.Frame(window, width=910, height=910)



#back to menu button
back = tk.Button(frm_show_teams_menu, text="Back to menu", fg="Black",height=6,width=12, command= back_to_menu_sub)
back.place(x= 5, y=5 )
#profile button
profile = tk.Button(frm_show_teams_menu, text=('profile'), fg='black',height=6, width=12, command= profile_sub)
profile.place(x=785,y=5)
#brocks team
brock_photo = tk.PhotoImage(file='brock.png')
btn_brock = tk.Button(frm_show_teams_menu, image=(brock_photo), fg="black",height=120,width=120, command=lambda: show_team_sub("brock")) # 0 is brock
btn_brock.place(x= 135, y=135)
#mistys team
misty_photo = tk.PhotoImage(file='misty.png')
btn_brock = tk.Button(frm_show_teams_menu, image=(misty_photo), fg="black",height=120,width=120, command=lambda: show_team_sub("misty")) # 0 is brock
btn_brock.place(x= 395, y=135)







##Make a team ##########################################
frm_make_team = tk.Frame(window, width=910, height=910)

#back to menu button
back = tk.Button(frm_make_team, text="Back to menu", fg="Black",height=6,width=12, command= back_to_menu_sub)
back.place(x= 5, y=5 )
#profile button
#profile button
profile = tk.Button(frm_make_team, text=('profile'), fg='black',height=6, width=12, command= profile_sub)
profile.place(x=785,y=5)

#what to enter label
lbl_make_team = tk.Label(frm_make_team, text= 'Enter the desired \n pokemons name or \n pokedex number',foreground='black', height=6, width=18)
lbl_make_team.place(x= 365, y=275)
#entry for desired pokemon
txt_make_team = tk.Entry(frm_make_team, textvariable='Enter desired pokemon name or pokedex number', foreground='black')
txt_make_team.place(x= 365, y=395)
#submitt pokemon
btn_submit_pokemon = tk.Button(frm_make_team, text='submit', fg='black', height=5,width=12, command=check_pokemon_sub)
btn_submit_pokemon.place(x=395, y=525)





frm_reg_or_log.pack()

window.mainloop()