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
        self.saldo -= cantidad
    def __str__(self):
        return "Cuenta de {} con un saldo de {}".format(self.nombre, self.saldo)