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
        Initialisation du constructeur avec le nom d'un joueur.
        """
        self.nom = nom
    
    
    def chouette_1_2(self):
        """
        Methode qui permet de lancer les Chouettes et modifie les attributs 
        de classe 'Joueur.Chouette_1' et 'Joueur.Chouette_2'.

        Returns
        -------
        None.

        """        
        self.Chouette_1 = rd.randint(1, 6)
        self.Chouette_2 = rd.randint(1, 6)
        return 


    def cul(self):
        """
        Methode qui permet de lancer le Cul et modifie l'attributs de classe 
        'Joueur.Cul'.

        Returns
        -------
        None.

        """
        self.Cul = rd.randint(1, 6)
        return 


    def ajout_ptsjoueur(self, pts):
        """
        Gère le score et modifie l'attribut de classe 'Joueur.PtsJoueur'.

        Parameters
        ----------
        pts : int
            Points à ajouter.
            Attention ! S'il y a une perte de points, 'pts' doit être négatif.

        Returns
        -------
        None.

        """    
        self.PtsJoueur += pts
        return 
    
    
    def ajout_grelottine(self, nb_grelottine):
        """
        Gère les Grelottines et modifie l'attribut de classe 'Joueur.Grelottine'

        Parameters
        ----------
        nb_grelottine : int
            Grelottines à ajouter.
            Attention ! S'il y a une perte de Grelotinne, 'nb_grelottine' 
            doit être négatif.

        Returns
        -------
        None.

        """
        self.Grelottine += nb_grelottine
        return 