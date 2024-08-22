with open("archivos//mis_datos.txt", "w", encoding="UTF-8") as myfile:
    myfile.write("archivos//mis datos.txt print(myfile.read())")

# escribe lineas "a" para append lineas
with open("archivos//datos_line.txt", "w", encoding="UTF-8") as myfile:
    myfile.writelines(["1 archivos de mis datos.txt\n","2 print _myfile.read\n"])
    myfile.writelines(["3 archivos de mis datos.txt\n","4 print _myfile.read"])

with open("archivos//datos_line.txt",  encoding="UTF-8") as myfile:
   print(myfile.read())