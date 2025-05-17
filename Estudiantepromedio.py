class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def Notas(self):
        Resultado = (2 + 4 + 3)/3
        print(f"El estudiante {self.nombre} tiene notas de {self.nota1} - {self.nota2} - {self.nota3} y su promedio es de ", Resultado)

        
prom = Estudiante("Luis", 2, 4, 3)
prom.Notas()