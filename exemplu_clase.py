import random

nume = ["Ionescu", "Munteanu", "Toth", "Kiss", "Schmidt", "Smith"]
prenume = ["Ion", "Andrei", "David", "Vlad", "Robert", "Mihai"]
varste = range(13, 19, 1)
clase = [7,8,9,10,11,12]
scoli = ["Scoala Balcescu", "Scoala Dacia", "Scoala Oltea Doamna", "Liceul Emanuil Gojdu", "Liceul Mihai Eminscu", "Scoala Generala 16"]

discipline = ["romana", "matematica", "engleza", "fizica", "informatica"]

elevi =[]

class Elev:
    def __init__(self):
        self.nume = None
        self.varsta = None
        self.clasa = None
        self.scoala = None
        self.catalog = Catalog()

    def identificare(self):
        return "{}, {} ani, in clasa {} la {}".format(self.nume, self.varsta, self.clasa, self.scoala)

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

    def addRomana(self, nota):
        self.romana.append(nota)

    def addMatematica(self, nota):
        self.matematica.append(nota)

    def addFizica(self, nota):
        self.fizica.append(nota)

    def addEngleza(self, nota):
        self.engleza.append(nota)

    def addInfo(self, nota):
        self.informatica.append(nota)

    def getMedieRomana(self):
        if self.romana != None:
            sum = 0
            for k in range(len(self.romana)):
                sum += self.romana[k]
            medie = sum/len(self.romana)
            return medie
        return "Nu are note la Limba Romana"

for i in range(30):
    elevi.append(Elev())
    elevi[i].setNume("{} {}".format(random.choice(nume), random.choice(prenume)))
    elevi[i].setVarsta(random.choice(varste))
    elevi[i].setClasa(random.choice(clase))
    elevi[i].setScoala(random.choice(scoli))

for i in range(30):
    for j in range(random.randrange(3,7)):
        elevi[i].catalog.addRomana(random.randrange(4,11))

# for i in range(30):
#     print(elevi[i].catalog.romana)

print(elevi[13].catalog.romana)
print(elevi[13].catalog.getMedieRomana())
