#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:02:30 2021

@author: thierry
"""

import re
import tkinter as tk
import CDC_notice as nt
import CDC_handle_tie__test__ as tie_test
import CDC_autres as aut


class GlobalVars():
    """
    Class permettant de travailler comme avec des variables globales
    
    Str_joueur_gagnant : 'str' 
    List_joueurs_tie : [liste]
    """
    Str_joueur_gagnant = ''
    List_joueurs_tie = []
    
    

def event_chouette_velute(main_frame, top_event, Joueurs_obj, dict_var, detail_regle):
    
    def get_entry(warning):
        
        entry = aut.get_entry(var_texte, ligne_texte)
        if entry is None:
            return
        
        if entry not in [k.nom for k in Joueurs_obj]:
            warning.config(text = f"Le joueur {entry} n'existe pas")
            warning.pack()
            return

        else:
            warning.destroy()
            warning = tk.Label(top_event)
            warning.pack()
            main_frame.Str_joueur_gagnant = entry
 
            bouton_tie['state']='disabled'
            bouton_tie.destroy()

            warning['text'] = f"{entry} a gagné la {dict_var['nom_regle']}"
            ordre = lambda: [top_event.destroy(), recap(main_frame, main_frame.Str_joueur_gagnant, dict_var['score'])]
            bouton_next = tk.Button(top_event, text='Suivant', command=ordre)
            bouton_next.pack(side='bottom')
            return
            
            
    
    def recap(main_frame, joueur, score):

        # aut.clear_widget(main_frame.Liste_messages, main_frame.Liste_boutons)
        
        joueur_gagnant = [k for k in Joueurs_obj if k.nom == joueur][0]
        joueur_gagnant.ajout_ptsjoueur(dict_var['score'])
        
        recap = tk.Label(main_frame, text=f"{joueur_gagnant.nom} prend {dict_var['score']} points.")
        recap.pack()
        
        recap2 = tk.Label(main_frame, text=f"{joueur_gagnant.nom} a donc {joueur_gagnant.PtsJoueur} points au total")
        recap2.pack()
        
            
    
    nom_regle = dict_var['nom_regle']
            
    #### Affiche la regle de l'événement
    message_regle = tk.Label(top_event, text=detail_regle) 
    message_regle.pack()
    
    #### Demande qui a gagné l'événement
    question1 = tk.Label(top_event, text="Qui a gagné l'événement ?")
    question1.pack()
    
    ### Zone de saisie
    var_texte = tk.StringVar()
    ligne_texte = tk.Entry(top_event, textvariable=var_texte, width=30)
    ligne_texte.pack()
    
    ### Bouton pour afficher la notice de la règle sur une nouvelle frame
    # ordre = lambda: nt.affiche_notice(nom_regle, bouton_notice)
    # bouton_notice = tk.Button(top_event, text='Afficher la règle', command=ordre)
    # bouton_notice.pack(side='right')
    
    
    
    
    
    
    
    
    ### Bouton pour valider le nom du gagnant de l'event
    warning = tk.Label(top_event)
    bouton_gagnant_event = tk.Button(top_event, text='Ok', command=lambda : get_entry(warning))
    bouton_gagnant_event.pack(side='left')
    
    
    
    
    
    
    
    
    
    
    
    ordre_tie = lambda: tie_test.handle_tie(main_frame, top_event, Joueurs_obj, dict_var)
    bouton_tie = tk.Button(top_event, text='Egalité ?', command=ordre_tie)
    bouton_tie.pack() 
    
    return top_event






















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
            GlobalVars.List_joueurs_tie.append(key)
            
        if var_obj.get() == 0:
            GlobalVars.List_joueurs_tie.remove(key)

    var = dict()
    for k in Joueurs_obj:
        var[k.nom]=tk.IntVar()
        chk = tk.Checkbutton(top_checkbox, text=k.nom, variable=var[k.nom], onvalue=1, offvalue=0, command=lambda key=k: readstatus(key))
        chk.pack()

    bouton_valider = tk.Button(top_checkbox, text='Valider', command=lambda: pushbutton(main_frame, top_checkbox, Joueurs_obj, dict_var))
    bouton_valider.pack()


def pushbutton(main_frame, top_checkbox, Joueurs_obj, dict_var):
    if len(GlobalVars.List_joueurs_tie) < 2:
        pass
    
    else:
        # aut.clear_widget(main_frame.Liste_messages, main_frame.Liste_boutons, top_checkbox)
        
        temp = [k.nom for k in GlobalVars.List_joueurs_tie]
 
        for k in Joueurs_obj:
            k.ajout_ptsjoueur(-dict_var['score'])
            
            
        recap = tk.Label(main_frame, text=f"Les joueurs {', '.join(temp)} perdent {dict_var['score']} points.")
        recap.pack()
        
        tk.Label(main_frame, text="Récap des scores : ").pack()
        for joueur in Joueurs_obj:
            tk.Label(main_frame, text=f"{joueur.nom} a donc {joueur.PtsJoueur} points au total").pack()
            
            









