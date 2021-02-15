#Importation des modules pour les nbrs aléatoire et time permet de stoper le prog qq seconde
#Manque encore le fait de gérer les scores, je les ajouterais.
import random
import time


#Initilisation de la classe sorcier
#Le sorcier débute avec 100point de vie et 10 point d'attaque et posséde 5 potions.
#Erreur qui ma pris du temps, Soluce :
#random.unifrom permet d'avoir un nombre aléatoire entre deux valeur à virgules
#Pour avoir une décimal il faut utiliser round pour préciser la limite de nombres "flottants"
class Sorcier():
    pv = 100
    pa = 10
    NbrPotion = 5
    def BoisPotion(self):
        self.pv = self.pv + 15
        self.NbrPotion = self.NbrPotion - 1
    def DegatsSorcier(self):
        return self.pa * (round(random.uniform(0.1, 1),1))

#Initilisation de la classe guerrier
#Le guerrier débute avec 120point de vie et 20 point d'attaque
class Guerrier():
    pv = 120
    pa = 20
    def DegatsGuerrier(self):
        return self.pa * (round(random.uniform(0.1, 1),1))

#Démarage du combat
class Game():
    guerrier = Guerrier()
    sorcier = Sorcier()
    def launch(self):
        # Boucle du jeu 
            # Tour Guerrier
        while (Game.guerrier.pv > 0) and (Game.sorcier.pv > 0):
            print("Début du tour du guerrier")
            result = random.randint(1, 5)
            if (result == 1):
                Game.guerrier.pv = Game.guerrier.pv - Game.guerrier.DegatsGuerrier()
                print("Le Guerrier se trompe, et s'inflige lui même :", Game.guerrier.DegatsGuerrier(),"points de dégats")
                print("Le Guerrier n'a plus que :", Game.guerrier.pv, "points de vie")
            else:
                Game.sorcier.pv = Game.sorcier.pv - Game.guerrier.DegatsGuerrier()
                print("Le Guerrier inflige", Game.guerrier.DegatsGuerrier(),"points de dégats au Sorcier !")
                print("Le Sorcier n'a plus que :", Game.sorcier.pv, "points de vie")
            time.sleep(1)
            print("\n")
            
            # Tour du Sorcier
            if (Game.guerrier.pv > 0) and (Game.sorcier.pv > 0):
                result1 = random.randint(1, 2)
                if (result1 == 1):
                    if (Game.sorcier.NbrPotion > 0):
                        Game.sorcier.BoisPotion()
                        print("Le sorcier arrive à boire une potion, il va lui rester ", Game.sorcier.NbrPotion, "potion")
                        print("Le Sorcier à encore :", Game.sorcier.pv, "points de vie") Game.guerrier.pv = Game.guerrier.pv - Game.sorcier.DegatsSorcier()
                print("Le Sorcier inflige", Game.sorcier.DegatsSorcier(),"points de dégats au Guerrier !")
                print("Le Guerrier n'a plus que :", Game.guerrier.pv, "points de vie")
                time.sleep(1)
                print("\n")

