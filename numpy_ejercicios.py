import numpy as np


# Activar entorno virtual.
# .\datos\Scripts\activate

# Desactivar entorno virtual.
# .\datos\Scripts\deactivate

# Run the file.
# python numpy_ejercicios.py

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

# print("Arreglo 2D:\n", matrix)
# print("Forma (shape):", matrix.shape)
# print("Tipo de datos (dtype):", matrix.dtype)

# Crear un arreglo de dos dimensiones a partir de una lista de listas. 

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(arr, type(arr))

# Crear arreglo de ceros con forma (3,4).abs

arr = np.zeros((3,4))
# print(arr)

# Crear arreglo con unos con una forma (2,2).abs

arr = np.ones((2,2))
# print(arr)

# Modificar el valor de un elemento del array.

arr[1,1] = 10
# print(arr)

# Crear una matriz de identidad.abs

arr = np.eye(4)
# print(arr)

# Crear un arreglo 3d de ceros con una forma (2,3,4).abs

arr = np.zeros((2,3,4))
# print(arr)

# Modificar un elemento del array.abs

arr[0,1,2] = 5
# print(arr)

# Generar un array aleatorio de ejemplo.abs

arr = np.random.rand(2,5)
arr_transposed = arr.T  
# print(arr)
# print(arr_transposed)


arr_1 = np.array([[1,2], [3,4]])
arr_2 = np.array([[5,6], [7,8]])

# print(arr_1, arr_2)

# Concatenar arreglos horizontalmente.abs
arr_h = np.hstack((arr_1, arr_2))
# print(arr_h)

# Concatenar arreglos verticalmente.abs

arr_v = np.vstack((arr_1, arr_2))
# print(arr_v)

# Generar array de ejemplo.abs

arr = np.array([1,2,3,4,5])

suma = np.sum(arr)
# print(suma)

# Calcular el promedio de los elementos.abs

promedio = np.mean(arr)
# print(promedio)

# Calcular la mediana.abs

mediana = np.median(arr)
# print(mediana)

# Calcular el producto de los elementos.abs

producto = np.prod(arr)
# print(producto)

# Calcular la desviación estandar.abs

desv_est = np.std(arr)
# print(desv_est)

# Calcular varianza.

var = np.var(arr)
# print(var)

# Calcular minimo de los elementos.abs

minimo = np.min(arr)
# print(minimo)

# Calcular minimo de los elementos.abs

maximo = np.max(arr)
# print(maximo)

# Calcular la suma acumulativa.abs

cumsum = np.cumsum(arr)
# print(cumsum)

# Suma element-wise.abs

arr_suma = arr + arr
# print(arr_suma)

# Resta element-wise.abs

arr_resta = arr - arr
print(arr_resta)
