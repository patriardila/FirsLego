import pgzrun
import time
import random
import math
from pgzero.actor import Actor
from pgzero import clock
WIDTH = 800
HEIGHT = 600
FPS=30
TITLE= "FIRST DAY"

mode = "start"
score=0
background = Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\fondo.png")
bton_start= Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\check.png",(20,20))
titlejuego=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\titlehome.png",(350,60))
bton_home=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\homeempezar.png",(350,320))
title_home=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\titulo.png",(350,130))
screen2=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\fondo2.png")
ian= Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\personaje_ian.png",(300,300))
character= Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\personaje_ian.png")
any= Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\personaje_any.png",(500,300))
cancha=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\cancha.jpg")
ball=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\balon.png",(405,350))
map_levels=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\map_levels.png")
soccer=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\soccer.png")
soccer_arch=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\soccer_arch.png",(400,200))
eagle=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\eagle.png",(30,60))
background_info=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\background_info")
close=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\close.png",(700,100))
close1=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\close.png",(700,300))
any_talk=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\any_talk.png",(750,500))
next=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\avanzar.png",(750,550))
# Cargar las imágenes de los frames de la animación
frame1 = "C:\\Users\\patrardp\\Documents\\FIRST\\images\\frame1.png"
frame2 = "C:\\Users\\patrardp\\Documents\\FIRST\\images\\frame2.png"  
frame3 = "C:\\Users\\patrardp\\Documents\\FIRST\\images\\frame2.png" 
character.images = {"frame1": frame1, "frame2": frame2, "frame3": frame3}

cuadro_instrucciones = Rect((100, 100), (600, 200))
cuadro_instrucciones1 = Rect((100, 300), (600, 200))
sentences = ["SOY EL CONDOR y tu misión es ayudarme a encontrar mis PODERES:.", "1: Pasa por algunos lugares de mi COLEGIO.", "2: Realizar los RETOS que allí se proponen.", "3: Y MIS PODERES quedarán en mi MOCHILA"]
sentence2=["CLARO, TE AYUDARÉ¡¡", "1:Resolveré los RETOS y te ayudaré a encontrar tus PODERES", "2. Tambien conoceré tu colegio", "3. Y la forma cómo TE DIVIERTES en tu COLEGIO"]
show_phrase=False
show_phrase2=False
show_phrase_character=False
current_phrase=0
current_phrase2=0

def show_sentences():
    global show_phrase, current_phrase
    if current_phrase< len(sentences):
        show_phrase = True
        clock.schedule_unique(next_sentence, 1.0)  # Muestra la siguiente frase después de 1 segundo
        current_phrase += 1



def next_sentence():
    global show_phrase,  current_phrase
    if current_phrase < len(sentences):
        clock.schedule_unique(show_sentences, 1.0) 

def show_sentences2():
    global show_phrase2, current_phrase2
    if current_phrase2< len(sentence2):
        show_phrase2 = True
        clock.schedule_unique(next_sentence2, 1.0)  # Muestra la siguiente frase después de 1 segundo
        current_phrase2 += 1

def next_sentence2():
    global show_phrase2,  current_phrase2
    if current_phrase2 < len(sentence2):
        clock.schedule_unique(show_sentences2, 1.0) 


# Cargar los frames de la animación de caminar
frames = [f"frame{i}" for i in range(1, 4)]
current_frame = 0

# Crear el personaje
character = Actor(frames[current_frame])

def update_frame():
    global current_frame
    # Cambiar al siguiente frame
    current_frame = (current_frame + 1) % len(frames)
    character.image = frames[current_frame]


def draw():
    global mode
    if mode == "start":
        background.draw()
        titlejuego.draw()
        bton_home.draw()
        title_home.draw()
        bton_start.draw()
    elif mode=="character_menu":
        screen2.draw()
        ian.draw()
        any.draw()
    
    elif mode=="menu_levels_info":
        background_info.draw() 
        eagle.draw()
        any_talk.draw()
        next.draw()
        if show_phrase==True:
            
            screen.draw.filled_rect(cuadro_instrucciones, (255, 255, 255))
            y = cuadro_instrucciones.top + 10
            line_height = 30
            
            for i in range(current_phrase):
                screen.draw.text(sentences[i], (cuadro_instrucciones.left + 10, y), color="black") 
                # Dibuja las frases una debajo de la otra
                y += line_height
                close.draw()

        if show_phrase2==True:
            screen.draw.filled_rect(cuadro_instrucciones1, (255, 255, 255))
            y = cuadro_instrucciones1.top + 10
            line_height = 30
            
            for i in range(current_phrase2):
                screen.draw.text(sentence2[i], (cuadro_instrucciones.left + 10, y), color="black") 
                # Dibuja las frases una debajo de la otra
                y += line_height
                close1.draw()

    elif mode=="menu_levels":
        map_levels.draw()
        eagle.draw()
        character.draw()
                

        
    elif mode=="soccer":
        soccer.draw()
        screen.draw.text(str(score), center=(30, 20), color="white", fontsize = 36)
        ball.draw()
        soccer_arch.draw()

    
def on_mouse_down(button, pos):
    global mode
    global show_phrase
    global show_phrase2
    if button == mouse.LEFT and mode == 'start':
        if bton_start.collidepoint(pos):
            bton_start.y = 15
        elif bton_home.collidepoint(pos):
            mode = "character_menu"
    elif button == mouse.LEFT and mode == 'character_menu':
        if any.collidepoint(pos):
            character.image = "personaje_any"
            mode = "menu_levels_info"
        elif ian.collidepoint(pos):
           character.image = "ian_3"
           mode = "menu_levels_info"
    elif button == mouse.LEFT and mode == "menu_levels_info":
        if eagle.collidepoint(pos):
            show_sentences()   
        elif close.collidepoint(pos):
            
            show_phrase=False
        elif any_talk.collidepoint(pos):
            show_sentences2()
    
        elif close1.collidepoint(pos):
            show_phrase2=False   
            print("Close1 clicked")

        elif next.collidepoint(pos):
            mode="menu_levels"
            character.x=750
            character.y=50
       

        
    elif button == mouse.LEFT and mode == 'soccer':
        if ball.collidepoint(pos):
            target_x = random.randint(600, 700)
            target_y = random.randint(300, 500)
    
def on_key_down(key):
  
    
    if keyboard.down and character.y<550:
        character.y=character.y+25 
        update_frame() 
    elif keyboard.up and character.x<800:
        character.y= character.y-25

    elif keyboard.right and character.x < 580:
        character.x = character.x + 25
    elif keyboard.left and character.x > 20:
        character.x = character.x -25 

pgzrun.go()     




            
          
            
            
        
    
    