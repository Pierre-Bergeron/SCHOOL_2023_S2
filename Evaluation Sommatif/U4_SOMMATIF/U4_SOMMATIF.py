# Author : Pierre Bergeron
# Date   :
# Titre  : U4_SOMMATIF
# GIT    : SCHOOL_2023_S2
# DESCR. : Calcule et compare le volume/dimantion de (3) differante electromeneager

import math


class Refrigo:
    def __init__(self):
        # espace limit de lobjet
        self.intEmpLongueur = 82
        self.intEmpHauteur = 170
        self.intEmpProfondeur = 75

        # option 1 (dimention exterieur, exterieur)
        self.intObjLongueur = 0
        self.intObjHauteur = 0
        self.intObjProfondeur = 0

        self.inIntObjLongueur = 0
        self.inIntObjHauteur = 0
        self.inIntObjProfondeur = 0
        # option 2
        self.intObjLongueur2 = 0
        self.intObjHauteur2 = 0
        self.intObjProfondeur2 = 0

        self.inIntObjLongueur2 = 0
        self.inIntObjHauteur2 = 0
        self.inIntObjProfondeur2 = 0
        # option 3
        self.intObjLongueur3 = 0
        self.intObjHauteur3 = 0
        self.intObjProfondeur3 = 0

        self.inIntObjLongueur3 = 0
        self.inIntObjHauteur3 = 0
        self.inIntObjProfondeur3 = 0

        self.fit_isTrue = 0
        self.fit_isTrue2 = 0
        self.fit_isTrue3 = 0

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

    def check2(self):
        if self.intObjLongueur2 <= self.intEmpLongueur:
            if self.intObjHauteur2 <= self.intEmpHauteur:
                if self.intObjProfondeur2 <= self.intEmpProfondeur:
                    self.fit_isTrue2 = 1
                    print("Le réfigérateur va faire")
                else:
                    print("Ne fait pas")
            else:
                print("Ne fait pas")
        else:
            print("Ne fait pas")

    def check3(self):
        if self.intObjLongueur3 <= self.intEmpLongueur:
            if self.intObjHauteur3 <= self.intEmpHauteur:
                if self.intObjProfondeur3 <= self.intEmpProfondeur:
                    self.fit_isTrue3 = 1
                    print("Le réfigérateur va faire")
                else:
                    print("Ne fait pas")
            else:
                print("Ne fait pas")
        else:
            print("Ne fait pas")

    def cal_vol(self):
        if self.fit_isTrue == 1:
            volume = self.inIntObjLongueur * self.inIntObjHauteur * self.inIntObjProfondeur
            print("Le volume du réfrigérateur est: {} cm³".format(volume))
        else:
            print("Le volume na pas été calculer, tandis que le réfrigérateur ne fait pas.")

    def cal_vol2(self):
        if self.fit_isTrue2 == 1:
            volume = self.inIntObjLongueur2 * self.inIntObjHauteur2 * self.inIntObjProfondeur2
            print("Le volume du réfrigérateur est: {} cm³".format(volume))
        else:
            print("Le volume na pas été calculer, tandis que le réfrigérateur ne fait pas.")

    def cal_vol3(self):
        if self.fit_isTrue3 == 1:
            volume = self.inIntObjLongueur3 * self.inIntObjHauteur3 * self.inIntObjProfondeur3
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
Refrigo.inIntObjLongueur = int(input("Longueur du réfrigérateur: "))
Refrigo.inIntObjHauteur = int(input("Hauteur du réfrigérateur: "))
Refrigo.inIntObjProfondeur = int(input("Profondeur du réfrigérateur: "))

objFridge.check()
objFridge.check2()
objFridge.check3()
objFridge.cal_vol()
objFridge.cal_vol2()
objFridge.cal_vol3()


