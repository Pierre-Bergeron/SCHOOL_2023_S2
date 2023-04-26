# Author : Pierre Bergeron
# Date   :
# Titre  : U4_SOMMATIF
# GIT    : SCHOOL_2023_S2
# DESCR. : Calcule et compare le volume/dimantion de (3) differante electromeneager

import math


class Refrigo:
    def __init__(self):
        self.intObjLongueur = 0
        self.intObjHauteur = 0
        self.intObjProfondeur = 0

        self.intEmpLongueur = 82
        self.intEmpHauteur = 170
        self.intEmpProfondeur = 75

        self.extIntObjLongueur = 0
        self.extIntObjHauteur = 0
        self.extIntObjProfondeur = 0

        self.fit_isTrue = 0

    def check(self):
        if self.intObjLongueur <= self.intEmpLongueur:
            if self.intObjHauteur <= self.intEmpHauteur:
                if self.intObjProfondeur <= self.intEmpProfondeur:
                    self.fit_isTrue = 1
                    print("Le réfigérateur va faire")
                else:
                    print("Ne fait pas")
            else:
                print("Ne fait pas")
        else:
            print("Ne fait pas")

    def calcIn(self):
        if self.fit_isTrue == 1:
            volume = self.extIntObjLongueur * self.extIntObjHauteur * self.extIntObjProfondeur
            print("Le volume du réfrigérateur est: {} cm³".format(volume))
        else:
            print("Le volume na pas été calculer, tandis que le réfrigérateur ne fait pas.")


class MicroOnd:
    def __init__(self):
        self.intNAME_SIDE = 0


objFridge = Refrigo()



print("Entrée votre option 1;\n")
print("Dimantion exterieur;")
Refrigo.intObjLongueur = int(input("Longueur du réfrigérateur: "))
Refrigo.intObjHauteur = int(input("Hauteur du réfrigérateur: "))
Refrigo.intObjProfondeur = int(input("Profondeur du réfrigérateur: "))
print("Dimation interieur;")
Refrigo.extIntObjLongueur = int(input("Longueur du réfrigérateur: "))
Refrigo.extIntObjHauteur = int(input("Hauteur du réfrigérateur: "))
Refrigo.extIntObjProfondeur = int(input("Profondeur du réfrigérateur: "))

objFridge.check()
objFridge.calcIn()


