#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:02:37 2021

@author: thierry
"""
### CDC_handle_tie ligne 100
import tkinter as tk

import CDC_class_joueur as cl
import CDC_autres as aut
import CDC_amorcage as am
import CDC_notice as nt
import CDC_donne_event as d_ev
import CDC_fonctions as fct
import CDC_citations as citations


class Root(tk.Tk):
    """ 
    Class qui va amorcer le début du programme
    Le programme se déroule ensuite à la chaine
    
    ListeJoueurs : [liste] de 'str' contenant le nom des joueurs
    Joueurs_obj : [liste] d'objets contenant des instances de la class Joueur
                initialisées avec le nom des joueurs
    Firstplayer : 'str' représente le premier joueur qui commence
    Joueur_en_cours : obj représente l'instance de class du joueur entrain de jouer
    Joueur_gagnant : 'str' représente le premier joueur arrivé à 343
    Help_notice : 'str' prend le nom de la combinaison en cours pour que la class du même nom puisse appeler la notice
    """
    
    ### Initialisation des attributs de class
    ListeJoueurs = ['A', 'B', 'C']
    Joueurs_obj = [cl.Joueur('A'), cl.Joueur('B'), cl.Joueur('C')]
    Firstplayer = 'B'
    Joueur_en_cours = ''
    Joueur_gagnant = ''
    Help_notice = None
    
    def __init__(self, *args, **kwargs):
        """
        Initialisation du constructeur
        Il permet de d'amorcer le jeu à travers un Tkinter
        """
        tk.Tk.__init__(self, *args, **kwargs)
        ReOrganize()
        Help_notice(self)
        Citation_window(self)
        Score_window(self)

        
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
                
        Game()
        

class Game(tk.LabelFrame):
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
        tk.LabelFrame.__init__(self, master)
        self.place( x = 10, y = 10, width = 1000, height = 600)

        
        self.increment_iterateur()
        Root.Joueur_en_cours = Root.Joueurs_obj[self.It]
        
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
        """
        Permet de boucler sur la liste des joueurs
        Si on arrive à la fin de la liste, on reset It
        """
        if cls.It == len(Root.Joueurs_obj)-1:
            cls.It = -1
        cls.It +=1
        
        
    def poursuivre(self):
        """
        Créé un bouton "Suivant" pour lancer la prochaine class qui va gérer les règles du CDC
        """
        self.launch_button = tk.Button(self, text="Suivant", command=Regles_CDC)
        self.launch_button.pack()
        self.Liste_boutons.clear()
        self.Liste_boutons.append(self.launch_button)
        

        
    
##################################################################################################

    ######### CREER UNE AUTRE CLASS Regles_CDC qui va s'occuper d'annoncer les règles
    ######### à la fin, on vérifie s'il y a un gagnant, si non on relance Game
    
class Regles_CDC(tk.LabelFrame):
    """
    Class qui va gérer les règles du CDC en fonction des combinaisons après avoir lancer les dés
    Va annoncer les événements, incrémenter les points etc...
    """
        
    def __init__(self, master=None):
        """
        Initialisation du constructueur
        ...
        """
        tk.LabelFrame.__init__(self, master)
        self.place( x = 10, y = 10, width = 1000, height = 600)

        Game.Liste_boutons[0]['state'] = 'disabled'
        #### pour tester
        chouette_1 = 1
        chouette_2 = 2
        cul = 3
        ####
        
        
        bouton_joueur_suivant = tk.Button(self, text='Joueur suivant', command=lambda: Game(self))
        
        ######
        dict_var = am.give_the_rules(self, bouton_joueur_suivant, Root.Joueurs_obj, chouette_1, chouette_2, cul)
        Root.Help_notice = dict_var['nom_regle']
        ######
        
        if not dict_var['event']:
            ordre = lambda: aut.handle_no_event(self, btn, bouton_joueur_suivant, Root.Joueurs_obj[Game.It], dict_var['score'])
            btn = tk.Button(self, text='Ok', command=ordre)
            btn.pack()
            
        if dict_var['event']:
            d_ev.annonce_evenement(self, bouton_joueur_suivant, 
                                   Root.Joueurs_obj, 
                                   Root.Joueur_en_cours,
                                   dict_var)




######## TODO 19/07 : inserer is_there_a_winner




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
    






















class Score_window(tk.LabelFrame):
    """
    Gère l'affichage des joueurs et des scores
    """
    
    def __init__(self, master=None):
        """
        Initialisation du constructeur
        Place une section 'score' à droite de la page
        Affiche les joueurs et permet d'actualiser et de visualiser les scores
        
        Permet d'annoncer une bévue sur le joueur en cours et de lui faire perdre
        10 points par bévue
        """
        tk.LabelFrame.__init__(self, master)
        self.place( x = 1020, y = 10, width = 370, height = 600)
        
        
        self.label = tk.Label(self, text='Liste des joueurs')
        self.label.place(relx=0.5, rely=0.05, anchor='center')
        
        count = 0.1
        for k in Root.Joueurs_obj:
            tk.Label(self, text=k.nom).place(relx=0.5, rely=count, anchor='center')
            count += 0.05
        
        count+=0.1
        self.score_bouton = tk.Button(self, text="Score", command=lambda: self.affiche_score(count, self.score_bouton))
        self.score_bouton.place(relx=0.5, rely=count, anchor='center')
        
        
        #### Bévue
        count_bevue = count + 0.5
        self.bevue_bouton = tk.Button(self, text="Bévue", command=lambda: self.bevue(count_bevue))
        self.bevue_bouton.place(relx=0.5, rely=count_bevue, anchor='center')
        
        
        
    def affiche_score(self, count, btn):
        """
        Gere l'actualisation des scores avec un bouton
        count : variable de positionnement du Widget en fonction des précédents
        btn : score_bouton
        """
        btn.config(text="Actualiser")
        
        count+=0.1
        for k in Root.Joueurs_obj:
            txt =f"{k.nom}    :    {k.PtsJoueur} points"
            tk.Label(self, text=txt).place(relx=0.5, rely = count, anchor='center')
            count += 0.05
        
        
    def bevue(self, count):
        """
        Gere la bévue : fait perdre 10 pts au joueur entrain de joueur à chaque fois
        qu'on appuie dessus.
        count : variable de positionnement du Widget bévue en fonction des précédents
        """
        if isinstance(Root.Joueur_en_cours, cl.Joueur):
            count+=0.1
            Root.Joueur_en_cours.ajout_ptsjoueur(-fct.bevue())
            tk.Label(self, text=f"Le joueur {Root.Joueur_en_cours.nom} perd 10 points pour bévue").place(relx=0.5, rely=count, anchor='center')
        else:
            return
            
            
            
class Citation_window(tk.LabelFrame):
    """
    Gère l'aide pour les combinaison de dés
    """
    
    def __init__(self, master=None):
        """
        Initialisation du constructeur
        Place une section 'citation' au dessus des notices
        """
        tk.LabelFrame.__init__(self, master)
        self.place( x = 20, y = 500, width = 980, height = 100)
        
        self.citation_label = tk.Label(self)
        self.citation_label2 = tk.Label(self)
        self.after(20, self.call_citation)
        
    def call_citation(self):
        replique, indication = citations.citation()
        self.citation_label.config(text = replique)
        self.citation_label2.config(text = indication)
        self.citation_label.pack()
        self.citation_label2.pack()
        self.after(3000, self.call_citation)

            

class Help_notice(tk.LabelFrame):
    """
    Gère l'aide pour les combinaison de dés
    """
    
    def __init__(self, master=None):
        """
        Initialisation du constructeur
        Place une section 'notice' en bas de page
        """
        tk.LabelFrame.__init__(self, master)
        self.place( x = 10, y = 620, width = 1380, height = 170)
        
        
        self.notice_bouton = tk.Button(self)
        ordre = lambda : self.call_notice()
        self.notice_bouton.config(text="Help", command=ordre)
        self.notice_bouton.place(relx=0.5, rely=0.5, anchor='center')
        

    def call_notice(self):
        """
        Appelle la fonction nt.notice du fichier CDC_notice
        Affiche et ferme la notice de la combinaison en cours (valeur de Root.Help_notice)
        Ne fait rien sinon
        """
        if Root.Help_notice is None:
            return
        
        else:
            label_notice = tk.Label(self, text=nt.notice(Root.Help_notice)) 
            label_notice.pack()
            btn = tk.Button(self, text="Fermer", command=lambda:[label_notice.destroy(), btn.destroy()])
            btn.pack()




root = Root()
root.title("Jeu du Cul de Chouette")
root.geometry('1400x800')
# root1.wm_iconbitmap(r'/Users/thierry/Documents/Python_divers/CDC/owl1.ico')
root.mainloop()