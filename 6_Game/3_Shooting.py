import pygame
import os
import random

pygame.init()

screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

game_path = os.path.dirname(__file__)

pygame.display.set_caption("ROY - SHOOTING GAME")

background = pygame.image.load(f"{game_path}/images/background.png")

# Character
char = pygame.image.load(f"{game_path}/images/character.png")
char_size = char.get_rect().size
char_w = char_size[0]
char_h = char_size[1]
char_x = screen_width/2 - char_w/2
char_y = screen_height - char_h

char_to_x = 0
char_to_y = 0
char_speed= 0.6

#Bullets
bullet = pygame.image.load(f"{game_path}/images/bullet.png")
bullet_size = bullet.get_rect().size
bullet_w = bullet_size[0]
bullet_h = bullet_size[1]

bullets = []

bullet_speed = 5

# Enemy
enemy = pygame.image.load(f"{game_path}/images/enemy_1.png")
enemy_img = [
    pygame.image.load(f"{game_path}/images/enemy_1.png"),
    pygame.image.load(f"{game_path}/images/enemy_2.png"),
    pygame.image.load(f"{game_path}/images/enemy_3.png")
]
enemy_size = enemy.get_rect().size

enemies = []

enemy_speed = random.randint(1, 2)

enemies.append({
    "pos_x" : random.randint(0, screen_width - enemy_size[0]),
    "pos_y" : 0,
    "img_idx" : 0,
    "to_x" : enemy_speed + random.randint(-2, 0), 
    "to_y" : enemy_speed + random.randint(-2, 0)
})

enemies.append({
    "pos_x" : random.randint(0, screen_width - enemy_size[0]),
    "pos_y" : 0,
    "img_idx" : 0,
    "to_x" : enemy_speed + random.randint(-2, 0), 
    "to_y" : enemy_speed + random.randint(-2, 0)
})

bullet_to_remove = -1
enemy_to_remove = -1

# FPS : Frame per second
clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 40)
total_time = 30
start_ticks = pygame.time.get_ticks()

running = True
while running:
    frame = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_w:
                char_to_y -= char_speed
            elif  event.key == pygame.K_s:
                char_to_y += char_speed
            elif  event.key == pygame.K_a:
                char_to_x -= char_speed
            elif  event.key == pygame.K_d:
                char_to_x += char_speed

        if event.type == pygame.MOUSEBUTTONUP:
            bullet_x = char_x + (char_w/2)
            bullet_y = char_y
            bullets.append([bullet_x, bullet_y])

        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                char_to_y = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                char_to_x = 0

    # Character Move
    char_x += char_to_x * frame
    char_y += char_to_y * frame

    if char_x < 0:
        char_x = 0
    elif char_x > screen_width - char_w:
        char_x = screen_width - char_w
    if char_y < 0:
        char_y = 0
    elif char_y > screen_height - char_h:
        char_y = screen_height - char_h

    # Bullets Move
    bullets = [[bul[0], bul[1] - bullet_speed] for bul in bullets]
    bullets = [[bul[0], bul[1]] for bul in bullets if bul[1] < screen_height]

    # Enemies Move
    for enemy in enemies:
        enemy_x = enemy["pos_x"]
        enemy_y = enemy["pos_y"]
        enemy_img_idx = enemy["img_idx"]

        enemy_size = enemy_img[enemy_img_idx].get_rect().size

        if enemy_x < 0 or enemy_x > screen_width - enemy_size[0]:
            enemy["to_x"] *= -1
        if enemy_y < 0 or enemy_y > screen_height - enemy_size[1]:
            enemy["to_y"] *= -1

        enemy["pos_x"] += enemy["to_x"]
        enemy["pos_y"] += enemy["to_y"]
 
 #################################################

    # Character hitbox
    char_hit = char.get_rect()
    char_hit.left = char_x
    char_hit.top = char_y

    # Enemy hitbox
    for e_idx, enemy in enumerate(enemies):
        enemy_x = enemy["pos_x"]
        enemy_y = enemy["pos_y"]
        enemy_img_idx = enemy["img_idx"]

        enemy_hit = enemy_img[enemy_img_idx].get_rect()
        enemy_hit.left = enemy_x
        enemy_hit.top = enemy_y

        # Enemy vs Character
        if char_hit.colliderect(enemy_hit): 
            running = False
            game_result = "GAME OVER"
            break
    
        # Bullets hitbox
        for b_idx, bul in enumerate(bullets):
            bullet_x = bul[0]
            bullet_y = bul[1]

            bullet_hit = bullet.get_rect()
            bullet_hit.left = bullet_x
            bullet_hit.top = bullet_y

            # Bullet vs Enemies
            if bullet_hit.colliderect(enemy_hit):
                bullet_to_remove = b_idx 
                enemy_to_remove = e_idx


                # Check enemy status
                if enemy_img_idx < 2 :
                    enemy_w = enemy_hit.size[0]
                    enemy_h = enemy_hit.size[1]


                    # Next enemy's hitbox
                    next_enemy_hit = enemy_img[enemy_img_idx + 1].get_rect() 
                    next_enemy_w = next_enemy_hit.size[0]
                    next_enemy_h = next_enemy_hit.size[1]

                    enemy_speed *= 1.25

                    # Enemy change
                    enemies.append({
                        "pos_x" : enemy_x,
                        "pos_y" : enemy_y,
                        "img_idx" : enemy_img_idx + 1,
                        "to_x" : enemy_speed + random.randint(-5, -3), 
                        "to_y" : enemy_speed
                    })
                    enemies.append({
                        "pos_x" : enemy_x,
                        "pos_y" : enemy_y,
                        "img_idx" : enemy_img_idx + 1,
                        "to_x" : enemy_speed + random.randint(1, 3), 
                        "to_y" : enemy_speed
                    })
                break
        else: 
            continue
        break
                
    if bullet_to_remove > -1:
        del bullets[bullet_to_remove]
        bullet_to_remove = -1
   
    if enemy_to_remove > -1:
        del enemies[enemy_to_remove]
        enemy_to_remove = -1

    if len(enemies) == 0:
        game_result = "MISSION COMPLETE!!!"
        running = False

    # Rendering
    screen.blit(background, (0,0))
    screen.blit(char, (char_x, char_y))

    for bul_x, bul_y in bullets:
        screen.blit(bullet, (bul_x, bul_y))

    for enemy in enemies:
        enemy_x = enemy["pos_x"]
        enemy_y = enemy["pos_y"]
        enemy_img_idx = enemy["img_idx"]
        screen.blit(enemy_img[enemy_img_idx], (enemy_x, enemy_y))


    # Timer
    past_time = (pygame.time.get_ticks() - start_ticks)/1000
    timer = game_font.render(str(round((total_time - past_time), 2)), True, (255, 0, 0))
    screen.blit(timer, (10, 10))

    if total_time - past_time < 0:
        game_result = "Time OUT!!"
        running = False

    pygame.display.update()

# MSG
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(1000)
pygame.quit()