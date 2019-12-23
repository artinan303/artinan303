import pygame as pg
import random
import math
import time
# COLOURS
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

# SCREEN MEASURES
sWidth = 700
sHeight = 500

# ELEMENT VARS
bSize = 10
pHeight = 140
pWidth = 21

op = False




class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rocX = 10
        self.rocY = -4

    def collidesWith(self, paddle):
        if self.x >= paddle.x and self.x <= paddle.x + pWidth:
            if self.y + bSize >= paddle.y and self.y + bSize / 2 < paddle.y / 100 * 12.5:
                self.rocY += 12
                return True
            if self.y + bSize >= paddle.y + pHeight / 100 * 12.5 and self.y + bSize / 2 < paddle.y + pHeight / 100 * 27.5:
                self.rocY += 8
                return True
            if self.y + bSize / 2 >= paddle.y + pHeight / 100 * 27.5 and self.y + bSize / 2 < paddle.y + pHeight / 100 * 42.5:
                self.rocY += 4
                return True
            if self.y + bSize / 2 >= paddle.y + pHeight / 100 * 42.5 and self.y + bSize / 2 < paddle.y + pHeight / 100 * 57.5:
                return True
            if self.y + bSize / 2 >= paddle.y + pHeight / 100 * 57.5 and self.y + bSize / 2 < paddle.y + pHeight / 100 * 72.5:
                self.rocY -= 4
                return True
            if self.y + bSize / 2 >= paddle.y + pHeight / 100 * 72.5 and self.y + bSize / 2 < paddle.y + pHeight / 100 * 87.5:
                self.rocY -= 8
                return True
            if self.y + bSize / 2 >= paddle.y + pHeight / 100 * 87.5 and self.y + bSize / 2 < paddle.y + pHeight :
                self.rocY -= 12
                return True


class Paddle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rocX = 0
        self.rocY = 0

def main():
    pg.init()
    size = [sWidth,sHeight]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("game")
    clock = pg.time.Clock()
    done = False
    paddle1 = Paddle()
    paddle1.x = pWidth * 2
    paddle1.y = sHeight / 2 - pHeight
    paddle2 = Paddle()
    paddle2.x = sWidth - pWidth * 2
    paddle2.y = sHeight / 2 - pHeight
    ball1 = Ball()
    ball1.x = (sWidth / 2) - bSize
    ball1.y = (sHeight / 2) - bSize
    score1 = 0
    score2 = 0

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        keys = pg.key.get_pressed()
        # DEBUG
        if keys[pg.K_1]:
            ball1.rocX += 1
        elif keys[pg.K_2]:
            ball1.rocY += 1
        elif keys[pg.K_3]:
            ball1.rocX -= 1
        elif keys[pg.K_4]:
            ball1.rocY -= 1

        # MOVE
        if paddle1.y > 0:
            if keys[pg.K_w]:
                paddle1.y -= 10
        if paddle1.y + pHeight < sHeight:
            if keys[pg.K_s]:
                paddle1.y += 10
        if paddle1.y < 0:
            paddle1.y = 0
        elif paddle1.y > sHeight:
            paddle1.y = 0

        # TRACKING
        if op:
            if ball1.x > sWidth / 2 - bSize / 2:
                if paddle2.y + pHeight / 2 < ball1.y:
                    paddle2.y += 20
                elif paddle2.y + pHeight / 2 > ball1.y + bSize:
                    paddle2.y -= 20
            else:
                paddle2.y = sHeight / 2 - pHeight / 2
        else:
            if paddle2.y > 0:
                if keys[pg.K_UP]:
                    paddle2.y -= 10
            if paddle2.y + pHeight < sHeight:
                if keys[pg.K_DOWN]:
                    paddle2.y += 10
            if paddle2.y < 0:
                paddle2.y = 0
            elif paddle2.y > sHeight:
                paddle2.y = 0

        ball1.x += ball1.rocX
        ball1.y += ball1.rocY
        if ball1.y > sHeight - bSize:
            ball1.rocY *= -1
        if ball1.y < bSize:
            ball1.rocY *= -1
        if ball1.x > sWidth - bSize:
            score1 += 1
            pg.draw.circle(screen, BLACK, [int(ball1.x), int(ball1.y)], bSize)
            ball1.x = (sWidth / 2) - bSize
            ball1.y = (sHeight / 2) - bSize
            pg.draw.circle(screen, RED, [int(ball1.x), int(ball1.y)], bSize)
            ball1.rocX = 10
            ball1.rocY = -4
        if ball1.x < bSize:
            score2 += 1
            pg.draw.circle(screen, BLACK, [int(ball1.x), int(ball1.y)], bSize)
            ball1.x = (sWidth / 2) - bSize
            ball1.y = (sHeight / 2) - bSize
            pg.draw.circle(screen, RED, [int(ball1.x), int(ball1.y)], bSize)
            ball1.rocX = 10
            ball1.rocY = 4

        if paddle1.y >= sHeight:
            paddle1.y = sHeight
        if  paddle1.y <= 0:
            paddle1.y = 0
        screen.fill(BLACK)
        pg.draw.circle(screen, RED, [int(ball1.x), int(ball1.y)], bSize)
        #print(paddle1.y)
        if ball1.collidesWith(paddle1):
            ball1.rocX *= -1
            if ball1.rocX < 30:
                ball1.rocX += 2
            #ball1.rocY *= -1
        if ball1.collidesWith(paddle2):
            ball1.rocX *= -1
            if ball1.rocX > -30:
                ball1.rocX -= 2
            #ball1.rocY *= -1
        pg.draw.rect(screen, BLUE, [int(paddle1.x), int(paddle1.y), pWidth, pHeight])
        pg.draw.rect(screen, BLUE, [int(paddle2.x), int(paddle2.y), pWidth, pHeight])

        # SCORE
        score = str(score1) + ":" + str(score2)
        font = pg.font.Font('freesansbold.ttf', 32)
        text = font.render(score, True, WHITE)
        textRect = text.get_rect()
        textRect.center = (sWidth/2,30)
        screen.blit(text, textRect)
        clock.tick(60)
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
