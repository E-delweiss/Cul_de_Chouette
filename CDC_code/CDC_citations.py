#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:07:02 2021

@author: Thierry
"""

import json
import random as rd

path = "citation/citations.json"
with open(path, 'r') as jsonFile:
    data_json = json.load(jsonFile)


def citation():
    """
    Produit une citation de Kaamelott à partir d'un fichier .json (ne prend
    pas le livre VI)
    Note : citation 756 manquante
    Note 2 : on ne prend que les citations inférieures à 250 caractères

    Returns
    -------
    replique : str
        Chaine contenant la réplique
    indication : str
        Chaine contenant le personnage, la saison et l'épisode de la série.

    """
    idx = str(rd.randint(0, len(data_json)))
    while idx == '756' or len(data_json[idx]['citation']) >= 200 or data_json[idx]['infos']['saison'] == 'Livre VI ':
        idx = str(rd.randint(0, len(data_json)))
    
    replique = data_json[idx]['citation']
    perso = data_json[idx]['infos']['personnage']
    saison = data_json[idx]['infos']['saison']
    try: 
        ep = data_json[idx]['infos']['episode']
    except KeyError:
        ep = ''
    
    nb_word = 20
    if len(replique.split()) >= nb_word:
        replique1 = " ".join(replique.split()[:nb_word//2])
        replique2 = " ".join(replique.split()[nb_word//2:])
        replique = replique1 +'\n'+replique2
    
    if perso is None:
        perso = 'Inconnu'
    
    indication = "- " + perso + '. '+ saison[:-1] + ', ep' + ep[1:]
    return replique, indication





"""
long = []
for k in range(len(data_json)):
    if k == 756:
        continue
    
    long.append(len(data_json[str(k)]['citation'].split()))
    
    
import pandas as pd
long_s = pd.Series(long)





s = 'the heart was made to be broken.'

for i, word in enumerate(s.split(), 1):
    if i % 4:
        print(word)
    else:
        print(word)
"""