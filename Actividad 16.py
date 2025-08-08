class Libros:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    def mostrar_lib(self):
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
        libro = Libros(titulo, autor, anio)
        lista_libros.append(libro)
        print("")
    except ValueError:
        print("Error: El año debe ser un número entero.\n")
def mostrar_libros():
    if not lista_libros:
        print("No hay libros registrados.\n")
    else:
        print("--- Lista de libros ---")
        for i, libro in enumerate(lista_libros, start=1):
            print(f"{i}.- ", end="")
            libro.mostrar_lib()
print("")
def eliminar_libro():
    libro_buscado = input("Ingresa el título del libro que desea eliminar: ")
    encontrado = False
    for libro in lista_libros:
        if libro.titulo.lower() == libro_buscado.lower():
            lista_libros.remove(libro)
            print("Libro eliminado\n")
            encontrado = True
        if not encontrado:
            print("El libro no fue encontrado\n")
print("\n")
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
            mostrar_libros()
        case "3":
            print("---ELIMINAR LIBRO POR TÍTULO---")
            eliminar_libro()
        case "4":
            print("Programa terminado, gracias por utilizarlo")
