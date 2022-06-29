from abc import ABC, abstractmethod

class OperacionesBasicas:
    def __init__(self, num1 , num2) :
        self._num1 = num1
        self._num2 = num2

    @abstractmethod
    def adiccion(self):
        pass
    
    @abstractmethod
    def sustraccion(self):
        pass

    @abstractmethod
    def multiplicacion(self):
        pass

    @abstractmethod
    def division(self):
        pass

    @property
    def numero_uno(self):
        return self._num1
    
    @property
    def numero_dos(self):
        return self._num2

    @numero_uno.setter
    def numero_uno(self, num1):
        self._num1 = num1
    
    @numero_dos.setter
    def numero_dos(self, num2):
        self._num2 = num2

    def __str__(self):
        return f"Los numeros elgidos son: numero uno-->[{self._num1}] y el numero dos-->[{self._num1}]"
