class Cuadrado:
    def __init__(self, dimension):
        if dimension < 2:
            raise ValueError("La dimensión debe ser mayor o igual a 2.")
        self.dimension = dimension

    def dibujar(self):

        print('*' * self.dimension)
        

        for _ in range(self.dimension - 2):
            print('*' + ' ' * (self.dimension - 2) + '*')
        

        print('*' * self.dimension)


dimension = int(input('Escribe la dimension N>=2 del cuadrado a dibujar: '))
cuadrado = Cuadrado(dimension)
cuadrado.dibujar()
