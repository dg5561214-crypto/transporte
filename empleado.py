class empleado:
    def __init__(self,nombre,identificacion,salario):

        self.nombre=nombre
        self.identificacion=identificacion
        self.salario=salario

    def mostrar_datos(self):
        print("nombre:",self.nombre)
        print("identificacion:",self.identificacion)
        print("salario:",self.salario)

    def trabajar(self):
        print(self.nombre,"esta trabajando como",self.puesto)

class desarrollador(empleado):
    def __init__(self, nombre, identificacion, salario,lenguaje_programacion):
        super().__init__(nombre, identificacion, salario)
        self.lenguaje_programacion=lenguaje_programacion

    def programar(self):
        print("esta programando en python")

class diseñador(empleado):
    def __init__(self, nombre, identificacion, salario,herramienta_diseño):
        super().__init__(nombre, identificacion, salario)
        self.herramienta_diseño=herramienta_diseño

    def diseñar(self):
        print("el empleado esta diseñando")

class instructor(empleado):
    def __init__(self, nombre, identificacion, salario,especialidad):
        super().__init__(nombre, identificacion, salario)
        self.especialidad=especialidad

    def orientar_formacion(self):
        print("el empleado esta orientando la formacion de los empleados")

empleado1=empleado("maria",234456,188895989898)
empleado1.mostrar_datos()

desarrollador1=desarrollador("juan",12345,3000000,"python")
desarrollador1.programar()

diseñador1=diseñador("ana",67890,2800000,"figma")
diseñador1.diseñar()


