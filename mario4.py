import pygame

pygame.init()

screen_height = 1000
screen_width = 1000
screen = pygame.display.set_mode((screen_height,screen_width))
name_of_game = pygame.display.set_caption("Builder","Builder")

tile_size = 50
game_over = 0

image1 = pygame.image.load("sky.png")
image2 = pygame.image.load("sun.png")

class World:
    def __init__(self,data):
        self.worldist = []
        row = 0
        image3 = pygame.image.load('dirt.png')
        image4 = pygame.image.load('grass.png')
        for line in data:
            column = 0
            for item in line:
                if item == 1:
                    set_images = pygame.transform.scale(image3,[tile_size,tile_size])
                    create_box = set_images.get_rect()
                    create_box.x = tile_size * column
                    create_box.y = tile_size * row
                    tile = (set_images,create_box)
                    self.worldist.append(tile)
                    #self.worldist.append([set_images,create_box])
                if item == 2:
                    set_images = pygame.transform.scale(image4,[tile_size,tile_size])
                    create_box = set_images.get_rect()
                    create_box.x = tile_size * column
                    create_box.y = tile_size * row
                    tile = (set_images, create_box)
                    self.worldist.append(tile)
                    #self.worldist.append([set_images,create_box])
                if item ==3:
                    blob = Enemy(tile_size * column,tile_size * row +10)
                    blob_group.add(blob)
                if item ==6:
                    lava = Lava(tile_size * column,tile_size * row +25 )
                    lava_group.add(lava)
                column = column + 1
            row = row + 1

    def draw(self) :
        for image in self.worldist:
            pygame.draw.rect(screen,(255,255,255),image[1],10 )
            screen.blit(image[0],image[1])


class Player:
    def __init__(self,x,y):
        self.jumped = False
        self.guy_images_right = []
        self.guy_images_left = []
        self.index = 0
        self.angle = 180
        i = 1
        while i < 5:
            self.image_right =  pygame.image.load(f'guy{i}.png')
            self.set_images_right = pygame.transform.scale(self.image_right, [40, 80])
            self.set_images_left = pygame.transform.flip(self.set_images_right,True,False )
            #self.create_box = self.set_images_right.get_rect()
            #self.create_box.x = x
            #self.create_box.y = y
            self.guy_images_right.append(self.set_images_right)
            self.guy_images_left.append(self.set_images_left)
            i += 1
        self.set_images = self.guy_images_right[self.index]
        self.direction = 0
        self.create_box = self.set_images.get_rect()
        self.create_box.x = x
        self.create_box.y = y
        self.width = self.set_images.get_width()
        self.height = self.set_images.get_height()
        self.vel_y = 0




    '''
        image3 = pygame.image.load('guy1.png')
        self.set_images = pygame.transform.scale(image3,[40,80])
        self.create_box = self.set_images.get_rect()
        self.create_box.x = x
        self.create_box.y = y
        self.jumped = False 
        '''

    def update(self,game_over):



        dx= 0
        dy =0


        '''
        screen.blit(self.set_images, self.create_box)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx -= 5
                if event.key == pygame.K_RIGHT:
                    dx += 5
        self.create_box.x += dx
        self.create_box.y += dy
        #screen.blit(self.set_images, self.create_box)

        '''
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



            if key[pygame.K_SPACE] and self.jumped == False:
                #dy = -15
                self.vel_y = -15
                self.jumped = True


            if key[pygame.K_SPACE] == False:
                self.jumped = False

            self.vel_y += 1
            if self.vel_y >10:
                self.vel_y = 6
            dy += self.vel_y
            #dy += 1


      # collison
            p = 0
            for items in World1.worldist:
                if items[1].colliderect(self.create_box.x + dx, self.create_box.y,self.width,self.height):
                    dx = 0
                if items[1].colliderect(self.create_box.x, self.create_box.y + dy,self.width,self.height):
                    if self.vel_y >= 0:
                        #dy = items[1].top - self.create_box.bottom
                        dy = 0
                        #self.vel_y = 0
                    if self.vel_y < 0:
                        dy = 0
                        #dy = items[1].bottom - self.create_box.top
                        #self.vel_y = 0


                    #print(f"Sprite+{self.create_box.y}")
                    #print(items[1].y)
                    #dy = 950


            self.create_box.x += dx
            self.create_box.y += dy



            #if self.create_box.bottom > screen_height - 50:
                #self.create_box.bottom = screen_height -50
            if self.create_box.top < 50:
                self.create_box.top = 50

            if pygame.sprite.spritecollide(self,blob_group,False):
                game_over = -1

            if pygame.sprite.spritecollide(self,lava_group,False):
                game_over = -1



        screen.blit(self.set_images, self.create_box)
        pygame.draw.rect(screen,(255,255,255),self.create_box,2)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
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
        if abs(self.move_counter)  > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.load_image = pygame.image.load("lava.png")
        self.image = pygame.transform.scale(self.load_image, (tile_size  , tile_size//2 ))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y







world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 3, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]



#Player1 = Player(screen_height-1000,screen_width-80)
#Player1 = Player(100,screen_height - 130)
Player1 = Player(50,screen_height - 130)

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
World1 = World(world_data)


run_game = True
while run_game:

    screen.blit(image1,(0,0))
    screen.blit(image2, (100,100))
    World1.draw()
    blob_group.draw(screen)
    blob_group.update()
    lava_group.draw(screen)
    game_over = Player1.update(game_over)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    pygame.display.update()
pygame.quit()


