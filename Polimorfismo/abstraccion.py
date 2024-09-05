class Auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
        print(self._estado)
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("conduciendo")
        
mi_auto = Auto()
mi_auto.conducir()