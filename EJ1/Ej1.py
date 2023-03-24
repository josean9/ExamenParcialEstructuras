class libro():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return "Titulo: " + self.titulo + ", Autor: " + self.autor + ", Paginas: " + str(self.paginas)

    def __len__(self):
        return self.paginas

    def __del__(self):
        print("Libro borrado")