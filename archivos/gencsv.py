import pandas as pd

df = pd.read_csv("archivos//datos.csv")

# convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)
#print(type(df['edad'][0]))


# reemplaza datos en columna especifica
df['apellido'].replace("Xepeda","Mera", inplace = True)
#print(df['apellido'])

# Elimina columnas sin valor
df = df.dropna()
#print(df)

# Eliminar filas repetidas
df = df.drop_duplicates()
print(df)

# Crear archivo csv con datos limpios
df.to_csv("archivos//fileclean.csv")
