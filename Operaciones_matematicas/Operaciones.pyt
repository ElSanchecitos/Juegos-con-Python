

class Operaciones(OperacionesBasicas):
    def __init__(self, numero1, numero2):
        OperacionesBasicas.__init__(self, numero1, numero2)

    def adiccion(self):
        return numero_uno + numero_dos 

    def sustraccion(self):
        return numero_uno - numero_dos

    def multiplicacion(self):
        return numero_uno * numero_dos 
    
    def division(self):
        return numero_uno / numero_dos 

    def __str__(self) -> str:
        return f"{OperacionesBasicas.__str__(self)} RTA: suma[{self.adiccion}], resta[{self.sustraccion}], multiplicacion[{self.multiplicacion}], division[{self.division}]" 

operacion1 = Operaciones(2,3)
print(operacion1.adiccion())


