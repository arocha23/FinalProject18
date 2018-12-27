import pygame
import sys
import time

black = (0, 0, 0)
white = (255, 255, 255)
cool_blue = (30, 144, 255)
cooler_blue = (30, 175, 255)
display_width = 1000
display_height = 500

pygame.init()
game_screen = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption('Clicker')
clock = pygame.time.Clock()

def txt_obj(text, font):
    """Creates object for text to be created on"""
    Text_Surface = font.render(text, True, black)
    return Text_Surface, Text_Surface.get_rect()

# def display_messages(text, xr, yr):
#     cool_titletext = pygame.Font.font('Quicksand-Regular.ttf', 50)
#     txt_surface, txt_rect = txt_obj(text, cool_titletext)
#     txt_rect.center = (display_width*xr, display_height*yr)
#     game_screen.blit(txt_surface, txt_rect)
#     pygame.display.update()



def startButton(x, y, width, height, old_color, new_color):
    """Used for the start button, enters the game"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(game_screen, old_color,(x, y, width, height))
    if x + width > mouse[0] > x and  y + height > mouse[1] > y:
        pygame.draw.rect(game_screen, new_color, (x, y , width, height))
        if click != None and click[0] == 1:
            print("hi")
    else:
        pygame.draw.rect(game_screen, old_color,(x, y, width, height))

def anyOtherButton(x, y, width, height, old_color, new_color):
    """Will be used for any other button other than the start button."""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(game_screen, old_color,(x, y, width, height))
    if x + width > mouse[0] > x and  y + height > mouse[1] > y:
        pygame.draw.rect(game_screen, new_color, (x, y , width, height))
        if click != None and click[0] == 1:
            print("i need to figure this one out lol")
    else:
        pygame.draw.rect(game_screen, old_color,(x, y, width, height))



def game_intro():
    """Main menu screen"""
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                sys.exit()
                
        game_screen.fill(white)
        cool_titletext = pygame.font.Font("Quicksand-Regular.ttf", 50)
        txt_surface, txt_rect = txt_obj("Welcome to Productivity Clicker", cool_titletext)
        txt_rect.center = ((display_width/2), (display_height/2))
        game_screen.blit(txt_surface, txt_rect)
        
        startButton(400, 300, 250, 50, cool_blue, cooler_blue)
        button_text = pygame.font.Font("Quicksand-Regular.ttf",30)
        txt_surface, txt_rect = txt_obj("Start", button_text)
        txt_rect.center = ((400+(250/2)), (300+(50/2)))
        game_screen.blit(txt_surface, txt_rect)


        pygame.display.update()
        clock.tick(15)


# class Status:
#     def __init__(self, productivity, increment):
#         self.productivity = productivity
#         self.increment = increment
    
#     def is_clicked(self):
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:

def start_game():
    """Running game, WIP"""
    game = True
    while game:
        game_screen.fill(white)

        cool_subtext = pygame.font.Font('Quicksand-Regular.ttf', 50)
        txt_surface, txt_rect = txt_obj("this is where numbers are", cool_subtext)
        txt_rect.center = ((display_width/4),(display_height/4))
        game_screen.blit(txt_surface, txt_rect)
        
game_intro()
time.sleep(1)


pygame.quit()
quit()
