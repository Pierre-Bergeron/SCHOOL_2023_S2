# Auteur : Pierre-Bergeron
# Date   : MR18/23
# Titre  : U2_SOMMATIF
# GIT    : SCHOOL_2023_S2

import numpy as np
import pyperclip as clp

# Légende (Ref d'article, quantité en stock, prix, commende automatique, description)
ArrInv = np.array([[1, 10.0, 50.00, "Actif", "USB power bank"],
                   [2, 6.0, 15.99, "Actif", "Phone Charger"],
                   [3, 2.0, 9.99, "Null", "Power Block USB"],
                   [4, 26.0, 4.99, "Null", "USB Light"],
                   [5, 87.0, 38.77, "Actif", "Wireless Charger"]])
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
    # Cette section demontre tous information sur le produit utilisent sa referance.
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
    # Cette section es un POS pour passer un produit comme transaction et l'enlever de l'inventaire pas la suite
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
    # Cette section est pour ajuster la quantité en stock
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
        # Cette section est pour recevoir du stock d'une commende
        elif strInv == "2":
            ArtId = int(input("Referance de l'article : "))
            Id = ArtId - 1
            RcvQ = int(input("Quantité Reçu : "))
            PrvQ = float(ArrInv[Id][1])
            ArrInv[Id][1] = PrvQ + RcvQ
            print("Nouvelle Quantité est ", ArrInv[Id][1], " en stock.")

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
            ArrInv[Id][1] = Nqty
            ArrInv[Id][2] = Ncost
            ArrInv[Id][3] = Nipfr
            ArrInv[Id][4] = Ndesc


            print("\nVous avez soumis : {} | {}$ | {}u | {}\n".format(Ndesc, Ncost, Nqty, Nipfr))
            done = input("Retour? (Y) : ")
    # Supprime les donnee d'un article mais garde le Ref # vide pour pouvoir le re-ajoute plus tard.
    elif strSelection == "5":
        ArtId = int(input("Referance de l'article : "))
        Id = ArtId - 1
        na = "N/A"
        nl = "Null"
        ArrInv[Id][1] = na
        ArrInv[Id][2] = na
        ArrInv[Id][3] = nl
        ArrInv[Id][4] = na
        print("L'article {} à été supprimer, vous pouvez toujours la modifié".format(ArtId))
        done = input("Retour? (Y) : ")
    # Cree un audit de l'inventaire et meme la valeur total des article combiner.
    elif strSelection == "6":
        print("  REF | QTY | PRIX | IPFR | DESCRIPTION")
        print(np.matrix(ArrInv))
        print("  REF | QTY | PRIX | IPFR | DESCRIPTION\n")

        ArrInv_Len = len(ArrInv) - 1
        a = 0
        Qty_tot = 0
        Cst_tota = 0
        while a <= ArrInv_Len:
            Qty_tot = Qty_tot + float(ArrInv[a][1])
            Cst_tota = Cst_tota + (float(ArrInv[a][1]) * float(ArrInv[a][2]))
            a = a + 1
        Cst_tot = round(Cst_tota, 2)
        print("L'inventaire contient {} articles individuel en total.\nEt elle veaux {}$ CAD en total.".format(Qty_tot, Cst_tot))

        done = input("Retour? (Y) : ")
print("Passé une belle journée.")
# Les autres options suivent.
