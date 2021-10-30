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
    Fonction qui test si une des règles est applicable. Et applique la fonction
    en question.

    Parameters
    ----------
    chouette_1 : int
        Valeur de la première Chouette.
    chouette_2 : int
        Valeur de la deuxième Chouette.
    cul : int
        Valeur du Cul.

    Returns
    -------
    dict
        Dictionnaire contenant les informations retives à la combinaison produite
        par 'chouette_1', 'chouette_2' et 'cul'.
        
        Parameters
        ----------
        nom_regle : str
            Nom de la règle
        score : int
            Points perdus/gagnés (>=0)
        is_event : bool
            Indique s'il y a un événement supplémentaire
    """    
    dico_dice = {'chouette_1':chouette_1, 'chouette_2':chouette_2, 'cul':cul}
    
    if rls.la_chouette(dico_dice):
        nom_regle = 'Chouette'
        is_event = False
        score = fct.la_chouette(dico_dice)
    
    
    elif rls.la_velute(dico_dice) and \
                        rls.la_suite_velutee(dico_dice) == False and \
                        rls.la_chouette_velute(dico_dice) == False:
        nom_regle = 'Velute'
        is_event = False
        score = fct.la_velute(dico_dice)
        
    elif rls.la_chouette_velute(dico_dice):
        nom_regle = 'Chouette-Velute'
        is_event = True
        score = fct.la_chouette_velute(dico_dice)
            
    
    elif rls.le_cul_de_chouette(dico_dice):
        nom_regle = 'Cul de Chouette'
        is_event = False
        score = fct.le_cul_de_chouette(dico_dice)
    
        
    elif rls.la_suite(dico_dice) and rls.la_suite_velutee(dico_dice) == False:
        nom_regle = 'Suite'
        is_event = True
        score = fct.la_suite(dico_dice)
            
    elif rls.la_suite_velutee(dico_dice):
        nom_regle = 'Suite-Velutée'
        is_event = True
        score = fct.la_suite_velutee(dico_dice)


    elif rls.artichette(dico_dice):
        pass
    
    elif rls.la_soufflette(dico_dice):
        pass
    
    else:
        print("En cours d'implementation")
        nom_regle = 'NaN'
        is_event = 'NaN'
        score = 'NaN'
        
    return {'nom_regle':nom_regle, 'score':score, 'is_event':is_event}