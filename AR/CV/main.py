import pygame
import random
import math

ancho_celda = 50
columnas = filas = 10
width = columnas * ancho_celda
height = filas * ancho_celda

class snake:
    bbody = []
    dirx = 0
    diry = 1
    cap = pygame.Vector2(math.ceil(columnas/2), math.ceil(filas/2))

    def move(self):
        for i in range( len(self.bbody) - 1, -1, -1) :
            if i == 0:
                self.bbody[i] = pygame.Vector2(self.cap)
            else:
                self.bbody[i] = pygame.Vector2(self.bbody[i-1])

        self.cap.x += self.dirx
        self.cap.y += self.diry

    def move_until_last(self):
        for i in range( len(self.bbody) - 1, -1, -1) :
            if i == 0:
                self.bbody[i] = pygame.Vector2(self.cap)
            else:
                if i != len(self.bbody) - 1:
                    self.bbody[i] = pygame.Vector2(self.bbody[i-1])

        self.cap.x += self.dirx
        self.cap.y += self.diry


def main():
    pygame.init()

    screen = pygame.display.set_mode((filas*ancho_celda, columnas*ancho_celda))
    s = snake()
    apple = pygame.Vector2(random.randint(0, columnas-1), random.randint(0, filas-1))
    clock = pygame.time.Clock()
    eat = False
    pause = False
    running = True
    while running:
        clock.tick(3)
        screen.fill((0, 0, 0))

        for i in range(columnas):
            pygame.draw.line(screen, (255, 255, 255), (i*ancho_celda, 0), (i*ancho_celda, height))
        for i in range(filas):
            pygame.draw.line(screen, (255, 255, 255), (0, i*ancho_celda), (width, i*ancho_celda))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if s.diry == 0:
                        s.dirx = 0
                        s.diry = -1
                if event.key == pygame.K_DOWN:
                    if s.diry == 0:
                        s.dirx = 0
                        s.diry = 1
                if event.key == pygame.K_LEFT:
                    if s.dirx == 0:
                        s.dirx = -1
                        s.diry = 0
                if event.key == pygame.K_RIGHT:
                    if s.dirx == 0:
                        s.dirx = 1
                        s.diry = 0
                if event.key == pygame.K_p:
                    pause = not pause

        if not pause:
            if not eat:
                s.move()
            else:
                s.move_until_last()
                eat = False

            if s.cap.x == apple.x and s.cap.y == apple.y:
                eat = True
                apple = pygame.Vector2(random.randint(0, columnas-1), random.randint(0, filas-1))
                if not s.bbody:
                    s.bbody.append(pygame.Vector2(s.cap))
                else:
                    s.bbody.append(pygame.Vector2(s.bbody[-1]))

        pygame.draw.rect(screen, (255, 0, 0), pygame.rect.Rect(apple.x*ancho_celda+1, apple.y*ancho_celda+1, ancho_celda-1, ancho_celda-1))
        pygame.draw.rect(screen, (0, 0, 255), pygame.rect.Rect(s.cap.x*ancho_celda+1, s.cap.y*ancho_celda+1, ancho_celda-1, ancho_celda-1))
        r = len(s.bbody)
        for i in range(r):
            pygame.draw.rect(screen, (0, 0, 255), pygame.rect.Rect(s.bbody[i].x*ancho_celda+1, s.bbody[i].y*ancho_celda+1, ancho_celda-1, ancho_celda-1))

        pygame.display.update()


if __name__ == "__main__":
    main()
