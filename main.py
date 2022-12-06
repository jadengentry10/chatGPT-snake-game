# Import the pygame module
import pygame
import random
import os
import pygame.mixer
# Initialize the pygame library
pygame.init()

# Initialize the mixer
pygame.mixer.init()


# Check if the file exists and if not create it
if not os.path.exists('high_score.txt'):
    # Create the file if it doesn't exist
    open('high_score.txt', 'w').close()
    with open('high_score.txt', 'w') as file:
        file.write(str(1))


# Initialize the game score
score = 0
high_score = 1
clock = pygame.time.Clock()
with open("high_score.txt", "r")as file:
    high_score = int(file.read())
# Define the colors to use in the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a game window with a size of 400x400 pixels
screen = pygame.display.set_mode((400, 400), pygame.DOUBLEBUF)

# Set the title of the game window
pygame.display.set_caption("Snake")

# Set the frame rate of the game
FPS = 10

# Define the size of the game grid
GRID_SIZE = 20

# Define the size of each grid cell
CELL_SIZE = 20

# RED COLOR
RED = (255, 0, 0)

# Define the initial position and direction of the snake
snake = [(200, 200), (200, 220), (200, 240)]
direction = "UP"

# Define the initial position of the food
food_pos = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)


# Load the sound file
sound = pygame.mixer.music.load('main_track.mp3')
# Set the volume of the music
pygame.mixer.music.set_volume(0.5)
# Play the music in a loop
pygame.mixer.music.play(-1)
# Main game loop
while True:

    dt = clock.tick()
    fps = 1000 / dt
    fps = round(fps)
    pygame.time.Clock().tick(FPS)
    screen.fill(color=(100, 150, 100))
    # Draw the snake on the screen
    for x, y in snake:
        pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
    # Draw the food on the screen
    pygame.draw.rect(
        screen, RED,  (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Create a font for displaying the score
    font = pygame.font.SysFont("Helvetica", 16)
    text = font.render(f"Score: {score}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    fps_text = font.render(f"FPS: {fps:.2f}", True, WHITE)
    # Draw the score
    screen.blit(text, (5, 5))
    screen.blit(high_score_text, (290, 5))
    screen.blit(fps_text, (200, 5))

    # Process input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if score > high_score:
            # update high score
            high_score = score
            file = open("high_score.txt", "w")
            file.write(str(high_score))

    # Change the direction of the snake based on the arrow keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            if event.key == pygame.K_DOWN:
                direction = "DOWN"
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                direction = "RIGHT"
    # Update the position of the snake based on its direction
    x, y = snake[0]
    if direction == "UP":
        y -= 20
    if direction == "DOWN":
        y += 20
    if direction == "LEFT":
        x -= 20
    if direction == "RIGHT":
        x += 20

    # Check if the snake has collided with the boundaries of the game screen or itself
    if x < 0 or x >= 400 or y < 0 or y >= 400 or (x, y) in snake:
        pygame.mixer.music.stop()
        # Load the sound file
        death_sound = pygame.mixer.Sound('death_sound.mp3')

        # Set the volume of the sound
        death_sound.set_volume(1.0)

        # Play the sound
        death_sound.play()
        # Display game over message
        font = pygame.font.SysFont("Helvetica", 32)
        text = font.render("Game Over!", True, WHITE)
        screen.blit(text, (100, 100))

        # Prompt the player to press a key to play again
        font = pygame.font.SysFont("Helvetica", 16)
        text = font.render("Press any key to play again", True, WHITE)
        screen.blit(text, (100, 200))

        # Wait for player input
        pygame.display.flip()
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # Reset the game state and continue the game loop
                # Play the music in a loop
                pygame.mixer.music.play(-1)
                score = 0
                snake = [(200, 200), (180, 200), (160, 200)]
                direction = "RIGHT"
                x = random.randint(0, 19) * 20
                y = random.randint(0, 19) * 20
                food_pos = (x, y)
                break
    snake.insert(0, (x, y))

    # Check if the snake has collided with the food
    if snake[0] == food_pos:
        # Generate a new food position
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20

        food_pos = (x, y)
        # Increment the score
        score += 1

    else:
        # Remove the last element of the snake
        snake.pop()
    pygame.display.update()
