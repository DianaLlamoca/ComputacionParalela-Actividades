#Ejercicios de paralelismo de datos
#Ejercicio 1: Procesamiento paralelo de imágenes con OpenCV y Multiprocessing
#Descripción: Divide una imagen en varios segmentos y aplica un filtro (por ejemplo, filtro de
#desenfoque) a cada segmento en paralelo usando el módulo multiprocessing.

#Tareas:
#Cargar una imagen utilizando OpenCV.
#Dividir la imagen en segmentos.
#Aplicar un filtro de desenfoque a cada segmento en paralelo.
#Unir los segmentos procesados y guardar la imagen resultante.
#Pistas:
#Usa cv2.imread para cargar la imagen.
#Usa multiprocessing.Pool para el procesamiento paralelo.
#Usa numpy.hstack o numpy.vstack para unir los segmentos procesados.

import cv2
import numpy as np
from multiprocessing import Pool

def apply_blur(segment):
    return cv2.GaussianBlur(segment, (15, 15), 0)

if __name__ == '__main__':
    def parallel_image_processing(image_path):
        image = cv2.imread(image_path)
        #cv2.imshow("imagen",image)
        print(f"shape de la imagen {image.shape}")
        height, width, _ = image.shape
        segments = np.array_split(image, 4, axis=1)
        #Se divide la imagen en 4 segmentos de la forma [np.array[],np.array[],np.array[].np.array[]). 

        #Acá, por cada segmento, se crea 1 proceso, el cual aplicará la función de desenfoque gaussiano a cada porción de la imagen
        with Pool(processes=4) as pool:
            blurred_segments = pool.map(apply_blur, segments) #Claramente, segments es un iterable de arrays

        #Esta función junta los 4 segmentos divididos anteriormente
        blurred_image = np.hstack(blurred_segments)
        #Se guarda la imagen a partir de blurred_image, pues estos contienen los segmentos ya unidos, con las operaciones del desenfoque aplicadas en cada uno de ellos
        cv2.imwrite('blurred_image.jpg', blurred_image)

    parallel_image_processing('input_image.jpg')
