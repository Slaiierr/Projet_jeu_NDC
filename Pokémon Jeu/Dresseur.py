class Dresseur:

    def __init__(self, Nom: str, xp=0, particularite=""):

        self.nom = Nom
        self.__experience = xp
        self.particularite = particularite

### MUTATEURS ###
    def set_experience(self, value):
        self.__xp += value


### ACCESSEURS ###

    def get_experience(self):
        return self.__experience


### JEU ###

    def __str__(self):
        return (str(self.nom) + " est au niveau " + str(self.get_experience()) + ". Particularité : " + str(self.particularite))


sacha = Dresseur("Sacha", 0, "Super Fort")
print(sacha)
