class Libros:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    def mostrar_libros(self):
        print(f"Título: {self.titulo}\n"
              f"Autor: {self.autor}\n"
              f"Año de publicación: {self.anio}")
