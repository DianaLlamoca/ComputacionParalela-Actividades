#10 . Implementa un programa en Python que simule un sistema de snoop bus utilizando hilos. Cada hilo
#representa un núcleo con su propia caché y observa una lista compartida de operaciones de memoria.

import threading
import time

shared_memory = [0] * 10
bus_operations = []
bus_lock = threading.Lock()


class Cache:
    def __init__(self, id):
        self.id = id
        self.cache = [0] * 10

    def read(self, index):
        with bus_lock:
            #Acá se agrega las operaciones de lectura para cada núcleo, pero como la condicional
            #de la función "snoop" no se cumplirá, pues la operación es  de lectura, mas no de escritura,
            #solo se limitará a leer el dato (eso hace el return self.cache[index], el cual devuelve el valor)
            bus_operations.append((self.id, 'read', index))
        return self.cache[index]

    def write(self, index, value):
        with bus_lock:
            #Se agrega a la lista de operaciones del bus, puesto que los hilos demonios estarán ejecutándose
            #en segundo plano en la tarea "snoop". Entonces, la condicional "if bus_operations" de la función
            #"snoop" se cumplirá, y ejecutará el contenido
            bus_operations.append((self.id, 'write', index, value))
            print(f"bus_operations {bus_operations}")
        self.cache[index] = value

    def snoop(self):
        while True:
            print("entré al bucle snoop")
            with bus_lock:
                #Debido a que luego de un tiempo, la lista que representa las operaciones en el bus
                #se va llenando, esta condicional se cumplirá
                if bus_operations:
                    print("realizo la operación para el hilo demonio 1")
                    #Se obtiene la primera operación (que sería la operación de "escritura" para el núcleo 1
                    #el cual es una tupla
                    op = bus_operations.pop(0) #op tiene la forma: [(id,operación, índice, valor)]

                    #Se agarra el elemento de la posición 1 de la tupla, que representa la operación hecha por los núcleos
                    if op[1] == 'write':
                        #Como esta condicional, luego de las operaciones de "write" se va a cumplir, entonces
                        #en la caché de ese núcleo (representado por un hilo), se coloca ese "valor" en el "índice".
                        #Es decir, en la caché de ese núcleo se realiza la operación de escritura para ese valor en el índice indicado
                        #Y así para cada uno de los hilos demonios en la función "snoop"
                        
                        #De manera resumida, cada hilo (núcleo) está escribiendo sus valores en sus cachés respectivas
                        self.cache[op[2]] = op[3]
                        print("caché",self.cache)
                    
                    #La lista bus_operations al final quedará vacía (pues se usa el comando .pop)
            time.sleep(0.01)

def cpu_task(cache, index, value):
    #Se realiza la operación de "write" y se agrega dicha operación a la lista que representa las operaciones en el bus
    cache.write(index, value)
    print(f"CPU {cache.id} wrote {value} at index {index}")

    #print(cache.cache) #Imprimí este valor para ver la caché de cada hilo (en este caso, el hilo representa a un núcleo)

    #Se hace una pausa de 1 segundo, permitiendo que los demás hilos (núcleos) escriban y lean sus valores
    time.sleep(1)
    #Se debe tener en cuenta que los hilos demonios se ejecutan en segundo plano, por lo que al terminar
    #los 4 hilos de realizar las operaciones de lectura y escritura, los hilos demonios empezarán
    #a realizar la tarea en la función "snoop"

    #Se realiza la operación de "read" y se agrega dicha operación a la lista que representa las operaciones en el bus
    read_value = cache.read(index)
    print(f"CPU {cache.id} read {read_value} from index {index}")

def main():
    caches = [Cache(i) for i in range(4)]
    threads = []

    for cache in caches:
        #Para cada caché, se crea un hilo demonio que se encargará de realizar la función "snoop"
        t = threading.Thread(target=cache.snoop)
        #Estos, al ser hilos demonios, se estarán ejecutando siempre en segundo plano hasta que el programa termine
        t.daemon = True
        t.start()

    for i, cache in enumerate(caches):
        #Se crearán 4 hilos, cada hilo se encargará de realizar la operación de "write" y "read" en cada una
        #de las cachés

        #El primer hilo (que representa a un núcleo), escribe el valor "i" (0 en la prim. iteración)
        #en su caché, al realizar la llamada a "cpu_task".
        #Luego, como en "cpu_task" está la función de "read", que lo que hace es leer dicho valor
        #que está almacenado en ese índice de la caché pasado por parámetro
        t = threading.Thread(target=cpu_task, args=(cache, i % 10, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
