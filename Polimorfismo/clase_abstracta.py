# plantilla quer no se instancia
from abc import ABC, abstractmethod

class Persona(ABC):
    @classmethod
    @abstractmethod
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad 
        self.profesion = profesion
        
    @classmethod
    @abstractmethod
    def actividad(self):
        pass
    
    def presentarse(self):
        print(f"Nombre: {self.nombre} edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion):
        super().__init__(nombre, edad, profesion)
        
    def actividad(self):
        print(f"Mi actvidad es:  {self.profesion}")
 
class Trabajador(Persona):
    def __init__(self, nombre, edad, profesion):
        super().__init__(nombre, edad, profesion)
        
    def actividad(self):
        print(f"Mi trabajo es como:  {self.profesion}") 
 
will = Trabajador("William", 59, "Cientifico")   
will.presentarse()
will.actividad()

andree = Estudiante("Andree", 33, "Estudiante")   
andree.presentarse()
andree.actividad()