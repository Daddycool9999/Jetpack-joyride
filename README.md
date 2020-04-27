# Jetpack-joyride
The game of Jetpack Joyride using python3 without use of any external libraries.


# JetpackJoyride
### How to run:
    python3 background.py
### Packages required:
    colorama
    pip3 install colorama
### About Jetpack Joyride:
    Jetpack Joyride is a 2011 side-scrolling endless runner action video game created 
    by Halfbrick Studios. The game features the same protagonist from Monster Dash,
    Barry Steakfries, who the player controls as he steals a jet pack from a top-secret laboratory. 
    The game has been met with very favorable reviews, and has won numerous awards.
### About Game:
   * This is an interactive game with numerous features.
   * You are given about 2 mins to win the game.
   * Random generation of all elements.
   * Random ordering of various hurdles
   * Smooth physics simulation
   * Bullet implementation, which shoots bullets towards players.
   * Smart enemy, boss which always tries to follows Mondo
   * Coins can be collected
   * Colors for characters
   * Follow OOP concepts
   * Powerups like Shields and Nitros.
    
### Description of files:
* coin.py
  
  This file contains class of coin.

* getch.py
  
  This file is for taking input

* a.txt
  
  This file contains ascii art of Game Over.

* b.txt

  This ile contains ascii art of Win.

* alarmexception.py
  
  This file is for exception

* character.txt
  
  This file contains class of person,mando and boss enemy.

* assignment_1.pdf

* __pycache__

* base.py
  
  This file creates the background of the game.

* background.py
  
  This file contains the main loop.

* nitro.py
  
  This file contains the class for the boost powerup

* bullet.py
  
  This file contains the class for bullets of mando and boss enemy

* obstacle.py

  This file contains the class for obstacles.

* magnet.py

  This file contains the class for magnet

* ES.py

  This file has a class containing functions that manage the after game screening


### Inheritance:
  hero and boss classes are inherited from person in character.py.
### Encapsulation :
  The fact that I’m using classes and objects suffice for this!
### Abstraction :
  This is used in hero,person,bullet etc many class.
### Polymorphism:
  gravity and scoreprint functions are only applied for hero class not for it's parent class-person, so they are changing for them.
### Controls:
w for up,d for right, a for left, b for shoot, space for shield.
