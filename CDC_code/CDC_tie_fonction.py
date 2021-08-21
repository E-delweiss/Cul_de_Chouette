#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:55:59 2021

@author: thierry
"""

import tkinter as tk
import random as rd
import CDC_handle_tie as hdl
import CDC_autres as aut


def tie_fonction(frame, liste_joueurs, *text_label, checkbox=False, command1=[], is_an_entry=False, dice_decision=False, command2=[]):
    """
    ???

    Parameters
    ----------
    frame : tkinter.Tk
        Fenetre principale.
    liste_joueurs : list[CDC_class_joueur.Joueur]
        Liste des joueurs inscrits.
    *text_label : str
        Texte des labels qui vont être créés.
    checkbox : bool, optional
        Création d'une checkbox. The default is False.
    command1 : str, optional
        Commande de la checkbox. The default is [].
        Non-optional if 'checkbox' is True.
    is_an_entry : bool, optional
        Création d'une zone de saisie. The default is False.
    dice_decision : bool, optional
        Gere les cas où les joueurs doivent se départager en lançant un dé.
        The default is False.
        ??? Pas sur que ça fonctionne
    command2 : str, optional
        Commande appelée dans la boucle 'dice_decision'. The default is [].
        Non-optional if 'dice_decision' is True.

    Returns
    -------
    None.

    """
    widget_list = []
    label1 = tk.Label(frame, text=text_label[0])
    label1.pack()
    widget_list.append(label1)
    
    #########################################################################
    if checkbox:
        var = dict()
        hdl.GlobalVars.List_joueurs_tie.clear()
        
        for k in liste_joueurs:
            var[k.nom]=tk.IntVar()
            checkbox = tk.Checkbutton(frame, text=k.nom, variable=var[k.nom], onvalue=1, offvalue=0, command=lambda key=k: readstatus(key, var))
            checkbox.pack()
        
        bouton_val_checkbox = tk.Button(frame, text='Valider', command=lambda: eval(command1))
        bouton_val_checkbox.pack()
        widget_list.append(bouton_val_checkbox)
        
        
    #########################################################################
    if dice_decision:
        var = dict()
        for k in hdl.GlobalVars.List_joueurs_tie:
            var[k] = rd.randint(1,6)
            label_dice_decision = tk.Label(frame, text=f'{k.nom} a fait {var[k]}')
            label_dice_decision.pack()
            widget_list.append(label_dice_decision)
            
        dico_temp = {key: value for key, value in var.items() if value in sorted(set(var.values()), reverse=True)[:1]}
        hdl.GlobalVars.List_joueurs_tie = list(dico_temp.keys())
        hdl.GlobalVars.Count += 1
        
        if len(hdl.GlobalVars.List_joueurs_tie)>1:
            tie_label = tk.Label(frame, text='Encore égalité !')
            tie_label.pack()
            widget_list.append(tie_label)
            tie_button = tk.Button(frame, text='Ok', command=lambda: eval(command2))
            tie_button.pack()
            widget_list.append(tie_button)
        
        else :
            pts = hdl.GlobalVars.Count * hdl.GlobalVars.Dict_var['score']
            tk.Label(frame, text=f"{hdl.GlobalVars.List_joueurs_tie[0].nom} à fait le plus grand score et perd {pts} points !").pack()
            print(hdl.GlobalVars.List_joueurs_tie[0])
            hdl.GlobalVars.List_joueurs_tie[0].ajout_ptsjoueur(pts)
            hdl.GlobalVars.Btn_jr_svt.pack()
    #########################################################################
    if is_an_entry:
        
        def set_entry():
            entry = aut.get_entry(var_texte, ligne_texte)
            if entry is None:
                return
            elif entry not in [k.nom for k in liste_joueurs]:
                txt = f"Le joueur {entry} n'existe pas"
                warning.config(text=txt)
                return
            elif entry not in [k.nom for k in hdl.GlobalVars.List_joueurs_tie]:
                txt=f"Le joueur {entry} n'appartient pas à l'égalité"
                warning.config(text=txt)      
                return  
            elif entry in [k.nom for k in hdl.GlobalVars.List_joueurs_tie]:
                bouton_submit.destroy()
                txt=f"{entry} a perdu la {hdl.GlobalVars.Dict_var['nom_regle']}"
                warning.config(text=txt)
                recap = tk.Label(frame, text=f"{entry} perd {hdl.GlobalVars.Dict_var['score']} points.")
                recap.pack()
                
                for k in liste_joueurs:
                    if k.nom in entry:
                        pts = hdl.GlobalVars.Dict_var['score']
                        k.ajout_ptsjoueur(pts)
                        
                hdl.GlobalVars.Btn_jr_svt.pack()
        
                
        var_texte = tk.StringVar()
        ligne_texte = tk.Entry(frame, textvariable=var_texte, width=30)
        ligne_texte.pack()
        warning = tk.Label(frame, text='')
        warning.pack()
        bouton_submit = tk.Button(frame, text='Ok', command=set_entry)
        bouton_submit.pack()
                
        
    
    
    hdl.GlobalVars.Widget_liste = widget_list
        
    return


def readstatus(key, var):
    """
    Permet de lire les choix fait dans la checkbox

    Parameters
    ----------
    key : CDC_class_joueur.Joueur
        Joueur retourné par une case de la checkbox.
    var : dict{str : tkinter.IntVar}
        Contient le choix fait par l'utilisateur via la checkbox
        
    Returns
    -------
    None.

    """
    var_obj = var.get(key.nom)
    if var_obj.get() == 1:
        hdl.GlobalVars.List_joueurs_tie.append(key)
    if var_obj.get() == 0:
        hdl.GlobalVars.List_joueurs_tie.remove(key)