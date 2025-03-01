import pandas as pd
import os

user_data = pd.read_csv('user_data.csv')

user_data.loc[user_data['username'] == 'aidan', 'poke1'] = 'pikachu'