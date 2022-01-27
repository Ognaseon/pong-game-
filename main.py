import pygame

from utils.constant import *
from utils.platform import Platform
from utils.ball import Ball

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong!')

platform_group = pygame.sprite.Group()
ball_group = pygame.sprite.GroupSingle()

r_lose, l_lose = 3, 3
speed = 5
font = pygame.font.SysFont('Arial', 40)

def font_set(l_lose, r_lose):
    global font
    font_l = font.render(f'{l_lose}', 1, 'White')
    font_r = font.render(f'{r_lose}', 1, 'White')
    font_l_rect = font_l.get_rect(topleft=(10, 10))
    font_r_rect = font_l.get_rect(topright=(WIDTH - 10, 10))
    SCREEN.blit(font_l, font_l_rect)
    SCREEN.blit(font_r, font_r_rect)
    

def losing(ball_group):
    global end_screen, r_lose, l_lose, speed

    if l_lose == 0 or r_lose == 0:
        r_lose, l_lose = 3, 3
        end_screen = True
        speed = 5


    if ball_group:
        if ball_group.sprite.rect.left >= WIDTH:
            r_lose -= 1
            speed += 2
            ball_group.sprite.kill()
            ball_w = Ball(platform_group, speed)
            ball_group.add(ball_w)
            
        elif ball_group.sprite.rect.right <= 0:
            l_lose -= 1
            speed += 2
            ball_group.sprite.kill()
            ball_w = Ball(platform_group, speed)
            ball_group.add(ball_w)


    return l_lose, r_lose, end_screen


def main():
    global end_screen, speed
    platform_l = Platform(100, HEIGHT//2, 'left')
    platform_r = Platform(WIDTH - 100, HEIGHT//2, 'right')
    platform_group.add(platform_l, platform_r)

    ball_w = Ball(platform_group, speed)
    ball_group.add(ball_w)

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    end_screen = False
                
        if not end_screen:
            SCREEN.fill('Black')
            l_lose, r_lose, end_screen = losing(ball_group)
            font_set(l_lose, r_lose)

            platform_group.draw(SCREEN)
            platform_group.update()

            ball_group.draw(SCREEN)
            ball_group.update()
        else:

            SCREEN.fill('Black')
            if l_lose == 0:
                lose_font = font.render(f'Gracz prawy wygrał!', 1, 'White')
                lose_font_rect = lose_font.get_rect(center=(WIDTH//2, HEIGHT//2))
                SCREEN.blit(lose_font, lose_font_rect)
            else:
                lose_font = font.render(f'Gracz lewy wygrał!', 1, 'White')
                lose_font_rect = lose_font.get_rect(center=(WIDTH//2, HEIGHT//2))
                SCREEN.blit(lose_font, lose_font_rect)

        pygame.display.update()

if __name__ == '__main__':
    end_screen = False
    main()