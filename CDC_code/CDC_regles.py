#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:32:28 2021

@author: thierry

Contient les fonctions permettant de déterminer si une règle est applicable 
"""

from itertools import permutations



def la_chouette(dico_dice):
    """
    Déterminer si la règle de "La Chouette" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul = dico_dice['cul']
    
    liste = [chouette_1, chouette_2, cul]
    
    if len(set(liste)) == 2:
        state = True
    
        if (liste[0]+liste[1]==liste[2] or 
            liste[0]+liste[2]==liste[1] or liste[1]+liste[2]==liste[0]):
            state = False
    else:
        state = False
        
    return state
    

def la_velute(dico_dice):
    """
    Déterminer si la règle de "La Velute" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul = dico_dice['cul']
    
    if (chouette_1+chouette_2) == cul or (chouette_1+cul) == chouette_2 or \
        (chouette_2+cul) == chouette_1:
        return True
    else:
        return False
    
    
def la_chouette_velute(dico_dice):
    """
    Déterminer si la règle de "La Chouette-Velute" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul = dico_dice['cul']
    
    liste = [chouette_1, chouette_2, cul]
    if len(set(liste))==2 and (liste[0]+liste[1]==liste[2] or 
        liste[0]+liste[2]==liste[1] or liste[1]+liste[2]==liste[0]):
        return True
    else:
        return False      
    
    
    
    
def le_cul_de_chouette(dico_dice):
    """
    Déterminer si la règle du "Cul de Chouette" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul = dico_dice['cul']
    
    liste = [chouette_1, chouette_2, cul]
    if len(set(liste)) == 1:
        return True
    else:
        return False
    
    

def la_suite(dico_dice):
    """
    Déterminer si la règle de "La Suite" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul = dico_dice['cul']
    
    liste = [chouette_1, chouette_2, cul]
    liste.sort()
    if liste[1] == liste[0]+1 and liste[2] == liste[1]+1:
        return True
    else:
        return False
    
    
def la_suite_velutee(dico_dice):
    """
    Déterminer si la règle de "La Suite-Velutée" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul        = dico_dice['cul']
    
    tuple_dice = (chouette_1,chouette_2,cul)
    liste_comb = []
    SUITE_VELUTEE = [1,2,3]
    for i in permutations(SUITE_VELUTEE,3):
        liste_comb.append(i)
    
    if tuple_dice in liste_comb:
        return True
    else:
        return False
    
    
def artichette(dico_dice):
    """
    Déterminer si la règle de "L'Artichette" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul        = dico_dice['cul']
    
    tuple_dice = (chouette_1,chouette_2,cul)
    liste_comb = []
    ARTICHETTE = [4,3,4]
    for i in permutations(ARTICHETTE,3):
        liste_comb.append(i)
        
    if tuple_dice in liste_comb:
        return True
    else:
        return False
        
  
def la_soufflette(dico_dice):
    """
    Déterminer si la règle de "La Soufflette" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul        = dico_dice['cul']
    
    tuple_dice = (chouette_1,chouette_2,cul)
    liste_comb = []
    SOUFFLETTE = [4,2,1]
    for i in permutations(SOUFFLETTE,3):
        liste_comb.append(i)
        
    if tuple_dice in liste_comb:
        return True
    else:
        return False
        
    
def le_bleu_rouge(dico_dice):
    """
    Déterminer si la règle du "Bleu Rouge" est applicable.
    
    input : dictionnaire contenant le nom des dés et leur valeur
    output : True /False
    

    Parameters
    ----------
    dico_dice : dict
        Dictionnaire contenant le nom des dés et leur valeur.

    Returns
    -------
    state : bool
        Indique si la combinaison a lieu ou non.

    """
    chouette_1 = dico_dice['chouette_1']
    chouette_2 = dico_dice['chouette_2']
    cul        = dico_dice['cul']
    
    tuple_dice = (chouette_1,chouette_2,cul)
    liste_comb = []
    BLEU_ROUGE = [3,4,3]
    for i in permutations(BLEU_ROUGE,3):
        liste_comb.append(i)
    
    if tuple_dice in liste_comb:
        return True
    else:
        return False
    
    
    
