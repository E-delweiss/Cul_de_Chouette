#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:41:06 2021

@author: thierry
"""

import re
import tkinter as tk

import CDC_geometry as geom
import CDC_gere_event as g_ev #a garder



def clear_widget(liste_messages=[], liste_boutons=[], *argv):
    """
    Permet de clear des widget selon différentes entrées possibles
    Note : liste_messages peut contenir des tk.Button et inversement,
    la distinction des deux permets juste une clarification du code.

    Parameters
    ----------
    liste_messages : list[tkinter.Label], optional
        Liste des label à clear. The default is [].
    liste_boutons : list[tkinter.Button], optional
        Liste des boutons à clear. The default is [].
    *argv : tkinter widget
        Autre widget à clear.

    Returns
    -------
    None.

    """
    widget_to_clear = liste_messages + liste_boutons
    
    for widget in widget_to_clear:
        widget.destroy()
        widget.update()
        
        
    for autre_widget in argv:
        autre_widget.destroy()
        autre_widget.update()
        
        


def set_PremierJet(premier_jet):
    """
    Mise à jour de 'Premier_jet' pour qu'il contienne uniquement le(s) 
    joueur(s) ayant fait le plus petit jet.

    Parameters
    ----------
    premier_jet : dict
        Contient les joueurs et leur score sur le premier jet de dé

    Returns
    -------
    premier_jet : dict
        Met à jour 'premier_jet' pour qu'il ne contienne que les joueurs ayant
        fait le plus petit jet de dé.

    """
    smaller_value = min(premier_jet.values())
    Liste_des_plus_petits = [k for k,v in premier_jet.items() if v==smaller_value]    
    
    ### Mise à jour
    dico_temp = premier_jet.copy()
    for k in premier_jet.keys():
        if k in Liste_des_plus_petits:
            pass
        else:
            del dico_temp[k]
            
    Premier_jet = dico_temp.copy()
    
    return Premier_jet


def toss_chouettes(main, joueur, *boutons, y=0):
    """
    Utilise les méthodes de la class Joueur pour modifier les attributs
    de class Chouette_1 et Chouette_2
    
    ATTENTION : modif sur les arguments
    old = (main, bouton_chouettes, bouton_cul, joueur)

    Parameters
    ----------
    main : tkinter.Tk
        Fenetre principale.
    joueur : CDC_class_joueur.Joueur
        Joueur qui va lancer les Chouettes.
    boutons : list[tkinter.Button]
        Boutons permettant de lancer les Chouettes [0] et le Cul [1].
    y : int, optional
        Valeur permettant de placer le label msg_chouette12. The default is 0

    Returns
    -------
    None.

    """
    joueur.chouette_1_2()
    if boutons:
        bouton_chouettes = boutons[0]
        bouton_cul = boutons[1]
        bouton_chouettes['state'] = 'disabled'
        bouton_cul['state'] = 'active'
    
    y += geom.OFFSET_BUTTON*2
    main.msg_chouette12 = tk.Label(main, text=f"Résultat : \nChouette1 score = {joueur.Chouette_1} \nChouette2 score = {joueur.Chouette_2}") 
    main.msg_chouette12.place(x=geom.MAINFRAME_CENTRE_X, y=y, anchor='center')
    main.Liste_labels.append(main.msg_chouette12)
    
    return



def toss_cul(main, bouton_chouettes, bouton_cul, joueur, y=0):
    """
    Utilise les méthodes de la class Joueur pour modifier l'attributs de
    class Cul

    Parameters
    ----------
    main : tkinter.Tk
        Fenetre principale.
    bouton_chouettes : tkinter.Button
        Bouton permettant de lancer les Chouettes.
    bouton_cul : tkinter.Button
        Bouton permettant de lancer le Cul.
    joueur : CDC_class_joueur.Joueur
        Joueur qui va lancer le Cul.
    y : int, optional
        Valeur permettant de placer le label msg_chouette12. The default is 0

    Returns
    -------
    None.

    """
    joueur.cul()
    
    y += geom.OFFSET_BUTTON
    main.message_cul = tk.Label(main, text=f"Résultat : \nCul score = {joueur.Cul}") 
    main.Liste_labels.append(main.message_cul)
    main.message_cul.place(x=geom.MAINFRAME_CENTRE_X, y=y, anchor='center')
    
    bouton_chouettes['state'] = 'disabled'
    bouton_cul['state'] = 'disabled'
    
    return
    
    


def get_entry(var_text, ligne_text):
    """
    Gere une entrée simple dans une zone de texte par l'utilisateur

    Parameters
    ----------
    var_text : tkinter.StringVar
        Saisie de l'utilisateur.
    ligne_text : tkinter.Entry
        Zone de saisie.

    Returns
    -------
    temp : str
        Texte saisi nettoyé : sans espace avant/après ; avec la première 
        lettre en majuscule et le reste en minuscule.

    """
    if var_text.get()=='':
        return None
    elif re.match('^ +$', var_text.get()):
        ligne_text.delete(0, tk.END)
        return None
    
    temp = var_text.get()
    temp = re.sub(r'^ +', '', temp)
    temp = temp.capitalize()
    
    return temp





def handle_no_event(main_frame, btn1, btn2, joueur, score):
    """
    Affiche les infos des gains/pertes du tour sur la frame principale
    quand on appuie sur "Ok".
    Ajoute un bouton "Continuer" sur la frame ppale pour passer au
    joueur suivant.
    Ajoute les pts en utilisant la méthode de class 'CDC_class_joueur.ajout_ptsjoueur()'
    
    Parameters
    ----------
    main_frame : tkinter.Tk
        Fenetre principale.
    btn1 : tkinter.Button
        Bouton de validation.
    btn2 : tkinter.Button
        Bouton pour passer au joueur suivant.
    joueur : CDC_class_joueur.Joueur
        Joueur en cours.
    score : int
        Score du joueur en cours.

    Returns
    -------
    None.

    """
    btn1['state'] = 'disabled'
    btn2.pack()
    if score >= 0:
        txt_score = f"{joueur.nom} gagne {score} points"
    elif score < 0:
        txt_score = f"{joueur.nom} perd {score} points"

    joueur.ajout_ptsjoueur(score)
    affiche_score = tk.Label(main_frame, text=txt_score) 
    affiche_score.pack()
    
    
    
    
def handle_is_event(main_frame, btn1, btn2, joueur, score):
    """
    ??? pourquoi c'est quasiment la même chose que le truc d'au dessus ?
    Affiche les infos des gains/pertes du tour sur la frame principale
    quand on appuie sur "Ok".
    Ajoute un bouton "Continuer" sur la frame ppale pour passer au
    joueur suivant.
    Ajoute les pts en utilisant la méthode de class 'CDC_class_joueur.ajout_ptsjoueur()'
    
    Parameters
    ----------
    main_frame : tkinter.Tk
        Fenetre principale.
    btn1 : tkinter.Button
        Bouton de validation.
    btn2 : tkinter.Button
        Bouton pour passer au joueur suivant.
    joueur : CDC_class_joueur.Joueur
        Joueur en cours.
    score : int
        Score du joueur en cours.

    Returns
    -------
    None.

    """
    btn1['state'] = 'disabled'
    btn2['state'] = 'active'
    if score >= 0:
        txt_score = f"{joueur.nom} gagne {score} points"
    elif score < 0:
        txt_score = f"{joueur.nom} perd {score} points"

    joueur.ajout_ptsjoueur(score)
    affiche_score = tk.Label(main_frame, text=txt_score) 
    affiche_score.pack()
    
    
    
def radiobox(main_frame, size_radiobox, *text_label):
    """
    Permet de créer des radiobutton de manière dynamique
    La fonction attend que l'utilisateur click sur le bouton pour renvoyer
    la valeur du radiobutton choisi.

    Parameters
    ----------
    frame : tkinter.Tk
        Fenetre principale.
    size_radiobox : int
        Nombre de radiobutton.
    *text_label : tk.Label
        Description de chaque radiobutton .

    Returns
    -------
    choice : str
        Description du radiobutton choisi.
    radiobox : list
        liste contenant les radiobuttons

    """
    global choice
    #Valeur defaut
    choice = text_label[0]
    
    def set_choice():
        global choice
        choice = text_label[var.get()]
    
    var, var2 = tk.IntVar(), tk.IntVar()
    radiobox = []
    for k in range(size_radiobox):
        radiobox.append(tk.Radiobutton(main_frame, text=text_label[k], variable=var, value=k, command=set_choice))
        radiobox[k].pack()
    
    btn = tk.Button(main_frame, text='Confirmer', command=lambda: [var2.set(1), [rb.config(state='disable') for rb in radiobox]])

    btn.pack()
    btn.wait_variable(var2)
    btn.destroy()

    return choice, radiobox


def set_entry(main_frame, Joueurs_obj, joueur_courant, var_text, ligne_text, warning, *text, final_ordre):
    """
    Permet de généré une entrée texte pour l'utilisateur
    Prend en charge les différentes erreurs d'entrée qui pourrait survenir

    Parameters
    ----------
    frame : tkinter.Tk
        Fenetre principale.
    Joueurs_obj : list[CDC_class_joueur.Joueur]
        Liste des joueurs inscrit au jeu.
    joueur_courant : CDC_class_joueur.Joueur
        Joueur en cours.
    var_text : tkinter.StringVar
        Texte saisi par l'utilisateur.
    ligne_text : tkinter.Entry
        Zone de saisie.
    warning : tkinter.Label
        Label annoncant les erreurs de saisie.
    *text : str
        Texte du label 'warning'.
    final_ordre : str
        ??? ordre final...

    Returns
    -------
    None.

    """
    entry = get_entry(var_text, ligne_text)
    if entry is None:
        return
    elif entry not in [k.nom for k in Joueurs_obj]:
        txt = text[0].format(arg1=entry)
        warning.config(text=txt)
        warning.pack()
        return
    elif entry == joueur_courant.nom:
        txt = text[1].format(arg1=entry)
        warning.config(text=txt)
        warning.pack()
        return
    elif final_ordre:
        eval(final_ordre)
        return
    
