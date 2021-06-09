# Import required libraries
import pygame
from random import choice

# Initialize pygame 
pygame.init()

# Initialize font settings 
myfont = pygame.font.SysFont('monospace', 50)
myfont2 = pygame.font.SysFont('monospace', 35)

# Display settings
display = {
    "width": 800,
    "height": 600
}

# Left paddle settings
paddleLeft = {
    "width": 20,
    "height": 150,
    "x": 0,
    "y": 250,
    "velocity": 20
}

# Right paddle settings
paddleRight = {
    "width": 20,
    "height": 150,
    "x": 780,
    "y": 250,
    "velocity": 20
}

# Ball settings
ball = {
    "radius": 20,
    "y": 300,
    "x": 400,
    "ver_speed": 5 * choice([-1, 1]),
    "hor_speed": 5 * choice([-1, 1])
}

# Initialize game window size in PIXELS, 800 by 600 should be fine
# Remember to store the window in a variable!
win = pygame.display.set_mode((display["width"], display["height"]))

# Score variables
Leftscore = 0
Rightscore = 0

# Define function to reset ball settings
def resetBallStats():
   ball["x"] = 400
   ball["y"] = 300
   ball["ver_speed"] = 5 * choice([-1, 1])
   ball["hor_speed"] = 5 * choice([-1, 1])

def gameOverScreen():
   win.fill((255,255,255))
   pygame.display.flip()
   textsurface2 = myfont2.render("Goodbye thanks for playing.", False, (0, 0, 0))
   win.blit(textsurface2, (125, 250))
   pygame.display.flip()
   timer = 0;
   while timer < 3:
      timer += 1
      pygame.time.delay(1000)
   pygame.quit()

# The Main game loop
while True:
    # Time delay
    pygame.time.delay(50)

    # Prepare window, fill RGB code (RED, GREEN, BLUE)
    win.fill((255, 255, 255))

    # Event checking
    pygame.event.get()

    # Check which keys were pressed 
    keys = pygame.key.get_pressed()

    # Paddle movements
    if keys[pygame.K_q] and paddleLeft["y"] >= 0:
        paddleLeft["y"] -= paddleLeft["velocity"]

    if keys[pygame.K_a] and paddleLeft["y"] + paddleLeft["height"] <= 600:
        paddleLeft["y"] += paddleLeft["velocity"]
    
    if keys[pygame.K_UP] and paddleRight["y"] >= 0:
        paddleRight["y"] -= paddleRight["velocity"]

    if keys[pygame.K_DOWN] and paddleRight["y"] + paddleRight["height"] <= 600:
        paddleRight["y"] += paddleRight["velocity"]

    # Ball movement
    ball["x"] += ball["hor_speed"]
    ball["y"] += ball["ver_speed"] 

    if ball["y"] - ball["radius"] <= 0:
        ball["ver_speed"] -= 1
        ball["ver_speed"] *= -1

    if ball["y"] + ball["radius"] >= display["height"]:
        ball["ver_speed"] += 1
        ball["ver_speed"] *= -1

    if ball["x"] - ball["radius"] <= 0:
        ball["hor_speed"] -= 1
        ball["hor_speed"] *= -1

    if ball["x"] + ball["radius"] >= display["width"]:
        ball["hor_speed"] += 1
        ball["hor_speed"] *= -1

    # Ball bouncing conditions (and scoring conditions)
    if ball["x"] <= paddleLeft["width"]:
        if ball["y"] > paddleLeft["y"] + paddleLeft["height"] or ball["y"] < paddleLeft["y"]:
          Leftscore += 1
          resetBallStats()

    if ball["x"] + ball["radius"] >= paddleRight["x"]:
        if ball["y"] > paddleRight["y"] + paddleRight["height"] or ball["y"] < paddleRight["y"]:
          Rightscore += 1
          resetBallStats()

    # Quit the game pressing L
    if keys[pygame.K_l]:
      break

    # Draw everything in the window (including text for the score tracking)
    pygame.draw.circle(win, (0, 0, 255), (ball["x"], ball["y"]), ball["radius"])
    pygame.draw.rect(win, (255, 0, 0), (paddleLeft["x"], paddleLeft["y"], paddleLeft["width"], paddleLeft["height"]))
    pygame.draw.rect(win, (255, 0, 0), (paddleRight["x"], paddleRight["y"], paddleRight["width"], paddleRight["height"]))

    textsurface = myfont.render("score: " + str(Rightscore) + "/" + str(Leftscore), False, (0, 0, 0))
    win.blit(textsurface, (250, 10))
    
    # Display update
    pygame.display.update()

# Quit pygame
gameOverScreen()
