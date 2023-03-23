# Auteur : Pierre-Bergeron
# Date   : MR18/23
# Titre  : U2_SOMMATIF
# GIT    : SCHOOL_2023_S2

import numpy as np
import pyperclip as clp

# Légende (Ref d'article, quantité en stock, prix, commende automatique, description)
ArrInv = np.array([[1, 10.0, 50.00, "Oui", "USB power bank"],
                   [2, 6.0, 15.99, "Oui", "Phone Charger"],
                   [3, 2.0, 9.99, "Non", "Power Block USB"],
                   [4, 26.0, 4.99, "Non", "USB Light"],
                   [5, 87.0, 38.77, "Non", "Wireless Charger"]])
strSelection = 0

while not (strSelection == "Q" or strSelection == "q"):
    print("""
  Menu
  ----
  1 - Rechèrche d'article
  2 - Passer une transaction
  3 - Inventaire
  4 - Ajouté ou Modifier un article 
  5 - Suprimer un article
  6 - Liste les articles
  Q - Quitter
  """)
    strSelection = input("Indiquer votre choix : ")

    if strSelection == "1":
        ArtId = int(input("Referance de l'article : "))
        Id = ArtId - 1
        Desc = ArrInv[Id][4]
        Cost = ArrInv[Id][2]
        Qty = ArrInv[Id][1]
        IPFR_S = ArrInv[Id][3]
        print("Article : ", Desc)
        print("Prix : ", Cost, "$")
        print("En Stock : ", Qty, " unité")
        print("Orde Auto : ", IPFR_S)

        done = input("Retour? (Y) : ")

    elif strSelection == "2":
        ArtId = int(input("Referance de l'article : "))
        Id = ArtId - 1
        print("Quantité Disponible : ", ArrInv[Id][1])
        AchQ = int(input("Quantité acheté : "))
        prix = float(ArrInv[Id][2])

        itc = ArrInv[Id][2]
        sub = prix * AchQ
        hst = round(sub * 0.13, 2)
        tot = round(sub + hst, 2)

        print("Sous-total -- ", sub, "$", " -- (", AchQ, " * ", itc, "$)")
        print("HST (ON) ---- ", hst, "$")
        print("Total ------- ", tot, "$")
        conf = input("Voulez vous passé la transaction (O/N)? ")
        if conf == "O":
            ArrInv[Id][1] = float(ArrInv[Id][1]) - AchQ
        else:
            print("**Transaction Annuler**")
        print("Nouvelle Quantité en Stock : ", ArrInv[Id][1])

        done = input("Retour? (Y) : ")

    elif strSelection == "3":
        print("""
        1 - Conte d'inventaire
        2 - Commende Recu
        """)
        strInv = input("Indiquer votre choix : ")
        if strInv == "1":
            ArtId = int(input("Referance de l'article : "))
            Id = ArtId - 1
            print("Quantité En Stock : ", ArrInv[Id][1])
            NewQ = int(input("Quantité Actuelle : "))
            ArrInv[Id][1] = NewQ
            print("Quantité changer à ", ArrInv[Id][1], " en stock.")

            done = input("Retour? (Y) : ")
        elif strInv == "2":
            ArtId = int(input("Referance de l'article : "))
            Id = ArtId - 1
            RcvQ = int(input("Quantité Reçu : "))
            PrvQ = float(ArrInv[Id][1])
            ArrInv[Id][1] = PrvQ + RcvQ
            print("Nouvelle Quantité est ", ArrInv[Id][1], " en stock.")

            done = input("Retour? (Y) : ")
    elif strSelection == "4":
        print("""
            1 - Ajouté un article
            2 - Modifié un article
        """)
        strItm = input("Indiquer votre choix : ")
        if strItm == "1":

            done = input("Retour? (Y) : ")
        elif strItm == "2":
            ArtId = int(input("Referance de l'article : "))
            Id = ArtId - 1
            Desc = ArrInv[Id][4]
            Cost = ArrInv[Id][2]
            Qty = ArrInv[Id][1]
            IPFR_S = ArrInv[Id][3]
            print("\nInformation Acctuel sur L'Article")
            print("Description ---------- ", Desc)
            print("Prix ----------------- ", Cost, "$")
            print("Quantité ------------- ", Qty)
            print("Commande Automatique - ", IPFR_S)
            print("\n**Nouvelle Information**")
            print("Utilise **Ctrl + V** si il a aucun changement")

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

            # fonction pour modifier les donnees va etre ICI


            print("\nVous avez soumis : {} | {}$ | {}u | {}\n".format(Ndesc, Ncost, Nqty, Nipfr))
            done = input("Retour? (Y) : ")
        print("4")

    elif strSelection == "5":
        print("5")

    elif strSelection == "6":
        print("6")
print("Passé une belle journée.")
# Les autres options suivent.
