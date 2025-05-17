class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrar_info(self):
        estado = "Prestado" if self.prestado else "Disponible"
        print(f"Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}")

libro1 = Libro("Entrevista con el vampiro", "Anne Rice")
libro1.mostrar_info()
libro1.prestar()
libro1.mostrar_info()
libro1.prestar()
libro1.devolver()
libro1.mostrar_info()