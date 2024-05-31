#12 . Implementa un programa en Python que simule el protocolo MESI. Crea una clase CacheLine con
#los cuatro estados y simule operaciones de lectura y escritura que provoquen transiciones de estado.
class CacheLine:
    def __init__(self):
        self.state = 'I'  # Initial state is Invalid
        self.value = None

    def read(self):
        if self.state == 'I':
            self.state = 'S'
            print("Transition to Shared")
        return self.value

    def write(self, value):
        if self.state in ('I', 'S'):
            #Modificado significa que únicamente este procesador tiene una copia válida del bloque en su
            #caché, la copia en la memoria principal está "desactualizada" y ninguna otra caché puede tener una copia
            #válida del bloque
            #El dato que ese procesador, en su caché tiene, es diferente al dato de la memoria principal
            self.state = 'M'
            print("Transition to Modified")
        self.value = value

    def get_state(self):
        return self.state

def main():
    cache_line = CacheLine()

    # Simulate write operation
    print("Writing value 42")
    cache_line.write(42)
    print(f"State after write: {cache_line.get_state()}")

    # Simulate read operation
    print("Reading value")
    #Acá se simula la operación de lectura, donde se verifica que si el estado es "I" (inválido), entonces
    #el estado cambia a "S" (compartido). Sin embargo, como en la operación anterior de escritura (write)
    #el estado fue cambiado de "I" a "M", entonces el estado actual es "M", por lo que no entraría
    #en la condicional del "read" en "if self.state=="I"", ya que el estado actual es "M".
    #Dando como resultado en el print el estado "M".
    value = cache_line.read()
    print(f"State after read: {cache_line.get_state()}")

if __name__ == "__main__":
    main()
