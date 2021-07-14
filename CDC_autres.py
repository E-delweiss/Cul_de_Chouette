#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:41:06 2021

@author: thierry
"""

import re
import tkinter as tk



def clear_widget(liste_messages=[], liste_boutons=[], *argv):
    widget_to_clear = liste_messages + liste_boutons
    
    for widget in widget_to_clear:
        widget.destroy()
        widget.update()
        
        
    for autre_widget in argv:
        autre_widget.destroy()
        autre_widget.update()
        
        


def set_PremierJet(Premier_jet):
    """
    Mise à jour de {Premier_jet} pour qu'il contienne uniquement le(s) joueur(s) ayant fait le plus petit jet
    Retourne {Premier_jet} mis à jour
    """
    smaller_value = min(Premier_jet.values())
    Liste_des_plus_petits = [k for k,v in Premier_jet.items() if v==smaller_value]    
    
    ### Mise à jour
    dico_temp = Premier_jet.copy()
    for k in Premier_jet.keys():
        if k in Liste_des_plus_petits:
            pass
        else:
            del dico_temp[k]
            
    Premier_jet = dico_temp.copy()
    
    return Premier_jet




def toss_chouettes(main, bouton_chouettes, bouton_cul, joueur):
    """
    Utilise les méthodes de la class Joueur pour modifie les attributs
    de class Chouette_1 et Chouette_2
    """
    joueur.chouette_1_2()

    main.msg_chouette12 = tk.Label(main, text=f"Résultat : \nChouette1 score = {joueur.Chouette_1} \nChouette2 score = {joueur.Chouette_2}") 
    main.msg_chouette12.pack()
    main.Liste_labels.append(main.msg_chouette12)
    
    bouton_chouettes['state'] = 'disabled'
    bouton_cul['state'] = 'active'
    
    return



def toss_cul(main, bouton_chouettes, bouton_cul, joueur):
    """
    Utilise les méthodes de la class Joueur pour modifie l'attributs de
    class Cul
    """
    joueur.cul()
    
    main.message_cul = tk.Label(main, text=f"Résultat : \nCul score = {joueur.Cul}") 
    main.Liste_labels.append(main.message_cul)
    main.message_cul.pack()
    
    bouton_chouettes['state'] = 'disabled'
    bouton_cul['state'] = 'disabled'
    
    return
    
    


def get_entry(var_texte, ligne_texte):
    """
    ???
    """
    
    if var_texte.get()=='' or re.match('^ +$', var_texte.get()):
         ligne_texte.delete(0, tk.END)
         return None
    
    temp = var_texte.get()
    temp = re.sub(r'^ +', '', temp)
    temp = temp.capitalize()
    
    return temp



def handle_no_event(main_frame, btn1, btn2, joueur, score):
    """
    Affiche les infos des gains/pertes du tour sur la frame principale
    quand on appuie sur "Ok"
    Ajoute un bouton "Continuer" sur la frame ppale pour passer au
    joueur suivant
    Ajoute les pts en utilisant la méthode de class 'ajout_ptsjoueur()'
    
    main_frame : self i.e. fenetre ppale
    btn1 : bouton de validation
    btn2 : bouton pour passer au joueur suivant
    joueur : instance de class du joueur en cours
    score : int
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