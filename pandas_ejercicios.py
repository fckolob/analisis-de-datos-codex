import pandas as pd
import numpy as np

# Activar entorno virtual.
# .\datos\Scripts\activate

# Series de pandas.
numeros = [3, 4, 5, 6]
numeros, type(numeros)

# Crear una serie a partir de una lista.

serie = pd.Series(numeros)
#print(serie)
#print(type(serie))

# Crear un dataframe a partir de un diccionario.

data = {
    "nombre": ["Juan", "Maria", "Pedro", "Ana"],
    "edad": [25, 30, 35, 40],
    "ciudad": ["Bogota", "Medellin", "Cali", "Barranquilla"]
}

df = pd.DataFrame(data=data)
# print(df)
# print(type(df))

# Exportar un dataframe.

df.to_csv("data.csv")

# Importar un dataframe.

df_importado = pd.read_csv("data.csv", index_col=0)
#print(df_importado)

# Seleccionar una columna.

nombres = df["nombre"]
# print(nombres)
# print(type(nombres))

# Seleccionar una o mas columnas.

df_seleccionado = df[["nombre", "edad"]]
#print(df_seleccionado)
#print(type(df_seleccionado))

# Filtrar por indice.
fila = df.loc[2]
#print(fila)
#print(type(fila))

# Filtrar por condiciones.
mayores_33 = df[df["edad"] > 33]
#print(mayores_33)
#print(type(mayores_33))

# Filtrar por multiples condiciones.
mayores_33_y_name_starts_with_p = df[(df["edad"] > 33) & (df["nombre"].str.startswith("P"))]
#print(mayores_33_y_name_starts_with_p)
#print(type(mayores_33_y_name_starts_with_p))

# Filtrar por query.
mayores_33_y_name_starts_with_p = df.query("edad > 33 and nombre.str.startswith('P')")
#print(mayores_33_y_name_starts_with_p)
#print(type(mayores_33_y_name_starts_with_p))

# Filtrar por isin.
maria = df[df["nombre"].isin(["Maria"])]
# print(maria)
# print(type(maria))

def longitud_5(nombre):
    return len(nombre) == 5

# print(df[df["nombre"].apply(longitud_5)])

# Filtrar por edades entre 25 y 35 años (inclusivo).abs
# print(df[df["edad"].between(25, 35)])

data_x = {
    "nombre": ["Juan", "Maria", "Pedro", "Ana"],
    "edad": [25, 30, np.nan, 40],
    "ciudad": ["Bogota", "Medellin", "Cali", None]
}

df_x = pd.DataFrame(data=data_x)
# print(df_x)
# print(type(df_x))

# Rellenar los datos faltantes.

df_x_fill = df_x.fillna(
    {
        "edad" : df_x["edad"].mean(),
        "ciudad" : "Desconocido" 
    }
)
# print(df_x_fill)
# print(type(df_x_fill))

# Eliminar filas con datos faltantes.
df_x_drop = df_x.dropna()
# print(df_x_drop)
# print(type(df_x_drop))  

# Reemplazar valores especificos de una columna.
df_x_replace = df_x.replace(
    {
        "ciudad" : {None : "Desconocido"},
        "edad" : {np.nan : "edad no especificada"}
    }
)
# print(df_x_replace)
# print(type(df_x_replace))

# Interpolar valores.abs

df_x_interpolate = df_x.copy()
df_x_interpolate["edad"] = df_x["edad"].interpolate()

# print(df_x_interpolate)
# print(type(df_x_interpolate))

data_duplicada = {
    "nombre": ["Juan", "Maria", "Pedro", "Ana", "Juan", "Maria", "Pedro", "Ana"],
    "edad": [25, 30, np.nan, 40, 25, 30, np.nan, 40],
    "ciudad": ["Bogota", "Medellin", "Cali", "Barranquilla", "Bogota", "Medellin", "Cali", "Barranquilla"]
}

df_duplicada = pd.DataFrame(data=data_duplicada)
# print(df_duplicada)
# print(type(df_duplicada))

# Eliminar duplicados.
df_sin_duplicados = df_duplicada.drop_duplicates()

# print(df_sin_duplicados)
# print(type(df_sin_duplicados))

# Renombrar columnas.abs

df_x_renombrado = df_x.copy()
df_x_renombrado.rename(columns={"nombre" : "name", "edad" : "age", "ciudad" : "city"}, inplace=True)
# print(df_x_renombrado)
# print(type(df_x_renombrado))

# Ordenar columnas.
columnas_ordenadas = ["ciudad", "edad", "nombre"]
df_x_ordenado = df_x[columnas_ordenadas]
# print(df_x_ordenado)
# print(type(df_x_ordenado))

# Transformación de datos.abs

def cuadrado(x) : 
    return x ** 2

df_x["edad cuadrado"] = df_x["edad"].apply(cuadrado)
# print(df_x)
# print(type(df_x))

# Agrupar datos.

data_y = {
    "nombre": ["Juan", "Maria", "Pedro", "Ana"],
    "edad": [25, 30, 26, 40],
    "ciudad": ["Barranquilla", "Medellin", "Cali", "Barranquilla"],
    "puntuacion" : [8, 9, 7, 6] 
}

df_y = pd.DataFrame(data=data_y)
# print(df_y)
# print(type(df_y))

# Agrupar datos por ciudad.

grouped = df_y.groupby("ciudad")
# print(grouped.groups)
# print(type(grouped.groups))

# Calcular el promedio de las edades y las puntuacione por ciudad.abs

agregated_data = grouped.agg (
    {
        "edad" : "mean",
        "puntuacion" : "sum"
    }
)   
# print(agregated_data)
# print(type(agregated_data))

# Definir una funcion de agregacion personalizada.abs

def rango(series) :
    return series.max() - series.min()

# Aplicar la funcion agg al grupo.abs

agregated_data_custom = grouped.agg(
    {
        "edad" : rango,
        "puntuacion" : rango
    }
)

# print(agregated_data_custom)
# print(type(agregated_data_custom))

data_y["categoria"] = ["a", "b", "a", "b"]

df_y_categoria = pd.DataFrame(data=data_y)
# print(df_y_categoria)
# print(type(df_y_categoria))

# Agrupar datos por ciudad y categoria.abs

grouped_multi = df_y_categoria.groupby(["ciudad", "categoria"])
# print(grouped_multi.groups)

# Calcular suma de edades y puntuaciones por ciudad y por categoria.abs

agregated_data_multi = grouped_multi.agg(
    {
        "edad": "sum",
        "puntuacion": "mean"
    }
)

# print(agregated_data_multi)


# Crear un dataframe de ejemplo.

data_z = {"Nombre": ["Juan", "Ana", "Luis", "Laura"],
"Edad": [25, 33, 30, 28]}

df_z = pd.DataFrame(data_z  )

# Agregar un nueva columna.abs

df_z["Ciudad"] = ["Madrid", "Barcelona", "Madrid", "Valencia"]

# print(df_z)

# Generar una nueva fila.abs

new_row = pd.Series({"Nombre": "Pedro", "Edad": 45, "Ciudad": "Barcelona"})

# Agregar fila al dataframe.abs

df_z = pd.concat([df_z, new_row.to_frame().T], ignore_index=True)

# print(df_z)

# Crear un dataframe de ejemplo.abs

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Laura"],
    "Edad": [25, 33, 30, 28],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia"]
}

df1 = pd.DataFrame(data)

# Crear un segundo dataframe de ejemplo.abs

data2 = {
    "Nombre": ["Carla", "Irene"],
    "Edad": [38, 27],
    "Ciudad": ["Madrid", "Bilbao"]
}

df2 = pd.DataFrame(data2)

# Combinar los dos dataframes.abs

df_combined = pd.concat([df1, df2], ignore_index=True)

print(df_combined)
