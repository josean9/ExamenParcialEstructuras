def decorado1(funcion):
    def funcion_decorada(*args, **kwargs):
        print("Decorador 1")
        return funcion(*args, **kwargs)
    return funcion_decorada