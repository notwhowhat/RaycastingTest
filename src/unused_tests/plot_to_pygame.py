import pygame
import math, sys

FOV = 60
DEG_RAD = 0.0174533

map = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Raycaster')
clock = pygame.time.Clock()

for i in range(len(map[0])):
    for j in range(len(map[1])):
        if map[i][j] == 1:
            map[i][j] = 1 # should be a random color, but ill add shading

posx, posy = (1, 1)
exitx, exity = (3, 3)
rot = math.pi / 4

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill((255, 255, 255))
        draw_3d()

        pygame.display.update()
        clock.tick(60)

def draw_3d():
    for i in range(FOV):
        rot_i = rot + (i - FOV / 2) * DEG_RAD
        x, y, = (posx, posy)
        sin, cos = (0.02 * math.sin(rot_i), 0.02 * math.cos(rot_i))
        n = 0

        while True:
            xx, yy = (x, y)
            x, y = (x + cos, y + sin)
            n += 1
            if map[int(x)][int(y)] != 0:
                h = 1 / (0.02 * n)
                break
        pygame.draw.line(screen, (0, 0, 0), (-h, x), (h, x))

if __name__ == '__main__':
    main()