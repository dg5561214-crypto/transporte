class persona:
    def __init__(self,nombre,documento,edad):

        self.nombre=nombre
        self.documento=documento
        self.edad=edad

    def mostrar_datos(self):
        print("nombre:",self.nombre)
        print("documento:",self.documento)
        print("edad:",self.edad)

    def presentarse(self):
        print("hola soy:", self.nombre)

class aprendiz(persona):
    def __init__(self,nombre,documento,edad,ficha_formacion):
        super().__init__(nombre,documento,edad)
        self.ficha_formacion=ficha_formacion

    def estudiar(self):
        print(self.nombre,"el aprendiz esta estudian base datos",self.ficha_formacion)

class instructor(persona):
    def __init__(self,nombre,documento,edad,especialidad):
        super().__init__(nombre,documento,edad)
        self.especialidad=especialidad

    def orientar_formacion(self):
        print("esta orientando la formacion",self.nombre)

class coordinador(persona):
    def __init__(self,nombre,documento,edad,area):
        super().__init__(nombre,documento,edad)
        self.area=area

    def coordinar(self):
        print(self.nombre,"esta cordinando el sistema",self.area)

aprendiz1=aprendiz("laura",1012345678,17,2876101)
aprendiz1.estudiar()

instructor1=instructor("diego",86065705,45,"desarrollo de software")
instructor1.orientar_formacion()
    
