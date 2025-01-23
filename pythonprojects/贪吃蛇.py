import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (0, 0, 0)  # Background color

# Set up the game window size
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set snake properties
snake_block = 20  # Increase the size of the snake
snake_speed = 10

# Set clock
clock = pygame.time.Clock()

# Font settings
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def draw_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        # Create a gradient effect for the snake's color
        color = (0 + i * 15 % 255, 255 - i * 15 % 255, 0)  # Adjust as needed
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])


def your_score(score):
    value = score_font.render("Score: " + str(score), True, white)  # Score color
    screen.blit(value, [0, 0])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


def generate_food(snake_List, snake_block):
    while True:
        foodx = (
            round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        )
        foody = (
            round(random.randrange(0, height - snake_block) / snake_block) * snake_block
        )
        if [foodx, foody] not in snake_List:
            return foodx, foody


def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = generate_food(snake_List, snake_block)

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("You Lost! Press C to Play Again or Q to Quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)  # Set background color to black
        pygame.draw.rect(
            screen, red, [foodx, foody, snake_block, snake_block]
        )  # Food size increased
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats the food
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_List, snake_block)
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
