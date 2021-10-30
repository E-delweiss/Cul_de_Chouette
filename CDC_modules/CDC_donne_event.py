#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:55:31 2021

@author: thierry


Contient les annonces spéciales pour certaines combinaisons où les joueurs
doivent intéragir entre eux (dire qqch, prendre un dé, défier qqn...)
"""

import tkinter as tk
import CDC_gere_event as g_ev


def annonce_evenement(main_frame, btn_jr_svt, joueurs_obj, joueur_courant, dict_var):
    """
    Permet de créer une nouvelle fenetre où sera annoncées :
        - Le nom de la combinaison
        - La règle de cette combinaison
        
    input :
        main_frame : frame tkinter principale
        btn_jr_svt : bouton qui va relancer le jeu
        Joueurs_obj : liste des instances de la class Root
        dict_var : dictionnaire créé par d_rls.quelle_regle()
        
    output :
        new_frame créée avec ses widgets par g_ev.event_[...]
    """
    
    nom_regle = dict_var['nom_regle']
    
    if nom_regle == 'Chouette-Velute':
        detail_regle = "Le premier joueur qui frappe dans ses mains en criant \"Pas mou le caillou\" gagne les points "

    elif nom_regle == 'Suite':
        detail_regle = "Tous les joueurs doivent taper du poing sur la table en criant \"Grelotte ça picote !\"."    
        
    elif nom_regle == 'Suite-Velutée':
        detail_regle = ""
        
    combinaison = tk.Label(main_frame, text=nom_regle+' !!!')
    combinaison.pack()
    g_ev.event(main_frame, btn_jr_svt, joueurs_obj, joueur_courant, dict_var, detail_regle)        

        
    return


