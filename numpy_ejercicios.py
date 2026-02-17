import numpy as np

# Activar entorno virtual.
# .\datos\Scripts\activate

# Desactivar entorno virtual.
# .\datos\Scripts\deactivate

# Crear arreglo de una dimensión con 5 elementos.abs

arr1 = np.array([1,2,3,4,5,6])

# print("Arreglo ID:", arr1)
# print("Forma (shape):", arr1.shape)
# print("Tipo de datos (dtype):", arr1.dtype)

# Cambiar la forma del arreglo a una matriz 2x3.abs

arr2 = arr1.reshape((2,3))

# print("Arreglo 2D:\n", arr2)
# print("Forma (shape):", arr2.shape)
# print("Tipo de datos (dtype):", arr2.dtype)

# Crear una matriz (4,4) con numeros aleatorios entre 0 y 1.

matrix = np.random.rand(4,4) 

print("Arreglo 2D:\n", matrix)
print("Forma (shape):", matrix.shape)
print("Tipo de datos (dtype):", matrix.dtype)