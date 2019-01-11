import pygame
import random

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
max_fps = 60
background_image = pygame.image.load("lightbluebg.jpg")
background_image = pygame.transform.scale(background_image, (1000, 500))

image_one = pygame.image.load("animeprgm.png")
image_two = pygame.image.load("motivation.png")
image_three = pygame.image.load("productivity.png")

image_list = [image_one, image_two, image_three]
x_ = random.randint(0, 800)
y_ = random.randint(0, 400)

display_rdmImg = random.choice(image_list)
display_rdmImg = pygame.transform.scale(display_rdmImg, (70, 80))

class Player:
    """Return a new person object"""
    player_attributes = {}
    player_attributes['score'] = 0

    def __init__(self):
        self.player_attributes['score'] = 0

    def get_score(self):
        return(str(round(self.player_attributes['score'])))

    def inc_score_tick(self):
        self.player_attributes['score'] += 1/15
        return(self.player_attributes['score'])

    def inc_score_click(self):
        self.player_attributes['score'] += 1
        return(self.player_attributes['score'])

    def dec_score(self):
        self.player_attributes['score'] -= 1
        return(self.player_attributes['score'])

class Upgrade1(Player):
    """First button upgrade"""
    def __init__(self):
        Player.__init__(self)
    
    def inc_score(self):
        self.player_attributes['score'] += 9
        return(self.player_attributes['score']) 

class Upgrade2(Player):
    """Second button upgrade"""
    def __init__(self):
        Player.__init__(self)
    

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
    pygame.draw.rect(game_screen, old_color,(x, y, width, height))
    if x + width > mouse[0] > x and  y + height > mouse[1] > y:
        pygame.draw.rect(game_screen, new_color, (x, y , width, height))
    else:
        pygame.draw.rect(game_screen, old_color,(x, y, width, height))

class Button(pygame.Rect):
    """Button class for any button after menu screen"""
    def __init__(self, x, y, width, height, message, old_color, new_color, player_object):
        super().__init__(x, y, width, height)
        self.message = message
        self.old_color = old_color
        self.new_color = new_color
        self.player_object = player_object
    
    def clicked(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(game_screen, self.old_color, (self.x, self.y, self.width, self.height))
        if self.x + self.width > mouse[0] > self.x and  self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(game_screen, self.new_color, (self.x, self.y , self.width, self.height))
            if click != None and click[0] == 1:
                self.player_object.inc_score_click()
                print("Clicks of Productivity: ", self.player_object.get_score())
                pygame.display.update()
                clock.tick(max_fps)
        else:
            pygame.draw.rect(game_screen, self.old_color, (self.x, self.y, self.width, self.height))
        
        button_text = pygame.font.Font("Quicksand-Regular.ttf", 15)
        txt_surface, txt_rect = txt_obj(self.message, button_text)
        txt_rect.center = ((self.x + (self.width/2)), (self.y + (self.height/2)))
        game_screen.blit(txt_surface, txt_rect)




def game_intro():
    """Main menu screen"""
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                break
                
        game_screen.fill(white)
        cool_titletext = pygame.font.Font("Quicksand-Regular.ttf", 50)
        txt_surface, txt_rect = txt_obj("Welcome to Productivity Clicker", cool_titletext)
        txt_rect.center = ((display_width/2), (display_height/2))
        game_screen.blit(txt_surface, txt_rect)
        
        start_button = startButton
        start_button(400, 300, 250, 50, cool_blue, cooler_blue)
        button_text = pygame.font.Font("Quicksand-Regular.ttf",30)
        txt_surface, txt_rect = txt_obj("Start", button_text)
        txt_rect.center = ((400+(250/2)), (300+(50/2)))
        game_screen.blit(txt_surface, txt_rect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 400 + 250 > mouse[0] > 400 and  300 + 50 > mouse[1] > 300:
            if click != None and click[0] == 1:
                print("hi")
                game_screen.fill(white)
                pygame.display.update()
                break
                # start_game()
                # done = True
                # return None
            

        pygame.display.update()
        clock.tick(max_fps)



def start_game():
    """Running game, WIP"""
    initial_button = Player()
    button1 = Upgrade1()
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                break
        
        game_screen.blit(background_image, [0, 0])
                
        button_text = pygame.font.Font("Quicksand-Regular.ttf", 15)
        prod_button = Button(200, 300, 250, 50, "Click to increase productivity!", cool_blue, cooler_blue, initial_button)
        upgrade1 = Button(300, 400, 250, 50, "Buy something", cool_blue, cooler_blue, button1)
        prod_button.clicked()
        upgrade1.clicked()
        txt_surface, txt_rect = txt_obj("Clicks of Productivity: " + initial_button.get_score(), button_text)
        txt_rect.center = ((200+(250/2)), (225+(50/2)))
        game_screen.blit(txt_surface, txt_rect)
        initial_button.inc_score_tick() 
        pygame.display.update()
        clock.tick(15)
        
game_intro()
start_game()
pygame.quit()

# Seize the means of production