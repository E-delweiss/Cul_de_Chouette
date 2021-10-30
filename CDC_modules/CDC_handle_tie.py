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
    Classe permettant de stocker des variables pour les autres modules

    Attributs
    ----------
    Main_frame : tkinter.Tk
        Fenetre principale.
    Str_joueur_gagnant : ???
        ???
    Btn_jr_svt : tkinter.Button
        ???
    Joueurs_obj : list[CDC_class_joueur.Joueur]
        Liste des joueurs inscrits au jeu
    List_joueurs_tie : list[CDC_class_joueur.Joueur]
        Liste des joueurs étant en situation d'égalité
    Dict_var : dict
        Dictionnaire qui rassemble les éléments relatifs à une combinaison
    Widget_liste : list[tkinter.Widget]
        Liste des widgets à destroy
    Count : int
        Permet de sauvegarder l'occurence des égalités et de multiplier 'Count'
        par le score de la combinaison.
    
    """
    
    Main_frame = ''
    Str_joueur_gagnant = ''
    Btn_jr_svt = ''
    Joueurs_obj = []
    List_joueurs_tie = []
    Dict_var = {}
    Widget_liste = []
    Count = 0
    
    
    
    
# def readstatus(key, var):
#     """
#     ???

#     Parameters
#     ----------
#     key : dict
#         DESCRIPTION.
#     var : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
#     var_obj = var.get(key.nom)
#     if var_obj.get() == 1:
#         GlobalVars.List_joueurs_tie.append(key)
#     if var_obj.get() == 0:
#         GlobalVars.List_joueurs_tie.remove(key)
        

def handle_tie(main_frame, btn_jr_svt, joueurs_obj, dict_var):
    """
    Enregistre les variables provenant du main comme attributs
    de GlobalVars.
    Appelle 'CDC_tie_fonction.tie_fonction' pour gérer une première égalité et
    faire une checkbox.

    Parameters
    ----------
    main_frame : tkinter.Tk
        Fenetre principale.
    btn_jr_svt : tkinter.Button
        Bouton permettant de passer au joueur suivant.
    joueurs_obj : list[CDC_class_joueur.Joueur]
        Liste des joueurs inscrits au jeu.
    dict_var : dict
        Dictionnaire qui rassemble les éléments relatifs à une combinaison.

    Returns
    -------
    None.

    """
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
    """
    Gere ce qu'il se passe une fois que l'utilisateur choisi les joueurs ayant
    fait égalité.
    Démarre l'événement relatif à la combinaison en cours.

    Returns
    -------
    None.

    """
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
        GlobalVars.Btn_jr_svt.pack()
            
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
    Créé une seconde checkbox si l'égalité persiste et appel 'yes_tie_fct_end'
    comme commande de la checkbox pour départager les joueurs par un lancé de dés.
    
    Parameters
    ----------
    text1 : str
        Texte du label qui vient avant la checkbox.
    command1 : str
        Commande qui va être appelé par la checkbox.

    Returns
    -------
    None.

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
    Appelée dans 'yes_tie_fct' pour départager les joueurs ayant fait égalités
    par un lancé de dés géré par le if 'dice_decision' dans la fonction
    'CDC_tie_fonction.tie_fonction'.

    Returns
    -------
    None.

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
    """
    Génère une entrée par le if 'is_and_entry' de la fonction 
    'CDC_tie_fonction.tie_fct' permettant de savoir qui est le dernier joueur
    ayant répondu à l'événement.
    Gère aussi les mauvaises entrées de l'utilisateur.

    Parameters
    ----------
    text : str
        Texte pour demander à l'utilisateur de faire une saisie.

    Returns
    -------
    None.

    """
    tie_fct.tie_fonction(GlobalVars.Main_frame,
                     GlobalVars.Joueurs_obj,
                     text,
                     checkbox = False,
                     is_an_entry = True)
    