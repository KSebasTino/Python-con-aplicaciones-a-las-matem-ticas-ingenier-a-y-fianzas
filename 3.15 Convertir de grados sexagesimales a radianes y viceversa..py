class Evaluacion:
    def __init__(self, calificacion, asistencia):
        self.calificacion = calificacion
        self.asistencia = asistencia

    def obtener_clasificacion(self):
        if self.calificacion > 9.0 and self.asistencia == 1:
            return 'A Excelente con Mención Honorífica.'
        elif self.calificacion > 9.0 and self.asistencia != 1:
            return 'A Excelente.'
        elif self.calificacion > 8.0 and self.asistencia == 1:
            return 'B Muy bien con Mención.'
        elif self.calificacion > 8.0 and self.asistencia != 1:
            return 'B Muy bien.'
        elif self.calificacion > 7.5:
            return 'C Bien'
        else:
            return 'R Reprobado. Lo siento mucho.'

    def mostrar_clasificacion(self):
        clasificacion = self.obtener_clasificacion()
        print(f'La calificación es: {clasificacion}')

if __name__ == "__main__":
    calificacion = float(input('Dame una calificación: '))
    asistencia = int(input('Dame la asistencia: 1 si asistió o 0 si no asistió. '))

    evaluacion = Evaluacion(calificacion, asistencia)
    evaluacion.mostrar_clasificacion()
