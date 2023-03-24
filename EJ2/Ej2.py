class Animal():
    def __init__(self, nombre, edad, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad}"

    def __repr__(self):
        return f"Edad: {self.nombre} Edad: {self.edad}"
class Mamifero(Animal):
    def __init__(self, nombre, edad, altura, peso, tipo):
        super().__init__(nombre, edad, altura, peso)
        self.tipo = tipo

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

    def __repr__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"
class Oviparo(Animal):
    def __init__(self, nombre, edad, altura, peso, tipo):
        super().__init__(nombre, edad, altura, peso)
        self.tipo = tipo

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

    def __repr__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"
class Pollo(Oviparo):
    def __init__(self, nombre, edad, altura, peso, tipo, ruido):
        super().__init__(nombre, edad, altura, peso, tipo)
        self.ruido = ruido
        ruido = "Pio Pio"

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

    def __repr__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"
    def hacer_ruido(self):
        print(self.ruido)
class Gato(Mamifero):
    def __init__(self, nombre, edad, altura, peso, tipo, ruido):
        super().__init__(nombre, edad, altura, peso, tipo)
        self.ruido = ruido
        ruido = "Miau Miau"

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

    def __repr__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"
    def hacer_ruido(self):
        print(self.ruido)
class Ormitorrinco(Oviparo):
    def __init__(self, nombre, edad, altura, peso, tipo, ruido):
        super().__init__(nombre, edad, altura, peso, tipo)
        self.ruido = ruido
        ruido = "No hace ruido"

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"

    def __repr__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Tipo: {self.tipo}"
    def hacer_ruido(self):
        print(self.ruido)