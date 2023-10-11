import pyxel

class Jeu:
    def __init__(self, vies=4):
        # taille de la fenetre 128x128 pixels
        pyxel.init(128, 128, title="Nuit du c0de")

        # position initiale du vaisseau
        self.vaisseau_x = 60
        self.vaisseau_y = 60
        
        self.vies = vies

        pyxel.run(self.update, self.draw)

    def vaisseau_deplacement(self):
        if pyxel.btn(pyxel.KEY_D) and self.vaisseau_x > 0 and self.vaisseau_x < 120:
            self.vaisseau_x += 1
        if pyxel.btn(pyxel.KEY_Q) and self.vaisseau_x > 0 and self.vaisseau_x < 120:
            self.vaisseau_x -= 1
        if pyxel.btn(pyxel.KEY_Z) and self.vaisseau_y > 0 and self.vaisseau_y < 120:
            self.vaisseau_y += 1
        if pyxel.btn(pyxel.KEY_S) and self.vaisseau_y > 0 and self.vaisseau_y < 120:
            self.vaisseau_y += 1

    def vies(self):
        if self.vaisseau_x == 0 or self.vaisseau_x == 120 or self.vaisseau_y == 0 or self.vaisseau_y == 120:
            self.vies -= 1


    def update(self):

        #déplacements du vaisseau
        self.vaisseau_deplacement()
        
        #système de vies
        self.vies()
        
    def draw(self):

        # vide la fenetre
        pyxel.cls(0)

        # vaisseau (carre 8x8)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)


Jeu()