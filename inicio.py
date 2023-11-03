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
eagle=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\condortalk",(300,450))
background_info=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\background_info")
close=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\close.png",(700,100))
close1=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\close1.png",(700,100))
close2=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\close2.png",(700,100))
any_talk=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\any_talk1.png",(750,500))
next=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\avanzar.png",(750,500))
info_play=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\cuadro_info",(750,500))
backpack_info=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\mochila_info",(500,450))
coin1=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\moneda2.png",(250,280))
coin2=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\moneda1.png",(80,430))
coin3=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\moneda3.png",(90,140))
coin4=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\moneda4.png",(570,180))
path=Actor("C:\\Users\\patrardp\\Documents\\FIRST\\images\\camino.png")
# Cargar las imágenes de los frames de la animación
frame1 = "C:\\Users\\patrardp\\Documents\\FIRST\\images\\frame1.png"
frame2 = "C:\\Users\\patrardp\\Documents\\FIRST\\images\\frame2.png"  
frame3 = "C:\\Users\\patrardp\\Documents\\FIRST\\images\\frame3.png" 
character.images = {"frame1": frame1, "frame2": frame2, "frame3": frame3}
show_text_coin1=False
show_text_coin2=False
show_text_coin3=False
show_text_coin4=False


# Cargar los frames de la animación de caminar
frames = [f"frame{i}" for i in range(1, 4)]
current_frame = 0

# Crear el personaje para caminar 
character = Actor(frames[current_frame])

def update_frame():
    global current_frame
    # Cambiar al siguiente frame
    current_frame = (current_frame + 1) % len(frames)
    character.image = frames[current_frame]



sentences = ["SOY EL CONDOR","Ayudame a encontrar mis PODERES", "1: Pasa por algunos lugares de mi COLEGIO.", "2: Realizar los RETOS que allí se proponen.", "3: Y MIS PODERES quedarán en mi MOCHILA"]
sentence2=["CLARO, TE AYUDARÉ¡¡", "1:Resolveré los RETOS y te ayudaré a encontrar tus PODERES", "2. Tambien conoceré tu colegio", "3. Y la forma cómo TE DIVIERTES en tu COLEGIO"]
sentence3=["LA MOCHILA", "Guarda los PODERES obtenidos en cada RETO", "Aquí podrás RECARGARTE de ENERGIA", "Debes dar CLICK sobre cada PODER que esta en la MOCHILA"]
#Variable para activar los cuadros de información que estan en el modo "menu_levels_info"
show_phrase=False
show_phrase2=False
show_phrase3=False

show_phrase_character=False
#variables que almacena la posición de cada frase que aparecerá en los cuadros de información en el modo "menu_levels_info"
current_phrase=0
current_phrase1=0
current_phrase2=0


#Funciones que permiten mostrar las frases en los cuadros de información una debajo de la otra y por timepos
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
    global show_phrase2, current_phrase1
    if current_phrase1< len(sentence2):
        show_phrase2 = True
        clock.schedule_unique(next_sentence2, 1.0)  # Muestra la siguiente frase después de 1 segundo
        current_phrase1 += 1
def next_sentence2():
   
    if current_phrase1 < len(sentence2):
        clock.schedule_unique(show_sentences2, 1.0) 
def show_sentences3():
    global show_phrase3, current_phrase2
    if current_phrase2< len(sentence3):
        show_phrase3 = True
        clock.schedule_unique(next_sentence3, 1.0)  # Muestra la siguiente frase después de 1 segundo
        current_phrase2 += 1
def next_sentence3():
   
    if current_phrase2 < len(sentence3):
        clock.schedule_unique(show_sentences3, 1.0) 




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
        character.draw()
        next.draw()
        backpack_info.draw()
        if show_phrase==True:
            
            info_play.draw()
            y = info_play.top + 30
            line_height = 30
            
            for i in range(current_phrase):
                screen.draw.text(sentences[i], (info_play.left + 25, y), color="black") 
                # Dibuja las frases una debajo de la otra
                y += line_height
                close.draw()

        elif show_phrase2==True:
            info_play.draw()
            y = info_play.top + 30
            line_height = 30
            
            
            for i in range(current_phrase1):
                screen.draw.text(sentence2[i], (info_play.left + 25, y), color="black") 
                # Dibuja las frases una debajo de la otra
                y += line_height
                close1.draw()

        elif show_phrase3==True:
            info_play.draw()
            y = info_play.top + 30
            line_height = 30
            
            
            for i in range(current_phrase2):
                screen.draw.text(sentence3[i], (info_play.left + 25, y), color="black") 
                # Dibuja las frases una debajo de la otra
                y += line_height
                close2.draw()

    elif mode=="menu_levels":
        map_levels.draw()
        path.draw()
        
        
        coin1.draw()
        coin2.draw()
        coin3.draw()
        coin4.draw()
        character.draw()   
        screen.draw.text("da clic sobre cada moneda", center=(500, 80), color="white", fontsize = 25) 
        screen.draw.text("para conocer su poder", center=(500,100 ), color="white", fontsize = 25) 
        if show_text_coin1:
            screen.draw.text("Poder de velocidad", center=(250, 250), color="white", fontsize = 16) 
        elif show_text_coin2:
            screen.draw.text("Poder de volar", center=(80, 380), color="white", fontsize = 16) 
        elif  show_text_coin3:
            screen.draw.text("Poder de la fuerza", center=(90, 120), color="white", fontsize = 16) 
        elif show_text_coin4:
            screen.draw.text("Poder de la resistencia", center=(579, 160), color="white", fontsize = 16) 
        
    elif mode=="soccer":
        soccer.draw()
        screen.draw.text(str(score), center=(30, 20), color="white", fontsize = 36)
        ball.draw()
        soccer_arch.draw()

   
            
def on_mouse_down(button, pos):
    global mode
    global show_phrase
    global show_phrase2
    global show_phrase3
    global show_text_coin1, show_text_coin2, show_text_coin3, show_text_coin4
    if button == mouse.LEFT and mode == 'start':
        if bton_start.collidepoint(pos):
            bton_start.y = 15
        elif bton_home.collidepoint(pos):
            mode = "character_menu"
    elif button == mouse.LEFT and mode == 'character_menu':
        if any.collidepoint(pos):
            character.image = "any_talk1"
            character.x= 400
            character.y=450
            mode = "menu_levels_info"

        elif ian.collidepoint(pos):
            character.image = "ian_talk1"
            character.x= 400
            character.y=450
            mode = "menu_levels_info"

    elif  mode == "menu_levels_info":
        if eagle.collidepoint(pos):
            show_sentences()  
            info_play.x=400 
            info_play.y=200
        elif close.collidepoint(pos):
            show_phrase=False
    
        if character.collidepoint(pos):
            
            show_sentences2()
            info_play.x=400 
            info_play.y=200
    
        elif close1.collidepoint(pos):
            print("Close1 clicked")
            show_phrase2=False 
    
            
        if backpack_info.collidepoint(pos):
            show_sentences3()
            info_play.x=400 
            info_play.y=200
    
        elif close2.collidepoint(pos):
            show_phrase3=False   
            print("Close1 clicked")

        elif next.collidepoint(pos):
            mode="menu_levels"
            if character.image=="ian_talk1":
                character.image="ian_3"
                character.x=750
                character.y=50
            elif character.image=="any_talk1":
                character.image="any_walk1"
                character.x=750
                character.y=50
        
    elif mode=="menu_levels":

        if  coin1.collidepoint(pos):
            show_text_coin1 = not show_text_coin1
        elif  coin2.collidepoint(pos):
            show_text_coin2 = not show_text_coin2
        elif  coin3.collidepoint(pos):
            show_text_coin3 = not show_text_coin3
        elif  coin4.collidepoint(pos):
            show_text_coin4 = not show_text_coin4


def collisiones():
    global mode
    if mode == "menu_levels":
        if coin1.colliderect(character):
            mode = "soccer"

def on_key_down(key):
    if keyboard.down:
        if character.colliderect(path) and character.x==750 or character.x==80 or character.x==530 or character.x==340:
            update_frame()
            character.y += 10
    elif  keyboard.up:
        if character.colliderect(path) and character.x==530 or character.x==340 or character.x==750 or character.x==80:
            character.y -= 10
            update_frame()
    elif  keyboard.right:
        if character.colliderect(path):
            character.x += 10
            update_frame()
    elif keyboard.left:
        if character.colliderect(path):
            character.x -= 10 
            update_frame()
        


def update():
    collisiones()
    
     
    



pgzrun.go()   





            
          
            
            
        
    
    