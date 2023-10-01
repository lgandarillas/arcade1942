"""
Luis Gandarillas Fernandez - Arcade 1942

Run game: python3 juego.py
"""

import pyxel
import constants
from point import Point
from bala import Bala

class Player():
    """ Player es el jugador principal del juego, Lockheed P-38"""
    def __init__(self):
        
        # Definimos la posicion inicial
        self.__point = Point(pyxel.width / 2 - constants.LOCKHEED_1[3]/2,
                             pyxel.height - constants.LOCKHEED_1[4])
        
        # Inicialmente esta vivo y tiene 3 vidas
        self.__is_alive = True
        self.__vidas = 3
        
        # Definimos ancho y alto
        self.__width = constants.LOCKHEED_1[3]
        self.__height = constants.LOCKHEED_1[4]
        
        # Asignar velocidades
        self.__speed_x = constants.LOCKHEED_SPEED[0]
        self.__speed_y = constants.LOCKHEED_SPEED[1]
        
        # Creo lista de balas
        self.__balas = []
        self.__bala_type = constants.BALA_PLAYER
        
        # Puntos actuales y maximos
        self.__score = 0
        self.__max_score = 0
        
        # Variables para hacer loops
        self.__loop = False
        self.__tloop = False
        
        # Bonus de balas dobles
        self.__bonus = False
    
    
    def __reset(self):
        """Reinicia los parametros basicos del jugador."""
        # Reposicionamos al avion en la posicion inicial
        self.__point = Point(pyxel.width / 2 - constants.LOCKHEED_1[3]/2,
                             pyxel.height - constants.LOCKHEED_1[4])
        
        # El avion vuelve a estar vivo
        self.__is_alive = True
        
        # Actualizamos max score y reiniciamos el score
        self.__max_score = self.__score
        self.__score = 0
        
        
    
    def __disparar(self):
        """Crea un objeto de la clase bala en la posicion de Player,
        si se pulsa el espacio disparo una bala."""
        if self.__bonus:
            if pyxel.btnp(pyxel.KEY_SPACE):
                # Bala izquierda
                self.__balas.append(Bala(self.x + self.__width/2 - 5, 
                                         self.y, self.__bala_type))
                pyxel.play(1, 2)
                
                # Bala derecha
                self.__balas.append(Bala(self.x + self.__width/2 + 5, 
                                         self.y, self.__bala_type))
                pyxel.play(1, 2)
        else:
            # Bala unica
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.__balas.append(Bala(self.x + self.__width/2, 
                                         self.y, self.__bala_type))
                pyxel.play(1, 2)
    
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
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def bonus(self, value):
        self.__bonus = value
    
    @property 
    def loop(self):
        return self.__loop
    
    @property
    def score(self):
        return self.__score
    
    @score.setter 
    def score(self, value):
        self.__score = value
    
    @property 
    def max_score(self):
        return self.__max_score
    
    @max_score.setter 
    def max_score(self, value):
        self.__max_score = value
    
    @property
    def balas(self):
        return self.__balas
    
    
    def __bajar(self):
        """Hace que el objeto baje sumando posiciones a y."""
        self.__point.y += self.__speed_y
    
    def __subir(self):
        """Hace que el objeto suba restando posiciones a y."""
        self.__point.y -= self.__speed_y
    
    def __derecha(self):
        """Desplaza el objeto a la derecha sumando posiciones a x."""
        self.__point.x += self.__speed_x
    
    def __izquierda(self):
        """Desplaza el objeto a la izquierda restando posiciones a x."""
        self.__point.x -= self.__speed_x
    
    def __hacer_loop(self):
        """El avion hace un loop para evitar ser abatido."""
        if pyxel.btn(pyxel.KEY_Z):
            self.__loop = True
            self.__tloop = pyxel.frame_count
    
    def __limitar(self):
        """Limita las posiciones de player para que no salga de la pantalla."""
        self.__point.x = max(self.__point.x, 0)
        self.__point.x = min(self.__point.x, pyxel.width - self.__width)
        self.__point.y = max(self.__point.y, 0)
        self.__point.y = min(self.__point.y, pyxel.height - self.__height)
        
    def __desaparecer(self, lst):
        """Elimina los objetos que no estan vivos de la lista."""
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
    def __pintar_player(self):
        """Pinta el sprite de player subiendo."""
        pyxel.blt(self.__point.x, self.__point.y,
            constants.LOCKHEED_1[0],
            constants.LOCKHEED_1[1] if pyxel.frame_count % 5 == 0 else constants.LOCKHEED_2[1],
            constants.LOCKHEED_1[2],
            constants.LOCKHEED_1[3], constants.LOCKHEED_1[4],
            constants.TRANSPARENTE)
    
    def __pintar_loop(self):
        """Pintar avion haciendo loop."""
        pyxel.blt(self.__point.x, self.__point.y,
            constants.LOCKHEED_LOOP[0], constants.LOCKHEED_LOOP[1], 
            constants.LOCKHEED_LOOP[2], constants.LOCKHEED_LOOP[3], 
            constants.LOCKHEED_LOOP[4], constants.TRANSPARENTE)
    
    def __mover(self):
        """Comprueba el movimiento del jugador."""
        # MOVERSE A LA IZQUIERDA
        if pyxel.btn(pyxel.KEY_LEFT):
            self.__izquierda()
        
        # MOVERSE A LA DERECHA
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.__derecha()
        
        # MOVERSE ARRIBA
        if pyxel.btn(pyxel.KEY_UP):
            self.__subir()
        
        # MOVERSE ABAJO
        if pyxel.btn(pyxel.KEY_DOWN):
            self.__bajar()
    
    def update(self):
        
        # Comprobar si el avion se mueve
        self.__mover()
                
        # Comprobar si esta haciendo un loop
        self.__hacer_loop()

        
        # Limitar posicion de player
        self.__limitar()
        
        # Comprueba si he disparado
        self.__disparar()
        
        # Comprueba la lista de balas para eliminar las balas muertas
        self.__desaparecer(self.__balas)
    
    
    def draw(self):
        # Pintar avion normal
        if self.__loop == False:
            self.__pintar_player()
        
        # Pintar avion haciendo looping
        elif self.__loop == True and pyxel.frame_count - self.__tloop < 10:
            self.__pintar_loop()
        
        # Pasados 10 frames deja de hacer looping
        elif self.__loop == True and pyxel.frame_count - self.__tloop >= 10:
            self.__loop = False
            self.__tloop = False
        
        # Compruebo la lista de balas, en caso de haber las dibujo
        for b in self.__balas:
            b.draw()
