"""
Luis Gandarillas Fernandez - 100471965@alumnos.uc3m.es
Olivia Grima Perez - 100474858@alumnos.uc3m.es

Juego 1942
Ejecutar el juego desde juego.py
"""

class Point():
    """Sirve para calcular las coordenadas x e y de un objeto"""
    
    def __init__(self, x, y):
        
        if type(x) != int and type(x) != float:
            raise TypeError("x debe der un numero")
        else:
            self.__x = x
        
        if type(y) != int and type(y) != float:
            raise TypeError("x debe der un numero")
        else:
            self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value