class Computadora:
    def __init__(self, nombre, ram, procesador, grafica):
        self.nombre = nombre
        self.ram = ram
        self.procesador = procesador
        self.grafica = grafica
        self.encendido = False  

    def Caracteristicas(self):
        print(f"El pc ideal para ti se llama {self.nombre} y cuenta con {self.ram} de ram {self.procesador} procesador y {self.grafica} de grafica")

    def encender(self):  
        if not self.encendido:  
            self.encendido = True
            print(f"La computadora {self.nombre} está encendida.")  
        else:
            print("La computadora ya está encendida")  

    def apagar(self):  
        if self.encendido:  
            self.encendido = False
            print(f"La computadora {self.nombre} está apagada.")  
        else:
            print("Esta computadora ya está apagada.")  

    def actualizar_ram(self, nueva_ram):  
        if not self.encendido:  
            print("Por favor, encienda la computadora antes de actualizar la RAM para evitar daños o bugs en la RAM.")
            return
        if nueva_ram > self.ram:
            print(f"Actualizando RAM de {self.ram}GB a {nueva_ram}GB.")
            self.ram = nueva_ram
        else:
            print("La nueva RAM debe ser mayor que la actual.")

pc1 = Computadora("predator", 16, "Ryzen 5 5600g", 32)


pc1.Caracteristicas()
pc1.encender()  
pc1.actualizar_ram(32)
pc1.apagar()

