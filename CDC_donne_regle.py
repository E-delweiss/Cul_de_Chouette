#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 13:42:36 2021

@author: thierry
"""

import CDC_regles as rls
import CDC_fonctions as fct


def quelle_regle(chouette_1, chouette_2, cul):
    """
    Fonction qui test si une des règle est applicable. Et applique la fonction
    en question
    
    input: valeurs des dés
    output: dict{}
        - nom_regle : nom de la règle (str)
        - score : pts perdus/gagnés (int>=0)
        - is_event : appelle CDC_event s'il y a un événement supplémentaire (None
        si non)
    
    """
    dico_dice = {'chouette_1':chouette_1, 'chouette_2':chouette_2, 'cul':cul}
    
    if rls.la_chouette(dico_dice):
        nom_regle = 'Chouette'
        is_event = False
        score = fct.la_chouette(dico_dice)
    
    
    elif rls.la_velute(dico_dice):
        nom_regle = 'Velute'
        is_event = False
        score = fct.la_velute(dico_dice)
        
        if rls.la_chouette_velute(dico_dice):
            nom_regle = 'Chouette-Velute'
            is_event = True
            score = fct.la_chouette_velute(dico_dice)
            
    
    elif rls.le_cul_de_chouette(dico_dice):
        nom_regle = 'Cul de Chouette'
        is_event = False
        score = fct.le_cul_de_chouette(dico_dice)
        
    elif rls.la_suite(dico_dice):
        pass
    
    elif rls.la_suite_velutee(dico_dice):
        pass
    
    elif rls.artichette(dico_dice):
        pass
    
    elif rls.la_soufflette(dico_dice):
        pass
    
    else:
        print('il ny a rien')
        nom_regle = None
        is_event = None
        score = None
        
    return {'nom_regle':nom_regle, 'score':score, 'is_event':is_event}








