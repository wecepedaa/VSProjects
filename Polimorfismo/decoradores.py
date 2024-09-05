def acabados(funcion):
    def funcion_modificada():
        print("Antes de llamar a funcion como parametro")
        funcion()
        print("Despues de llamar  a la funcion")
    return funcion_modificada
        
#def saludo():
#    print("Hola Willy")
    
#saludo_modificado = decorador(saludo)
#saludo_modificado()

@acabados
def saludo():
    print("Hola Willian")

saludo()