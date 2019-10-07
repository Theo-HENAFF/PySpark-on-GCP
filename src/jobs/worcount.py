# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:19:18 2019

@author: HENAFF
"""
import os
from pathlib import Path

main_path = Path.cwd()
home_path = main_path.parent.parent
res_path = str(home_path) + "\\ressources\\"
print(main_path)
print(home_path)

count = 0
for file in os.listdir(res_path):
    if file.endswith(".txt"):
        s_file = res_path+str(file)
        f = open(s_file,"r")
        for ligne in f:
            if any("\n" in s for s in ligne) and len(ligne) == 1:
                None
            else:
                print(ligne.split(" "))
                count += len(ligne.split(" "))
        f.close()
print(count)