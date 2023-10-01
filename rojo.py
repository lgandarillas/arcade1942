"""
Luis Gandarillas Fernandez - Arcade 1942

Run game: python3 juego.py
"""

import pyxel
import random
import constants
from point import Point
from bala import Bala
from enemigo import Enemigo

class Rojo(Enemigo):
    """Aparecerán en grupo siguiendo una formación. Habitualmente dan 2 o 3
    vueltas hasta que desaparecen. Normalmente no disparan. Si se les destruye,
    obtendrás ciertas ventajas, como la capacidad de disparar doble."""
    
    def __init__(self, sep):
        
        super().__init__()
        
        if type(sep) != int and type(sep) != float:
            raise TypeError("sep debe der un numero")
        else:
            # Definimos la posicion inicial del enemigo
            # la posicion x varia segun sep para que no se superpongan
            self.__point = Point(-sep, 50)
        
        # Inicialmente esta vivo y tiene 1 vida
        self.__is_alive = True
        self.__vidas = 1
        
        # Defino el tipo de enemigo
        self.__type = 1
        
        # Definimos ancho y alto
        self.__width = constants.ROJO_DER_1[3]
        self.__height = constants.ROJO_DER_1[4]
        
        # Asignar velocidades
        self.__speed = constants.ROJO_SPEED[0]
        
        # Selecciono aleatoriamente el punto en x del disparo
        # Ponemos coordenadas negativa para que algunos enemigos rojos no disparen
        self.__disparo = random.randint(-20, 50)
        
        # Creo lista de balas
        self.__balas = []
        
        # Vueltas decide aleatoriamente si dan 2 o 3 vueltas
        self.__vueltas = 2 if random.random() <= 0.5 else 3
        self.__vueltas_dadas = 0
        
        # Variables de control para ver en que tramo se encuentra el avion
        """La asignacion de los cuartos de la circunferenica es la siguiente:
            - Cuarto 1: Superior derecha
            - Cuarto 2: Inferior derecha
            - Cuarto 3: Inferior izquierda
            - Cuarto 4: Superior izquierda"""
        self.__recto = True     # El avion va recto al principio y al final
        self.__cuarto1 = False  # Primer cuarto de la circunferenica
        self.__cuarto23 = False # Segundo y tercer cuarto de la circunferencia
        self.__cuarto4 = False  # Cuarta parte de la circunferenica
        

    def __disparar(self):
        """Disparo añadiendo un objeto de la clase Bala a la lista de balas
        en el frame elegido aleatoriamente en el constructor"""
        if self.__disparo == self.__point.x:
            self.__balas.append(Bala(self.__point.x + constants.BOMB_DOWN_1[3]/2,
                                     self.__point.y + constants.BOMB_DOWN_1[4],
                                     constants.BALA_ENEMY))
    
    @property
    def is_alive(self):
        return self.__is_alive
    
    @is_alive.setter  
    def is_alive(self, value):
        self.__is_alive = value
    
    @property
    def x(self):
        return self.__point.x 
    
    @property
    def y(self):
        return self.__point.y 
    
    @property 
    def w(self):
        return self.__width
    
    @property
    def h(self):
        return self.__height
    
    @property
    def vidas(self):
        return self.__vidas
    
    @vidas.setter 
    def vidas(self, value):
        self.__vidas = value
    
    @property 
    def balas(self):
        return self.__balas
    
    @property
    def type(self):
        return self.__type
    

    # FUNCIONES PARA DESPLAZAR AL ENEMIGO
    def __derecha(self):
        """Desplaza el objeto a la derecha sumando posiciones a x."""
        self.__point.x += self.__speed
    
    def __izquierda(self):
        """Desplaza el objeto a la izquierda restando posiciones a x."""
        self.__point.x -= self.__speed
        
        
    def __mover_recta_i(self):
        """Se desplaza hacia la derecha durante la recta inicial."""
        if self.__point.x < 60 and self.__recto:
            self.__derecha()
            if self.__point.x == 60:
                self.__recto = False
                self.__cuarto1 = True
    
    def __mover_recta_f(self):
        """Se desplaza hacia la derecha durante la recta final."""
        if self.__recto and self.__point.x >= 60:
            self.__derecha()
        
        # Matar el avion si sale de la pantalla
        if self.__point.x > 120:
            self.__morir()
    
    
    def __mover_cuarto1(self):
        """Movimiento en funcion de la ecuacion del circulo para un radio y un
        centro dado, para el primer cuarto."""
        if self.__point.x >= 60 and self.__cuarto1:
            x = self.__point.x + self.__speed
            self.__derecha()
            self.__point.y = 70 - (-x**2 + 120*x - 3200)**(1/2)
            # Desactivo la variable semicirculo superior
            if self.__point.x == 80:
                self.__cuarto1 = False
                self.__cuarto23 = True
    
    def __mover_cuarto23(self):
        """Movimiento en funcion de la ecuacion del circulo para un radio y un
        centro dado, para el segundo y tercer cuarto."""
        if self.__point.x <= 80 and self.__cuarto23:
            x = self.__point.x - self.__speed
            self.__izquierda()
            self.__point.y = 70 + (-x**2 + 120*x - 3200)**(1/2)
            if self.__point.x == 40:
                self.__cuarto23 = False
                self.__cuarto4 = True
            
    def __mover_cuarto4(self):
        """Movimiento en funcion de la ecuacion del circulo para un radio y un
        centro dado, para el ultimo cuarto."""
        if self.__point.x >= 40 and self.__point.x < 60 and self.__cuarto4:
            x = self.__point.x + self.__speed
            self.__derecha()
            self.__point.y = 70 - (-x**2 + 120*x - 3200)**(1/2)
            
            # Desactivo la variable semicirculo superior
            if self.__point.x == 60:
                self.__cuarto4 = False
                self.__vueltas_dadas += 1
                if self.__vueltas_dadas == self.__vueltas:
                    self.__recto = True
                else:
                    self.__cuarto1 = True
    
        
    def __desaparecer(self, lst):
        """Elimina los objetos que no estan vivos de la lista."""
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
    
    def __morir(self):
        """El objeto muere asignando el valor booleano False a la variable."""
        self.__is_alive = False


    def __pintar_recto(self):
        # Sprite del enemigo rojo a 0 grados
        pyxel.blt(self.__point.x, self.__point.y, constants.ROJO_DER_1[0],
            constants.ROJO_DER_1[1] if pyxel.frame_count % 5 == 0 else\
                constants.ROJO_DER_2[1],
            constants.ROJO_DER_1[2],
            constants.ROJO_DER_1[3], constants.ROJO_DER_1[4],
            constants.TRANSPARENTE)
    
    
    def __pintar_cuarto1(self):
        # Sprite del enemigo rojo a 315 grados
        pyxel.blt(self.__point.x, self.__point.y, constants.ROJO_315[0],
            constants.ROJO_315[1],
            constants.ROJO_315[2],
            constants.ROJO_315[3], constants.ROJO_315[4],
            constants.TRANSPARENTE)  
        
        
    def __pintar_cuarto23(self):
        # Sprite del enemigo rojo a 225 grados
        if self.__point.x >= 60:
            pyxel.blt(self.__point.x, self.__point.y, constants.ROJO_225[0],
                constants.ROJO_225[1],
                constants.ROJO_225[2],
                constants.ROJO_225[3], constants.ROJO_225[4],
                constants.TRANSPARENTE)
        # Sprite del enemigo rojo a 135 grados
        if self.__point.x < 60:
            pyxel.blt(self.__point.x, self.__point.y, constants.ROJO_135[0],
                constants.ROJO_135[1],
                constants.ROJO_135[2],
                constants.ROJO_135[3], constants.ROJO_135[4],
                constants.TRANSPARENTE) 
    
    
    def __pintar_cuarto4(self):
        # Sprite del enemigo rojo a 45 grados
        pyxel.blt(self.__point.x, self.__point.y, constants.ROJO_45[0],
            constants.ROJO_45[1],
            constants.ROJO_45[2],
            constants.ROJO_45[3], constants.ROJO_45[4],
            constants.TRANSPARENTE) 
    
    def __mover(self):
        """Comprobar movimiento del enemigo rojo."""
        # MOVIMIENTO RECTA INICIAL: Desde la izquierda hasta (60, 50)
        self.__mover_recta_i()
        
        # MOVIMIENTO VUELTAS
        # Desplazamiento hacia abajo-derecha hasta (80, 70)
        self.__mover_cuarto1()
        # Desplazamiento hasta la izquierda a (40, 70)
        self.__mover_cuarto23()
        # Desplazamiento arriba-derecha hasta (60, 50)
        self.__mover_cuarto4()
            
        # MOVIMIENTO RECTA FINAL: Desde la posicion (60, 50) hata la derecha
        self.__mover_recta_f()
        
        
    def update(self):
        # Comprobar movimiento del enemigo rojo
        self.__mover()
        
        # comprobar si el enemigo rojo ha disparado
        self.__disparar()
        
        # Eliminar las balas en caso de estar muertas
        self.__desaparecer(self.__balas)
        
        
        
    def draw(self):
        if self.__is_alive:
            for b in self.__balas:
                b.draw()
        
        # En funcion de las variables de control pinto el sprite adecuado
        if self.__recto:
            self.__pintar_recto()
        
        if self.__cuarto1:
            self.__pintar_cuarto1()
        
        if self.__cuarto23:
            self.__pintar_cuarto23()
        
        if self.__cuarto4:
            self.__pintar_cuarto4()
