# Author : Pierre Bergeron
# Date : MA23/23
# File : U6_SOMMATIF

import tkinter as tk
import numpy as np
import math
import datetime


# Article Array
ArrInv = np.array([[1, 10.0, 50.00, "Actif", "USB power bank"],
                   [2, 6.0, 15.99, "Actif", "Phone Charger"],
                   [3, 2.0, 9.99, "Null", "Power Block USB"],
                   [4, 26.0, 4.99, "Null", "USB Light"],
                   [7, 87.0, 38.77, "Actif", "Wireless Charger"],
                   [6, 21.0, 21.99, "Null", "White Brd Case (30pc)"],
                   [5, 0.0, 19.98, "Null", "Christmas Lights"]])

# Global function
# id_sel (1 = Desc, 2 = IPFR status, 3 = inventory, 4 = prix, 5 = ref)
def pull(id_ref, id_sel):
    scr_id = id_ref - 1
    if id_sel == 1:
        desc = ArrInv[scr_id][4]
        return desc
    elif id_sel == 2:
        ipfr = ArrInv[scr_id][3]
        return ipfr
    elif id_sel == 3:
        qty_inv = ArrInv[scr_id][1]
        return qty_inv
    elif id_sel == 4:
        prix = ArrInv[scr_id][2]
        return prix
    elif id_sel == 5:
        ref_id_arr = ArrInv[scr_id][0]
        return ref_id_arr
    else:
        null = "null"
        return null

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

def find_ref(id_ref):
    row = 0
    arraylen = len(ArrInv)
    while row < arraylen:
        if id_ref == ArrInv[row][0]:
            rowId = row + 1
            return rowId
        else:
            row = row + 1
# element for de l'exam et choix du frame
page1 = tk.Frame(pageA)
page2 = tk.Frame(pageA)
page3 = tk.Frame(pageA)
page4 = tk.Frame(pageA)
page5 = tk.Frame(pageA)
page6 = tk.Frame(pageA)
page7 = tk.Frame(pageA)


for frame in (page1, page2, page3, page4, page5, page6, page7):
    frame.grid(row=0, column=0, sticky='nsew')

page1['bg'] = '#becee5'
page2['bg'] = '#E5F6DF'
page3['bg'] = '#E5F6DF'
page4['bg'] = '#E5F6DF'
page5['bg'] = '#E5F6DF'
page6['bg'] = '#E5F6DF'
page7['bg'] = '#E5F6DF'

# Frame Window Change Btn
btn_frame_page2 = tk.Button(page1, text="Page 2", highlightbackground='#becee5', command=lambda: show_frame(page2))
btn_frame_page2.grid(row=5, column=5, columnspan='2')
btn_frame_page3 = tk.Button(page1, text="Page 3", highlightbackground='#becee5', command=lambda: show_frame(page3))
btn_frame_page3.grid(row=6, column=5, columnspan='2')
btn_frame_page4 = tk.Button(page1, text="Page 4", highlightbackground='#becee5', command=lambda: show_frame(page4))
btn_frame_page4.grid(row=7, column=5, columnspan='2')
btn_frame_page5 = tk.Button(page1, text="Page 5", highlightbackground='#becee5', command=lambda: show_frame(page5))
btn_frame_page5.grid(row=8, column=5, columnspan='2')
btn_frame_page6 = tk.Button(page1, text="Page 6", highlightbackground='#becee5', command=lambda: show_frame(page6))
btn_frame_page6.grid(row=9, column=5, columnspan='2')
btn_frame_page7 = tk.Button(page1, text="Page 7", highlightbackground='#becee5', command=lambda: show_frame(page7))
btn_frame_page7.grid(row=10, column=5, columnspan='2')

# frame 1 (page1) - option selection screen ( choisir son option)
SpaceUs = tk.Label(page1, text='                               ')
SpaceUs.grid(row=0)

page1Titre = tk.Label(page1, text='Menu', bg="#D3D3D3")
page1Titre.grid(row='0', column='0',  sticky='n')

page2Titre = tk.Label(page1, text="Recherche d'article", bg="#becee5")
page2Titre.grid(row='1', column='0', sticky='e')


# UF_CH_SAVE = tk.Button(page1, text="Acheter", highlightbackground='#becee5', command=None)
# UF_CH_SAVE.grid(row=2, column=5, columnspan='2')

lotterieChoiseDate = tk.Label(page1, text=datenow, bg='#becee5')
lotterieChoiseDate.grid(row=2, column='0', sticky='e')


# Demontre les numero que tu a choisi dans le 2e frame
def find_article_page2():
    article_id_sumitted = find_ref(articleNum_Input.get())
    article_desc = pull(article_id_sumitted, 1)
    article_prix = pull(article_id_sumitted, 4)
    article_ipfr = pull(article_id_sumitted, 2)
    article_invt = pull(article_id_sumitted, 3)

    desc_page2_txt['text'] = article_desc
    prix_page2_txt['text'] = article_prix
    ipfr_page2_txt['text'] = article_ipfr
    invt_page2_txt['text'] = article_invt

# frame 2 (page 2) search item by article
Titre2 = tk.Label(page2, text="Numéro d'article :", bg='#E5F6DF')
Titre2.grid(row=0, column=0, sticky='e')

articleNum_Input = tk.Entry(page2, bg="#FFFFFF", width=5, highlightbackground='#becee5')
articleNum_Input.grid(row=0, column=1, columnspan=2)

articleNum_Submit = tk.Button(page2, text="Recherché l'article", highlightbackground='#becee5', command=find_article_page2)
articleNum_Submit.grid(row=0, column=3, columnspan=2)

desc_page2_lbl = tk.Label(page2, text='Description :', bg='#E5F6DF')
desc_page2_lbl.grid(row=2, column=0, sticky='e')
desc_page2_txt = tk.Label(page2, text='', bg='#E5F6DF')
desc_page2_txt.grid(row=2, column=1)

prix_page2_lbl = tk.Label(page2, text='Prix /Unité :', bg='#E5F6DF')
prix_page2_lbl.grid(row=3, column=0, sticky='e')
prix_page2_txt = tk.Label(page2, text='', bg='#E5F6DF')
prix_page2_txt.grid(row=3, column=1)

ipfr_page2_lbl = tk.Label(page2, text='IPFR Status :', bg='#E5F6DF')
ipfr_page2_lbl.grid(row=4, column=0, sticky='e')
ipfr_page2_txt = tk.Label(page2, text='', bg='#E5F6DF')
ipfr_page2_txt.grid(row=4, column=1)

invt_page2_lbl = tk.Label(page2, text='Inventaire  :', bg='#E5F6DF')
invt_page2_lbl.grid(row=5, column=0, sticky='e')
invt_page2_txt = tk.Label(page2, text='', bg='#E5F6DF')
invt_page2_txt.grid(row=5, column=1)

btn_page2_menu = tk.Button(page2, text="Retour au menu", highlightbackground='#becee5', command=lambda: show_frame(page1))
btn_page2_menu.grid(row=7, column=0, columnspan=2)

Status = tk.Label(page2, text='État :', bg='#E5F6DF')
Status.grid(row=10, column=0, sticky='e')
Status1 = tk.Label(page2, text='', bg='#E5F6DF')
Status1.grid(row=3, column=1, columnspan=5)

show_frame(page1)
pageA.mainloop()