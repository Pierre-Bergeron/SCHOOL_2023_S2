# Author : Pierre Bergeron
# Date : MA23/23
# File : U6_SOMMATIF

import tkinter as tk
import math
import datetime
import random

# Main window settings
pageA = tk.Tk()
pageA.title("Great Company Inventory Sysyem")
pageA['bg'] = "#ffffff"
pageA.geometry("1004x350")
# 1004x700 original size
pageA.rowconfigure(0, weight=1)
pageA.columnconfigure(0, weight=1)

# Date settings
date = datetime.date.today()
datenow = "Date :", date, "|"









# Frame settings
def show_frame(frame):
    frame.tkraise()

# element for de l'exam et choix du frame
page1 = tk.Frame(pageA)
WinNum = tk.Frame(pageA)
for frame in (page1, WinNum):
    frame.grid(row=0, column=0, sticky='nsew')

page1['bg'] = '#becee5'
WinNum['bg'] = '#E5F6DF'

# FRAME 1 - lotterieChoise ( Choisir vos numbero)
SpaceUs = tk.Label(page1, text='                               ')
SpaceUs.grid(row=0)

page1Titre = tk.Label(page1, text='page 1 :', bg="#D3D3D3")
page1Titre.grid(row='0', column='0',  sticky='n')

page2Titre = tk.Label(page1, text='page2 :', bg="#becee5")
page2Titre.grid(row='1', column='0', sticky='e')

UF_CH1 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH1.grid(row=1, column=1)
UF_CH1.insert(0, "0")
UF_CH2 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH2.grid(row=1, column=2)
UF_CH2.insert(0, "0")
UF_CH3 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH3.grid(row=1, column=3)
UF_CH3.insert(0, "0")
UF_CH4 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH4.grid(row=1, column=4)
UF_CH4.insert(0, "0")
UF_CH5 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH5.grid(row=1, column=5)
UF_CH5.insert(0, "0")
UF_CH6 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH6.grid(row=1, column=6)
UF_CH6.insert(0, "0")
UF_CH7 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH7.grid(row=1, column=7)
UF_CH7.insert(0, "0")
UF_CH8 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH8.grid(row=1, column=8)
UF_CH8.insert(0, "0")
UF_CH9 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH9.grid(row=1, column=9)
UF_CH9.insert(0, "0")
UF_CH10 = tk.Entry(page1, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH10.grid(row=1, column=10)
UF_CH10.insert(0, "0")



UF_CH_SAVE = tk.Button(page1, text="Acheter", highlightbackground='#becee5', command=None)
UF_CH_SAVE.grid(row=2, column=5, columnspan='2')



# Bouton pour traiter les numero
VERNUM = tk.Label(page1, text='Vos numéro :', bg='#becee5')
VERNUM.grid(row=3, column=0, sticky='e')

lotterieChoiseDate = tk.Label(page1, text=datenow, bg='#becee5')
lotterieChoiseDate.grid(row=2, column='0', sticky='e')

UF_CH_SUB = tk.Button(page1, text="Joué Mètenet", highlightbackground='#becee5', command=lambda: show_frame(WinNum))
UF_CH_SUB.grid(row=5, column=5, columnspan='2')

# Demontre les numero que tu a choisi dans le 2e frame
Titre2 = tk.Label(WinNum, text='Vos Numéro :', bg='#E5F6DF')
Titre2.grid(row=0, column=0, sticky='e')
NUM1 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM1.grid(row=0, column=1)
NUM2 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM2.grid(row=0, column=2)
NUM3 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM3.grid(row=0, column=3)
NUM4 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM4.grid(row=0, column=4)
NUM5 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM5.grid(row=0, column=5)
NUM6 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM6.grid(row=0, column=6)
NUM7 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM7.grid(row=0, column=7)
NUM8 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM8.grid(row=0, column=8)
NUM9 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM9.grid(row=0, column=9)
NUM10 = tk.Label(WinNum, text='', bg='#E5F6DF')
NUM10.grid(row=0, column=10)

# Demontre les numero gangnent dans le 2e frame
WinN = tk.Label(WinNum, text='Numéro Gagnant :', bg='#E5F6DF')
WinN.grid(row=1, column=0, sticky='e')
WinN1 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN1.grid(row=1, column=1)
WinN2 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN2.grid(row=1, column=2)
WinN3 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN3.grid(row=1, column=3)
WinN4 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN4.grid(row=1, column=4)
WinN5 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN5.grid(row=1, column=5)
WinN6 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN6.grid(row=1, column=6)
WinN7 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN7.grid(row=1, column=7)
WinN8 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN8.grid(row=1, column=8)
WinN9 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN9.grid(row=1, column=9)
WinN10 = tk.Label(WinNum, text='', bg='#E5F6DF')
WinN10.grid(row=1, column=10)

R1 = tk.Label(WinNum, text='', bg='#E5F6DF')
R1.grid(row=2, column=1)
R2 = tk.Label(WinNum, text='', bg='#E5F6DF')
R2.grid(row=2, column=2)
R3 = tk.Label(WinNum, text='', bg='#E5F6DF')
R3.grid(row=2, column=3)
R4 = tk.Label(WinNum, text='', bg='#E5F6DF')
R4.grid(row=2, column=4)
R5 = tk.Label(WinNum, text='', bg='#E5F6DF')
R5.grid(row=2, column=5)
R6 = tk.Label(WinNum, text='', bg='#E5F6DF')
R6.grid(row=2, column=6)
R7 = tk.Label(WinNum, text='', bg='#E5F6DF')
R7.grid(row=2, column=7)
R8 = tk.Label(WinNum, text='', bg='#E5F6DF')
R8.grid(row=2, column=8)
R9 = tk.Label(WinNum, text='', bg='#E5F6DF')
R9.grid(row=2, column=9)
R10 = tk.Label(WinNum, text='', bg='#E5F6DF')
R10.grid(row=2, column=10)

Status = tk.Label(WinNum, text='État :', bg='#E5F6DF')
Status.grid(row=3, column=0, sticky='e')
Status1 = tk.Label(WinNum, text='', bg='#E5F6DF')
Status1.grid(row=3, column=1, columnspan=5)

show_frame(page1)
pageA.mainloop()