import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game objects
ball = pygame.Rect(350, 250, 10, 10)
player1 = pygame.Rect(50, 250, 10, 50)
player2 = pygame.Rect(740, 250, 10, 50)

# Set initial velocity for the ball
velocity = [2, -2]

# Set the initial score for each player
player1_score = 0
player2_score = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get player 1's input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.top -= 3
    if keys[pygame.K_DOWN]:
        player1.top += 3

    # Get player 2's input
    if keys[pygame.K_w]:
        player2.top -= 3
    if keys[pygame.K_s]:
        player2.top += 3

    # Move the ball
    ball.left += velocity[0]
    ball.top += velocity[1]

    # Check for collision with the wall
    if ball.top <= 0 or ball.bottom >= 600:
        velocity[1] = -velocity[1]
    if ball.left <= 0:
        player2_score += 1
        ball.center = (400, 300)
    if ball.right >= 800:
        player1_score += 1
        ball.center = (400, 300)

    # Check for collision with the paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        velocity[0] = -velocity[0]

    # Clear the screen
    screen.fill(BLACK)

    # Draw the game objects
    pygame.draw.rect(screen, WHITE, ball)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)

    # Draw the score
    font = pygame.font.Font(None, 36)
    score1 = font.render(str(player1_score), 1, WHITE)
    score2 = font.render(str(player2_score), 1, WHITE)
    screen.blit(score1, (350, 10))
    screen.blit(score2, (420, 10))

    # Update the screen
    pygame.display.flip()
