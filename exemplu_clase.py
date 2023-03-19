import random

nume = ["Ionescu", "Munteanu", "Toth", "Kiss", "Schmidt", "Smith"]
prenume = ["Ion", "Andrei", "David", "Vlad", "Robert", "Mihai"]
clase = [7,8,9,10,11,12]
scoli = ["Scoala Balcescu", "Scoala Dacia", "Scoala Oltea Doamna", "Liceul Emanuil Gojdu", "Liceul Mihai Eminscu", "Scoala Generala 16"]

elevi =[]

class Elev:
    def __init__(self):
        self.nume = None
        self.varsta = None
        self.clasa = None
        self.scoala = None
        self.catalog = Catalog()

    def identificare(self):
        print("Sunt {}, elev in clasa {} la {}".format(self.nume, self.clasa, self.scoala))

    def getNume(self):
        return self.nume

    def setNume(self, nume):
        self.nume = nume

    def getVarsta(self):
        return self.varsta

    def setVarsta(self, varsta):
        self.varsta = varsta

    def getClasa(self):
        return self.clasa
    
    def setClasa(self, clasa):
        self.clasa = clasa

    def getScoala(self):
        return self.scoala

    def setScoala(self, scoala):
        self.scoala =scoala


class Catalog:
    def __init__(self):
        self.romana = []
        self.matematica = []
        self.engleza = []
        self.fizica = []
        self.informatica = []    

for i in range(30):
    elevi.append(Elev())
    elevi[i].setNume("{} {}".format(random.choice(nume), random.choice(prenume)))

for i in range(30):
    print(elevi[i].getNume())
