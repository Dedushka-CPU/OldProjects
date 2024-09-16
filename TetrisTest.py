import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
width, height = 400, 500

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Размер блока тетриса
block_size = 25

# Класс блока
class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((block_size, block_size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

# Класс фигуры тетриса
class Tetromino(pygame.sprite.Group):
    def __init__(self, color, shape):
        super().__init__()
        self.blocks = []
        self.color = color

        for position in shape:
            block = Block(color, position[0] * block_size, position[1] * block_size)
            self.add(block)
            self.blocks.append(block)

    def move(self, dx, dy, other_tetrominos):
        # Проверка, не произошло ли столкновение с другими блоками
        for block in self.blocks:
            new_x = block.rect.x + dx
            new_y = block.rect.y + dy

            if not (0 <= new_x < width and 0 <= new_y < height) or any(
                block.rect.colliderect(other_block.rect) for other_tetromino in other_tetrominos
                for other_block in other_tetromino.blocks
                if (other_block.rect.x, other_block.rect.y) != (new_x, new_y)
            ):
                return False

        # Если столкновение не произошло, двигаем блок
        for block in self.blocks:
            block.rect.x += dx
            block.rect.y += dy

        return True

    def reached_bottom(self):
        return any(block.rect.y >= height - block_size for block in self.blocks)

    def check_collision(self, other_tetrominos):
        for tetromino in other_tetrominos:
            for block in self.blocks:
                for other_block in tetromino.blocks:
                    if block.rect.colliderect(other_block.rect):
                        return True
        return False

    def update_grid(self, grid):
        # Добавление блоков текущей фигуры в сетку
        for block in self.blocks:
            grid[block.rect.x // block_size][block.rect.y // block_size] = True

    def draw(self, screen):
        for block in self.blocks:
            screen.blit(block.image, block.rect)

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Тетрис")

# Создание сетки
grid = [[False] * (height // block_size) for _ in range(width // block_size)]

# Создание списка для хранения фигур
all_tetrominos = []

# Флаг для отслеживания таймера
falling_timer = pygame.time.get_ticks()
falling_interval = 500  # Интервал в миллисекундах

# Основной цикл игры
while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Если прошло достаточно времени, спускаем фигуру вниз
    if current_time - falling_timer >= falling_interval:
        falling_timer = current_time

        # Если нет активной фигуры или текущая фигура достигла нижней границы или столкнулась с другой фигурой
        if not all_tetrominos or all_tetrominos[-1].reached_bottom() or all_tetrominos[-1].check_collision(all_tetrominos[:-1]):
            # Создаем новую фигуру
            new_tetromino = Tetromino(white, [(0, 0), (1, 0), (2, 0), (1, 1)])
            all_tetrominos.append(new_tetromino)

        # Обработка движения фигуры вниз
        if not all_tetrominos[-1].reached_bottom() and not all_tetrominos[-1].check_collision(all_tetrominos[:-1]):
            all_tetrominos[-1].move(0, block_size, all_tetrominos)
        else:
            # Фиксация фигуры и создание новой
            all_tetrominos[-1].update_grid(grid)
            all_tetrominos[-1] = Tetromino(red, [(0, 0), (1, 0), (2, 0), (1, 1)])

    # Обработка управления фигурой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        all_tetrominos[-1].move(-block_size, 0, all_tetrominos[:-1])

    if keys[pygame.K_RIGHT]:
        all_tetrominos[-1].move(block_size, 0, all_tetrominos[:-1])

    # Очистка экрана
    screen.fill(black)

    # Отрисовка сетки
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]:
                pygame.draw.rect(screen, red, (x * block_size, y * block_size, block_size, block_size))

    # Отрисовка всех фигур
    for tetromino in all_tetrominos:
        tetromino.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Установка частоты обновления экрана (FPS)
    pygame.time.Clock().tick(5)  # Уменьшил FPS для лучшей видимости движения
