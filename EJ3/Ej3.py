from Decoradores import *
class CuentaBancaria(): #Creamos la clase CuentaBancaria
    def __init__(self, nombre, saldo, Id, NumeroCuenta, FechaApertura):
        self.nombre = nombre
        self.saldo = saldo
        self.Id = Id
        self.NumeroCuenta = NumeroCuenta
        self.FechaApertura = FechaApertura
    @decoradorTransferencia
    def depositar(self, cantidad): #Metodo para depositar dinero
        self.saldo += cantidad
    @decoradorRetirada
    def retirar(self, cantidad): #Metodo para retirar dinero
        if cantidad > self.saldo: #Si la cantidad a retirar es mayor al saldo
            print("No se puede retirar mas dinero del que se tiene") 
        else: #Si no
            self.saldo -= cantidad
    @decoradorTransferencia
    def transferir(cuentaDeLaQueSeRetira, cuentaDeLaQueSeDeposita, cantidad): #Metodo para transferir dinero de una cuenta a otra
        if cantidad > cuentaDeLaQueSeRetira.saldo:
            print("No se puede retirar mas dinero del que se tiene")
        else:
            cuentaDeLaQueSeRetira.saldo -= cantidad
            cuentaDeLaQueSeDeposita.saldo += cantidad
    def transeferirMain(): #Metodo para transferir dinero de una cuenta a otra
        cuenta1 = input("Ingrese el nombre de la cuenta de la que se va a retirar: ")
        cuenta2 = input("Ingrese el nombre de la cuenta de la que se va a depositar: ")
        cantidad = int(input("Ingrese la cantidad a transferir: "))
        CuentaBancaria.transferir(cuenta1, cuenta2, cantidad)
    def __str__(self): #Metodo para imprimir los atributos de la clase
        return "Cuenta de {} con un saldo de {}".format(self.nombre, self.saldo)
class CuentaPlazoFijo(CuentaBancaria): #Creamos la clase CuentaPlazoFijo
    def __init__(self, nombre, saldo, Id, NumeroCuenta, FechaApertura, FechaVencimiento, Interes):
        super().__init__(nombre, saldo, Id, NumeroCuenta, FechaApertura) #Llamada al constructor de la clase padre
        self.FechaVencimiento = FechaVencimiento #Atributos de la clase hija
        self.Interes = int(Interes)
    @decoradorRetirada
    def retirar(self, cantidad): #Metodo para retirar dinero con un cierto interes
        if cantidad+cantidad*self.Interes/100 > self.saldo:
            print("No se puede retirar mas dinero del que se tiene")
        else:
            self.saldo -= cantidad+cantidad*self.Interes/100
    @decoradorTransferencia
    def depositar(self, cantidad):
        return super().depositar(cantidad)
    def __str__(self):
        return "Cuenta de {} con un saldo de {} y un interes de {}".format(self.nombre, self.saldo, self.Interes)
class CuentaVip(CuentaBancaria): #Creamos la clase CuentaVip
    def __init__(self, nombre, saldo, Id, NumeroCuenta, FechaApertura, Descubierto):
        super().__init__(nombre, saldo, Id, NumeroCuenta, FechaApertura) #Llamada al constructor de la clase padre
        self.Descubierto = Descubierto #Atributos de la clase hija
    @decoradorRetirada
    def retirar(self, cantidad): #Metodo para retirar dinero con un cierto descubierto
        if cantidad > self.saldo+self.Descubierto:
            print("No se puede retirar mas dinero del que se tiene")
        else:
            self.saldo -= cantidad
    @decoradorTransferencia
    def depositar(self, cantidad):
        return super().depositar(cantidad)
    def __str__(self):
        return "Cuenta de {} con un saldo de {} y un descubierto de {}".format(self.nombre, self.saldo, self.Descubierto)