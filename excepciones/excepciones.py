def suma_dos():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado=   int(a) + int(b)
        except ValueError as e:
            print(f"Error:  {e}")
        except Exception as e:
            print(f"Ingrese numeros solo enteros {type(e).__name__}")
        else:
            break
        finally:
            pass
    return resultado
    
    
print(f"resultado: {suma_dos()}")