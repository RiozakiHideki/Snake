import random
import pygame

pygame.init()  # Инициализируем библиотеку pygame
dis = pygame.display.set_mode([1296, 729])  # задаём разрешение окну
clock = pygame.time.Clock()  # необходимо в конце для fps

cube = pygame.image.load('images/cube.png')  # загружаем нашу картинку
cube_rect = cube.get_rect()  # получаем координаты и размер объекта
# т.к. координат ещё не задано, получается (0, 0, 27, 27)

size = cube_rect.size[0]  # переменная для удобства. равна 27
cube_rect.x = size  # задаём координату x нашему кубу
cube_rect.y = size  # задаём координату y нашему кубу

# парсим возможные координаты для красного квадрата
possible_coordinates_x = list(range(size, dis.get_width() - size, size))
possible_coordinates_y = list(range(size, dis.get_height() - size, size))

red_cube = pygame.image.load('images/red_cube.png')  # картинка красного квадрата
red_cube_rect = red_cube.get_rect()  # координаты и размер красного квадрата
red_cube_rect.x = random.choice(possible_coordinates_x)  # координата x красного квадрата (рандомная из списка возможных)
red_cube_rect.y = random.choice(possible_coordinates_y)  # координата x красного квадрата (рандомная из списка возможных)

# Инициализация сегментов змейки
segments = [cube_rect]


direction = 'right'  # Начальное направление движения змейки
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            if event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'

    if direction == 'down':
        new_head = segments[0].move(0, +size)
    elif direction == 'up':
        new_head = segments[0].move(0, -size)
    elif direction == 'left':
        new_head = segments[0].move(-size, 0)
    elif direction == 'right':
        new_head = segments[0].move(+size, 0)
    else:
        new_head = segments[0].copy()

    # Проверка на выход за границы экрана
    if new_head.x < 27 or new_head.x >= dis.get_width() - 27 or new_head.y < 27 or new_head.y >= dis.get_height() - 27:
        running = False

    # Проверка на столкновение с собой
    if new_head in segments:
        running = False

    segments.insert(0, new_head)

    if new_head.colliderect(red_cube_rect):
        red_cube_rect.x = random.choice(possible_coordinates_x)
        red_cube_rect.y = random.choice(possible_coordinates_y)
    else:
        segments.pop()

    print(segments)
    dis.fill((0, 0, 0))
    for segment in segments:
        dis.blit(cube, segment.topleft)

    dis.blit(red_cube, red_cube_rect)
    pygame.display.update()
    clock.tick(10)
pygame.quit()
