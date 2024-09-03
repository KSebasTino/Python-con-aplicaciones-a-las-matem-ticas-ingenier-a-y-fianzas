class Intereses_de_una_cuenta_bancaria:
    def __init__(self,saldo):
        self.saldo = saldo

    def Interes(self):
        if self.saldo < 10000.00:
            self.saldo *=1.03
        else:
            self.saldo *=1.04
    def mostrar_saldo(self):
        print('Saldo final es %5.2f'% self.saldo)


if __name__ == "__main__":
    saldo_inicial= float(input('Ingrese su saldo actual: '))
    cuenta = Intereses_de_una_cuenta_bancaria(saldo_inicial)
    cuenta.Interes()
    cuenta.mostrar_saldo()