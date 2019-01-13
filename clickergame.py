import pygame
import random
import time

black = (0, 0, 0)
white = (255, 255, 255)
cool_blue = (30, 144, 255)
cooler_blue = (30, 175, 255)
gray = (211, 211, 211)
crimson = (220, 20, 60)
limegreen = (50, 205, 50)
display_width = 1000
display_height = 500

pygame.init()
game_screen = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption('Clicker')
clock = pygame.time.Clock()
max_fps = 60
background_image = pygame.image.load("lightbluebg.jpg")
background_image = pygame.transform.scale(background_image, (display_width, display_height))
instructions_background = pygame.image.load("yellow-background-3.jpg")
instructions_background = pygame.transform.scale(instructions_background, (display_width, display_height))
button_text = pygame.font.Font("Quicksand-Regular.ttf", 15)
bigger_button_text = pygame.font.Font("Quicksand-Regular.ttf", 20)
cool_titletext = pygame.font.Font("Quicksand-Regular.ttf", 50)


image_one = pygame.image.load("animeprgm.png")
image_one = pygame.transform.smoothscale(image_one, (200, 200))
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

def txt_obj(text, font):
    """Creates object for text to be created on"""
    Text_Surface = font.render(text, True, black)
    return Text_Surface, Text_Surface.get_rect()

def start_button(x, y, width, height, old_color, new_color):
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
        self.color = old_color
        self.player_object = player_object
    
    
    def clicked(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.width > mouse[0] > self.x and  self.y + self.height > mouse[1] > self.y:
            self.color = self.new_color
            if click is not None and click[0] == 1:
                self.player_object.inc_score_click()
                print("Clicks of Productivity: ", self.player_object.get_score())
                return True
        else:
            self.color = self.old_color
            return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        txt_surface, txt_rect = txt_obj(self.message, button_text)
        txt_rect.center = ((self.x + (self.width/2)), (self.y + (self.height/2)))
        screen.blit(txt_surface, txt_rect)

class Clicker(Player):
    """Clicker button"""
    def __init__(self):
        self.growth_value = 1/15
        self.dec_value = 5
        self.multiplier = 2
        Player.__init__(self)
    
    def inc_score_click(self):
        self.player_attributes['score'] += 1 
        return(self.player_attributes['score'])
    
    def inc_score_tick(self):
        self.player_attributes['score'] += self.growth_value
        return(self.player_attributes['score'])
    
    def get_pps(self):
        return(str(round(self.growth_value * 15, 3)))
    
    def dec_score1(self):
        self.player_attributes['score'] -= self.dec_value
        return(self.player_attributes['score'])
    
    def dec_score1_5(self):
        self.player_attributes['score'] -= self.dec_value * 23/5
        return(self.player_attributes['score'])
    
    def dec_score2(self):
        self.player_attributes['score'] -= self.dec_value * 20
        return(self.player_attributes['score'])

    def dec_score3(self):
        self.player_attributes['score'] -= self.dec_value * 50
        return(self.player_attributes['score'])

    def dec_score4(self):
        self.player_attributes['score'] -= self.dec_value * 100
        return(self.player_attributes['score'])
    
    def dec_score5(self):
        self.player_attributes['score'] -= self.dec_value * 150
        return(self.player_attributes['score'])
    
    def dec_score6(self):
        self.player_attributes['score'] -= self.dec_value * 300
        return(self.player_attributes['score'])
    
    def upgrade_inc1(self):
        self.growth_value *= self.multiplier
    
    def upgrade_inc2(self):
        self.growth_value *= (self.multiplier * 2)

    def upgrade_inc3(self):
        self.growth_value *= (self.multiplier * 4)


clicker = Clicker()

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
        txt_surface, txt_rect = txt_obj("Welcome to Productivity Clicker", cool_titletext)
        txt_rect.center = ((display_width/2), (display_height/2))
        game_screen.blit(txt_surface, txt_rect)
        

        start_button(400, 300, 250, 50, cool_blue, cooler_blue)
        button_text = pygame.font.Font("Quicksand-Regular.ttf",30)
        txt_surface, txt_rect = txt_obj("Start", button_text)
        txt_rect.center = ((400+(250/2)), (300+(50/2)))
        game_screen.blit(txt_surface, txt_rect)
        game_screen.blit(image_one, (200, 300))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 400 + 250 > mouse[0] > 400 and  300 + 50 > mouse[1] > 300:
            if click != None and click[0] == 1:
                print("hi")
                game_screen.fill(white)
                pygame.display.update()
                break
            
        pygame.display.update()
        clock.tick(max_fps)

def return_instructions1():
    """Blits instructions pt.1"""
    txt_surface, txt_rect = txt_obj("You have midterms soon, but you aren't being too productive.", bigger_button_text)
    txt_rect.center = ((display_width/2), (display_height/2))
    game_screen.blit(txt_surface, txt_rect)

def return_instructions2():
    """Blits instructions pt.2"""
    txt_surface, txt_rect = txt_obj("All you gotta do is click to get more productivity.", bigger_button_text)
    txt_rect.center = ((display_width/2), ((display_height/2) + 100))
    game_screen.blit(txt_surface, txt_rect)

def instructions():
    """Instructions page"""
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
        
        game_screen.blit(instructions_background, [0, 0])
        txt_surface, txt_rect = txt_obj("Instructions", cool_titletext)
        txt_rect.center = ((display_width/2), (display_height/2 - 100))
        game_screen.blit(txt_surface, txt_rect)
        return_instructions1()
        return_instructions2()
        ok_button = Button(375, 400, 250, 50, "Let's get this bread.", limegreen, limegreen, clicker)
        ok_button.draw(game_screen)
        if ok_button.clicked():
            done = True
        pygame.display.update()
        clock.tick(max_fps)


prod_button = Button(200, 300, 250, 50, "Click to increase productivity!", cool_blue, cooler_blue, clicker)
upgrade1 = Button(500, 100, 250, 50, "Buy a helpful colleague: 5 Prod.", gray, cooler_blue, clicker)
upgrade1_5 = Button(500, 100, 450, 50, "Buy the unintelligent creator of this game: 23 Prod.", gray, cooler_blue, clicker)
upgrade2 = Button(500, 200, 350, 50, "Buy the smartest kid in the grade: 100 Prod.", gray, cooler_blue, clicker)
upgrade3 = Button(500, 300, 250, 50, "Buy Slader: 250 Prod.", gray, cooler_blue, clicker)
upgrade4 = Button(500, 400, 400, 50, "Buy Shia LaBeouf inspiration DVD: 500 Prod.", gray, cooler_blue, clicker)
upgrade5 = Button(500, 100, 250, 50, "Buy a teacher: 750 Prod.", gray, cooler_blue, clicker)
upgrade6 = Button(500, 200, 250, 50, "Buy teacher's entire lesson plans: 1500 Prod.", gray, cooler_blue, clicker)

def return_clicks():
    txt_surface, txt_rect = txt_obj("Clicks of Productivity: " + clicker.get_score(), button_text)
    txt_rect.center = ((200+(250/2)), (225+(50/2)))
    game_screen.blit(txt_surface, txt_rect)

def return_pps():
    txt_surface, txt_rect = txt_obj("Productivity per Second: " + clicker.get_pps(), button_text)
    txt_rect.center = ((200 + (250/2), (175 + (50/2))))
    game_screen.blit(txt_surface, txt_rect)

def start_game():
    """Running game, WIP"""

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                quit()
                
        game_screen.blit(background_image, [0, 0])
                
        prod_button.clicked()
        return_clicks()
        return_pps()
        clicker.inc_score_tick()
        prod_button.draw(game_screen)
        upgrade1.draw(game_screen)
        if int(clicker.get_score()) >= 5:
            upgrade1.clicked()
            if upgrade1.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score1()
                loop = False
        pygame.display.update()
        clock.tick(15)
        
def part_2():
    """After upgrade1 is clicked"""
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                quit()
        
        game_screen.blit(background_image, [0, 0])
        prod_button.clicked()
        return_clicks()
        return_pps()
        clicker.inc_score_tick()
        if int(clicker.get_score()) >= 23:
            upgrade1_5.clicked()
            if upgrade1_5.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score1_5() 
                loop = False
        elif int(clicker.get_score()) >= 100:
            upgrade2.clicked()
            if upgrade2.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score2()
                loop = False
        prod_button.draw(game_screen)
        upgrade1_5.draw(game_screen)
        upgrade2.draw(game_screen)
        pygame.display.update()
        clock.tick(15)

def part_3():
    """After upgrade1_5 or 2 is clicked"""
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                quit()
        
        game_screen.blit(background_image, [0, 0])
        prod_button.clicked()
        return_clicks()
        return_pps()
        clicker.inc_score_tick()
        if int(clicker.get_score()) >= 100:
            upgrade2.clicked()
            if upgrade2.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score2()
                loop = False
        elif int(clicker.get_score()) >= 250:
            upgrade3.clicked()
            if upgrade3.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score3()
                loop = False
        prod_button.draw(game_screen)
        upgrade2.draw(game_screen)
        upgrade3.draw(game_screen)
        pygame.display.update()
        clock.tick(15)

def part_4():
    """After upgrade2 or 3 is clicked"""
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                quit()
        
        game_screen.blit(background_image, [0, 0])
        prod_button.clicked()
        return_clicks()
        return_pps()
        clicker.inc_score_tick()
        if int(clicker.get_score()) >= 250:
            upgrade3.clicked()
            if upgrade3.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score3()
                loop = False
        elif int(clicker.get_score()) >= 500:
            upgrade4.clicked()
            if upgrade4.clicked():
                clicker.upgrade_inc2()
                clicker.dec_score4()
                loop = False
        prod_button.draw(game_screen)
        upgrade3.draw(game_screen)
        upgrade4.draw(game_screen)
        pygame.display.update()
        clock.tick(15)

def part_5():
    """After upgrade3 or 4 is clicked"""
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                quit()
        
        game_screen.blit(background_image, [0, 0])
        prod_button.clicked()
        return_clicks()
        return_pps()
        clicker.inc_score_tick()
        if int(clicker.get_score()) >= 500:
            upgrade4.clicked()
            if upgrade4.clicked():
                clicker.upgrade_inc2()
                clicker.dec_score4()
                loop = False
        elif int(clicker.get_score()) >= 750:
            upgrade5.clicked()
            if upgrade5.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score5()
                loop = False
        prod_button.draw(game_screen)
        upgrade4.draw(game_screen)
        upgrade5.draw(game_screen)
        pygame.display.update()
        clock.tick(15)

def part_6():
    """After upgrade4 is clicked"""
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                quit()
        
        game_screen.blit(background_image, [0, 0])
        prod_button.clicked()
        return_clicks()
        return_pps()
        clicker.inc_score_tick()
        if int(clicker.get_score()) >= 750:
            upgrade5.clicked()
            if upgrade5.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score5()
                loop = False
        elif int(clicker.get_score()) >= 1500:
            upgrade6.clicked()
            if upgrade6.clicked():
                clicker.upgrade_inc1()
                clicker.dec_score6()
                loop = False
        prod_button.draw(game_screen)
        upgrade5.draw(game_screen)
        upgrade6.draw(game_screen)
        pygame.display.update()
        clock.tick(15)

game_intro()
instructions()
start_game()
part_2()
part_3()
part_4()
part_5()
part_6()
pygame.quit()


# Seize the means of production