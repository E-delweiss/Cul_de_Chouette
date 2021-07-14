#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:34:57 2021

@author: thierry
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 00:11:59 2021

@author: thierry

Contient les règles du jeu pour chaque combinaisons. 
Source : https://fr.wikibooks.org/wiki/Boîte_à_jeux/Le_cul_de_chouette
"""

import tkinter as tk


def affiche_notice(nom_regle, bouton_notice):
    """
    Créé un bouton pour afficher la règle de l'événement
    Créé un bouton pour fermer la fenetre
    """
    top_notice = tk.Toplevel()
    print('AFFICHE REGLE : ', nom_regle)
    message_notice = tk.Label(top_notice, text=notice(nom_regle)) 
    message_notice.pack()
    bouton_notice['state'] = 'disabled'
    
    ordre = lambda :[top_notice.destroy(), top_notice.update()]
    bouton_fermer_notice = tk.Button(top_notice, text="Fermer", command=ordre)
    bouton_fermer_notice.pack()
    
    




def notice(nom_regle):
    if nom_regle == 'Chouette':
        txt = "Deux dés identiques. \nLa valeur de la Chouette correspond \
au carré de la valeur des deux dés identiques"
            

    if nom_regle == 'Velute':
        txt = "La somme de deux dés est égale à la valeur du troisième dé. \
\nLa Velute a pour valeur le chiffre le plus élevé des trois.\
\nLa valeur de la Velute correspond au double du carré de la Velute."
        

    if nom_regle == 'Chouette-Velute':
        txt = "Une Chouette + une Velute.\
\nLa Chouette-Velute a la valeur de sa Velute.\
\n Le premier joueur qui frappe dans ses mains en criant \
\"Pas mou le caillou !\" gagne les points de la Chouette-Velute.\
\nSi plusieurs joueurs sont à égalité lors de l'annonce, \
alors les points de la Chouette-Velute sont soustraits \
des scores des joueurs concernés."
    

    if nom_regle == 'Cul de Chouette':
        txt = "Trois dés identiques.\
\nLa valeur du Cul de Chouette correspond à 40pts + 10 * valeur du dé."
    
    
    if nom_regle == 'Suite':
        txt = "Trois dés qui se suivent.\
\nTous les joueurs doivent taper du poing sur la table en criant \
\"Grelotte ça picote !\".\
\nLe dernier joueur à le faire perd 10 pts.\
\nSi égalité, les joueurs concernés se départagent en criant \
\"Sans fin est la moisissure des bières bretonnes !\""
    #### Rajouter la suite...
            
    
    if nom_regle == 'Suite-Velutée':
        txt = "Trois dés formant 1,2 et 3.\
\nLa combinaison Suite s'applique.\
\nSi le lanceur arrive à attraper au moins une des chouettes \
en disant \"Patte de canard !\",\
\nil valide alors sa Velute et rend par le fait même impossible la Suite-Velutée.\
\nAutrement, le premier joueur à attraper les chouettes en criant \
\"Velutée !\" doit les relancer \net la combinaison finale prend effet à son bénéfice.\
\nSi deux joueurs, qui ne sont ni l'un ni l'autre le lanceur, \
\nse saisissent chacun d'une chouette et s'exclame \"Velutée\" \
ils peuvent relancer chacun leur chouette \net la combinaison \
finale est soustraite du score du brasseur de la Suite-Velutée, \
seuls les points s'appliquent."
            

    if nom_regle == 'Artichette ':
        txt = "Trois dés formant 4, 3 et 4.\
\nLe joueur peut remporter la valeur de sa Chouette de 4 \
en criant \"Raitournelle!\".\
\nAttention : si un joueur lui crie d’abord \"Artichette!\" en \
le désignant du doigt, \nil lui fait perdre 16 pts, et la \
Chouette de 4 n’est pas valable.\
\n\nEn cas d'égalité, le joueur ayant réalisé l'Artichette est \
prioritaire et remporte donc 16 pts."
            
            
    if nom_regle == 'Souflette':
        txt = "Trois dés formant 4, 2 et 1."
        #### Rajouter la suite...
    



    return txt








"""
Regle supplémentaire pour La Suite. 
S'il y a toujours égalité, les joueurs concernés se départagent en lançant chacun un dé, 
et celui qui fait le plus grand score perd les 10 pts.

Si plusieurs joueurs font le même plus grand score, ils recommencent pour se départager, 
mais cette fois pour perdre 20 pts, puis 30 pts, etc. Si un joueur annonce jusqu'à “ bretonnes ” 
sans qu'il n'y ait eu d'égalité sur la première annonce, il y a Bévue.
"""

