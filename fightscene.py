import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
cool_blue = (30, 144, 255)
cooler_blue = (30, 175, 255)
gray = (211, 211, 211)
crimson = (220, 20, 60)
red = (255, 0, 0)
limegreen = (50, 205, 50)
display_width = 1000
display_height = 500
cool_titletext = pygame.font.Font("Quicksand-Regular.ttf", 20)


game_screen = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption('Clicker')
clock = pygame.time.Clock()
person = pygame.image.load("blueperson.png").convert_alpha()
communistpic = pygame.image.load("communistguy.png").convert_alpha()

all_sprites_list = pygame.sprite.Group()

def txt_obj(text, font):
    """Creates object for text to be created on"""
    Text_Surface = font.render(text, True, black)
    return Text_Surface, Text_Surface.get_rect()

def display_message(text, x, y):
    txt_surface, txt_rect = txt_obj(text, cool_titletext)
    txt_rect.center = (x, y)
    game_screen.blit(txt_surface, txt_rect)
    pygame.display.update()

class Sprite(pygame.sprite.Sprite):
    """Basic objects"""
    def __init__(self, width, height):
        super().__init__()
        self.image = person
        self.rect = self.image.get_rect()
        self.attack = 50
       
    def draw(self):
        game_screen.blit(self.image, (25, 100))
        pygame.display.update()
        clock.tick(10)

    def attack(self, opponent):
        damage = self.attack
        opponent.hp -= damage
        display_message(f"You attack with {damage}!", 1000, 800)
        display_message(f"Communist has {opponent.hp} health. Keep pressing spacebar!", 1000, 700)
        pygame.display.update()

class Communist(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = communistpic
        self.rect = self.image.get_rect()
        self.hp = 50000

    def draw(self):
        game_screen.blit(self.image, (425, -50))
        pygame.display.update()
        clock.tick(10)
    
    def displayhp(self):
        display_message(f"Communist HP: {self.hp}", 250, 150)
        pygame.display.update()
    

person1 = Sprite(250, 50)
red_guy = Communist(250, 50)
game_screen.fill(white)
red_guy.draw()
person1.draw()
display_message("You are pitted against a communist!", 500, 175)
display_message("Keep hitting spacebar to attack", 500, 200)
game = True
while game:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                quit()
    
    red_guy.displayhp()
    key = pygame.key .get_pressed()
    if key[pygame.K_SPACE]:
        person1.attack(red_guy)
    pygame.display.update()
    clock.tick(10)
