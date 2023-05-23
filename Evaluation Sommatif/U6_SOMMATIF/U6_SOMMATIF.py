# Author : Pierre Bergeron
# Date : MA23/23
# File : U6_SOMMATIF

import tkinter as tk
import numpy as np
import math


# Article Array
ArrInv = np.array([[0, 0.0, 0.00, "null", "Article Inconnu"],
                   [1, 10.0, 50.00, "Actif", "USB power bank"],
                   [2, 6.0, 15.99, "Actif", "Phone Charger"],
                   [3, 2.0, 9.99, "Null", "Power Block USB"],
                   [4, 26.0, 4.99, "Null", "USB Light"],
                   [7, 87.0, 38.77, "Actif", "Wireless Charger"],
                   [6, 21.0, 21.99, "Null", "White Brd (30pc)"],
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
pageA.geometry("315x350")
# 1004x700 original size
pageA.rowconfigure(0, weight=1)
pageA.columnconfigure(0, weight=1)


# Frame settings
def show_frame(frame):
    frame.tkraise()

def find_ref(id_ref):
    row = 0
    not_on_file = 1
    arraylen = len(ArrInv)
    while row < arraylen:
        if id_ref == ArrInv[row][0]:
            rowId = row + 1
            return rowId
        else:
            row = row + 1
    if row >= arraylen:
        return 1
    else:
        print("FUNCTION find_ref FAILED")


# element for de l'exam et choix du frame

page1 = tk.Frame(pageA)
page2 = tk.Frame(pageA)
page3 = tk.Frame(pageA)
page3B = tk.Frame(pageA)
page4 = tk.Frame(pageA)
page5 = tk.Frame(pageA)
page6 = tk.Frame(pageA)
page7 = tk.Frame(pageA)


for frame in (page1, page2, page3, page3B, page4, page5, page6, page7):
    frame.grid(row=0, column=0, sticky='nsew')

page1['bg'] = '#becee5'
page2['bg'] = '#E5F6DF'
page3['bg'] = '#E5F6DF'
page3B['bg'] = '#E5F6DF'
page4['bg'] = '#E5F6DF'
page5['bg'] = '#E5F6DF'
page6['bg'] = '#E5F6DF'
page7['bg'] = '#E5F6DF'

# Frame Window Change Btn
btn_frame_page2 = tk.Button(page1, text="Recherché un article", width=25, highlightbackground='#becee5', command=lambda: show_frame(page2))
btn_frame_page2.grid(row=2, column=1, sticky='n')
btn_frame_page3 = tk.Button(page1, text="Passer une transaction", width=25, highlightbackground='#becee5', command=lambda: show_frame(page3))
btn_frame_page3.grid(row=3, column=1, sticky='n')
btn_frame_page4 = tk.Button(page1, text="Inventaire", width=25, highlightbackground='#becee5', command=lambda: show_frame(page4))
btn_frame_page4.grid(row=4, column=1, sticky='n')
btn_frame_page5 = tk.Button(page1, text="Ajouté ou Modifier un article", width=25, highlightbackground='#becee5', command=lambda: show_frame(page5))
btn_frame_page5.grid(row=5, column=1, sticky='n')
btn_frame_page6 = tk.Button(page1, text="Suprimer un article", width=25, highlightbackground='#becee5', command=lambda: show_frame(page6))
btn_frame_page6.grid(row=6, column=1, sticky='n')
btn_frame_page7 = tk.Button(page1, text="Lister les articles", width=25, highlightbackground='#becee5', command=lambda: show_frame(page7))
btn_frame_page7.grid(row=7, column=1, sticky='n')


blk_space1 = tk.Label(page1, text='', width=4, bg="#D3D3D3")
blk_space1.grid(row=0, column=0)
blk_space2 = tk.Label(page1, text='', width=4, bg="#D3D3D3")
blk_space2.grid(row=0, column=3)
page1Titre = tk.Label(page1, text='Menu Principale', width=25, bg="#D3D3D3")
page1Titre.grid(row=0, column=1, sticky='n')


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
page2_titre = tk.Label(page2, text="Numéro d'article :", bg='#E5F6DF')
page2_titre.grid(row=0, column=0, sticky='e')

articleNum_Input = tk.Entry(page2, bg="#FFFFFF", width=6, highlightbackground='#E5F6DF')
articleNum_Input.grid(row=0, column=1)

articleNum_Submit = tk.Button(page2, text="Rechercher", highlightbackground='#E5F6DF', command=find_article_page2)
articleNum_Submit.grid(row=0, column=3)

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

page2_space = tk.Label(page2, text='', bg='#E5F6DF')
page2_space.grid(row=6, column=0)
btn_page2_menu = tk.Button(page2, text="Retour au menu", highlightbackground='#E5F6DF', command=lambda: show_frame(page1))
btn_page2_menu.grid(row=7, column=0, sticky='n')

# Page 3 (Transaction)
def get_desc_1():
    article_id_sumitted = find_ref(id_inp_prd_1.get())
    article_desc = pull(article_id_sumitted, 1)
    desc_txt_prd_1['text'] = article_desc

def get_desc_2():
    article_id_sumitted = find_ref(id_inp_prd_2.get())
    article_desc = pull(article_id_sumitted, 1)
    desc_txt_prd_2['text'] = article_desc

def get_desc_3():
    article_id_sumitted = find_ref(id_inp_prd_3.get())
    article_desc = pull(article_id_sumitted, 1)
    desc_txt_prd_3['text'] = article_desc


page3_titre = tk.Label(page3, text="Article à acheté;", bg='#E5F6DF')
page3_titre.grid(row=0, column=0, columnspan=2, sticky='n')
label_REF = tk.Label(page3, text="⬇Article ID⬇", bg='#E5F6DF')
label_REF.grid(row=1, column=0, columnspan=2, sticky='n')
label_DESC = tk.Label(page3, text="⬇Description⬇", bg='#E5F6DF')
label_DESC.grid(row=1, column=2, columnspan=2, sticky='n')
label_QTY = tk.Label(page3, text="⬇Quantité⬇", bg='#E5F6DF')
label_QTY.grid(row=1, column=4, columnspan=2, sticky='n')

id_inp_prd_1 = tk.Entry(page3, bg="#FFFFFF", width=6, highlightbackground='#E5F6DF')
id_inp_prd_1.grid(row=2, column=0, columnspan=2)
id_inp_prd_1.insert(0, "0")
desc_txt_prd_1 = tk.Label(page3, text='', font=("Arial", 10), width=15, bg="#E5F6DF")
desc_txt_prd_1.grid(row=2, column=2)
desc_btn_sync_1 = tk.Button(page3, text="G", width=2, highlightbackground="#E5F6DF", command=get_desc_1)
desc_btn_sync_1.grid(row=2, column=3)
qty_inp_prd_1 = tk.Entry(page3, bg="#FFFFFF", width=6, highlightbackground='#E5F6DF')
qty_inp_prd_1.grid(row=2, column=4, columnspan=2)
qty_inp_prd_1.insert(0, "0")

id_inp_prd_2 = tk.Entry(page3, bg="#FFFFFF", width=6, highlightbackground='#E5F6DF')
id_inp_prd_2.grid(row=3, column=0, columnspan=2)
id_inp_prd_2.insert(0, "0")
desc_txt_prd_2 = tk.Label(page3, text='', font=("Arial", 10), width=15, bg="#E5F6DF")
desc_txt_prd_2.grid(row=3, column=2)
desc_btn_sync_2 = tk.Button(page3, text="G", width=2, highlightbackground="#E5F6DF", command=get_desc_2)
desc_btn_sync_2.grid(row=3, column=3)
qty_inp_prd_2 = tk.Entry(page3, bg="#FFFFFF", width=6, highlightbackground='#E5F6DF')
qty_inp_prd_2.grid(row=3, column=4, columnspan=2)
qty_inp_prd_2.insert(0, "0")

id_inp_prd_3 = tk.Entry(page3, bg="#FFFFFF", width=6, highlightbackground='#E5F6DF')
id_inp_prd_3.grid(row=4, column=0, columnspan=2)
id_inp_prd_3.insert(0, "0")
desc_txt_prd_3 = tk.Label(page3, text='', font=("Arial", 10), width=15, bg="#E5F6DF")
desc_txt_prd_3.grid(row=4, column=2)
desc_btn_sync_3 = tk.Button(page3, text="G", width=2, highlightbackground="#E5F6DF", command=get_desc_3)
desc_btn_sync_3.grid(row=4, column=3)
qty_inp_prd_3 = tk.Entry(page3, bg="#FFFFFF", width=6, highlightbackground='#E5F6DF')
qty_inp_prd_3.grid(row=4, column=4, columnspan=2)
qty_inp_prd_3.insert(0, "0")

def purchase_review():
    article_id_sumitted1 = find_ref(id_inp_prd_1.get())
    article_desc1 = pull(article_id_sumitted1, 1)
    pur_1_desc['text'] = article_desc1

    qty_buy_1 = int(qty_inp_prd_1.get())
    prd_1_prix = float(pull(article_id_sumitted1, 4))
    prd_1_tot = qty_buy_1 * prd_1_prix
    pur_1_qty['text'] = qty_buy_1
    pur_1_prix['text'] = prd_1_prix
    pur_1_tot['text'] = prd_1_tot

    article_id_sumitted2 = find_ref(id_inp_prd_2.get())
    article_desc2 = pull(article_id_sumitted2, 1)
    pur_2_desc['text'] = article_desc2

    qty_buy_2 = int(qty_inp_prd_2.get())
    prd_2_prix = float(pull(article_id_sumitted2, 4))
    prd_2_tot = qty_buy_2 * prd_2_prix
    pur_2_qty['text'] = qty_buy_2
    pur_2_prix['text'] = prd_2_prix
    pur_2_tot['text'] = prd_2_tot

    article_id_sumitted3 = find_ref(id_inp_prd_3.get())
    article_desc3 = pull(article_id_sumitted3, 1)
    pur_3_desc['text'] = article_desc3

    qty_buy_3 = int(qty_inp_prd_3.get())
    prd_3_prix = float(pull(article_id_sumitted3, 4))
    prd_3_tot = qty_buy_3 * prd_3_prix
    pur_3_qty['text'] = qty_buy_3
    pur_3_prix['text'] = prd_3_prix
    pur_3_tot['text'] = prd_3_tot

    # Add sub, HST, tot calculation here ...

    print(prd_1_tot)
    print(prd_2_tot)
    print(prd_3_tot)
    print("here")
    show_frame(page3B)



purchase_next = tk.Button(page3, text="Suivent", highlightbackground="#E5F6DF", command=purchase_review)
purchase_next.grid(row=5, column=0, columnspan=6)


label_prh_desc = tk.Label(page3B, text="⬇Produit⬇", bg='#E5F6DF')
label_prh_desc.grid(row=0, column=0, sticky='n')
label_prh_qty = tk.Label(page3B, text="⬇Quantité⬇", bg='#E5F6DF')
label_prh_qty.grid(row=0, column=2, sticky='n')
label_prh_prix = tk.Label(page3B, text="⬇Prix⬇", bg='#E5F6DF')
label_prh_prix.grid(row=0, column=3, sticky='n')
label_prh_tot = tk.Label(page3B, text="⬇Total⬇", bg='#E5F6DF')
label_prh_tot.grid(row=0, column=4, sticky='n')

pur_1_desc = tk.Label(page3B, text="", font=("Arial", 10), bg='#E5F6DF')
pur_1_desc.grid(row=1, column=0, sticky='n')
pur_2_desc = tk.Label(page3B, text="", font=("Arial", 10), bg='#E5F6DF')
pur_2_desc.grid(row=2, column=0, sticky='n')
pur_3_desc = tk.Label(page3B, text="", font=("Arial", 10), bg='#E5F6DF')
pur_3_desc.grid(row=3, column=0, sticky='n')

pur_1_qty = tk.Label(page3B, text="", bg='#E5F6DF')
pur_1_qty.grid(row=1, column=2, sticky='n')
pur_2_qty = tk.Label(page3B, text="", bg='#E5F6DF')
pur_2_qty.grid(row=2, column=2, sticky='n')
pur_3_qty = tk.Label(page3B, text="", bg='#E5F6DF')
pur_3_qty.grid(row=3, column=2, sticky='n')

pur_1_prix = tk.Label(page3B, text="", bg='#E5F6DF')
pur_1_prix.grid(row=1, column=3, sticky='n')
pur_2_prix = tk.Label(page3B, text="", bg='#E5F6DF')
pur_2_prix.grid(row=2, column=3, sticky='n')
pur_3_prix = tk.Label(page3B, text="", bg='#E5F6DF')
pur_3_prix.grid(row=3, column=3, sticky='n')

pur_1_tot = tk.Label(page3B, text="", bg='#E5F6DF')
pur_1_tot.grid(row=1, column=4, sticky='n')
pur_2_tot = tk.Label(page3B, text="", bg='#E5F6DF')
pur_2_tot.grid(row=2, column=4, sticky='n')
pur_3_tot = tk.Label(page3B, text="", bg='#E5F6DF')
pur_3_tot.grid(row=3, column=4, sticky='n')

show_frame(page1)
pageA.mainloop()