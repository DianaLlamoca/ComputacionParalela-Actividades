from multiprocessing import Pool
import numpy as np

def matrix_multiply_segment(args):
    A_segment, B = args
    return np.dot(A_segment, B)

if __name__ == "__main__":
    #Se crean dos matrices de forma 1000x1000
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)

    #Se define el número de procesos a usar
    num_processes = 4

    #Se define el tamaño de los segmentos
    segment_size = A.shape[0] // num_processes #-->1000/4=250

    #Se crean los 4 segmentos, cada uno de ellos será utilizado por un proceso
    #Cada elemento de la lista es una matriz, de la forma (250*100)*(1000*1000), la forma que se necesita para realizar el producto matricial
    segments = [(A[i * segment_size:(i + 1) * segment_size], B) for i in range(num_processes)]


    with Pool(num_processes) as pool:
        #Se crean 4 procesos y se le pasa cada segmento con la tarea a realizar
        results = pool.map(matrix_multiply_segment, segments)

    #Una vez se tengan los resultados para cada segmento, se unen cada uno de los resultados
    C = np.vstack(results)
    print("Matrix multiplication completed.")
