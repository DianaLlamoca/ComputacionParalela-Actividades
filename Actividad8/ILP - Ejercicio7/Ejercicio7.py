#7 . Implementa un programa en Python que demuestre el paralelismo de instrucciones utilizando hilos. Crea
#un conjunto de tareas independientes que se ejecuten en paralelo utilizando el módulo threading.
import threading
import numpy as np

def task_1():
    cont=0
    while cont<5000:
        cont+=1
    print("Tarea 1 finalizada")

def task_2():
    matriz1=np.random.randn(20,10)
    matriz2=np.random.randn(10,15)
    print("Tarea 2 finalizada")
    return (np.dot(matriz1,matriz2))

def task_3():
    print(f"Hola desde el hilo {threading.current_thread()}")

def task_4():
    print("Tarea 4 iniciada")

def main():
    threads = []
    tasks = [task_1, task_2, task_3, task_4]
    for task in tasks:
        thread = threading.Thread(target=task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
