#dsa.py

import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 15
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker Game")

# Create the paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [random.choice([-5, 5]), -5]

# Create the blocks
block_width, block_height = 80, 30
blocks = []
for row in range(5):
    for col in range(10):
        block = pygame.Rect(col * block_width + 5, row * block_height + 5, block_width - 5, block_height - 5)
        blocks.append(block)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(5, 0)

    # Move the ball
    ball.move_ip(ball_speed)

    # Check for collisions with walls
    if ball.left < 0 or ball.right > WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top < 0:
        ball_speed[1] = -ball_speed[1]

    # Check for collisions with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Check for collisions with blocks
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed[1] = -ball_speed[1]

    # Clear the screen
    window.fill(WHITE)

    # Draw the paddle
    pygame.draw.rect(window, BLUE, paddle)

    # Draw the ball
    pygame.draw.circle(window, RED, ball.center, BALL_RADIUS)

    # Draw the blocks
    for block in blocks:
        pygame.draw.rect(window, BLUE, block)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

