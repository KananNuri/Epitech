import pygame
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((600, 600))

image_path = Path(__file__).parent / "assets" / "background.png"
background = pygame.image.load(image_path)
background = pygame.transform.scale(background, (600, 600))


def draw_stickman():
    # Head
    pygame.draw.circle(screen, "white", (300, 220), 30, 3)

    # Body
    pygame.draw.line(screen, "white", (300, 250), (300, 360), 3)

    # Arms
    pygame.draw.line(screen, "white", (300, 280), (250, 320), 3)
    pygame.draw.line(screen, "white", (300, 280), (350, 320), 3)

    # Legs
    pygame.draw.line(screen, "white", (300, 360), (250, 430), 3)
    pygame.draw.line(screen, "white", (300, 360), (350, 430), 3)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    draw_stickman()

    pygame.display.update()

pygame.quit()