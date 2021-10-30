#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:02:37 2021

@author: thierry
"""

import random as rd

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
    Le programme se déroule ensuite à la chaine.

    Parameters
    ----------
    ListeJoueurs : list[str]
        Liste contenant le nom des joueurs.
    Joueurs_obj : list[CDC_class_joueur.Joueur]
        Liste content des instances de la class Joueur
    Joueur_en_cours : CDC_class_joueur.Joueur
        Instance de la class Joueur représentant le joueur entrain de jouer
    Firstplayer : str
        Nom du premier joueur qui commence la partie
    Joueur_gagnant : str
        Nom du premier joueur qui arrive à 343
    Help_notice : str
        Nom de la combinaison en cours
        
    """
    ListeJoueurs = []
    Joueurs_obj = []
    Firstplayer = ''
    Joueur_en_cours = ''
    Joueur_gagnant = ''
    Help_notice = None
    
    def __init__(self, *args, **kwargs):
        """
        Initialisation du constructeur
        Il permet de d'amorcer le jeu à travers un Tkinter
        """
        tk.Tk.__init__(self, *args, **kwargs)
        Inscription_des_joueurs(self)
        Help_notice(self)
        Citation_window(self)
        Score_window(self)

        
class Inscription_des_joueurs(tk.LabelFrame):
    """
    Class qui permet d'inscrire le nom des joueurs
    Attention il faut 3 joueurs minimum
    
    Parameters
    ----------
    Liste_labels : list[tkinter.Label]
        Liste contenant des widgets Label
    Liste_boutons : list[tkinter.Button]
        Liste contenant des widgets Button
        
    """
    
    Liste_labels = []
    Liste_boutons = []
    
    def __init__(self, master):
        """
        Initialisation du constructeur
        Il permet de créer une main frame pour gérer les inscriptions
        """
        tk.LabelFrame.__init__(self, master)
        self.place( x = 10, y = 10, width = 1000, height = 600)
              
        ### Demande a l'utilisateur de rentrer les joueurs
        self.message = tk.Label(self, text="Lister le nom des joueurs")
        self.message.place(relx=0.5, rely=0.1, anchor='center')
        self.Liste_labels.append(self.message)
        
        # Créé une zone de saisie
        self.var_texte = tk.StringVar()
        self.ligne_texte = tk.Entry(self, textvariable=self.var_texte, width=30)
        self.ligne_texte.place(relx=0.5, rely=0.15, anchor='center')
        
        # Ajouter avec 'espace'
        self.ligne_texte.focus_set()
        self.ligne_texte.bind('<space>', self.add_player)
        
        ### Creation d'un bouton pour ajouter un joueur
        self.bouton_ajouter = tk.Button(self, text="Ajouter", width=5, command=self.add_player)        
        self.bouton_ajouter.place(relx=0.4, rely=0.19)
        self.Liste_boutons.append(self.bouton_ajouter)

        ### Ferme le widget
        self.bouton_fin_ajouter = tk.Button(self, text="Fin", width=5, command=self.affiche_joueur)
        self.bouton_fin_ajouter.place(relx=0.5, rely=0.19)
        self.ligne_texte.bind('<Return>', self.affiche_joueur)
        self.Liste_boutons.append(self.bouton_fin_ajouter)

    
    
    def add_player(self, event=None):
        """
        Permet d'ajouter des joueurs à Root.Liste_joueurs

        Parameters
        ----------
        event : TYPE, optional

        Returns
        -------
        None.

        """
        entry = aut.get_entry(self.var_texte, self.ligne_texte)
        if entry is None:
            return
        
        ### Test sur l'existance d'un joueur
        if entry in Root.ListeJoueurs:
            self.message["text"] = f"Le joueur {entry} existe déjà."
        else:
            ### Ajout d'un joueur
            Root.ListeJoueurs.append(entry)
            self.message["text"] = f"Le joueur {entry} a été ajouté."
            self.ligne_texte.delete(0, tk.END)
            
            ### Chaque joueur correspond à une instance de la class cl.Joueur
            Root.Joueurs_obj = [cl.Joueur(k) for k in Root.ListeJoueurs]
            
    
    def affiche_joueur(self, event=None):
        """
        Vérifie qu'il y a au moins 3 joueurs.
        Remplace les Widgets précédents par un Label listant les joueurs qui 
        ont été ajoutés

        Parameters
        ----------
        event : TYPE, optional

        Returns
        -------
        None.

        """
        if len(Root.ListeJoueurs) < 3:
            self.message["text"] = "Le jeu se joue à 3 minimum, rajoutez des joueurs."
            self.Liste_labels.append(self.message)
            return
        
        else:
            self.destroy()
            self.update()
            
            Quel_joueur_commence()
            Score_window()
        
        
    def fin_inscriptions(self, event=None):
        """
        Permet de clear les Widgets précédents et de passer 
        au nouveau Widget "Quel_joueur_commence"

        Parameters
        ----------
        event : TYPE, optional

        Returns
        -------
        None.

        """
        self.destroy()
        self.update()
        
        Quel_joueur_commence()
        Score_window()
        
        
        
        
class Quel_joueur_commence(tk.LabelFrame):
    """
    Permet de déterminer le joueur qui va commencer.
    
    Parameters
    ----------
    Liste_labels : [tkinter.Label]
        Contient des widgets Label
    Liste_boutons : [tkinter.Button]
        Contient des widgets Button
    Premier_jet : {keys = nom des joueurs, values = score de leur premier jet}
        Contient le premier jet de dé qui va déterminer qui commence. 
        key    : nom des joueurs
        values : score
    Iterateur : int
        ???
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
        tk.LabelFrame.__init__(self)
        self.place( x = 10, y = 10, width = 1000, height = 600)
        
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
        Alimente Premier_jet avec le nom des joueurs et leur score de dé
        Appelle la fonction is_tie()

        Returns
        -------
        None.

        """
        ### Lancé du premier dé et stockage dans {Premier_jet}
        self.Premier_jet[Root.Joueurs_obj[self.Iterateur].nom] = rd.randint(1, 1000)
        
        
        self.liste_labels[self.Iterateur]["text"] = f"{Root.Joueurs_obj[self.Iterateur].nom} a fait {self.Premier_jet[Root.Joueurs_obj[self.Iterateur].nom]} !"
        self.liste_boutons[self.Iterateur]["state"] = 'disable'
        
        self.Iterateur += 1
        
        if self.Iterateur == len(Root.Joueurs_obj):
            self.bouton_suivant = tk.Button(self, text="Suivant", command=self.est_ce_que_egalite)
            self.bouton_suivant.place(relx=0.46, rely=0.4)
            self.Liste_boutons.append(self.bouton_suivant)




    def est_ce_que_egalite(self):
        """
        Détermine s'il y a une égalité dans les scores
        Si oui : annonce les joueurs ayant le plus petit score et appelle there_is_tie()
        Si non : annonce le joueur qui commence et clear la Frame

        Returns
        -------
        None.

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
            self.message_firstplayer = tk.Label(self, text=f"{Root.Firstplayer} commence en premier !")
            self.message_firstplayer.place(x=400, y=280)
            self.Liste_labels.append(self.message_firstplayer)
            
            ordre = lambda :[aut.clear_widget(self.Liste_labels, self.Liste_boutons), ReOrganize()]
            self.bouton_fin = tk.Button(self, text='Commencer le jeu', command=ordre)
            self.bouton_fin.place(x=405, y=300)
            self.Liste_boutons.append(self.bouton_fin)


    def egalite(self):
        """
        Gere l'égalité
        Appelle est_ce_que_egalite() pour boucler si l'égalité persiste

        Returns
        -------
        None.

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
    """
    Permet de réorganiser [Joueurs_obj] afin que 'Firstplayer' commence en premier
    Lance le début du jeu
    
    """
    def __init__(self):
        """
        Initialisation du constructeur
        
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
    
    Parameters
    ----------
    Liste_labels : [tkinter.Label]
        Contient des widgets Label
    Liste_boutons : [tkinter.Button]
        Contient des widgets Button
    It : int
        ???
    
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

        Returns
        -------
        None.

        """
        if cls.It == len(Root.Joueurs_obj)-1:
            cls.It = -1
        cls.It +=1
        
        
    def poursuivre(self):
        """
        Créé un bouton "Suivant" pour lancer la prochaine class qui va gérer 
        les règles du CDC

        Returns
        -------
        None.

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
    Class qui va gérer les règles du CDC en fonction des combinaisons après 
    avoir lancer les dés.
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
        chouette_1 = Root.Joueur_en_cours.Chouette_1
        chouette_2 = Root.Joueur_en_cours.Chouette_2
        cul = Root.Joueur_en_cours.Cul
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
        self.after(15000, self.call_citation)
            
            

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