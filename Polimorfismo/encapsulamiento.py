class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor"
        self._otro_atributo = "otro"
        
obj = MiClase()
#print(obj.__atributo_privado)
#print(obj._otro_atributo)


class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
        
will = Persona("William",60)
print(will.get_nombre())

will.set_nombre("Edward")
print(will.get_nombre())
