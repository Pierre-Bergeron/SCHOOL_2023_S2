# Author : Pierre Bergeron
# Date   :
# Titre  : U4_SOMMATIF
# GIT    : SCHOOL_2023_S2
# DESCR. : Calcule et compare le volume/dimantion de (3) differante electromeneager

import math


class Refrigo:
    def __init__(self):
        self.intObjLargeur = 0
        self.intObjHauteur = 0
        self.intObjProfondeur = 0

        self.intEmpLargeur = 0
        self.intEmpHauteur = 0
        self.intEmpProfondeur = 0

    def check(self):
        if self.intObjLargeur <= self.intEmpLargeur:
            if self.intObjHauteur <= self.intEmpHauteur:
                if self.intObjProfondeur <= self.intEmpProfondeur:
                    print("Le {} va faire".format(self.__init__()))


objFridge = Refrigo()
objFridge


