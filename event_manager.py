import bot
import tkinter as tk
from tkinter.filedialog import asksaveasfile, askopenfilename, askdirectory


def on_submission(inp, res_field):
    input_temp_var = inp.get()
    evnt_titles = bot.get_event_titles(input_temp_var)
    if(len(evnt_titles) > 0):
        for e in evnt_titles:
            res_field.insert(tk.END, f'{e}\n')
    else:
        print('No results found!')

def save_to_file(text, file_name):
    file_path = askdirectory()
    f = open(file_path + f'/{file_name}.txt', 'w', encoding='utf-8')
    f.write(text.get('0.0', 'end'))
    f.close()