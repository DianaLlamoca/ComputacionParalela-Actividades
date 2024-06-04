Implementación de un simulador de Protocolo MESI:
Descripción: Implementa un simulador simple del protocolo MESI en Python. Simula varios procesadores y cachés que acceden y modifican líneas de datos, cambiando los
estados de las líneas de caché según las reglas de MESI.

class CacheLine:
    def __init__(self):
        self.state = 'Invalid'
        self.data = None

class Processor:
    def __init__(self, id):
        self.id = id
        self.cache = {}

    def read(self, address):
        if address in self.cache and self.cache[address].state != 'Invalid':
            return self.cache[address].data
        else:
            self.cache[address] = CacheLine()
            self.cache[address].state = 'Shared'
            self.cache[address].data = memory_read(address)
            return self.cache[address].data

    def write(self, address, data):
        if address in self.cache and (self.cache[address].state == 'Shared' or self.cache[address].state == 'Exclusive'):
            self.cache[address].state = 'Modified'
            self.cache[address].data = data
        else:
            self.cache[address] = CacheLine()
            self.cache[address].state = 'Modified'
            self.cache[address].data = data
            memory_write(address, data)

def memory_read(address):
    # Simula una lectura de memoria principal
    return "data_from_memory"

def memory_write(address, data):
    # Simula una escritura en memoria principal
    pass

# Ejemplo de uso
p1 = Processor(1)
p2 = Processor(2)
p1.write(0x1A, "data1")
p2.read(0x1A)
