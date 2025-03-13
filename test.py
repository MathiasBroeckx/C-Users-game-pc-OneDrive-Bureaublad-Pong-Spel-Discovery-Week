import pygame
import sys


def start_screen():
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game Start Screen")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Fonts
    font_title = pygame.font.Font(None, 74)
    font_text = pygame.font.Font(None, 36)

    # Text surfaces
    title_text = font_title.render("Pong Game", True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    blink = True
    clock = pygame.time.Clock()

    while True:
        screen.fill(BLACK)
        screen.blit(title_text, title_rect)

        # Blinking text effect
        if blink:
            start_text = font_text.render("Press any key to start", True, WHITE)
            start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(start_text, start_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return  # Start the game

        pygame.time.wait(500)
        blink = not blink
        clock.tick(30)


if __name__ == "__main__":
    start_screen()
    print("Game started!")  # Replace with your game logic
