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


# 1=DESC, 2=IPFR, 3=QTY, 4=COST
def push(id_ref, id_sel, data_push):
    scr_id = id_ref - 1
    if id_sel == 1:
        ArrInv[scr_id][4] = data_push
        return
    elif id_sel == 2:
        ArrInv[scr_id][3] = data_push
        return
    elif id_sel == 3:
        ArrInv[scr_id][1] = data_push
        return
    elif id_sel == 4:
        ArrInv[scr_id][2] = data_push
        return
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
page4A = tk.Frame(pageA)
page4B = tk.Frame(pageA)
page5 = tk.Frame(pageA)
page6 = tk.Frame(pageA)
page7 = tk.Frame(pageA)
confirm_page = tk.Frame(pageA)


for frame in (page1, page2, page3, page3B, page4, page4A, page4B, page5, page6, page7, confirm_page):
    frame.grid(row=0, column=0, sticky='nsew')

page1['bg'] = '#becee5'
page2['bg'] = '#E5F6DF'
page3['bg'] = '#E5F6DF'
page3B['bg'] = '#E5F6DF'
page4['bg'] = '#becee5'
page4A['bg'] = '#E5F6DF'
page4B['bg'] = '#E5F6DF'
page5['bg'] = '#E5F6DF'
page6['bg'] = '#E5F6DF'
page7['bg'] = '#E5F6DF'
confirm_page['bg'] = "#2FEF10"

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

    art_id_prd1['text'] = id_inp_prd_1.get()
    art_id_prd2['text'] = id_inp_prd_2.get()
    art_id_prd3['text'] = id_inp_prd_3.get()


    # Add sub, HST, tot calculation here ...

    sub_total = prd_1_tot + prd_2_tot + prd_3_tot
    sub_tot_rnd = round(sub_total, 2)
    fnl_sub_txt['text'] = sub_tot_rnd
    hst_total = sub_total * 0.13
    hst_total_rnd = round(hst_total, 2)
    fnl_hst_txt['text'] = hst_total_rnd
    tot_total = sub_total * 1.13
    tot_total_rnd = round(tot_total, 2)
    fnl_tot_txt['text'] = tot_total_rnd

    show_frame(page3B)


def trans_approved():
    prd_1_qty = int(qty_inp_prd_1.get())
    prd_2_qty = int(qty_inp_prd_2.get())
    prd_3_qty = int(qty_inp_prd_3.get())
    article_id_1 = int(id_inp_prd_1.get())
    article_id_2 = int(id_inp_prd_2.get())
    article_id_3 = int(id_inp_prd_3.get())

    invt_new_qty1 = float(pull(article_id_1, 3)) - prd_1_qty
    push(article_id_1, 3, invt_new_qty1)
    invt_new_qty2 = float(pull(article_id_2, 3)) - prd_2_qty
    push(article_id_2, 3, invt_new_qty2)
    invt_new_qty3 = float(pull(article_id_3, 3)) - prd_3_qty
    push(article_id_3, 3, invt_new_qty3)

    show_frame(confirm_page)



# 1=DESC, 2=IPFR, 3=QTY, 4=COST


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


clr_row_4_1 = tk.Label(page3B, text='', width=10, bg="#D3D3D3")
clr_row_4_1.grid(row=4, column=0)
clr_row_4_2 = tk.Label(page3B, text='', width=10, bg="#D3D3D3")
clr_row_4_2.grid(row=4, column=2)
clr_row_4_3 = tk.Label(page3B, text='', width=6, bg="#D3D3D3")
clr_row_4_3.grid(row=4, column=3)

label_sub_tot = tk.Label(page3B, text='Sous-Total ➡︎', bg='#E5F6DF')
label_sub_tot.grid(row=5, column=0, sticky='e')
label_hst_tot = tk.Label(page3B, text='HST 13% ➡︎', bg='#E5F6DF')
label_hst_tot.grid(row=6, column=0, sticky='e')
label_tot_tot = tk.Label(page3B, text='Total ➡︎', bg='#E5F6DF')
label_tot_tot.grid(row=7, column=0, sticky='e')

fnl_sub_txt = tk.Label(page3B, text='', bg='#E5F6DF')
fnl_sub_txt.grid(row=5, column=4, sticky='n')
fnl_hst_txt = tk.Label(page3B, text='', bg='#E5F6DF')
fnl_hst_txt.grid(row=6, column=4, sticky='n')
fnl_tot_txt = tk.Label(page3B, text='', bg='#E5F6DF')
fnl_tot_txt.grid(row=7, column=4, sticky='n')

art_id_prd1 = tk.Label(page3B, text='', bg='#E5F6DF', fg='#E5F6DF')
art_id_prd1.grid(row=8, column=0, sticky='n')
art_id_prd2 = tk.Label(page3B, text='', bg='#E5F6DF', fg='#E5F6DF')
art_id_prd2.grid(row=9, column=0, sticky='n')
art_id_prd3 = tk.Label(page3B, text='', bg='#E5F6DF', fg='#E5F6DF')
art_id_prd3.grid(row=10, column=0, sticky='n')

purchase_aprv = tk.Button(page3B, text="Apprové la transaction", highlightbackground="#E5F6DF", command=trans_approved)
purchase_aprv.grid(row=8, column=1, columnspan=3)

option_page4 = tk.Label(page4, text="Options d'inventaire", font=("Arial", 34), bg='#becee5')
option_page4.grid(row=0, column=0, columnspan=3, sticky='n')
btn_frame_page4A = tk.Button(page4, text="Comté un article", width=25, highlightbackground='#becee5', command=lambda: show_frame(page4A))
btn_frame_page4A.grid(row=1, column=1, sticky='n')
btn_frame_page4B = tk.Button(page4, text="Commande Recu", width=25, highlightbackground='#becee5', command=lambda: show_frame(page4B))
btn_frame_page4B.grid(row=2, column=1, sticky='n')

def invt_4A_detail():
    id_4A = find_ref(page4A_id_inp.get())
    desc_4A = pull(id_4A, 1)
    prev_qty_4A = pull(id_4A, 3)
    page4A_desc_txt['text'] = desc_4A
    page4A_curCT_txt['text'] = prev_qty_4A

def set_inventory_ct():
    id_4A_s = find_ref(page4A_id_inp.get())
    new_qty_4A = int(page4A_accCT_inp.get())
    push(id_4A_s, 3, new_qty_4A)
    show_frame(confirm_page)


page4A_id_label = tk.Label(page4A, text="ID d'article :", bg='#E5F6DF')
page4A_id_label.grid(row=0, column=0, sticky='e')
page4A_id_inp = tk.Entry(page4A, bg="#FFFFFF", width=5, highlightbackground='#E5F6DF')
page4A_id_inp.grid(row=0, column=2, sticky='n')
page4A_id_detail = tk.Button(page4A, text="Détail sur l'article", highlightbackground="#E5F6DF", command=invt_4A_detail)
page4A_id_detail.grid(row=0, column=3, columnspan=2, sticky='n')

page4A_desc_label = tk.Label(page4A, text="Description :", bg='#E5F6DF')
page4A_desc_label.grid(row=2, column=0, sticky='e')
page4A_desc_txt = tk.Label(page4A, text="", bg='#E5F6DF')
page4A_desc_txt.grid(row=2, column=1, columnspan=3)

page4A_curCT_label = tk.Label(page4A, text="Quantité :", bg='#E5F6DF')
page4A_curCT_label.grid(row=3, column=0, sticky='e')
page4A_curCT_txt = tk.Label(page4A, text="", bg='#E5F6DF')
page4A_curCT_txt.grid(row=3, column=1, columnspan=3)

page4A_accCT_label = tk.Label(page4A, text="Quantité acctuel :", bg='#E5F6DF')
page4A_accCT_label.grid(row=4, column=0, sticky='e')
page4A_accCT_inp = tk.Entry(page4A, bg="#FFFFFF", width=5, highlightbackground='#E5F6DF')
page4A_accCT_inp.grid(row=4, column=2, sticky='n')
page4A_id_subm = tk.Button(page4A, text="Soummettre", highlightbackground="#E5F6DF", command=set_inventory_ct)
page4A_id_subm.grid(row=4, column=3, columnspan=2, sticky='n')






confirm_page_titre = tk.Label(confirm_page, text="Demande acceptée", font=("Arial", 35), bg='#2FEF10')
confirm_page_titre.grid(row=0, column=0, columnspan=3, sticky='n')
confirm_page_rtn = tk.Button(confirm_page, text="Retour au menu", highlightbackground="#2FEF10", command=lambda: show_frame(page1))
confirm_page_rtn.grid(row=1, column=0, columnspan=3)




show_frame(page1)
pageA.mainloop()