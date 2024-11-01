import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RECT_SIZE = 50
BALL_SIZE = 20
RECT_COLOR = (255, 0, 0)
BALL_COLOR = (0, 0, 255)
BG_COLOR = (0, 0, 0)
FPS = 60
GRAVITY = 0.2  # Lower gravity for a more "floaty" effect
JUMP_STRENGTH = -5
BUTTON_COLOR = (0, 255, 0)
BUTTON_HOVER_COLOR = (0, 200, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36
TITLE_FONT_SIZE = 48

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncy Walls - Python Edition")

# Font
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, TITLE_FONT_SIZE)

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

        # Draw title
        draw_text('Bouncy Walls', title_font, BUTTON_TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text('Python Edition', font, BUTTON_TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 50)

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
    rect_y = SCREEN_HEIGHT // 4  # Spawn near the top
    rect_vel_y = 0

    # Ball position
    ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
    ball_y = random.randint(0, SCREEN_HEIGHT - BALL_SIZE)

    # Score
    score = 0

    # Step 3: Create the main game loop
    clock = pygame.time.Clock()
    running = True

    while running:
        # Step 4: Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
            main_menu()

        # Check for collision with the top of the screen
        if rect_y < 0:
            main_menu()

        # Check for collision with the ball
        if (rect_x < ball_x + BALL_SIZE and
            rect_x + RECT_SIZE > ball_x and
            rect_y < ball_y + BALL_SIZE and
            rect_y + RECT_SIZE > ball_y):
            score += 1
            ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
            ball_y = random.randint(0, SCREEN_HEIGHT - BALL_SIZE)

        # Step 6: Rendering
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, RECT_SIZE, RECT_SIZE))
        pygame.draw.ellipse(screen, BALL_COLOR, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
        draw_text(f'Score: {score}', font, BUTTON_TEXT_COLOR, screen, 70, 30)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Step 7: Cleanup
    pygame.quit()
    sys.exit()

# Start the game with the main menu
main_menu()