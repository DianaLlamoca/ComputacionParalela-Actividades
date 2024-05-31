#8 . Implementa un programa en Python que simule la coherencia de caché utilizando threading. Crea
#un sistema donde múltiples hilos modifiquen una variable compartida y utilice bloqueos para
#garantizar la coherencia.
import threading

#Se crea la variable compartida con un valor inicial de 0
shared_value = 0
#Creamos el lock que servirá para controlar el acceso a la variable compartida.
#Se encuentra en uno de dos estados: "bloqueado" o "desbloqueado"
lock = threading.Lock()

def modify_shared_value():
    #Establecemos que la variable sea global
    global shared_value
    for _ in range(10000):
        #La sentencia "with" evita colocar los comandos ".acquire" y ".release". Cuando un hilo
        #entra en la sentencia, el lock cambia a estado "bloqueado", haciendo que los otros hilos
        #esperen a que el hilo actual termine de ejecutarse para que el estado de lock cambie a "release"
        with lock:
            #Esto se resume a sumar en 1 a la variable compartida por cada iteración
            temp = shared_value
            temp += 1
            shared_value = temp
       
def main():
    #Se crea una lista donde se almacenarán los hilos creads
    threads = []
    #Se crean 4 hilos y se inicializa
    for _ in range(4):
        t = threading.Thread(target=modify_shared_value)
        threads.append(t)
        t.start()
    #Se espera a que los 4 hilos terminen su ejecución para finalizar el programa
    for t in threads:
        t.join()
    #Una vez que los 4 hilos hayan terminado, se imprime el valor final, que debe ser 40000
    #pues se usó "block", por lo que solo 1 hilo pudo acceder a modificar la
    #variable global, evitando así cualquier problema en el valor de la variable compartida
    print(f"Final value: {shared_value}")

if __name__ == "__main__":
    main()
