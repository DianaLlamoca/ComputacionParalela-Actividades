#Ejercicio 3: Procesamiento paralelo de archivos con Dask

#Descripción: Utiliza Dask para procesar un conjunto de archivos CSV en paralelo, realizando una
#agregación (por ejemplo, promedio de una columna específica).

#Tareas:
#Leer varios archivos CSV con Dask.
#Procesar los archivos en paralelo para calcular el promedio de una columna específica.
#Combinar los resultados y obtener el promedio total.

#Pistas:
#Usa dask.dataframe.read_csv para leer los archivos.
#Usa dask.dataframe para realizar las operaciones en paralelo.

import dask.dataframe as dd
def parallel_csv_processing(file_paths):
    #Los 4 archivos se van a leer de manera paralela, pues un Dask DataFrame es una colección de muchos Pandas DataFrames.
    #El marco de datos de dask se compone de particiones, en este caso serán 4 (por los archivos csv enviados, obvio)
    df = dd.read_csv(file_paths)
    #print(df)

    #Podemos acceder a cada una de las particiones con el comando ".partitions[num_part]"
    #print(df.partitions[0]) #Es un resultado "lazy". Es decir, que no se carga en memoria hasta que se llame con ".compute"
    #print(df.partitions[0].compute())

    #Calculamos la media:
    #De esta manera, se calcula la media, para la partición 0, de la columna "sueldo"
    #print(df.partitions[0]["sueldo"].mean().compute()) #Si no se coloca el ".compute", se obtendrá un "lazy result"

    #Sin embargo, si se quiere calcular la media para el conjunto total de particiones.
    #Es decir, la media de la columna "sueldo" de las 4 particiones, solo colocamos lo siguiente:
    #print(df["sueldo"].mean().compute())

    #Una vez que los archivos se hayan leído, se procederá a calcular la media total de las 4 particiones
    average_value = df['sueldo'].mean().compute() #Debería ser 5221.9, como se calculó antes
    ##El .compute sirve para obtener el resultado en sí mismo, ya que si no se coloca ello
    #es un resultado "lazy". Es decir, que no se carga en memoria hasta que sea llamado (en este caso, con "compute")
    return average_value

file_paths = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv']
average = parallel_csv_processing(file_paths)
print(f"Average value: {average}")
