# Auteur : Pierre-Bergeron
# Date   : MR18/23
# Titre  : U2_SOMMATIF
# GIT    : SCHOOL_2023_S2

import numpy as np
import math

# Legende (Ref d'article, quantite en stock, prix, commende automatique, description)
ArrInv = np.array([[1, 10, 50.00, "Oui","USB power bank"],[2, 6, 15.99, "Oui", "Phone Charger"],[3, 2, 9.99, "Non", "Power Block USB"],[4, 26, 4.99, "Non", "USB Light"]])
strSelection = 0
while not (strSelection == "Q" or strSelection == "q"):
  print("""
  Menu
  ----
  1 - Rechèrche d'article
  2 - Passer Une Transaction
  3 - Conte d'article
  4 - Ajouté un article 
  5 - Suprimer un article
  6 - Commande Recu
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

  elif strSelection == "3":
    ArtId = int(input("Referance de l'article : "))
    Id = ArtId - 1
    print("Quantité En Stock : ", ArrInv[Id][1])
    NewQ = int(input("Quantité Actuelle : "))
    ArrInv[Id][1] = NewQ
    print("Quantité changer à ", ArrInv[Id][1], " en stock.")

  elif strSelection == "4":
    print("4")


# Les autres options suivent.
