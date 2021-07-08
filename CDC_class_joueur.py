#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:58:08 2021

@author: thierry
"""

"""
Contient la class "Joueur" qui défini le profil de chaque joueur en 
rassemblant ses données de jeu : dés, points, gains, pertes...
Les méthodes contenues dans la class "Joueur" modifient les attributs de class
"""


import random as rd

class Joueur:
    ### Initialisation des attributs de class
    Chouette_1 = 0
    Chouette_2 = 0
    Cul        = 0
    
    PtsJoueur = 0
    Bevue = 0
    Grelottine = 0
    
    def __init__(self, nom):
        """
        Initialisation du constructeur avec le nom d'un joueur
        """
        
        self.nom = nom
    
    
    @classmethod
    def chouette_1_2(cls):
        """ Lance les Chouettes et modifie les attributs 
        de class Chouette_1 et Chouette_2"""
        
        cls.Chouette_1 = rd.randint(1, 6)
        cls.Chouette_2 = rd.randint(1, 6)
        
        # print(f"Score : {cls.Chouette_1} et {cls.Chouette_2}")
        return 


    @classmethod
    def cul(cls):
        """Lance le Cul et modifie l'attribut de class Cul"""
        
        cls.Cul = rd.randint(1, 6)
        
        # print(f"Score : {cls.Cul}")
        return 


    @classmethod
    def ajout_ptsjoueur(cls, pts):
        """
        Gère le score et modifie l'attribut de class PtsJoueur
        Attention ! S'il y a une perte de points il faut que 
        'pts' soit négatif
        """
        
        cls.PtsJoueur += pts
        
        # print(f"Joueur : {self.nom} Points = {cls.PtsJoueur}")
        return 
    
    
    @classmethod
    def ajout_grelottine(cls, nb_grelottine):
        """
        Gère les Grelottines et modifie l'attribut de class Grelottine
        Attention ! S'il y a une perte de Grelotinne il faut que 
        'nb_grelottine' soit négatif
        """
        
        cls.Grelottine += nb_grelottine
        
        # print(f"Le joueur {self.nom} a maintenant {cls.Grelottine} Grelottine.")
        return 