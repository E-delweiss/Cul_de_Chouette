#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:07:02 2021

@author: Thierry
"""

import json

path = "citations.json"
with open(path, 'r') as jsonFile:
    data_json = json.load(jsonFile)


replique = data_json['0']['citation']
Perso = data_json['0']['infos']['personnage']
Saison = data_json['0']['infos']['saison']
Ep = data_json['0']['infos']['episode']




# phrase = "{0}\n{1!s:30}-{2}, {3}ep.{4}".format(replique, ' ', Perso, Saison, Ep)
phrase = "{0}\n{1!s:3}-{2}, {3}ep.{4}".format(replique, ' ', Perso, Saison, Ep)
print(phrase)

### prendre les phrases <150 caractères ?

"""
length = []
for k in range(len(data_json)):
    try:
        it = str(k)
        length.append(len(data_json[it]['citation']))
    except KeyError:
        pass
"""