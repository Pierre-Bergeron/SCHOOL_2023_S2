# Author : Pierre Bergeron
# Date   :
# Titre  : U4_SOMMATIF
# GIT    : SCHOOL_2023_S2
# DESCR. : Calcule et compare le volume/dimantion de (3) differante electromeneager

import math


class Refrigo:
    def __init__(self):
        self.intObjLargeur = 4
        self.intObjHauteur = 2
        self.intObjProfondeur = 6

        self.intEmpLargeur = 5
        self.intEmpHauteur = 2
        self.intEmpProfondeur = 5

    def check(self):
        if self.intObjLargeur <= self.intEmpLargeur:
            if self.intObjHauteur <= self.intEmpHauteur:
                if self.intObjProfondeur <= self.intEmpProfondeur:
                    print("Le Frigo va faire")
                else:
                    print("ne fait pas")
            else:
                print("ne fait pas")
        else:
            print("ne fait pas")

class MicroOnd:
    def __init__(self):
        self.intNAME_SIDE = 0


objFridge = Refrigo()
objFridge.check()


