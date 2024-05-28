#Ejercicio 6: Procesamiento paralelo de archivos con concurrent.futures

#Descripción: Implementa un sistema para procesar múltiples archivos de texto en paralelo, donde cada archivo se
#lee y se realiza una operación de conteo de palabras.

#Tareas:
#Crear una lista de archivos de texto.
#Usar concurrent.futures.ThreadPoolExecutor para procesar los archivos en paralelo.
#Contar las palabras en cada archivo y almacenar los resultados en un diccionario.

#Pistas:
#Usa ThreadPoolExecutor para paralelizar la lectura y el conteo de palabras.
#Usa un diccionario compartido para almacenar los resultados.

import concurrent.futures
import os

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        #Acá se lee el archivo
        text = file.read()
        #print(f"text(file.read()) {text}")

        #Se divide cada palabra por espacio encontrado, el cual se almacena en una lista
        #print(f"text.split() {text.split()}")

    #Se toma el tamaño de la lista, pues el tamaño de la misma representa la cantidad de palabras del texto
    word_count = len(text.split())
    #print(f"word_count {word_count}")

    #Se retorna el nombre del archivo, así como el número de palabras que hay en el texto
    return (file_path, word_count)

def parallel_word_count(file_paths):
    #Se crea un diccionario en donde se almacenará el resultado final
    results = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #Se crea un grupo de hilos para que realicen las tareas y los valores serán almacenados en un diccionario
        #de la forma {feature:file_path} #pues submit devuelve un objeto de tipo "future".
        #Y se pasa cada archivo txt a enviar
        future_to_file = {executor.submit(count_words_in_file, file_path): file_path for file_path in file_paths}

        #".as_completed" lo que hace es colocar el resultado de acuerdo a quién finaliza primero (es decir,
        #que el orden en que son enviados los archivos no importa, sino quién terminó de realizarse primero)
        for future in concurrent.futures.as_completed(future_to_file):
            #Acá se ingresa al diccionario que tiene de clave el "future", es decir, el "file_path" o nombre del archivo
            file_path = future_to_file[future]
            print(file_path)

            #Acá se establece un manejo de errores para que el programa no se "cuelgue" en cuanto aparezca un error
            try:
                # Con .result() se obtiene el resultado del future, de lo contrario, solo se devolverá un objeto del tipo "future"
                #El resultado, claramente, es lo que devuelve la función "count_words_in_file", pues es la tarea que se asignó a cada hilo
                file_path, count = future.result() #Se devuelve el nombre del archivo, y el conteo de palabras
                results[file_path] = count #En el diccionario creado inicialmente, se establece la forma {clave:valor}, clave=nombre_del_archivo,valor=conteo de palabras

            #Esto solo se ejecutará si se levanta un error
            except Exception as exc:
                print(f"{file_path} generated an exception: {exc}")
    return results

file_paths = ["file1.txt", "file2.txt", "file3.txt"]
word_counts = parallel_word_count(file_paths)
print(word_counts)
