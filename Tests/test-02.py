import pyxel
import random


class Jeu:
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        pyxel.init(128, 128, title="Nuit du c0de")

        # position initiale du vaisseau
        self.vaisseau_x = 60
        self.vaisseau_y = 60

        self.ennemis_liste = []

        self.vies = 4

        pyxel.run(self.update, self.draw)

    def vaisseau_deplacement(self):
        """déplacement avec les touches de directions"""

        if pyxel.btn(pyxel.KEY_D) and self.vaisseau_x < 120:
            self.vaisseau_x += 1
        if pyxel.btn(pyxel.KEY_Q) and self.vaisseau_x > 0:
            self.vaisseau_x += -1
        if pyxel.btn(pyxel.KEY_S) and self.vaisseau_y < 120:
            self.vaisseau_y += 1
        if pyxel.btn(pyxel.KEY_Z) and self.vaisseau_y > 0:
            self.vaisseau_y += -1

    def ennemis_creation(self):
        """création aléatoire des ennemis"""
        # un ennemi par seconde
        if (pyxel.frame_count % 30 == 0):
            self.ennemis_liste.append([random.randint(0, 120), 0])

    def ennemis_deplacement(self):
        """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""
        for ennemi in self.ennemis_liste:
            ennemi[1] += 1
            if ennemi[1] > 128:
                self.ennemis_liste.remove(ennemi)

    def vaisseau_suppression(self):
        """disparition du vaisseau et d'un ennemi si contact"""

        for ennemi in self.ennemis_liste:
            if ennemi[0] <= self.vaisseau_x+8 and ennemi[1] <= self.vaisseau_y+8 and ennemi[0]+8 >= self.vaisseau_x and ennemi[1]+8 >= self.vaisseau_y:
                self.ennemis_liste.remove(ennemi)
                self.vies -= 1

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du vaisseau
        self.vaisseau_deplacement()

        # ennemis création + déplacements
        self.ennemis_creation()
        self.ennemis_deplacement()

        self.vaisseau_suppression()

    # =====================================================
    # == DRAW
    # =====================================================

    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""
        # affiche vies
        pyxel.text(0, 0, 'Vies: ' + str(self.vies), 7)
        # si le vaisseau possede des vies le jeu continue
        if self.vies > 0:

            # vaisseau (carre 8x8)
            pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)

            # ennemis
            for ennemi in self.ennemis_liste:
                pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)

        # sinon: GAME OVER
        else:

            pyxel.text(50, 64, 'GAME OVER', 7)


Jeu()
