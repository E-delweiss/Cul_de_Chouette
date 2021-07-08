#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:02:37 2021

@author: thierry
"""

import random as rd
import re

import tkinter as tk

import CDC_class_joueur as cl
import CDC_autres as aut


class Root(tk.Tk):
    """ 
    Class qui va amorcer le début du programme
    Le programme se déroule ensuite à la chaine
    
    ListeJoueurs : [liste] de 'str' contenant le nom des joueurs
    Joueurs_obj : [liste] d'objets contenant des instances de la class Joueur
                initialisées avec le nom des joueurs
    Firstplayer : 'str' représente le premier joueur qui commence
    Joueur_gagnant : 'str' représente le premier joueur arrivé à 343
    """
    
    ### Initialisation des attributs de class
    ListeJoueurs = []
    Joueurs_obj = []
    Firstplayer = ''
    Joueur_gagnant = ''
    
    def __init__(self, *args, **kwargs):
        """
        Initialisation du constructeur
        Il permet de d'amorcer le jeu à travers un Tkinter
        """
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        ### Run Inscription des joueurs
        Inscription_des_joueurs(self)

        
class Inscription_des_joueurs(tk.Frame):
    """
    Class qui permet d'inscrire le nom des joueurs
    Attention il faut 3 joueurs minimum
    
    Liste_labels : [liste] contenant des widgets Label
    Liste_boutons : [liste] contenant des widgets Button
    """
   
    Liste_labels = []
    Liste_boutons = []
    
    def __init__(self, master):
        """
        Initialisation du constructeur
        Il permet de créer une main frame pour gérer les inscriptions
        """
        
        tk.Frame.__init__(self, master)
        self.pack(fill=tk.BOTH)


        ### Demande a l'utilisateur de rentrer les joueurs
        self.message = tk.Label(self, text="Lister le nom des joueurs", anchor='w')
        self.message.pack()
        self.Liste_labels.append(self.message)
        
        # Créé une zone de saisie
        self.var_texte = tk.StringVar()
        self.ligne_texte = tk.Entry(self, textvariable=self.var_texte, width=30)
        self.ligne_texte.pack()
        
        # Ajouter avec 'espace'
        self.ligne_texte.focus_set()
        self.ligne_texte.bind('<space>', self.add_player)
        
        ### Creation d'un bouton pour ajouter un joueur
        self.bouton_ajouter = tk.Button(self, text="Ajouter", command=self.add_player)        
        self.bouton_ajouter.pack(side="left")
        self.Liste_boutons.append(self.bouton_ajouter)

        ### Ferme le widget
        self.bouton_fin_ajouter = tk.Button(self, text="Fin", command=self.affiche_joueur)
        self.bouton_fin_ajouter.pack(side="right")
        self.ligne_texte.bind('<Return>', self.affiche_joueur)
        self.Liste_boutons.append(self.bouton_fin_ajouter)

    
    
    def add_player(self, event=None):
        """
        Permet d'ajouter des joueurs à Root.Liste_joueurs
        Un message s'affiche à chaque ajout
        """
        ### Test sur la présence d'un texte
        if self.var_texte.get()=='' or re.match('^ +$', self.var_texte.get()):
            return
        
        temp = self.var_texte.get()
        temp = re.sub(r'^ +', '', temp)
        temp = temp.capitalize()
        
        ### Test sur l'existance d'un joueur
        if temp in Root.ListeJoueurs:
            self.message["text"] = f"Le joueur {temp} existe déjà."
        
        
        else:
            ### Ajout d'un joueur
            Root.ListeJoueurs.append(temp)
            self.message["text"] = f"Le joueur {temp} a été ajouté."
            self.ligne_texte.delete(0, tk.END)
            
            ### Chaque joueur correspond à une instance de la class cl.Joueur
            Root.Joueurs_obj = [cl.Joueur(k) for k in Root.ListeJoueurs]
            
    
    def affiche_joueur(self, event=None):   
        """
        - Vérifie qu'il y a au moins 3 joueurs
        - Remplace les Widgets précédents par la liste des joueurs qui ont été ajoutés
        Créé un bouton "Suivant"
        """
        if len(Root.ListeJoueurs) < 3:
            self.message["text"] = "Le jeu se joue à 3 minimum, rajoutez des joueurs."
            self.Liste_labels.append(self.message)
        
        else:
            aut.clear_widget(self.Liste_labels, self.Liste_boutons, self.ligne_texte)

            self.message = tk.Label(self, text=f"Les {len(Root.ListeJoueurs)} joueurs sont :")
            self.message.pack(side='top', fill='both', expand='True')
            self.Liste_labels.append(self.message)
            
            for k in Root.ListeJoueurs:
                self.message = tk.Label(self, text='- '+k)
                self.message.pack()
                self.Liste_labels.append(self.message)
            
            

            ### Fin des inscriptions et lancement de la partie
            self.bouton_fin_des_inscriptions = tk.Button(self, text="Suivant", command=lambda:[self.destroy(), self.update(), Quel_joueur_commence(self)])
            self.bouton_fin_des_inscriptions.pack(side="bottom")
            self.Liste_boutons.append(self.bouton_fin_des_inscriptions)
            
            ### Binding
            self.bouton_fin_des_inscriptions.focus_set()
            self.bouton_fin_des_inscriptions.bind('<Return>', self.fin_inscriptions)
        
        
    def fin_inscriptions(self, event=None):
        """Permet de clear les Widgets précédents et de passer 
        au nouveau Widget parent "WhosStarting" """
        self.destroy()
        self.update()
        
        Quel_joueur_commence(self)
        
        
        
class Quel_joueur_commence(tk.Frame):
    """
    Class qui permet de déterminer le joueur qui va commencer
    
    Liste_labels : [liste] contenant des widgets Label
    Liste_boutons : [liste] contenant des widgets Button
    Premier_jet : {keys = nom des joueurs, values = score de leur premier jet}
    Iterateur : ???
    """
    
    Premier_jet = {}
    Liste_labels = []
    Liste_boutons = []
    Iterateur = 0
    
    
    def __init__(self, master=None):
        """
        Initialisation du constructueur
        Il permet de créer une main frame pour annoncer le joueur qui commence
        """
        
        tk.Frame.__init__(self, master=None)
        self.pack(fill=tk.BOTH)
        
        self.message_pres = tk.Label(self, text="Chaque joueur va lancer 1 dé.\nLe joueur qui a le plus petit score commence.\n")
        self.message_pres.pack(side="top")
        self.Liste_labels.append(self.message_pres)
        
        self.liste_labels = []
        self.liste_boutons  = []
        for joueur in Root.Joueurs_obj:
            self.message = tk.Label(self, text=f"Cliquer sur le bouton pour que {joueur.nom} lance un dé.")
            self.message.pack()
            self.Liste_labels.append(self.message)
            
            self.bouton_jet_dice = tk.Button(self, text="Lancer un dé", command=self.lancer_dice)
            self.bouton_jet_dice.pack()
            self.Liste_boutons.append(self.bouton_jet_dice)
            
            ### Ces widgets vont être remplacés dynamiquement
            self.liste_labels.append(self.message)
            self.liste_boutons.append(self.bouton_jet_dice)
            
    def lancer_dice(self):
        """
        Alimente {Premier_jet} avec le nom des joueurs et leur score de dé
        Appelle la fonction is_tie()
        """
        
        ### Lancé du premier dé et stockage dans {Premier_jet}
        self.Premier_jet[Root.Joueurs_obj[self.Iterateur].nom] = rd.randint(1, 1000)
        
        
        self.liste_labels[self.Iterateur]["text"] = f"{Root.Joueurs_obj[self.Iterateur].nom} a fait {self.Premier_jet[Root.Joueurs_obj[self.Iterateur].nom]} !"
        self.liste_boutons[self.Iterateur]["state"] = 'disable'
        
        self.Iterateur += 1
        
        if self.Iterateur == len(Root.Joueurs_obj):
            self.bouton_suivant = tk.Button(self, text="Suivant", command=self.est_ce_que_egalite)
            self.bouton_suivant.pack(side='bottom')
            self.Liste_boutons.append(self.bouton_suivant)




    def est_ce_que_egalite(self):
        """
        Détermine s'il y a une égalité dans les scores
        Si oui : annonce les joueurs ayant le plus petit score et appelle there_is_tie()
        Si non : annonce le joueur qui commence et clear la Frame
        """
        
        ### Clear la frame
        aut.clear_widget(self.Liste_labels, self.Liste_boutons, self.message_pres)
        
        ### Mise à joueur de {Premier_jet}
        self.Premier_jet = aut.set_PremierJet(self.Premier_jet)
        
        
        ### Si égalité, len(Premier_jet) > 1
        if len(self.Premier_jet) > 1:
            self.message_tie = tk.Label(self, text="Egalité !")
            self.message_tie.pack(side='top', fill='both', expand='True')
            self.Liste_labels.append(self.message_tie)
            
            temp = ', '.join([k for k in self.Premier_jet.keys()])
            self.message_tie2 = tk.Label(self, text=f" Les joueurs {temp} doivent se départager")
            self.message_tie2.pack(side='top', fill='both', expand='True')
            self.Liste_labels.append(self.message_tie2)
            
            self.bouton_relance_dice = tk.Button(self, text="Relancer les dés", command=self.egalite)
            self.bouton_relance_dice.pack()
            self.Liste_boutons.append(self.bouton_relance_dice)
            
        else:
            ### S'il n'y a pas égalité retourne le premier joueur
            Root.Firstplayer = ''.join(self.Premier_jet)
            self.message_firstplayer = tk.Label(self, text=f"{Root.Firstplayer} va commencer en premier !")
            self.message_firstplayer.pack(side='top', fill='both', expand='True')
            self.Liste_labels.append(self.message_firstplayer)
            
            ordre = lambda :[aut.clear_widget(self.Liste_labels, self.Liste_boutons), ReOrganize()]
            self.bouton_fin = tk.Button(self, text='Commencer le jeu', command=ordre)
            self.bouton_fin.pack()
            self.Liste_boutons.append(self.bouton_fin)


    def egalite(self):
        """
        Gere l'égalité
        Appelle est_ce_que_egalite() pour boucler si l'égalité persiste
        
        """        
        aut.clear_widget(self.Liste_labels, self.Liste_boutons)
        
        for k in self.Premier_jet.keys():
            self.Premier_jet[k] = rd.randint(1, 6)
            
            self.message_tie3 = tk.Label(self, text=f"{k} a fait {self.Premier_jet[k]} !\n")
            self.message_tie3.pack()
            self.Liste_labels.append(self.message_tie3)
        
        
        self.bouton_continue = tk.Button(self, text='Continuer', command=self.est_ce_que_egalite)
        self.bouton_continue.pack()
        self.Liste_boutons.append(self.bouton_continue)
        
        
class ReOrganize():
    
    def __init__(self):
        """
        Initialisation du constructeur
        Permet de réorganiser [Joueurs_obj] afin que 'Firstplayer' commence en premier
        + Lance le début du jeu
        """
        for k in range(len(Root.ListeJoueurs)):
            if Root.Joueurs_obj[k].nom == Root.Firstplayer:
                temp = Root.Joueurs_obj[k]
                Root.Joueurs_obj.remove(temp)
                Root.Joueurs_obj.insert(0, temp)
                
        Game(self)
        

class Game(tk.Frame):
    """
    Permet de faire lancer les dés aux joueurs
    Liste_labels : [liste] contenant des widgets Label
    Liste_boutons : [liste] contenant des widgets Button
    It : 
    """
    Liste_labels = []
    Liste_boutons = []
    It = -1
    
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=None)
        self.pack(fill=tk.BOTH)

        
        self.increment_iterateur()
        self.is_there_a_winner()
        
        
        self.msg_lance_dice = tk.Label(self, text=f"{Root.Joueurs_obj[self.It].nom} va lancer les deux Chouettes puis le Cul")
        self.msg_lance_dice.pack(side='top')
        self.Liste_labels.append(self.msg_lance_dice)
        
        
        self.bouton_chouettes = tk.Button(self, text="Lancer les Chouettes")
        self.bouton_cul = tk.Button(self, text="Lancer le Cul", state='disabled')
        self.bouton_chouettes.pack(side='top')
        self.Liste_boutons.append(self.bouton_chouettes)
        self.Liste_boutons.append(self.bouton_cul)
        
        ordre1 = lambda: aut.toss_chouettes(self, self.bouton_chouettes, self.bouton_cul, Root.Joueurs_obj[self.It])
        ordre2 = lambda: [aut.toss_cul(self, self.bouton_chouettes, self.bouton_cul, Root.Joueurs_obj[self.It]),  self.poursuivre()]
        
        self.bouton_chouettes.config(command=ordre1)
        self.bouton_cul.config(command=ordre2, state='disabled')
        self.bouton_cul.pack(side='top')

        
    @classmethod
    def increment_iterateur(cls):
        cls.It +=1
        
        
    def poursuivre(self):
        """
        Créé un bouton "Suivant" pour lancer la prochaine class qui va gérer les règles du CDC
        en fonction des combinaisons
        """
        self.launch_button = tk.Button(self, text="Suivant", command=Regles_CDC)
        self.launch_button.pack(side='bottom')
        

        
    
##################################################################################################

    ######### CREER UNE AUTRE CLASS Regles_CDC qui va s'occuper d'annoncer les règles
    ######### à la fin, on vérifie s'il y a un gagnant, si non on relance Game
    
class Regles_CDC():
    pass
    
    ########################### A METTRE DANS UNE AUTRE CLASS >>> Si les conditions sont validées, on relance
    ########################### Game(), si non on annonce un gagnant
    ##### In process...
    def is_there_a_winner(self):
        temp = [k.PtsJoueur for k in Root.Joueurs_obj if k.PtsJoueur >= 343]
        
        # for joueur in Root.Joueurs_obj:
        if self.It < len(Root.Joueurs_obj) and not temp :
            print('pass1')
            pass
        
        elif self.It == len(Root.Joueurs_obj) and not temp:
            print('pass2')
            Game.It = 0
            
        elif temp:
            # deal_with_winner()
            print('ON A UN GAGNANT !')
            pass
        

    def loop_player(self):
        
        self.bouton_next = tk.Button(self, text='Suivant') 
        
        ### Faire les trucs du CDC pour le joueur
        ordre = lambda: self.call_rule(Root.Joueurs_obj[self.It])
        self.bouton_next['command'] = ordre
            
        self.bouton_next.pack(side='top')
        self.Liste_boutons.append(self.bouton_next)

