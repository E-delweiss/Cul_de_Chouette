#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:44:20 2021

@author: thierry
"""

import tkinter as tk
import CDC_gere_event as g_ev

########
#### TODO on va voir si on peut gérer l'égalité de manière générale


def handle_tie(main_frame, top, Joueurs_obj, dict_var):
    # Lister les joueurs qui sont a égalité
    # Faire une boucle if >>> if event == chouette-velute >>> ceux qui font égalité perdent des pts
    
    top.destroy()
    top.update()
    
    top_checkbox = tk.Toplevel()
    
    l = tk.Label(top_checkbox, text='Quels joueurs ont fait égalité ?')
    l.pack()
    
    def readstatus(key):
        var_obj = var.get(key.nom)
        if var_obj.get() == 1:
            g_ev.GlobalVars.List_joueurs_tie.append(key)
            
        if var_obj.get() == 0:
            g_ev.GlobalVars.List_joueurs_tie.remove(key)

    var = dict()
    for k in Joueurs_obj:
        var[k.nom]=tk.IntVar()
        chk = tk.Checkbutton(top_checkbox, text=k.nom, variable=var[k.nom], onvalue=1, offvalue=0, command=lambda key=k: readstatus(key))
        chk.pack()

    enter_button = tk.Button(top_checkbox, text='Valider', command=lambda: pushbutton(main_frame, top_checkbox, Joueurs_obj, dict_var))
    enter_button.pack()


def pushbutton(main_frame, top_checkbox, Joueurs_obj, dict_var):
    if len(g_ev.GlobalVars.List_joueurs_tie) < 2:
        pass
    
    else:
        top_checkbox.destroy()
        top_checkbox.update()
        
        # for k, v in zip(main_frame.Liste_boutons, main_frame.Liste_messages):
        #     k.destroy(), v.destroy()
        #     k.update(), v.update()
            
        for k in Joueurs_obj:
            print(k.PtsJoueur)
        print('\n')
        
        temp = [k.nom for k in g_ev.GlobalVars.List_joueurs_tie]
        print(temp)
        # for k in Joueurs_obj:
        #     if k.nom in temp:
                
        Joueurs_obj[0].ajout_ptsjoueur(-dict_var['score'])
        Joueurs_obj[1].ajout_ptsjoueur(-dict_var['score'])

                
        for k in Joueurs_obj:
            print(k.PtsJoueur)
            
            
        recap = tk.Label(main_frame, text=f"Les joueurs {', '.join(temp)} perdent {dict_var['score']} points.")
        recap.pack()
        
        tk.Label(main_frame, text="Récap des scores : ").pack()
        for joueur in Joueurs_obj:
            tk.Label(main_frame, text=f"{joueur.nom} a donc {joueur.PtsJoueur} points au total").pack()