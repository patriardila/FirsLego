import pgzrun
import time
import random
from pgzero.actor import Actor
WIDTH = 800
HEIGHT = 600
FPS=30
TITLE= "FIRST DAY"

mode = "start"


background = Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\fondo.png")
inicio= Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\check.png",(20,20))
titlejuego=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\titlehome.png",(350,60))
boton=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\homeempezar.png",(350,320))
title=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\titulo.png",(350,130))
pantalla2=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\mapa.jpg")
hombre= Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\hombre.png")
personaje= Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\mujer.png",(200,300))
mujer= Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\mujer.png",(30,300))
cancha=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\cancha.jpg")
balon=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\balon.png",(250,350))
def draw():
    global mode
    if mode == "start":
        background.draw()
        titlejuego.draw()
        boton.draw()
        title.draw()
        inicio.draw()
    elif mode=="pantalla2":
        pantalla2.draw()
        inicio.draw()
        hombre.draw()
        mujer.draw()
    elif mode=="cancha":
        cancha.draw()
        personaje.draw()
        balon.draw()
        

def on_mouse_down(button, pos):
    global mode
    if button == mouse.LEFT and mode == 'start':
        if inicio.collidepoint(pos):
            inicio.y = 15
        elif boton.collidepoint(pos):
            mode = "pantalla2"
    elif button == mouse.LEFT and mode == 'pantalla2':
        if mujer.collidepoint(pos):
            personaje.image = "mujer"
            mode = "cancha"
        elif hombre.collidepoint(pos):
            personaje.image = "hombre"
            mode = "cancha"
def on_key_down(key):
    if keyboard.up and personaje.y > 80:
        personaje.y = personaje.y - 25
        #NOTA PARA LOS TUTORES: este control debe ser utilizado 
        #¡para que la plataforma siga funcionando correctamente! Por favor, no lo ignore.
    elif keyboard.down and personaje.y<500:
        personaje.y=personaje.y+25 
    elif keyboard.right and personaje.x < 580:
        personaje.x = personaje.x + 25

def update():
    global mode
    if mode == "cancha":
        # Verifica si el personaje toca el balón
        if personaje.collidepoint(balon.x, balon.y):
            # Mueve el balón a una posición aleatoria de la pantalla
            time.sleep(1)
            balon.x = random.randint(0, WIDTH)
            balon.y = random.randint(0, HEIGHT)

pgzrun.go()     


pgzrun.go()

            
          
            
            
        
    
    