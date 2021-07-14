#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:16:01 2021

@author: thierry
"""

import tkinter as tk

import CDC_donne_regle as d_rls
import CDC_donne_event as d_ev


def give_the_rules(main_frame, Joueurs_obj, chouette_1, chouette_2, cul):
    
    dict_var = d_rls.quelle_regle(chouette_1, chouette_2, cul)
    
    # S'il n'y a pas d'événement particulier
    if dict_var['is_event'] is False :
        # frame_regle = tk.Toplevel()
        annonce_de_la_regle = tk.Label(main_frame, text=dict_var['nom_regle']+' !!!') 
        annonce_de_la_regle.pack()
        
        # return {'frame_regle':frame_regle, 'score':dict_var['score'], 'nom_regle':dict_var['nom_regle']}
        return {'event':False, 'score':dict_var['score'], 'nom_regle':dict_var['nom_regle']}
      
    # S'il y a un événement particulier           
    else:
        top_event = d_ev.annonce_evenement(main_frame, Joueurs_obj, dict_var)

        return {'top_event':None, 'score': dict_var['score'], 'nom_regle':dict_var['nom_regle']}
    
    
    
    

