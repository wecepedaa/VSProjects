import pandas as pd

#df = pd.read_csv("archivos\\datos.csv", names =["Nombre","Apellido","Edad"])
df = pd.read_csv("archivos\\datos.csv")

# obteniendo datos de la columna nombre
nombres =df["nombre"]
#print(nombres)

# Ordenar
dfsort = df.sort_values("edad")
#print(dfsort)

dfsort = df.sort_values("edad", ascending=True)
#print(dfsort)


# Concatenar df
df_concat = pd.concat([df,dfsort]) 
#print(df_concat)

# cuena filas, columnas
filas_cols =df.shape
#print(filas_cols)

# accediendo a elemento especifico iloc
#print(df.loc[2,"edad"])

# accediendo a elemento especifico iloc
#print(df.iloc[2,1])

# accediendo a elemento especifico iloc
#print(df.iloc[:2,1])

# accediendo a elemento especifico iloc con condicion
print(df.loc[df["edad"]>30, :])