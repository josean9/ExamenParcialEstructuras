def decoradorTransferencia(funcion):
    def funcion_decorada(*args, **kwargs):
        print("Se va a ejecutar la transferencia")
        return funcion(*args, **kwargs)
        print("Se ha ejecutado la transferencia")
    return funcion_decorada
def decoradorRetirada(funcion):
    def funcion_decorada(*args, **kwargs):
        print("Se va a ejecutar la retirada")
        return funcion(*args, **kwargs)
        print("Se ha ejecutado la transferencia")
    return funcion_decorada