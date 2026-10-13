class animal:
    def __init__(self,nombre,edad,peso):

        self.nombre=nombre
        self.edad=edad
        self.peso=peso

    def mostrar_datos(self):
        print("nombre:",self.nombre)
        print("edad:",self.edad)
        print("peso:",self.peso)

    def comer(self):
        print(self.nombre,"el animal esta comiendo concentrado",self.edad)

class perro(animal):
    def __init__(self,nombre,edad,peso,raza):
        super().__init__(nombre,edad,peso)
        self.raza=raza

    def ladrar(self):
        print("el perro esta ladrando")

class gato(animal):
    def __init__(self,nombre,edad,peso,color):
        super().__init__(nombre,edad,peso)
        self.color=color

    def maullar(self):
        print("el gato esta maullando:miau miau")

    def correr(self):
        print("el gato esta corriendo en la sala",self.color)

class ave(animal):
    def __init__(self,nombre,edad,peso,especie):
        super().__init__(nombre,edad,peso)
        self.especie=especie

    def volar(self):
        print("la paloma esta volando:",self.nombre)

    def cantar(self):
        print(self.nombre,"el ave esta cantando en el patio",self.especie)

class pato(animal):
    def __init__(self,nombre,edad,peso,patas):
        super().__init__(nombre,edad,peso)
        self.patas=patas

    def nadar(self):
        print("el pato esta nadando")

    def graznar(self):
        print(self.edad,"el pato hace cuac cuac",self.patas)

perro1=perro("luna",3,"23kg","pitbull")
perro1.ladrar()

perro2=perro("max",6,"45kg","doberman")
perro2.comer()

gato1=gato("mishi",8,"10kg","negro")
gato1.maullar()

gato2=gato("nube",5,"20kg","blanco")
gato2.correr()

ave1=ave("paco",9,"12kg","paloma")
ave1.volar()

ave2=ave("kiwi",4,"23kg","buho")
ave2.cantar()

pato1=pato("copo",6,"34kg",4)
pato1.nadar()

pato2=pato("nieve",7,"15kg",7)
pato2.graznar()

    
