class CuentaBancaria():
    def __init__(self, nombre, saldo, Id, NumeroCuenta, FechaApertura):
        self.nombre = nombre
        self.saldo = saldo
        self.Id = Id
        self.NumeroCuenta = NumeroCuenta
        self.FechaApertura = FechaApertura

    def depositar(self, cantidad):
        self.saldo += cantidad
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No se puede retirar mas dinero del que se tiene")
        else:
            self.saldo -= cantidad
    def transferir(cuentaDeLaQueSeRetira, cuentaDeLaQueSeDeposita, cantidad):
        if cantidad > cuentaDeLaQueSeRetira.saldo:
            print("No se puede retirar mas dinero del que se tiene")
        else:
            cuentaDeLaQueSeRetira.saldo -= cantidad
            cuentaDeLaQueSeDeposita.saldo += cantidad
    def transeferirMain():
        cuenta1 = input("Ingrese el nombre de la cuenta de la que se va a retirar: ")
        cuenta2 = input("Ingrese el nombre de la cuenta de la que se va a depositar: ")
        cantidad = int(input("Ingrese la cantidad a transferir: "))
        CuentaBancaria.transferir(cuenta1, cuenta2, cantidad)
    def __str__(self):
        return "Cuenta de {} con un saldo de {}".format(self.nombre, self.saldo)
class CuentaPlazoFijo(CuentaBancaria):
    def __init__(self, nombre, saldo, Id, NumeroCuenta, FechaApertura, FechaVencimiento, Interes):
        super().__init__(nombre, saldo, Id, NumeroCuenta, FechaApertura)
        self.FechaVencimiento = FechaVencimiento
        self.Interes = int(Interes)
    def retirar(self, cantidad):
        if cantidad+cantidad*self.Interes/100 > self.saldo:
            print("No se puede retirar mas dinero del que se tiene")
        else:
            self.saldo -= cantidad+cantidad*self.Interes/100
    def __str__(self):
        return "Cuenta de {} con un saldo de {} y un interes de {}".format(self.nombre, self.saldo, self.Interes)
class CuentaVip(CuentaBancaria):
    def __init__(self, nombre, saldo, Id, NumeroCuenta, FechaApertura, Descubierto):
        super().__init__(nombre, saldo, Id, NumeroCuenta, FechaApertura)
        self.Descubierto = Descubierto
    def retirar(self, cantidad):
        if cantidad > self.saldo+self.Descubierto:
            print("No se puede retirar mas dinero del que se tiene")
        else:
            self.saldo -= cantidad
    def __str__(self):
        return "Cuenta de {} con un saldo de {} y un descubierto de {}".format(self.nombre, self.saldo, self.Descubierto)