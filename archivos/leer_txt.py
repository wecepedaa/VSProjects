myfile = open("archivos//datos.txt", encoding="UTF-8")
print(myfile.read())
myfile.close()

myfile = open("archivos//datos.txt", encoding="UTF-8")
lineas = myfile.readlines()
myfile.close()
# una sola linea
#lineas = myfile.readline()
#lineas = myfile.readline(100)

print(lineas)


for i in lineas:
    print(i)
