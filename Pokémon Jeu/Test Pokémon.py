from random import *


class Pokemon:

    def __init__(self, Nom: str = "Anonyme",
                 Typ=choice(["eau", "air", "terre", "feu"]),
                 Vitesse=randint(1, 51),
                 Attaque=randint(51, 100),
                 Defense=randint(1, 50),
                 PvMax=randint(101, 150),
                 rea=0,
                 xp=0):

        self.nom = Nom
        self.type = Typ
        self.pts_vitesse = Vitesse
        self.pts_attaque = Attaque
        self.pts_defense = Defense
        self.pvMax = PvMax
        self.pvActuels = PvMax
        self.__compteur_rea = rea
        self.experience = xp


### ACCESSEURS ###


    def set_compteur_rea(self, valeur):
        self.__compteur_rea += valeur

    # def get_type(self):
    #     return self.__type

    # def get_pts_vitesse(self):
    #     return self.__pts_vitesse

    # def get_pts_attaque(self):
    #     return self.__pts_attaque

    # def get_pts_defense(self):
    #     return self.__pts_defense / 100

    # def get_pvMax(self):
    #     return self.__pvMax

    # def get_pvActuels(self):
    #     return self.__pvActuels


### JEU ###


    def __str__(self):
        """Indique si le pokémon est ko, sinon, ses stats"""
        if self.ko() == True:
            return (str(self.nom) + " est KO. Ammène le en soin pour le réanimer.")
        return (str(self.nom) + " -> pv actuels " + str(self.pvActuels) + ", attaque : " + str(self.pts_attaque) + ", défense : " + str(self.pts_defense) + ", vitesse : " + str(self.pts_vitesse))

    def fiche_pokemon(self):
        """Donne la fiche complète du pokémon"""
        return ("Ce pokémon s'appelle " + str(self.nom) + ", il est de type " + str(self.type) + ". Voici ses stats : " + ("pv actuels " + str(self.pvActuels) + ", attaque : " + str(self.pts_attaque) + ", défense : " + str(self.pts_defense) + ", vitesse : " + str(self.pts_vitesse) + ", il a été réanimé " + str(self.__compteur_rea) + " fois et il a " + str(self.experience) + " XP !"))

    def attaque(self, pokemonAdverse):
        """Permet aux pokémon d'attaquer un autre pokémon"""
        pokemonAdverse.pvActuels -= (self.pts_attaque - self.pts_attaque *
                                     pokemonAdverse.pts_defense / 100)

    def repos(self):
        """Permet au pokémon de se soigner de 20% """
        if self.ko() == True:
            return (str(self.nom) + " est KO. Ammène le en soin pour le réanimer.")
        else:
            if self.pvActuels <= self.pvMax * 0.2:
                self.pvActuels += self.pvMax * 0.2
            elif self.pvActuels > self.pvMax * 0.2 and self.pvActuels < self.pvMax:
                self.pvActuels = self.pvMax

    def reanimation(self):
        self.pvActuels = self.pvMax
        self.set_compteur_rea(1)
        return "Votre pokémon à été réanimé, il a toute sa vie."

    def ko(self):
        """Return True lorsque le pokémon est ko. C'est a dire que ses pv tombent à 0"""
        if self.pvActuels <= 0:
            return True
        return False


pic = Pokemon("Pic", "feu", 1, 100, 50, 100)
dracaufeu = Pokemon("Dracaufeu", "feu", 1, 50, 50, 100)

print(dracaufeu.fiche_pokemon)
