import pygame
import pygame_textinput
import Sql
from Paddle import Paddle
from ball import Ball
from brick import Brick
from ball import Shot

pygame.init()

# Define block color
White = (255, 255, 255)
Purple = (255, 0, 255)
DarkBlue = (36, 90, 190)
Red = (255, 0, 0,)
Orange = (255, 100, 0)
Yellow = (255, 255, 0)
Black = (10, 10, 10)

score = 0
lives = 3


def submitScore():
    # Create TextInput-object
    textinput = pygame_textinput.TextInput()
    font = pygame.font.Font(None, 74)
    text = font.render("Input name", 1, Black)
    while True:
        screen.fill((225, 225, 225))
        screen.blit(text, (200, 300))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Feed it with events every frame
        if textinput.update(events):
            uname = textinput.get_text()
            break
        # Blit its surface onto the screen
        screen.blit(textinput.get_surface(), (250, 300))

        pygame.display.update()

    Sql.insert("test", uname, score)


# Opens game window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")

# sprite list
all_sprites_list = pygame.sprite.Group()


# Shot
shot = Shot(Black, 10, 10)

all_bricks = pygame.sprite.Group()
# Ball
ball = Ball(White, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# Paddle
paddle = Paddle(Purple, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

for i in range(7):
    brick = Brick(Red, 80, 30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(Orange, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(Yellow, 80, 30)
    brick.rect.x = 60 + i*100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# add sprites to list
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# Keeps the loop running
carryOn = True

# game clock
clock = pygame.time.Clock()

# ------ Main Program Loop ------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User action
        if event.type == pygame.QUIT:  # Clicked close
            carryOn = False  # Exit loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # press x to exit
                carryOn = False
    # paddle move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
    if keys[pygame.K_UP]:
        # Shot
        shot.rect.x = paddle.rect.x + 45
        shot.rect.y = paddle.rect.y - 15
        all_sprites_list.add(shot)

    # --- Game logic
    all_sprites_list.update()

    # wall bounce
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, White)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            submitScore()

            carryOn = False
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    # Collision paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # Brick collision
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            # Level complete
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, White)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            submitScore()

            carryOn = False
    shot_collision_list = pygame.sprite.spritecollide(shot, all_bricks, False)
    for brick in shot_collision_list:
        score += 1
        brick.kill()
        shot.kill()
        if len(all_bricks) == 0:
            # Level complete
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, White)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            carryOn = False
            submitScore()

    # --- Graphic
    # Set screen color
    screen.fill(DarkBlue)
    pygame.draw.line(screen, White, [0, 38], [800, 38], 2)

    # Display score and lives
    font = pygame.font.Font(None, 34)
    text = font.render('Score: ' + str(score), 1, White)
    screen.blit(text, (20, 10))
    text = font.render('Lives: ' + str(lives), 1, White)
    screen.blit(text, (650, 10))

    # draw sprites
    all_sprites_list.draw(screen)

    # --- Update screen
    pygame.display.flip()

    # --- limit to 60fps
    clock.tick(60)

# Exit game engine
pygame.quit()
