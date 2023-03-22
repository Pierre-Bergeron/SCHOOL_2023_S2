#start
# Exemple d'un système de menu de base.
import numpy as np

tblInv = np.array()
strSelection = 0
while not (strSelection == "Q" or strSelection == "q"):
  print("""
  Menu
  ----
  1 - Saisir les valeurs
  2 - Effacer les valeurs
  3 - Imprimer les valeurs à l'écran
  4 - 
  5 - 
  6 - 
  Q - Quitter

  """)
  strSelection = input("Indiquer votre choix : ")

  if strSelection == "1":
    print("Ici, le programme exécute l'option 1.")
  elif strSelection == "3":
    print("Ici, le programme exécute l'option 1.")
  elif strSelection == "3":
    print("Ici, le programme exécute l'option 3.")
  # Les autres options suivent.
