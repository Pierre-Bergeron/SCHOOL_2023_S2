# Author : Pierre Bergeron
# Date   : MR30/23
# Titre  : U3_SOMMATIF
# GIT    : SCHOOL_2023_S2
# DESCR. :

import numpy as np
import pyperclip as clp

# Légende (Ref d'article, quantité en stock, prix, commende automatique, description)
ArrInv = np.array([[1, 10.0, 50.00, "Actif", "USB power bank"],
                   [2, 6.0, 15.99, "Actif", "Phone Charger"],
                   [3, 2.0, 9.99, "Null", "Power Block USB"],
                   [4, 26.0, 4.99, "Null", "USB Light"],
                   [5, 87.0, 38.77, "Actif", "Wireless Charger"]])
strSelection = ""


# Fonction Pull, Push, Del, Edit
# Sub_sel (1 = Description, 2 = Cost, 3 = QTY, 4 = IPFR)
# id_sel (1 = Desc, 2 = IPFR status, 3 = inventory, 4 = prix, 5 = ref)
def find(id_ref):
    row = 0
    arraylen = len(ArrInv)
    while row < arraylen:
        if id_ref == ArrInv[row][0]:
            rowId = row + 1
            return rowId
        else:
            row = row + 1
def pull(id_ref, id_sel):
    scr_id = id_ref - 1
    if id_sel == 1:
        o1 = ArrInv[scr_id][4]
        return o1
    elif id_sel == 2:
        o2 = ArrInv[scr_id][3]
        return o2
    elif id_sel == 3:
        o3 = ArrInv[scr_id][1]
        return o3
    elif id_sel == 4:
        o4 = ArrInv[scr_id][2]
        return o4
    elif id_sel == 5:
        o5 = ArrInv[scr_id][0]
        return o5
    else:
        null = "null"
        return null


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


while not (strSelection == "Q" or strSelection == "q"):
    print("""
  Menu
  ----
  1 - Recherché un article
  2 - Passer une transaction
  3 - Inventaire
  4 - Ajouté ou Modifier un article 
  5 - Suprimer un article
  6 - Liste les articles
  Q - Quitter
  """)
    strSelection = input("Indiquer votre choix : ")
    # Cette section demontre tous information sur le produit utilisent sa referance.
    if strSelection == "1":
        ArtId = input("Referance de l'article : ")
        Id = find(ArtId)

        Desc, IPFR_S, Qty, Cost = pull(Id, 1), pull(Id, 2), pull(Id, 3), pull(Id, 4)
        print("\n", "Article : ", Desc, "\n", "Prix : ", Cost, "$", "\n", "En Stock : ", Qty, " unité", "\n",
              "Orde Auto : ",
              IPFR_S)

        done = input("Retour? (Y) : ")
    # Cette section es un POS pour passer un produit comme transaction et l'enlever de l'inventaire pas la suite
    elif strSelection == "2":
        ArtId = input("Referance de l'article : ")
        Id = find(ArtId)
        print("Quantité Disponible : ", pull(Id, 3))
        AchQ = int(input("Quantité acheté : "))
        prix = float(pull(Id, 4))

        sub = prix * AchQ
        hst = round(sub * 0.13, 2)
        tot = round(sub + hst, 2)

        print("Sous-total -- ", sub, "$", " -- (", AchQ, " * ", pull(Id, 2), "$)")
        print("HST (ON) ---- ", hst, "$")
        print("Total ------- ", tot, "$")
        conf = input("Voulez vous passé la transaction (O/N)? ")
        if conf == "O":
            setQTY = float(pull(Id, 3)) - AchQ
            push(Id, 3, setQTY)
        else:
            print("**Transaction Annuler**")

        print("Nouvelle Quantité en Stock : ", pull(Id, 3))

        done = input("Retour? (Y) : ")
    # Cette section est pour ajuster la quantité en stock
    elif strSelection == "3":
        print("""
        1 - Conte d'inventaire
        2 - Commende Recu
        """)
        strInv = input("Indiquer votre choix : ")
        if strInv == "1":
            ArtId = input("Referance de l'article : ")
            Id = find(ArtId)
            print("Quantité En Stock : ", pull(Id, 3))
            NewQ = int(input("Quantité Actuelle : "))
            push(Id, 3, NewQ)
            print("Quantité changer à ", pull(Id, 3), " en stock.")

            done = input("Retour? (Y) : ")
        # Cette section est pour recevoir du stock d'une commende
        elif strInv == "2":
            ArtId = input("Referance de l'article : ")
            Id = find(ArtId)
            RcvQ = int(input("Quantité Reçu : "))
            PrvQ = float(pull(Id, 3))
            AddedQ = PrvQ + RcvQ
            push(Id, 3, AddedQ)
            print("Nouvelle Quantité est ", pull(Id, 3), " en stock.")

            done = input("Retour? (Y) : ")
    # Cette section est pour ajouté une nouvelle article ou modifier une existante
    elif strSelection == "4":
        print("""
            1 - Ajouté un article
            2 - Modifié un article
        """)
        strItm = input("Indiquer votre choix : ")
        # Ajoute une nouvelle article au array
        if strItm == "1":
            Id_len = len(ArrInv)
            Nid = Id_len + 1
            Ndesc1 = input("Description de l'article : ")
            Ncst = float(input("Le prix de l'article : "))
            Nqty1 = int(input("Quantité d'article     : "))
            Nipfr_s = input("Commende automatique ? (Actif / Null) : ")
            NewItm = np.array([Nid, Nqty1, Ncst, Nipfr_s, Ndesc1])
            ArrInv = np.vstack([ArrInv, NewItm])

            done = input("Retour? (Y) : ")
        # Modifie une article a partir de ca referance
        elif strItm == "2":
            ArtId = input("Referance de l'article : ")
            Id = find(ArtId)
            Desc, IPFR_S, Qty, Cost = pull(Id, 1), pull(Id, 2), pull(Id, 3), pull(Id, 4)

            print("\nInformation Acctuel sur L'Article")
            print("Description ---------- ", Desc)
            print("Prix ----------------- ", Cost, "$")
            print("Quantité ------------- ", Qty)
            print("Commande Automatique - ", IPFR_S)
            print("\n**Nouvelle Information**")
            print("Utilise **Ctrl + V** si il a aucun changement")

            # Ajoute la donne presedent du clavier a ton press-papier (Cntl + V)
            clpstack = clp.paste()
            clp.copy(Desc)
            Ndesc = input("Nouvelle Description : ")
            clp.copy(clpstack)

            clp.copy(Cost)
            Ncost = input("Nouveaux prix        : ")
            clp.copy(clpstack)

            clp.copy(Qty)
            Nqty = input("Nouvelle Quantité     : ")
            clp.copy(clpstack)

            clp.copy(IPFR_S)
            Nipfr = input("Commande Automatique : ")
            clp.copy(clpstack)

            # Save les donne sur le Array ici
            push(Id, 1, Ndesc)
            push(Id, 4, Ncost)
            push(Id, 3, Nqty)
            push(Id, 2, Nipfr)

            print("\nVous avez soumis : {} | {}$ | {}u | {}\n".format(Ndesc, Ncost, Nqty, Nipfr))
            done = input("Retour? (Y) : ")
    # Supprime les donnee d'un article mais garde le Ref # vide pour pouvoir le re-ajoute plus tard.
    elif strSelection == "5":
        ArtId = input("Referance de l'article : ")
        Id = find(ArtId)
        na = "N/A"
        nl = "Null"
        push(Id, 1, na)
        push(Id, 2, nl)
        push(Id, 3, na)
        push(Id, 4, na)

        print("L'article {} à été supprimer, vous pouvez toujours la modifié".format(ArtId))
        done = input("Retour? (Y) : ")
    # Cree un audit de l'inventaire et meme la valeur total des article combiner.
    elif strSelection == "6":
        ArrInv_Len = len(ArrInv) - 1
        ArrInv_Len1 = len(ArrInv)
        a = 0
        b = 1
        print("  REF | QTY | PRIX | IPFR | DESCRIPTION")
        # id_sel (1 = Desc, 2 = IPFR status, 3 = inventory, 4 = prix, 5 = ref)
        while b <= ArrInv_Len1:
            print(f"{pull(b, 5):^7} {pull(b,3):^5} {pull(b, 4):6} {pull(b, 2):^6} {pull(b, 1)}")
            b = b + 1
        print("  REF | QTY | PRIX | IPFR | DESCRIPTION\n")


        Qty_tot = 0
        Cst_tota = 0
        while a <= ArrInv_Len:
            Qty_tot = Qty_tot + float(pull(a, 3))
            Cst_tota = Cst_tota + (float(pull(a, 3)) * float(pull(a, 4)))
            a = a + 1
        Cst_tot = round(Cst_tota, 2)
        print("L'inventaire contient {} articles individuel en total.\nEt elle veaux {}$ CAD en total.".format(Qty_tot,
                                                                                                               Cst_tot))

        done = input("Retour? (Y) : ")
print("Passé une belle journée.")
# Les autres options suivent.
