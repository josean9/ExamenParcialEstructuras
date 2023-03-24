class libro(): #Creamos la clase libro
    def __init__(self, titulo, autor, paginas): #Constructor de la clase
        self.titulo = titulo #Atributos de la clase
        self.autor = autor
        self.paginas = paginas

    def __str__(self): #Metodo para imprimir los atributos de la clase
        return "Titulo: " + self.titulo + ", Autor: " + self.autor + ", Paginas: " + str(self.paginas)

    def __len__(self): #Metodo para imprimir el numero de paginas
        return self.paginas

    def eliminarLibro(self): #Metodo para eliminar el libro
        print("Libro borrado")
libro1 = libro("El principito", "Antoine de Saint-Exupéry", 200) #Creamos un objeto de la clase libro 
print(libro1) #Imprimimos el objeto gracias al metodo __str__
