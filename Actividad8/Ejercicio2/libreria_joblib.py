import joblib

#Creamos la función a paralelizar
def Cubo(x):
    return x ** 3

## Creamos un objeto `Parallel()` con el número de procesos deseado
parallel = joblib.Parallel(n_jobs=2)
print(parallel)

#Lo que realmente queremos es decirle a Python qué funciones queremos llamar con qué argumentos, sin
#realmente llamarlas; en otras palabras, queremos retrasar la ejecución.

#Esto es lo que "delayed" nos permite hacer cómodamente, con una sintaxis clara. Si queremos decirle
#a Python que nos gustaría llamar Cubo(2) más tarde, simplemente podemos escribir
#delayed(Cubo)(2). Devuelta es la tupla (Cubo, [2], {}), que contiene:
#-una referencia a la función que queremos llamar, en este caso "Cubo"
#-todos los argumentos ("argumentos cortos") sin una palabra clave, por ejemplo "2"
#-todos los argumentos de palabras clave ("kwargs" cortos), en este caso, no le he colocado

# Paralelizamos la ejecución de la función --> delayed(funcion)(argumento)
resultados=(joblib.delayed(Cubo)(x) for x in range(3))
print(resultados) #Esto devuelve un generador, pues eso es que lo hace "delayed",--> Indicarle qué funciones queremos llamar, sin realmente llamarlas
print(next(resultados)) #Es una tupla

#Acá es donde esa "lista", dada por "joblib.delayed(Cubo)(x) for x in range(3), se pasa a la instancia "parallel"
#Luego, la "parallel" instancia crea 2 procesos y los distribuye a las tuplas de la lista y se obtiene el resultado
resultados_o=parallel(resultados)
print(resultados_o)
