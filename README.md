# Arcade1942
This project is a recreation of the game **1942** in Python, utilizing the **Pyxel** graphics library for visual representation. The game involves controlling an aircraft that can move across the screen, shoot at enemies, and avoid getting shot down.
## Class Design
The project has been developed following the Object-Oriented Programming (OOP) paradigm and features the following class design:
**Game**: The main class responsible for running the game and managing scenes.
Intro: Creates the game introduction.
**Island**: Represents the islands in the background of the game.
Point: Computes the coordinates (x, y) of an object.
**Player**: Creates and controls the main player.
**Enemy**: A base class for all enemies, with common attributes and methods.
**Regular, Bombardier, Superbombardier**: Classes for different types of enemies.
**Red**: A class for a special enemy that moves in circles.
**Bullet**: Represents bullets fired by players and enemies.
**Explosion**: Generates explosions when bullets hit enemies.
**Level**: Manages the creation of objects in the game.
**Gameover**: Displays the Game Over screen.
## Key Algorithms
The main algorithms employed in this project include:
Creation of enemy and bullet lists.
Animation of propellers on aircraft.
Player and enemy movement control.
Collision detection and impact detection.
Circular movement for the "Red" enemy.
