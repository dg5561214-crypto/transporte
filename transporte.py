class vehiculo:
    def __init__(self,marca,modelo,velocidad):
        
        self.modelo=modelo
        self.velocidad=velocidad
        self.marca=marca

    def mostrar_informacion(self):
        print("marca:",self.marca)  
        print("modelo:",self.modelo)
        print("velocidad:",self.velocidad)

    def acelerar(self):
        self.velocidad +=8
        print("el vehiculo acelero")

class automovil:
    def __init__(self,numero_puertas):
        self.numero_puertas=numero_puertas

    def tocar_bocina(self):
        print("la bocina esta sonando")

class motocicleta:
    def __init__(self,color):
        self.color=color

    def acelerar(self):
        print("la motocicleta esta acelerando")



vehiculo700 = vehiculo("toyota", "lexus", 50)
vehiculo700.mostrar_informacion()


automvil_repollo = automovil(4)
automvil_repollo.tocar_bocina()


