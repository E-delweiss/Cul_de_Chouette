#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:02:30 2021

@author: thierry
"""

import tkinter as tk
import CDC_handle_tie as tie
import CDC_autres as aut



def event(main_frame, btn_jr_svt, Joueurs_obj, joueur_courant, dict_var, detail_regle):
    """
    """
    def get_entry(warning):
        """
        """
        entry = aut.get_entry(var_texte, ligne_texte)
        if entry is None:
            return
        if entry not in [k.nom for k in Joueurs_obj]:
            warning.config(text = f"Le joueur {entry} n'existe pas")
            warning.pack()
            return
        
        else:
            main_frame.Str_joueur_gagnant = entry
            bouton_tie.destroy(), bouton_gagnant_event.destroy()
            warning.config(text = f"{entry} a gagné la {dict_var['nom_regle']}")
            warning.pack()
            ordre = lambda: [recap(main_frame, main_frame.Str_joueur_gagnant, dict_var['score']), btn.destroy()]
            btn = tk.Button(main_frame, text='Ok', command=ordre)
            btn.pack(side='bottom')
            return
    
    def recap(main_frame, joueur, score):      
        """
        """
        joueur_gagnant = [k for k in Joueurs_obj if k.nom == joueur][0]
        joueur_gagnant.ajout_ptsjoueur(dict_var['score'])
        recap = tk.Label(main_frame, text=f"\n{joueur_gagnant.nom} prend {dict_var['score']} points.")
        recap.pack()
        btn_jr_svt.pack()
        return
            
                
    #### Affiche la regle de l'événement
    message_regle = tk.Label(main_frame, text=detail_regle) 
    message_regle.pack()
    
    #### Pose la question relative à l'événement
    question(main_frame, dict_var)
    
    if dict_var['nom_regle'] in ['Chouette-Velute', 'Suite']:
        ### Zone de saisie
        var_texte = tk.StringVar()
        ligne_texte = tk.Entry(main_frame, textvariable=var_texte, width=30)
        ligne_texte.pack()
        
        ### Bouton pour valider le nom du gagnant de l'event
        warning = tk.Label(main_frame)
        bouton_gagnant_event = tk.Button(main_frame, text='Ok', command=lambda : get_entry(warning))
        bouton_gagnant_event.pack()
        
        ### Gestion d'une situation d'égalité
        bouton_tie = tk.Button(main_frame) 
        ordre_tie = lambda: [bouton_gagnant_event.config(state='disabled'), 
                      bouton_tie.config(state='disabled'),
                      ligne_texte.config(state='disabled'),
                      tie.handle_tie(main_frame, btn_jr_svt, Joueurs_obj, dict_var)]
        bouton_tie.config(text='Egalité ?', command=ordre_tie)
        bouton_tie.pack()
        
    
    
    elif dict_var['nom_regle'] == "Suite-Velutée":
        to_clear = []
        def valide_choice():
            if 'Patte' in choice :
                tk.Label(main_frame, text="f{joueur_courant.nom} valide sa Velute et condamne donc la Suite-Velutée.").pack()
                tk.Label(main_frame, text=f"{joueur_courant.nom} gagne {dict_var['score']} points !").pack()
                joueur_courant.ajout_ptsjoueur(dict_var['score'])
                
            elif 'Un joueur' in choice :
                tk.Label(main_frame, text="Quel joueur à crié \"Velutée !\" ?").pack()
                var_text = tk.StringVar()
                ligne_text = tk.Entry(main_frame, textvariable=var_text, width=30).pack()
                warning = tk.Label(main_frame)
                ordre = lambda : [aut.set_entry(main_frame, Joueurs_obj, 
                                                joueur_courant, var_text, ligne_text,
                                                warning,
                                                "Le joueur {arg1} n'existe pas",
                                                "Impossible, le joueur {arg1} est le lançeur",
                                                final_ordre = None)]
                bouton_gagnant_event = tk.Button(main_frame, text='Ok', command=ordre)
                bouton_gagnant_event.pack()
                
            else:
                pass       
        
        
        choice = aut.radiobox(main_frame, 3, "Le lançeur à crié \"Patte de canaaard !\"",
                                             "Un joueur a crié \"Velute !\"",
                                             "Deux joueurs au moins ont criés \"Velute !\"")
        
        choice_button = tk.Button(main_frame)
        choice_button.config(text="Valider", command=lambda:[choice_button.destroy(), valide_choice()])
        choice_button.pack()
        
   
        
        return 



def question(main_frame, dict_var):
    nom_regle = dict_var['nom_regle']
    
    if nom_regle == 'Chouette-Velute':
        text = "Qui a été le plus rapide ?"
        
    if nom_regle == 'Suite':
        text = "Qui est le dernier ?"
        
    if nom_regle == "Suite-Velutée":
        text = "Que s'est-il passé ?"
        
        
    question = tk.Label(main_frame, text=text)
    question.pack()
    
    
    
    