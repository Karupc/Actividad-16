class Libros:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    def mostrar_libros(self):
        print(f"Título: {self.titulo}\n"
              f"Autor: {self.autor}\n"
              f"Año de publicación: {self.anio}")
lista_libros = []
libro = []
def agregar_libros():
    try:
        titulo = input("Ingresar el título del libro: ")
        autor = input("Ingresar el autor del libro: ")
        anio = int(input("Ingresar el año de publicación: "))
        libro.append(titulo, autor, anio)
        lista_libros.append(libro)
    except ValueError:
        print("Error: El año debe ser un número entero.\n")
def mostrar_libros():

while True:
    print("---BIBLIOTECA---\n"
          "1.- Agregar libros\n"
          "2.- Mostrar la lista de libros\n"
          "3.- Eliminar libros por títulos\n"
          "4.- Salir del programa\n")
    opciones = input("Escriba el número de la opción que desea seleccionar: ")
    print("\n")
    match opciones:
        case "1":
            print("---AGREGAR LIBROS---")
            agregar_libros()
        case "2":
            print("---MOSTRAR LA LISTA DE LIBROS---")
