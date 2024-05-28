#Ejercicio 8: Evaluación de modelos en paralelo con joblib

#Descripción: Implementa un sistema para evaluar varios modelos de machine learning en paralelo utilizando joblib.

#Tareas:
#Entrenar varios modelos de machine learning con diferentes parámetros.
#Usar joblib.Parallel para evaluar los modelos en paralelo.
#Comparar los resultados y seleccionar el mejor modelo.

#Pistas:
#Usa joblib.Parallel y joblib.delayed para paralelizar la evaluación de los modelos. Usa una métrica de evaluación
#adecuada, como la precisión o el F1-score.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import Parallel, delayed

def evaluate_model(n_estimators, X_train, X_test, y_train, y_test):
    #Acá se crea el modelo con la cantidad de árboles pasada por parámetro
    model = RandomForestClassifier(n_estimators=n_estimators)
    #Se entrena al modelo con la data de entrenamiento
    model.fit(X_train, y_train)
    #Una vez que al modelo ya ha sido entrenado, el modelo ahora va a predecir para nuevos valores (la data de test)
    y_pred = model.predict(X_test)
    #Se devuelve el número de árboles en el bosque aleatorio, y el accuracy para ese modelo en específico
    return (n_estimators, accuracy_score(y_test, y_pred))

def parallel_model_evaluation():
    #Se carga la data
    iris = load_iris()
    
    #Una vez que se tiene la data, se realiza la división en data de train y test
    #Se establecen parámetros como el tamaño de la data de prueba (30% de los datos, y el random_state=42 es para que los datos sean los mismos por cada ejecución nueva del programa)
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)
    
    #Se establece la cantidad de árboles para cada modelo
    n_estimators_list = [10, 50, 100, 200]

    #Con "Parallel(n_jobs=4)" se están creando 4 procesos que se encargarán de entrenar un modelo y calcular el accuracy
    #Son 4 procesos, porque la cantidad de bosques aleatorios a crear son 4 (cada uno, con diferente cantidad de árboles)
    #delayed lo que hace es que permite especificar la tarea a realizar (la función evaluate_model), y los parámetros (n,X_train,X_test,y_train,y_test)
    #para cada uno de los valores en la lista "n_estimators_list"
    results = Parallel(n_jobs=4)(delayed(evaluate_model)(n, X_train, X_test, y_train, y_test) for n in n_estimators_list)

    #Cuando ya se obtienen los resultados, los valores son devueltos en una lista de tuplas de la forma:
    #(n_estimators, accuracy_score(y_test, y_pred)), pues así se estableció en la función "evaluate_model"
    return results

results = parallel_model_evaluation()
print(results)
