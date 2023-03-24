class Animal():
    def __init__(self, nombre, edad, altura, peso): #Creador de la clase padre con sus atributos
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def __str__(self): #Metodo para imprimir los atributos de la clase padre
        return f"Nombre: {self.nombre} Edad: {self.edad}"

   
class Mamifero(Animal):
    def __init__(self, nombre, edad, altura, peso, tipo):
        super().__init__(nombre, edad, altura, peso) #Llamada al constructor de la clase padre
        self.tipo = tipo #Atributo propio de la clase

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

    
class Oviparo(Animal):
    def __init__(self, nombre, edad, altura, peso, tipo):
        super().__init__(nombre, edad, altura, peso)
        self.tipo = tipo

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

 
class Pollo(Oviparo):
    def __init__(self, nombre, edad, altura, peso, tipo, ruido="Pio Pio"):
        super().__init__(nombre, edad, altura, peso, tipo)
        self.ruido = ruido #Atributo propio de la clase

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

 
    def hacer_ruido(self): #Metodo propio de la clase
        print(self.ruido)
class Gato(Mamifero):
    def __init__(self, nombre, edad, altura, peso, tipo, ruido="Miau Miau"):
        super().__init__(nombre, edad, altura, peso, tipo)
        self.ruido = ruido
        

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

    def hacer_ruido(self):
        print(self.ruido)
class Ormitorrinco(Oviparo):
    def __init__(self, nombre, edad, altura, peso, tipo, ruido="No hace ruido"):
        super().__init__(nombre, edad, altura, peso, tipo)
        self.ruido = ruido
        self.ruido = "No hace ruido"

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"


    def hacer_ruido(self):
        return(self.ruido)
gato1 = Gato("Gato", 2, 0.5, 5, "Mamifero") #Creacion de un objeto de la clase Gato 
print(gato1.hacer_ruido()) #Llamada al metodo hacer_ruido de la clase Gato