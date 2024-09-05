class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad  = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, n_nombre):
        self.__nombre = n_nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, n_edad):
        self.__edad = n_edad
        
    @edad.deleter
    def edad(self):
        del self.__edad
    
    
    
will = Persona("William", 59)
print(will.nombre, will.edad)

will.nombre="Edward"
will.edad=60
print(will.nombre, will.edad)

del will.nombre
will.nombre="Andree"
will.edad = 33
print(will.nombre, will.edad)