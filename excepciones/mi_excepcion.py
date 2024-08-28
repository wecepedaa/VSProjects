class MiException(Exception):
    def __init__(self, err):
        print(f"Clase Mi excepcion error --> {err}")
    
    
#raise MiException("SOlo Lanza mi exception - raise")   

try:
    raise MiException("Try la excepcion con raise")
except:
    print("Except section from except")
else:
    print("Except else")