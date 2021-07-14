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


def annonce_evenement(main_frame, Joueurs_obj, dict_var):
    """
    Permet de créer une nouvelle fenetre où sera annoncées :
        - Le nom de la combinaison
        - La règle de cette combinaison
        
    input :
        main_frame : frame tkinter principale
        Joueurs_obj : liste des instances de la class Root
        dict_var : dictionnaire créé par d_rls.quelle_regle()
        
    output :
        new_frame créée avec ses widgets par g_ev.event_[...]
    """
    
    nom_regle = dict_var['nom_regle']
    
    if nom_regle == 'Chouette-Velute':
        detail_regle = "Chouette Velute ! Le premier joueur qui frappe dans ses mains en criant \"Pas mou le caillou\" gagne les points "
        top_event = tk.Toplevel()    
        combinaison = tk.Label(top_event, text=nom_regle+' !!!')
        combinaison.pack()
        top_event = g_ev.event_chouette_velute(main_frame, top_event, Joueurs_obj, dict_var, detail_regle)        

    return top_event


