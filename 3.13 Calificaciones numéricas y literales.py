class Calificaiones_numericas_literales:
    def __init__(self, calificacion):
        self.calificacion = calificacion

    def obtener_clasificacion(self):
        if self.calificacion >= 9.0:
            return 'A'
        elif self.calificacion >= 8.0:
            return 'B'
        elif self.calificacion >= 7.5:
            return 'C'
        else:
            return 'R'

    def mostrar_clasificacion(self):
        clasificacion = self.obtener_clasificacion()
        print(f'La calificación es {clasificacion}')

# Ejemplo de uso
if __name__ == "__main__":
    calificacion = float(input('Ingrese la calificación: '))
    evaluacion = Calificaiones_numericas_literales(calificacion)
    evaluacion.mostrar_clasificacion()
