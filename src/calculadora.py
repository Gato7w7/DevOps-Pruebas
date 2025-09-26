from .operaciones import suma

class Calculadora:
    def __init__(self):
        self.historial = []
    
    def calcular_suma(self, a, b):
        resultado = suma(a, b)
        self.historial.append(f"{a} + {b} = {resultado}")
        return resultado
    
    def obtener_historial(self):
        return self.historial
    
    def limpiar_historial(self):
        self.historial = []