import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RECT_SIZE = 50
RECT_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -10
BUTTON_COLOR = (0, 255, 0)
BUTTON_HOVER_COLOR = (0, 200, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncy Walls - Python Edition")

# Font
font = pygame.font.Font(None, FONT_SIZE)

# Button positions and sizes
play_button_rect = pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50))
quit_button_rect = pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 50))

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(BG_COLOR)

        mx, my = pygame.mouse.get_pos()

        # Draw buttons
        if play_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, play_button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, play_button_rect)

        if quit_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, quit_button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, quit_button_rect)

        draw_text('Play', font, BUTTON_TEXT_COLOR, screen, play_button_rect.centerx, play_button_rect.centery)
        draw_text('Quit', font, BUTTON_TEXT_COLOR, screen, quit_button_rect.centerx, quit_button_rect.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game_loop()
                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

def game_loop():
    # Rectangle position and velocity
    rect_x = SCREEN_WIDTH // 2
    rect_y = SCREEN_HEIGHT // 2
    rect_vel_y = 0

    # Step 3: Create the main game loop
    clock = pygame.time.Clock()
    running = True

    while running:
        # Step 4: Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Step 5: Game logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rect_x > 0:
            rect_x -= 5
        if keys[pygame.K_RIGHT] and rect_x < SCREEN_WIDTH - RECT_SIZE:
            rect_x += 5
        if keys[pygame.K_UP]:
            rect_vel_y = JUMP_STRENGTH

        # Apply gravity
        rect_vel_y += GRAVITY
        rect_y += rect_vel_y

        # Check for collision with the bottom of the screen
        if rect_y > SCREEN_HEIGHT - RECT_SIZE:
            rect_y = SCREEN_HEIGHT - RECT_SIZE
            rect_vel_y = 0

        # Check for collision with the top of the screen
        if rect_y < 0:
            rect_y = 0
            rect_vel_y = 0

        # Step 6: Rendering
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, RECT_SIZE, RECT_SIZE))
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Step 7: Cleanup
    pygame.quit()
    sys.exit()

# Start the game with the main menu
main_menu()