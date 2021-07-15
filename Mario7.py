import pickle
import pygame
from pygame.locals import *
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_height = 1000
screen_width = 1000
screen = pygame.display.set_mode((screen_height, screen_width))
name_of_game = pygame.display.set_caption("Builder", "Builder")

font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)

tile_size = 50
game_over = 1
game_active = False
level = 0
max_levels = 7
score = 0


white = (255, 255, 255)
blue = (0, 0, 255)

image1 = pygame.image.load("sky.png")
image2 = pygame.image.load("sun.png")
image_dead = pygame.image.load("ghost.png")
game_restart = pygame.image.load("restart_btn.png")
game_start = pygame.image.load("start_btn.png")
game_exit = pygame.image.load("exit_btn.png")
game_save = pygame.image.load("save_btn.png")
game_load = pygame.image.load("load_btn.png")

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def reset_level(level):
    Player1.reset(100, screen_height - 130)
    blob_group.empty()
    lava_group.empty()
    exit_group.empty()
    if path.exists(f"level{level}_data"):
        pickle_in = open(f"level{level}_data", 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data)

    return world


class World:
    def __init__(self, data):
        self.worldist = []
        row = 0
        image3 = pygame.image.load('dirt.png')
        image4 = pygame.image.load('grass.png')
        for line in data:
            column = 0
            for item in line:
                if item == 1:
                    img = pygame.transform.scale(image3, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column * tile_size
                    img_rect.y = row * tile_size
                    tile = (img, img_rect)
                    self.worldist.append(tile)
                    # self.worldist.append([set_images,rect])
                if item == 2:
                    img = pygame.transform.scale(image4, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column * tile_size
                    img_rect.y = row * tile_size
                    tile = (img, img_rect)
                    self.worldist.append(tile)
                    # self.worldist.append([set_images,rect])
                if item == 3:
                    blob = Enemy(tile_size * column, tile_size * row + 15)
                    blob_group.add(blob)
                if item == 6:
                    lava = Lava(column * tile_size, row * tile_size + (tile_size // 2))
                    lava_group.add(lava)
                if item == 7:
                    coin = Coin(column * tile_size + (tile_size // 2), row * tile_size + (tile_size // 2))
                    coin_group.add(coin)
                if item == 8:
                    exit = Exit(column * tile_size, row * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                column = column + 1
            row = row + 1

    def draw(self):
        for image in self.worldist:
            screen.blit(image[0], image[1])
            pygame.draw.rect(screen, (255, 255, 255), image[1], 2)


class Player:
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):

        dx = 0
        dy = 0

        if game_over == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                dx -= 5
                self.index += 1
                if self.index >= len(self.guy_images_right):
                    self.index = 0
                self.set_images = self.guy_images_left[self.index]
                self.direction = 1

            if key[pygame.K_RIGHT]:
                dx += 5
                self.index += 1
                if self.index >= len(self.guy_images_right):
                    self.index = 0
                self.set_images = self.guy_images_right[self.index]
                self.direction = -1

            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                if self.direction == 1:
                    self.set_images = self.guy_images_left[0]
                if self.direction == -1:
                    self.set_images = self.guy_images_right[0]

            if key[pygame.K_SPACE] and self.jumped == False and self.jumped_again == False:
                # dy = -15
                self.vel_y = -20
                self.jumped = True

            if key[pygame.K_SPACE] == False:
                self.jumped = False

            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 6
            dy += self.vel_y
            # dy += 1

            # collison
            p = 0
            self.jumped_again = True
            for items in World1.worldist:
                if items[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                if items[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y >= 0:
                        dy = 0
                        self.jumped_again = False
                    if self.vel_y < 0:
                        dy = 0

            self.rect.x += dx
            self.rect.y += dy

            # if self.rect.bottom > screen_height - 50:
            # self.rect.bottom = screen_height -50
            if self.rect.top < 50:
                self.rect.top = 50

            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1

            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1

            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

        elif game_over == -1:
            self.set_images = image_dead
            if self.rect.y > 200:
                self.rect.y -= 5

        screen.blit(self.set_images, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        return game_over

    def reset(self, x, y):
        self.jumped = False
        self.guy_images_right = []
        self.guy_images_left = []
        self.index = 0
        self.angle = 180
        self.jumped_again = True
        i = 1
        while i < 5:
            self.image_right = pygame.image.load(f'guy{i}.png')
            self.set_images_right = pygame.transform.scale(self.image_right, [40, 80])
            self.set_images_left = pygame.transform.flip(self.set_images_right, True, False)
            # self.rect = self.set_images_right.get_rect()
            # self.rect.x = x
            # self.rect.y = y
            self.guy_images_right.append(self.set_images_right)
            self.guy_images_left.append(self.set_images_left)
            i += 1
        self.set_images = self.guy_images_right[self.index]
        self.direction = 0
        self.rect = self.set_images.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.set_images.get_width()
        self.height = self.set_images.get_height()
        self.vel_y = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("blob.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('coin.png')
		self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)



class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('exit.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button:
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (2 * tile_size, 2 * tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mouse_space = False

    def draw(self):
        Pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(Pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.mouse_space == False:
                self.mouse_space = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.mouse_space = False

        screen.blit(self.image, self.rect)
        return self.mouse_space


# Player1 = Player(screen_height-1000,screen_width-80)
# Player1 = Player(100,screen_height - 130)
Player1 = Player(50, screen_height - 130)

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()


score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin)


if path.exists(f"level{level}_data"):
    pickle_in = open(f"level{level}_data", 'rb')
    world_data = pickle.load(pickle_in)
World1 = World(world_data)

Button1 = Button(screen_width // 2 - 50, screen_height // 2 + 100, game_restart)
Button2 = Button(screen_width // 2 - 350, screen_height // 2, game_start)
Button3 = Button(screen_width // 2 + 150, screen_height // 2, game_exit)

run_game = True
while run_game:

    clock.tick(fps)

    screen.blit(image1, (0, 0))
    screen.blit(image2, (100, 100))
    if game_active == False:
        if Button2.draw():
            game_active = True
        if Button3.draw():
            run_game = False
    else:
        World1.draw()
        if game_over == 0:
            blob_group.update()
            if pygame.sprite.spritecollide(Player1, coin_group, True):
                score += 1
            draw_text('X ' + str(score), font_score, white, tile_size - 10, 10)
        lava_group.draw(screen)
        exit_group.draw(screen)
        coin_group.draw(screen)
        game_over = Player1.update(game_over)

        if game_over == -1:
            Button1.draw()
            if Button1.draw():
                world_data = []
                world = reset_level(level)
                # Player1.reset(100, screen_height - 130)
                game_over = 0
                score = 0

        if game_over == 1:
            level = level + 1
            if level <= max_levels:
                world_data = []
                World1 = reset_level(level)
                game_over = 0
            else:
                draw_text('YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2)
                if Button1.draw():
                    level = 1
                    world_data = []
                    World1 = reset_level(level)
                    game_over = 0
                    score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    pygame.display.update()
pygame.quit()


