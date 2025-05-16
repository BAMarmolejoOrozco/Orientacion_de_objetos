class Computadora:
    def __init__(self, nombre, ram, procesador, grafica):
        self.nombre = nombre
        self.ram = ram
        self.procesador = procesador
        self.grafica = grafica

    def Caracteristicas(self):
        print(f"El pc ideal para ti se llama {self.nombre} y cuenta con {self.ram} de ram {self.procesador} procesador y {self.grafica} de grafica")
        
pc1 = Computadora("predator", 16, "Ryzen 5 5600g", 32)
pc1.Caracteristicas()