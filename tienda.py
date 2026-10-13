class producto:
    def __init__(self,nombre,precio,codigo):

        self.nombre=nombre
        self.precio=precio
        self.codigo=codigo

    def mostrar_producto(self):
        print("nombre:",self.nombre)
        print("precio:",self.precio)
        print("codigo:",self.codigo)

    def calcular_precio(self):
        return self.calcular_precio
        

class producto_electronico(producto):
    def __init__(self, nombre, precio, codigo,garantia):
        super().__init__(nombre, precio, codigo)
        self.garantia=garantia

    def mostrar_garantia(self):
        print("garantia:",self.garantia)

class producto_alimenticio(producto):
    def __init__(self, nombre, precio, codigo,fecha_vencimiento):
        super().__init__(nombre, precio, codigo)
        self.fecha_vencimiento=fecha_vencimiento

    def verificar_vencimiento(self):
        from datetime import datetime
        fecha=datetime.strptime("14-09-2026", "%d-%m-%Y")
        hoy=datetime.today()
        if fecha < hoy:
            print("esta vencido")
        else:
            print("no esta vencido")

class ropa(producto):
    def __init__(self, nombre, precio, codigo,talla):
        super().__init__(nombre, precio, codigo)
        self.talla=talla

    def cambiar_talla(self,nueva_talla):
        self.nueva_talla=nueva_talla
        print("nueva talla:",self.talla)

#crear objetos
computador=producto_electronico("portatil HP",2500000,"ELE001","12 meses")
computador.mostrar_garantia()

celular=producto_electronico("samsung A54",1800000,"ELE002","12 meses")
celular.mostrar_producto()

leche=producto_alimenticio("leche alpina",4500,"ALI001","14-09-2026")
leche.verificar_vencimiento()


