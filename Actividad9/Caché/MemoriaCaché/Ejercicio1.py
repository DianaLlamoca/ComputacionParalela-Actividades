#1)Ejercicio: Medir la latencia de acceso a diferentes tamaños de datos en Python.
import time
import numpy as np

#Se crea la función que medirá la latencia para cada uno de los diferentes tamaños de cada dato
def measure_latency(array_size):
    #Se crea un array de ceros del tamaño indicado por parámetro
    array = np.zeros(array_size)
    #Se empieza a tomar el tiempo
    start_time = time.perf_counter()

    #Se accede a todos los elementos del array para luego ver el tiempo total empleado
    for i in range(array_size):
        array[i] += 1

    end_time = time.perf_counter()
    #Se obtiene el tiempo total
    latency = end_time - start_time
    return latency


sizes = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
latencies = []

for size in sizes:
    latency = measure_latency(size)
    latencies.append(latency)
    print(f"Tamaño del array: {size}, Latencia: {latency:.6f} segundos")

# Graficar los resultados
import matplotlib.pyplot as plt

#Se grafica cada uno de los diferentes tamaños de datos en Python con sus respectivas latencias
plt.plot(sizes, latencies, marker='o')
plt.xlabel('Tamaño del Array')
plt.ylabel('Latencia (segundos)')
plt.xscale('log')
plt.yscale('log')
plt.title('Latencia de Acceso a Datos en Diferentes Tamaños de Array')
plt.show()

#De lo cual se concluye que la latencia de acceso también depende del tamaño de los datos
