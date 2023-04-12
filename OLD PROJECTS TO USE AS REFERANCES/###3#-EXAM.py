# Pierre Bergeron
# Titre : ISC3U-EXAM
# Date : MA31/22
# Projet : Lotterie

import tkinter as tk
import math
import datetime
import random

# Main window settings
lotterie = tk.Tk()
lotterie.title("Lotterie Bergeron")
lotterie['bg'] = "#ffffff"
lotterie.geometry("1004x350")
# 1004x700 original size
lotterie.rowconfigure(0, weight=1)
lotterie.columnconfigure(0, weight=1)

# Date settings
date = datetime.date.today()
datenow = "Date :", date, "|"
# Genere les numero genant
Win1 = random.randint(1, 10)
Win2 = random.randint(1, 10)
Win3 = random.randint(1, 10)
Win4 = random.randint(1, 10)
Win5 = random.randint(1, 10)
Win6 = random.randint(1, 10)
Win7 = random.randint(1, 10)
Win8 = random.randint(1, 10)
Win9 = random.randint(1, 10)
Win10 = random.randint(1, 10)

print(Win1)
print(Win2)
print(Win3)
print(Win4)
print(Win5)
print(Win6)
print(Win7)
print(Win8)
print(Win9)
print(Win10)
print("-----")

# Liste pour verifier si le joueur a ganger
CHWIN = []
# Set my numbers
def get_data():
    CH1 = int(UF_CH1.get())
    CH2 = int(UF_CH2.get())
    CH3 = int(UF_CH3.get())
    CH4 = int(UF_CH4.get())
    CH5 = int(UF_CH5.get())
    CH6 = int(UF_CH6.get())
    CH7 = int(UF_CH7.get())
    CH8 = int(UF_CH8.get())
    CH9 = int(UF_CH9.get())
    CH10 = int(UF_CH10.get())
    # Clear list if multiple number change
    CHWIN.clear()
    # Filter les nombres
    if(CH1 <= 0):
        CH1a = 1
    elif(CH1 >= 11):
        CH1a = 10
    else:
        CH1a = CH1

    if (CH2 <= 0):
        CH2a = 1
    elif (CH2 >= 11):
        CH2a = 10
    else:
        CH2a = CH2

    if (CH3 <= 0):
        CH3a = 1
    elif (CH3 >= 11):
        CH3a = 10
    else:
        CH3a = CH3

    if (CH4 <= 0):
        CH4a = 1
    elif (CH4 >= 11):
        CH4a = 10
    else:
        CH4a = CH4

    if (CH5 <= 0):
        CH5a = 1
    elif (CH5 >= 11):
        CH5a = 10
    else:
        CH5a = CH5

    if (CH6 <= 0):
        CH6a = 1
    elif (CH6 >= 11):
        CH6a = 10
    else:
        CH6a = CH6

    if (CH7 <= 0):
        CH7a = 1
    elif (CH7 >= 11):
        CH7a = 10
    else:
        CH7a = CH7

    if (CH8 <= 0):
        CH8a = 1
    elif (CH8 >= 11):
        CH8a = 10
    else:
        CH8a = CH8

    if (CH9 <= 0):
        CH9a = 1
    elif (CH9 >= 11):
        CH9a = 10
    else:
        CH9a = CH9

    if (CH10 <= 0):
        CH10a = 1
    elif (CH10 >= 11):
        CH10a = 10
    else:
        CH10a = CH10

    print(CH1a)
    print(CH2a)
    print(CH3a)
    print(CH4a)
    print(CH5a)
    print(CH6a)
    print(CH7a)
    print(CH8a)
    print(CH9a)
    print(CH10a)

    VERNUM1['text'] = CH1a
    VERNUM2['text'] = CH2a
    VERNUM3['text'] = CH3a
    VERNUM4['text'] = CH4a
    VERNUM5['text'] = CH5a
    VERNUM6['text'] = CH6a
    VERNUM7['text'] = CH7a
    VERNUM8['text'] = CH8a
    VERNUM9['text'] = CH9a
    VERNUM10['text'] = CH10a
    #Num Frame 2
    NUM1['text'] = CH1a
    NUM2['text'] = CH2a
    NUM3['text'] = CH3a
    NUM4['text'] = CH4a
    NUM5['text'] = CH5a
    NUM6['text'] = CH6a
    NUM7['text'] = CH7a
    NUM8['text'] = CH8a
    NUM9['text'] = CH9a
    NUM10['text'] = CH10a

    WinN1['text'] = Win1
    WinN2['text'] = Win2
    WinN3['text'] = Win3
    WinN4['text'] = Win4
    WinN5['text'] = Win5
    WinN6['text'] = Win6
    WinN7['text'] = Win7
    WinN8['text'] = Win8
    WinN9['text'] = Win9
    WinN10['text'] = Win10

    if(CH1a == Win1):
        CHWIN.append('1')
        R1['text'] = "✅"
    else:
        CHWIN.append('0')
        R1['text'] = "❌"

    if(CH2a == Win2):
        CHWIN.append('1')
        R2['text'] = "✅"
    else:
        CHWIN.append('0')
        R2['text'] = "❌"

    if(CH3a == Win3):
        CHWIN.append('1')
        R3['text'] = "✅"
    else:
        CHWIN.append('0')
        R3['text'] = "❌"

    if(CH4a == Win4):
        R4['text'] = "✅"
        CHWIN.append('1')
    else:
        CHWIN.append('0')
        R4['text'] = "❌"

    if(CH5a == Win5):
        CHWIN.append('1')
        R5['text'] = "✅"
    else:
        CHWIN.append('0')
        R5['text'] = "❌"

    if(CH6a == Win6):
        CHWIN.append('1')
        R6['text'] = "✅"
    else:
        CHWIN.append('0')
        R6['text'] = "❌"

    if(CH7a == Win7):
        CHWIN.append('1')
        R7['text'] = "✅"
    else:
        CHWIN.append('0')
        R7['text'] = "❌"

    if(CH8a == Win8):
        CHWIN.append('1')
        R8['text'] = "✅"
    else:
        CHWIN.append('0')
        R8['text'] = "❌"

    if(CH9a == Win9):
        CHWIN.append('1')
        R9['text'] = "✅"
    else:
        CHWIN.append('0')
        R9['text'] = "❌"

    if(CH10a == Win10):
        CHWIN.append('1')
        R10['text'] = "✅"
    else:
        CHWIN.append('0')
        R10['text'] = "❌"

    # Verifie si le joueur a ganger
    if(CHWIN == ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']):
        print("WINNER")
        Status1['text'] = "Vous avez gangné le grolo! "
    else:
        print("SORRY NUMBERS DONT MATCH")
        Status1['text'] = "Désolé vous avez perdu. "
    # Final Set

    print(*CHWIN)




# Frame settings
def show_frame(frame):
    frame.tkraise()

# element for de l'exam et choix du frame
lotterieChoise = tk.Frame(lotterie)
WinNum = tk.Frame(lotterie)
for frame in (lotterieChoise, WinNum):
    frame.grid(row=0, column=0, sticky='nsew')

lotterieChoise['bg'] = '#becee5'
WinNum['bg'] = '#E5F6DF'

# FRAME 1 - lotterieChoise ( Choisir vos numbero)
SpaceUs = tk.Label(lotterieChoise, text='                               ')
SpaceUs.grid(row=0)

lotterieChoiseTitle = tk.Label(lotterieChoise, text='Choisisez vos numero gagnant :', bg="#D3D3D3")
lotterieChoiseTitle.grid(row='0', column='0',  sticky='n')
lotterieChoise1 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise1.grid(row='0', column='1')
lotterieChoise2 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise2.grid(row='0', column='2')
lotterieChoise3 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise3.grid(row='0', column='3')
lotterieChoise4 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise4.grid(row='0', column='4')
lotterieChoise5 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise5.grid(row='0', column='5')
lotterieChoise6 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise6.grid(row='0', column='6')
lotterieChoise7 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise7.grid(row='0', column='7')
lotterieChoise8 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise8.grid(row='0', column='8')
lotterieChoise9 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise9.grid(row='0', column='9')
lotterieChoise10 = tk.Label(lotterieChoise, text='--/ 1-10 /--', bg='#D3D3D3')
lotterieChoise10.grid(row='0', column='10')

lotterieChoixTitre = tk.Label(lotterieChoise, text='Votre choix :', bg="#becee5")
lotterieChoixTitre.grid(row='1', column='0', sticky='e')

UF_CH1 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH1.grid(row=1, column=1)
UF_CH1.insert(0, "0")
UF_CH2 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH2.grid(row=1, column=2)
UF_CH2.insert(0, "0")
UF_CH3 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH3.grid(row=1, column=3)
UF_CH3.insert(0, "0")
UF_CH4 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH4.grid(row=1, column=4)
UF_CH4.insert(0, "0")
UF_CH5 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH5.grid(row=1, column=5)
UF_CH5.insert(0, "0")
UF_CH6 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH6.grid(row=1, column=6)
UF_CH6.insert(0, "0")
UF_CH7 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH7.grid(row=1, column=7)
UF_CH7.insert(0, "0")
UF_CH8 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH8.grid(row=1, column=8)
UF_CH8.insert(0, "0")
UF_CH9 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH9.grid(row=1, column=9)
UF_CH9.insert(0, "0")
UF_CH10 = tk.Entry(lotterieChoise, bg="#FFFFFF", width='5', highlightbackground='#becee5')
UF_CH10.grid(row=1, column=10)
UF_CH10.insert(0, "0")



UF_CH_SAVE = tk.Button(lotterieChoise, text="Acheter", highlightbackground='#becee5', command=get_data)
UF_CH_SAVE.grid(row=2, column=5, columnspan='2')

# Demontre les numero que tu a choisi avent de joue
VERNUM1 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM1.grid(row=3, column=1)
VERNUM2 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM2.grid(row=3, column=2)
VERNUM3 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM3.grid(row=3, column=3)
VERNUM4 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM4.grid(row=3, column=4)
VERNUM5 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM5.grid(row=3, column=5)
VERNUM6 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM6.grid(row=3, column=6)
VERNUM7 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM7.grid(row=3, column=7)
VERNUM8 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM8.grid(row=3, column=8)
VERNUM9 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM9.grid(row=3, column=9)
VERNUM10 = tk.Label(lotterieChoise, text='', bg="#becee5")
VERNUM10.grid(row=3, column=10)

# Bouton pour traiter les numero
VERNUM = tk.Label(lotterieChoise, text='Vos numéro :', bg='#becee5')
VERNUM.grid(row=3, column=0, sticky='e')

lotterieChoiseDate = tk.Label(lotterieChoise, text=datenow, bg='#becee5')
lotterieChoiseDate.grid(row=2, column='0', sticky='e')

UF_CH_SUB = tk.Button(lotterieChoise, text="Joué Mètenet", highlightbackground='#becee5', command=lambda: show_frame(WinNum))
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

show_frame(lotterieChoise)
lotterie.mainloop()
