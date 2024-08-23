# 2 listas con nombres y apellidos cada una
nombres = ["william","edy","eduardo","carlo","xime"]
apellidos = ["cepeda","xepeda","raza","astudillo","cantos"]

with open("archivos/n_p.txt","w") as arch:
    arch.writelines("Los datos son: \n")
    # se crea dentro de una lista
    [arch.writelines(f"Nombre: {n.capitalize()} \tApellido: {a.capitalize()} \n") for n,a in zip(nombres, apellidos)]
    arch.writelines("Fin del archivo\n")
    
