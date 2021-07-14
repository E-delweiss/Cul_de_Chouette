#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:32:01 2021

@author: thierry

Contient uniquement les fonctions relatives aux règles du Cul De Chouette
"""



def la_chouette(dico_dice):
    """
    Applique la règle de La Chouette
    input : le score des dés chouette_1, chouette_2, cul
    output : score
    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul        = dico_dice['cul']
    
    score_dice = [chouette_1, chouette_2, cul]
    for i in range(1,7):
        doublon = score_dice.count(i)
        
        if doublon == 2:
            chouette = i
            score = chouette**2
            return score



def la_velute(dico_dice):
    """
    Applique la règle de "La Velute"
    input : score des dés chouette_1, chouette_2, cul
    output : score
    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul        = dico_dice['cul']
    
    velute = max(chouette_1, chouette_2, cul)
    score = 2*(velute**2)
    return score
    


##############################################################################

def la_chouette_velute(dico_dice):
    """
    Applique la règle de "La Chouette Velute" 
    input : score des dés chouette_1, chouette_2, cul
    output : score
    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul        = dico_dice['cul']    

    velute = max(chouette_1, chouette_2, cul)
    chouette_velute = 2*(velute**2)
    score = chouette_velute
    
    return score
    
    
def le_cul_de_chouette(dico_dice):
    """
    Applique la règle du "Cul De Chouette" 
    input : un des trois dés
    output : score
    """
    chouette_1 = dico_dice['chouette_1']

    cul_de_chouette = chouette_1
    score = 40 + 10 * cul_de_chouette
    
    return score

    
    
    
    
    