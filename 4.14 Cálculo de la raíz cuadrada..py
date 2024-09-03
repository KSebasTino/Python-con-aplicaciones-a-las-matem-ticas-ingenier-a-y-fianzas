class RaizCuadrada:
    def __init__(self, a, iteraciones=10):
        self.a = a
        self.iteraciones = iteraciones
        self.x = 1.0

    def calcular_raiz(self):
        for k in range(1, self.iteraciones):
            self.x = (self.x + self.a / self.x) / 2
            print(f'La raíz después de {k} iteraciones es: {self.x}')

if __name__ == "__main__":
    a = float(input('Dame el valor de a: '))

    raiz = RaizCuadrada(a)
    raiz.calcular_raiz()
