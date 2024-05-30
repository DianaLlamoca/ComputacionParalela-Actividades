#6 . Implementa un programa en Python que simule un predictor de bifurcaciones simple. Use un
#historial para predecir si una bifurcación será tomada o no y ajuste las predicciones basadas en los resultados.

class BranchPredictor:
    def __init__(self):
        self.history = {}

    def predict(self, branch):
        #El método get() se utiliza para acceder a un valor en un diccionario.
        #La ventaja de usar get() en lugar de simplemente acceder a la clave directamente es
        #que si la clave no existe en el diccionario, get() devuelve un valor predeterminado en lugar de
        # generar una excepción KeyError: diccionario.get(clave, valor_predeterminado)
        return self.history.get(branch, False)

    def update(self, branch, taken):
        self.history[branch] = taken

def main():
    #Se crea una instancia de la clase BrachPredictor, el cual tendrá un historial (por el constructor)
    #que representará al "historial de bifurcaciones" (este registra los patrones de bifurcaciones para
    #hacer predicciones más precisas) Si acierta, el procesador, como ha estado ejecutando instrucciones
    #basadas en predicciones anteriores, se ha "ganado tiempo" al haberse adelantado
    predictor = BranchPredictor()

    branches = [("branch1", True), ("branch2", False), ("branch1", False), ("branch2", True)]

    for branch, taken in branches:
        #El valor de la bifurcación para "branch1" es False. Sin embargo, al llamar al método ".predict"
        #como este realiza un "history.get", debido a que el "history" está vació al inicio, ".get" devolverá
        #el valor por defectó que se especificó, que sería "False"
        prediction = predictor.predict(branch)

        #El valor predicho, por ende, sería "False", pero el valor actual, sería "Trúe" (es decir, no coinciden)
        print(f"Predicted: {prediction}, Actual: {taken}")

        #Por ello, se llama al método ".update" para actualizar el valor en el diccionario "history".
        #donde el diccionario, finalmente, para "branch1", será de la forma {branch:True}
        predictor.update(branch, taken)

        #Acá se imprime el historial.
        print(f"history {predictor.history}")

        #Lo mismo para ("branch1",False) Sin embargo, como la clave "branch1" ya existe en el diccionario
        #"history", el comando ".get" ya no devolverá el valor por defecto "False", sino el valor existente, que
        #sería "True". Sin embargo, como en la segunda iteración "branch1" es False, entonces no coincide
        #con el valor predicho, por lo que se hace la actualización con ".update" y el valor, para esa
        #bifurcación, en "history", va a cambiar a False", quedando, finalmente {branch1,False}.

        #Lo mismo será para branch2

if __name__ == "__main__":
    main()
