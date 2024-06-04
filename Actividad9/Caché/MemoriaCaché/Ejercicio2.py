# Analiza la importancia de la localidad de referencia en el acceso a datos. Compara el tiempo de acceso cuando se recorren los datos de manera secuencial versus
de manera aleatoria.
import random

def measure_access_time(array, indices):
    start_time = time.perf_counter()
    
    for i in indices:
        array[i] += 1
    
    end_time = time.perf_counter()
    access_time = end_time - start_time
    return access_time

size = 10**6
array = np.zeros(size)
sequential_indices = list(range(size))
random_indices = sequential_indices.copy()
random.shuffle(random_indices)

sequential_time = measure_access_time(array, sequential_indices)
random_time = measure_access_time(array, random_indices)

print(f"Tiempo de acceso secuencial: {sequential_time:.6f} segundos")
print(f"Tiempo de acceso aleatorio: {random_time:.6f} segundos")
