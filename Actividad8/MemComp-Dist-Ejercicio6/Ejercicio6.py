#6 . Implementa un programa en Python que utilice el módulo multiprocessing para demostrar la memoria
#compartida. Crea varios procesos que incrementen una variable compartida de manera segura utilizando
#un Value y un Lock.

import multiprocessing

def increment(shared_value, lock):
    for _ in range(10000):
        #Con la sentencia "with", se evitará colocar los comandos ".acquire" y ".release"
        with lock:
            shared_value.value += 1
        #Por lo que cuando un proceso entra a dicha sentencia, el estado de "lock" cambia a  bloqueado, por
        #lo que solo ese proceso podrá ejecutarse, y una vez que finalice, "lock" cambia a "release", permitiendo
        #que el siguiente proceso ejecute.
def main():
    #Se crea una variable compartida de tipo entero "i" (integer) y se inicializa en 0
    shared_value = multiprocessing.Value('i', 0)

    #Se crea el objeto que servirá para controlar el acceso a la variable compartida
    lock = multiprocessing.Lock()
    processes = []

    for _ in range(4):
        #Para cada proceso que se crea, se pasan como parámetros los parámetros de la función "increment" --> (shared_value,lock)
        p = multiprocessing.Process(target=increment, args=(shared_value, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final value: {shared_value.value}")

if __name__ == "__main__":
    main()
