class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado_a = None  # Guarda el usuario que tiene el libro (None si está disponible)

    def prestar_a(self, usuario):
        if self.prestado_a is None:
            self.prestado_a = usuario
            usuario.libros_prestados.append(self)
            print(f"El libro '{self.titulo}' ha sido prestado a {usuario.nombre}.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado a {self.prestado_a.nombre}.")

    def devolver(self):
        if self.prestado_a is not None:
            usuario = self.prestado_a
            self.prestado_a = None
            usuario.libros_prestados.remove(self)
            print(f"El libro '{self.titulo}' ha sido devuelto por {usuario.nombre}.")
        else:
            print(f"El libro '{self.titulo}' no está prestado.")

    def mostrar_estado(self):
        if self.prestado_a:
            print(f"'{self.titulo}' está prestado a {self.prestado_a.nombre}.")
        else:
            print(f"'{self.titulo}' está disponible.")


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        libro.prestar_a(self)

    def devolver_libro(self, libro):
        libro.devolver()

    def mostrar_libros(self):
        if self.libros_prestados:
            print(f"{self.nombre} tiene los siguientes libros prestados:")
            for libro in self.libros_prestados:
                print(f" - {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene libros prestados.")

libro1 = Libro("El principe Lestat", "Anne Rice")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")

usuario1 = Usuario("Antonio")
usuario2 = Usuario("Luisa")

usuario1.tomar_prestado(libro1)
usuario2.tomar_prestado(libro2)

usuario1.mostrar_libros()
libro1.mostrar_estado()

usuario1.devolver_libro(libro1)
usuario2.tomar_prestado(libro2)

libro1.mostrar_estado()
usuario2.mostrar_libros()