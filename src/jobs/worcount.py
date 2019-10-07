# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:19:18 2019

@author: HENAFF
"""

import os

path = "C:/Users/HENAFF/Documents/Perso/"
count = 0
for file in os.listdir(path):
    if file.endswith(".txt"):
        s_file = path+str(file)
        f = open(s_file,"r")
        for ligne in f:
            if any("\n" in s for s in ligne) and len(ligne) == 1:
                None
            else:
                print(ligne.split(" "))
                count += len(ligne.split(" "))
        f.close()
print(count)