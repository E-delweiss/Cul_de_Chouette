#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:10:40 2021

@author: thierry
"""


import sys
sys.path.insert(0,"./CDC_modules")
import CDC_GUI_long as GUI
import CDC_geometry

title = "Jeu du Cul de Chouette"
root = GUI.Root()
root.title(title)
root.geometry(CDC_geometry.win_size)
root.mainloop()
