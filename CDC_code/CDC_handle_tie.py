#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:44:20 2021

@author: thierry
"""

import tkinter as tk
import CDC_autres as aut
import CDC_tie_fonction as tie_fct

########
#### TODO on va voir si on peut gérer l'égalité de manière générale
class GlobalVars():
    """
    Class permettant de stocker des variables pour les autres modules
    TODO
    Str_joueur_gagnant : 'str' 
    List_joueurs_tie : [liste]
    """
    Main_frame = ''
    Str_joueur_gagnant = ''
    Btn_jr_svt = ''
    Joueurs_obj = []
    List_joueurs_tie = []
    Dict_var = {}
    Widget_liste = []
    Count = 0
    
    
    
    
def readstatus(key, var):
    var_obj = var.get(key.nom)
    if var_obj.get() == 1:
        GlobalVars.List_joueurs_tie.append(key)
    if var_obj.get() == 0:
        GlobalVars.List_joueurs_tie.remove(key)
        

def handle_tie(main_frame, btn_jr_svt, joueurs_obj, dict_var):
    GlobalVars.Main_frame = main_frame
    GlobalVars.Btn_jr_svt = btn_jr_svt
    GlobalVars.Joueurs_obj = joueurs_obj
    GlobalVars.Dict_var = dict_var
    
    tie_fct.tie_fonction(GlobalVars.Main_frame,
                     GlobalVars.Joueurs_obj,
                     'Quels joueurs ont fait égalité ?',
                     checkbox = True,
                     command1 = "hdl.ending_tie()",
                     is_an_entry = False)

def ending_tie():
    if len(GlobalVars.List_joueurs_tie) < 2:
        return
    
    aut.clear_widget(GlobalVars.Widget_liste)
    #######################################################################         
    if GlobalVars.Dict_var['nom_regle'] == 'Chouette-Velute':
        temp = [k.nom for k in GlobalVars.List_joueurs_tie]
        for k in GlobalVars.Joueurs_obj:
            if k.nom in temp:
                k.ajout_ptsjoueur(-GlobalVars.Dict_var['score'])

        recap = tk.Label(GlobalVars.Main_frame, text=f"Les joueurs {', '.join(temp)} perdent {GlobalVars.Dict_var['score']} points.")
        recap.pack()
        GlobalVars.btn_jr_svt.pack()
            
    #######################################################################         
    if GlobalVars.Dict_var['nom_regle'] == 'Suite':
        
        temp = [k.nom for k in GlobalVars.List_joueurs_tie]
        egalite1 = tk.Label(GlobalVars.Main_frame, text=f"Les joueurs {', '.join(temp)} se départagent en criant \" Sans fin est la moisissure des bières bretonnes ! \"")
        egalite1.pack()
        is_tie = tk.Label(GlobalVars.Main_frame, text='Egalité ?')
        is_tie.pack()
        
        bouton_yes = tk.Button(GlobalVars.Main_frame, text='Oui, encore')
        bouton_no = tk.Button(GlobalVars.Main_frame, text="Non, c'est bon")
        to_clear = [egalite1, is_tie, bouton_yes, bouton_no]
        
        text1 = "Quels joueurs ont fait égalité ?"
        q1 = "Qui est le dernier ?"
        command1 = "hdl.yes_tie_fct_end()"
        
        bouton_yes.config(command=lambda: [aut.clear_widget(to_clear), yes_tie_fct(text1, command1)])
        bouton_yes.pack()
        bouton_no.config(command=lambda: [aut.clear_widget(to_clear), no_tie_fct(q1)])
        bouton_no.pack()
        
        
def yes_tie_fct(text1, command1):
    """
    Fonction générale qui créé une checkbox pour l'égalité
    """
    aut.clear_widget(GlobalVars.Widget_liste)
    GlobalVars.List_joueurs_tie.clear()
    
    tie_fct.tie_fonction(GlobalVars.Main_frame,
                     GlobalVars.Joueurs_obj,
                     text1,
                     checkbox = True,
                     command1 = command1,
                     is_an_entry = False)
    
def yes_tie_fct_end():
    """
    Fonction qui départage si l'égalité continue en lançant un dé
    """
    nom_joueurs_tie = [k.nom for k in GlobalVars.List_joueurs_tie]
    if len(nom_joueurs_tie) < 2:
        return
    
    tie_fct.tie_fonction(GlobalVars.Main_frame,
                     nom_joueurs_tie,
                     f"Les joueurs {', '.join(nom_joueurs_tie)} se départagent en lançant un dé, celui qui fait le plus grand score perd.",
                     checkbox = False,
                     is_an_entry = False,
                     dice_decision = True,
                     command2 = "hdl.yes_tie_fct_end()")

def no_tie_fct(text):
    tie_fct.tie_fonction(GlobalVars.Main_frame,
                     GlobalVars.Joueurs_obj,
                     text,
                     checkbox = False,
                     is_an_entry = True)
    