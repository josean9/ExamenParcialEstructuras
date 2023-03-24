def decorado1(funcion):
    def funcion_decorada(*args, **kwargs):
        print("Se va a ejecutar la transferencia")
        return funcion(*args, **kwargs)
        print("Se ha ejecutado la transferencia")
    return funcion_decorada
def decorador2(funcion):
    def funcion_decorada(*args, **kwargs):
        print("Se va a ejecutar la transferencia")
        return funcion(*args, **kwargs)
        print("Se ha ejecutado la transferencia")
    return funcion_decorada
@decorado1
def hola():
    print("Hola")
print(hola())