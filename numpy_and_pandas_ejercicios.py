import numpy as np
import pandas as pd

# Run the file.abs
# python numpy_and_pandas_ejercicios.py

# Crear un arreglo de numpy.

data = np.array([[1,2,3], [4,5,6], [7,8,9]])

# Crear un DataFrame a partir de el arreglo de Numpy.abs

df = pd.DataFrame(data, columns=["A", "B", "C"])
# print(df)

# Crear un array de Numpy a partir de un DataFrame de pandas.


data = {
    "A": [1,4,7],
    "B": [2,5,8],
    "C": [3,6,9]
}

df = pd.DataFrame(data)
arr = df.to_numpy()
# print(arr)

# Using df.values.

# print(df.values)

# Calcular el promedio de cada columna usando numpy.abs

mean_columns = np.mean(df, axis=0)
# print(mean_columns)

# Another way to do it.abs

# print(df.mean(axis=0))

# Calcular el promedio de cada fila.abs

print(df.mean(axis=1))
