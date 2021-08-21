#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:16:01 2021

@author: thierry
"""

import tkinter as tk

import CDC_donne_regle as d_rls


def give_the_rules(main_frame, btn_jr_svt, joueurs_obj, chouette_1, chouette_2, cul):
    """
    Permet de créer un dictionnaire reunissant les informations relatives à 
    la combinaison en cours.

    Parameters
    ----------
    main_frame : tkinter.Tk
        Fenetre principale.
    btn_jr_svt : tkinter.Button
        Bouton permettant de passer au joueur suivant.
    joueurs_obj : list[CDC_class_joueur.Joueur]
        Liste des joueurs inscrits au jeu.
    chouette_1 : int
        Valeur de la première Chouette.
    chouette_2 : int
        Valeur de la deuxième Chouette.
    cul : int
        Valeur du Cul.

    Returns
    -------
    dict
        Dictionnaire reunissant les informations relatives à la combinaison en cours
        - Est-ce qu'il y a un evenement particulier ?
        - Score de la combinaison ?
        - Nom de la combinaison ?

    """
    
    dict_var = d_rls.quelle_regle(chouette_1, chouette_2, cul)
    
    # S'il n'y a pas d'événement particulier
    if dict_var['is_event'] is False :
        annonce_de_la_regle = tk.Label(main_frame, text=dict_var['nom_regle']+' !!!') 
        annonce_de_la_regle.pack()
        
        return {'event':False, 'score':dict_var['score'], 'nom_regle':dict_var['nom_regle']}
      
    # S'il y a un événement particulier           
    else:
        return {'event':True, 'score': dict_var['score'], 'nom_regle':dict_var['nom_regle']}
    
    
    
    

