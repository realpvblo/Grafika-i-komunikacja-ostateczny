from mttkinter import mtTkinter as tk
from turtle import *

def onclick1():
    from PIL import Image, ImageDraw
    def make_bezier(xys):
        # xys should be a sequence of 2-tuples (Bezier control points)
        n = len(xys)
        combinations = pascal_row(n - 1)

        def bezier(ts):
            # This uses basic general formula for bezier curves
            # http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
            result = []
            for t in ts:
                tpowers = (t ** i for i in range(n))
                upowers = reversed([(1 - t) ** i for i in range(n)])
                coefs = [c * a * b for c, a, b in zip(combinations, tpowers, upowers)]
                result.append(
                    tuple(sum([coef * p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
            return result

        return bezier

    def pascal_row(n):
        # This returns the nth row of Pascal's Triangle
        result = [1]
        x, numerator = 1, n
        for denominator in range(1, n // 2 + 1):
            # print(numerator,denominator,x)
            x *= numerator
            x /= denominator
            result.append(x)
            numerator -= 1
        if n & 1 == 0:
            # n is even
            result.extend(reversed(result[:-1]))
        else:
            result.extend(reversed(result))
        return result

    # import Image
    # import ImageDraw

    if __name__ == '__main__':
        im = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)
        ts = [t / 100.0 for t in range(101)]

        xys = [(0, 100), (25, 50), (50, 0)]
        bezier = make_bezier(xys)
        points = bezier(ts)

        xys = [(50, 0), (75, 50), (100, 100)]
        bezier = make_bezier(xys)
        points.extend(bezier(ts))

        xys = [(100, 100), (85, 75), (75, 50)]
        bezier = make_bezier(xys)
        points.extend(bezier(ts))

        xys = [(75, 50), (50, 50), (25, 50)]
        bezier = make_bezier(xys)
        points.extend(bezier(ts))

    # letter P

    im = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    ts = [t / 100.0 for t in range(101)]

    xys = [(40, 60), (100, 20), (30, 30), (40, 20)]
    bezier = make_bezier(xys)
    points = bezier(ts)

    xys = [(40, 60), (40, 65), (40, 100)]
    bezier = make_bezier(xys)
    points.extend(bezier(ts))

    draw.polygon(points, fill=None, outline='red')
    im.save('Inicjaly/LetterP.png')

    # letter W

    im = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    ts = [t / 100.0 for t in range(101)]

    xys = [(10, 20), (25, 100), (50, 20)]
    bezier = make_bezier(xys)
    points = bezier(ts)

    xys = [(50, 20), (75, 100), (100, 20)]
    bezier = make_bezier(xys)
    points.extend(bezier(ts))

    draw.polygon(points, fill=None, outline='red')
    im.save('Inicjaly/LetterW.png')

def onclick2():
    import pygame
    import os
    # Init and Create Window (win)
    pygame.init()
    win_height = 540
    win_width = 960
    win = pygame.display.set_mode((win_width, win_height))

    # Load and Size Images
    # Hero (Player)
    left = [pygame.image.load(os.path.join("Assets/Hero", "L1.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L2.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L3.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L4.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L5.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L6.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L7.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L8.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L9.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L10.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L11.png")),
            pygame.image.load(os.path.join("Assets/Hero", "L12.png"))
            ]
    right = [pygame.image.load(os.path.join("Assets/Hero", "R1.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R2.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R3.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R4.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R5.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R6.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R7.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R8.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R9.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R10.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R11.png")),
             pygame.image.load(os.path.join("Assets/Hero", "R12.png"))
             ]
    # Enemy
    left_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "L1.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L2.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L3.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L4.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L5.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L6.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L7.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L8.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L9.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L10.png")),
                  pygame.image.load(os.path.join("Assets/Enemy", "L11.png"))
                  ]

    # Bullet
    bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Bullets", "light_bullet.png")), (80, 80))
    # Background
    background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Background.png")),
                                        (win_width, win_height))
    # Tower
    tower = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Princess", "P1.png")), (200, 200))

    # Music/Sounds
    pygame.mixer.music.load(os.path.join("Assets/Audio", "music.mp3"))
    pop_sound = pygame.mixer.Sound(os.path.join("Assets/Audio", "pop.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

    class Hero:
        def __init__(self, x, y):
            # Walk
            self.x = x
            self.y = y
            self.velx = 10
            self.vely = 6
            self.face_right = True
            self.face_left = False
            self.stepIndex = 0
            # Jump
            self.jump = False
            # Bullet
            self.bullets = []
            self.cool_down_count = 0
            # Health
            self.hitbox = (self.x, self.y, 64, 64)
            self.health = 30
            self.lives = 1
            self.alive = True

        def move_hero(self, userInput):
            if (userInput[pygame.K_RIGHT] or userInput[pygame.K_d]) and self.x <= win_width - 62:
                self.x += self.velx
                self.face_right = True
                self.face_left = False
            elif (userInput[pygame.K_LEFT] or userInput[pygame.K_a]) and self.x >= 0:
                self.x -= self.velx
                self.face_right = False
                self.face_left = True
            else:
                self.stepIndex = 0

        def draw(self, win):
            self.hitbox = (self.x + 15, self.y + 15, 30, 40)
            pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y, 30, 10))
            if self.health >= 0:
                pygame.draw.rect(win, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
            if self.stepIndex >= 9:
                self.stepIndex = 0
            if self.face_left:
                win.blit(left[self.stepIndex], (self.x, self.y))
                self.stepIndex += 1
            if self.face_right:
                win.blit(right[self.stepIndex], (self.x, self.y))
                self.stepIndex += 1

        def jump_motion(self, userInput):
            if userInput[pygame.K_SPACE] and self.jump is False:
                self.jump = True
            if self.jump:
                self.y -= self.vely * 4
                self.vely -= 1
            if self.vely < -6:
                self.jump = False
                self.vely = 6

        def direction(self):
            if self.face_right:
                return 1
            if self.face_left:
                return -1

        def cooldown(self):
            if self.cool_down_count >= 10:
                self.cool_down_count = 0
            elif self.cool_down_count > 0:
                self.cool_down_count += 1

        def shoot(self):
            self.hit()
            self.cooldown()
            if (userInput[pygame.K_f] and self.cool_down_count == 0):
                pop_sound.play()
                bullet = Bullet(self.x, self.y, self.direction())
                self.bullets.append(bullet)
                self.cool_down_count = 1
            for bullet in self.bullets:
                bullet.move()
                if bullet.off_screen():
                    self.bullets.remove(bullet)

        def hit(self):
            for enemy in enemies:
                for bullet in self.bullets:
                    if enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[
                        1] < bullet.y - 40 < \
                            enemy.hitbox[1] + enemy.hitbox[3]:
                        enemy.health -= 5
                        player.bullets.remove(bullet)

    class Bullet:
        def __init__(self, x, y, direction):
            self.x = x + 15
            self.y = y + 25
            self.direction = direction

        def draw_bullet(self):
            win.blit(bullet_img, (self.x, self.y))

        def move(self):
            if self.direction == 1:
                self.x += 15
            if self.direction == -1:
                self.x -= 15

        def off_screen(self):
            return not (self.x >= 0 and self.x <= win_width)

    class Enemy:
        def __init__(self, x, y, speed):
            self.x = x
            self.y = y
            self.speed = speed
            self.stepIndex = 0
            # Health
            self.hitbox = (self.x, self.y, 64, 64)
            self.health = 30

        def step(self):
            if self.stepIndex >= 33:
                self.stepIndex = 0

        def draw(self, win):
            self.hitbox = (self.x + 20, self.y + 10, 30, 45)
            pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y, 30, 10))
            if self.health >= 0:
                pygame.draw.rect(win, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
            self.step()
            win.blit(left_enemy[self.stepIndex // 3], (self.x, self.y))
            self.stepIndex += 1

        def move(self):
            self.hit()
            self.x -= speed

        def hit(self):
            if player.hitbox[0] < enemy.x + 32 < player.hitbox[0] + player.hitbox[2] and player.hitbox[
                1] < enemy.y + 80 < \
                    player.hitbox[1] + player.hitbox[3]:
                if player.health > 0:
                    player.health -= 1
                    if player.health == 0 and player.lives > 0:
                        player.lives -= 1
                        player.health = 30
                    elif player.health == 0 and player.lives == 0:
                        player.alive = False

        def off_screen(self):
            return not (self.x >= -50 and self.x <= win_width + 50)

    # Draw Game
    def draw_game():
        global tower_health, speed
        win.fill((0, 0, 0))
        win.blit(background, (0, 0))
        # Draw Player
        player.draw(win)
        # Draw Bullets
        for bullet in player.bullets:
            bullet.draw_bullet()
        # Draw Enemies
        for enemy in enemies:
            enemy.draw(win)
        # Draw Tower
        win.blit(tower, (0, 200))
        # Player Health
        if player.alive == False:
            win.fill((0, 0, 0))
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Umarłeś! Wciśnij R by zresetować', True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (win_width // 2, win_height // 2)
            win.blit(text, textRect)
            if userInput[pygame.K_r]:
                player.alive = True
                player.lives = 1
                player.health = 30
                tower_health = 2
                speed = 2
        font = pygame.font.Font('freesansbold.ttf', 32)
        tower_health = 2
        text = font.render(
            'Życia: ' + str(player.lives) + ' | Życia Księżniczki : ' + str(tower_health) + ' | Zabójstwa: ' + str(
                kills), True, (0, 0, 0), (255, 255, 255))
        win.blit(text, (150, 20))
        # Delay and Update
        pygame.time.delay(30)
        pygame.display.update()

    # Instance of Hero-Class
    player = Hero(250, 240)

    # Instance of Enemy-Class
    enemies = []
    speed = 2
    kills = 0

    # Tower
    tower_health = 2

    # Mainloop

    run = True
    while run:

        # Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Input
        userInput = pygame.key.get_pressed()

        # Shoot
        player.shoot()

        # Movement
        player.move_hero(userInput)
        player.jump_motion(userInput)

        # Tower Health
        if tower_health == 0:
            player.alive = False

        # Enemy
        if len(enemies) == 0:
            enemy = Enemy(750, 200, speed)
            enemies.append(enemy)
            if speed <= 10:
                speed += 0.25
        for enemy in enemies:
            enemy.move()
            if enemy.off_screen() or enemy.health == 0:
                enemies.remove(enemy)
            if enemy.x < 50:
                enemies.remove(enemy)
                tower_health -= 1
            if enemy.health == 0:
                kills += 1

        # Draw Game in Window
        draw_game()

def onclick3():
    import turtle
    turtle.speed(5)
    bgcolor('cyan')

    # sciany
    color('black', 'blue')
    begin_fill()
    turtle.left(270)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(400)
    end_fill()

    # dach
    color('black', 'red')
    begin_fill()
    turtle.right(135)
    turtle.forward(283)
    turtle.right(90)
    turtle.forward(283)
    end_fill()

    # komin
    color('black', 'brown')
    begin_fill()
    turtle.left(135)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(70)
    end_fill()

    # okno
    color('black', 'white')
    turtle.right(135)
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    end_fill()

    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
    color('black', 'white')
    begin_fill()
    turtle.forward(50)


    # okno

    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    end_fill()

    # drzwi
    turtle.penup()
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.pendown()
    color('black', 'brown')
    begin_fill()
    turtle.right(180)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(80)
    end_fill()

    turtle.penup()
    turtle.right(90)
    turtle.forward(450)
    turtle.pendown()

    # drzewo
    color('black', 'green')
    begin_fill()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(90)
    turtle.right(120)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(30)
    end_fill()

    turtle.penup()
    turtle.right(180)
    turtle.forward(400)
    turtle.pendown()

    # slonce
    r = 50
    color('black', 'yellow')
    begin_fill()
    turtle.circle(r)
    end_fill()

    turtle.penup()
    turtle.right(180)
    turtle.forward(400)
    turtle.right(90)
    turtle.pendown()

    # ziemia
    color('black', 'beige')
    begin_fill()
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(1000)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(1000)
    end_fill()

    turtle.mainloop()


root = tk.Tk()
root.title("GUI")

btn1 = tk.Button(root, text="Krzywe Beziera", command=onclick1)
btn2 = tk.Button(root, text="Gra Tower Defense", command=onclick2)
btn3 = tk.Button(root, text="Domek", command=onclick3)

btn1.pack()
btn2.pack()
btn3.pack()

root.mainloop()
