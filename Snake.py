import time

import pygame
from enum import Enum
import random


class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


speed = 10

window_width = 1080
window_height = 720

scale = 20

pygame.init()
pygame.display.set_caption("Snakeus")
window = pygame.display.set_mode((window_width, window_height))

refresh_controller = pygame.time.Clock()

snake_position = [250, 250]
snake_body = [[250, 250],
              [240, 250],
              [230, 250]]

food_position = [0, 0]
food_position[0] = random.randint(5, ((window_width - 2) // scale)) * scale
food_position[1] = random.randint(5, ((window_height - 2) // scale)) * scale

global score
score = 0


def handle_keys(direction):
    new_direction = direction
    for event in [e for e in pygame.event.get() if e.type == pygame.KEYDOWN]:
        if event.key == pygame.K_UP and direction != Direction.DOWN:
            new_direction = Direction.UP
        if event.key == pygame.K_DOWN and direction != Direction.UP:
            new_direction = Direction.DOWN
        if event.key == pygame.K_RIGHT and direction != Direction.LEFT:
            new_direction = Direction.RIGHT
        if event.key == pygame.K_LEFT and direction != Direction.RIGHT:
            new_direction = Direction.LEFT
    return new_direction


def move_snake(direction):
    if direction == Direction.UP:
        snake_position[1] -= scale
    if direction == Direction.DOWN:
        snake_position[1] += scale
    if direction == Direction.LEFT:
        snake_position[0] -= scale
    if direction == Direction.RIGHT:
        snake_position[0] += scale
    snake_body.insert(0, list(snake_position))


def generate_new_food():
    food_position[0] = random.randint(5, ((window_width - 2) // scale)) * scale
    food_position[1] = random.randint(5, ((window_height - 2) // scale)) * scale


def get_food():
    global score
    print(food_position)
    if abs(snake_position[0] - food_position[0]) < 20 and abs(snake_position[1] - food_position[1]) < 20:
        score += 10
        generate_new_food()
    else:
        snake_body.pop()


def repaint():
    window.fill(pygame.Color(0, 0, 0))
    for body in snake_body:
        pygame.draw.circle(window, pygame.Color(0, 255, 0), (body[0], body[1]), scale / 2)
    pygame.draw.rect(window, pygame.Color(255, 0, 0),
                     pygame.Rect(food_position[0] - scale / 2, food_position[1] - scale / 2, scale, scale))


def game_over_message():
    font = pygame.font.SysFont('Arial', scale * 3)
    render = font.render(f"Score: {score}", True, pygame.Color(255, 255, 255))
    rect = render.get_rect()
    rect.midtop = (window_width / 2, window_height / 2)
    window.blit(render, rect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    exit(0)


def game_over():
    if snake_position[0] < 0 or snake_position[0] > window_width - 10:
        game_over_message()
    if snake_position[1] < 0 or snake_position[1] > window_height - 10:
        game_over_message()
    for blob in snake_body[1:]:
        if snake_position[0] == blob[0] and snake_position[1] == blob[1]:
            game_over_message()


def paint_hud():
    font = pygame.font.SysFont("Arial", scale * 2)
    render = font.render(f"Score: {score}", True, pygame.Color(255, 255, 255))
    rect = render.get_rect()
    window.blit(render, rect)
    pygame.display.flip()


def game_loop():
    direction = Direction.RIGHT
    while True:
        direction = handle_keys(direction)
        move_snake(direction)
        get_food()
        repaint()
        game_over()
        paint_hud()
        pygame.display.update()
        refresh_controller.tick(speed)
        time.sleep(0.1)


if __name__ == "__main__":
    game_loop()
