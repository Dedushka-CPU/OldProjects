import pygame
import sys
import random

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ваша игра")

white = (255, 255, 255)
font = pygame.font.Font(None, 36)  

def generate_random_square():
    square_size = 50
    x = random.randint(0, width - square_size)
    y = random.randint(0, height - square_size)
    return pygame.Rect(x, y, square_size, square_size)

def generate_snake_segment(x, y):
    return pygame.Rect(x, y, character_size, character_size)

initial_segments = 300
character_size = 5
character_segments = [generate_snake_segment(width // 2 - character_size // 2 - i * character_size, height // 2 - character_size // 2) for i in range(initial_segments)]

random_square_rect = generate_random_square()

def check_collision():
    global character_segments, random_square_rect

    if character_segments[0].colliderect(random_square_rect):
        tail_segment = character_segments[-1]
        character_segments.append(generate_snake_segment(tail_segment.x, tail_segment.y))

        random_square_rect = generate_random_square()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    for i in range(len(character_segments) - 1, 0, -1):
        character_segments[i].x = character_segments[i - 1].x
        character_segments[i].y = character_segments[i - 1].y

    if keys[pygame.K_LEFT] and character_segments[0].x > 0:
        character_segments[0].x -= 1
    if keys[pygame.K_RIGHT] and character_segments[0].x < width - character_size:
        character_segments[0].x += 1
    if keys[pygame.K_UP] and character_segments[0].y > 0:
        character_segments[0].y -= 1
    if keys[pygame.K_DOWN] and character_segments[0].y < height - character_size:
        character_segments[0].y += 1

    check_collision()

    screen.fill(white)

    for segment in character_segments:
        pygame.draw.rect(screen, (0, 255, 0), segment)

    pygame.draw.rect(screen, (255, 0, 0), random_square_rect)

    text = font.render("Длина змейки: {}".format(len(character_segments)), True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()

pygame.quit()
sys.exit()
