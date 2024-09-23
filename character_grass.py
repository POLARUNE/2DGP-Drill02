from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')


x = 0
y = 0


while(True):
    while(x<760):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x , 90)
        x = x+20
        delay(0.01)

    while(y<560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(760 , y)
        y = y+20
        delay(0.01)
        
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 560)
        x = x-20
        delay(0.01)

    while(y>90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(30 , y)
        y = y-20
        delay(0.01)

    while(x<=400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x , 90)
        x = x+20
        delay(0.01)


    while(True):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        
        x = x+math.cos(x)
        y = y+math.sin(y)
        
        delay(0.01)
        

    
close_canvas()
