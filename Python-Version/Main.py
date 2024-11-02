import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Load sound effects
jump_sound = pygame.mixer.Sound('Python-Version/Assets/Sounds/jump.wav')
pickup_sound = pygame.mixer.Sound('Python-Version/Assets/Sounds/pickupCoin.wav')
bounce_sound = pygame.mixer.Sound('Python-Version/Assets/Sounds/bounce.wav')
death_sound = pygame.mixer.Sound('Python-Version/Assets/Sounds/hitHurt.wav')
click_sound = pygame.mixer.Sound('Python-Version/Assets/Sounds/blipSelect.wav')

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 30
BALL_SPAWN_MARGIN = 50
GRAVITY = 0.2
JUMP_STRENGTH = -5
FPS = 60
BG_COLOR = (0, 0, 0)
BALL_COLOR = (0, 255, 0)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36
TITLE_FONT_SIZE = 72
PLAYER_SIZE = (50, 50)  # New constant for player size

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncy Walls - Python Edition")

# Load and resize player image
player_image_original = pygame.image.load('Python-Version/Assets/sprites/player1.png')
player_image_original = pygame.transform.scale(player_image_original, PLAYER_SIZE)
player_rect = player_image_original.get_rect()

# Font
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, TITLE_FONT_SIZE)

# Button positions and sizes
play_button_rect = pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50))
mute_button_rect = pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 50))
quit_button_rect = pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 90, 200, 50))

# Mute state
is_muted = False

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    global is_muted
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

        if mute_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, mute_button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, mute_button_rect)

        if quit_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, quit_button_rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, quit_button_rect)

        draw_text('Play', font, BUTTON_TEXT_COLOR, screen, play_button_rect.centerx, play_button_rect.centery)
        draw_text('Mute' if not is_muted else 'Unmute', font, BUTTON_TEXT_COLOR, screen, mute_button_rect.centerx, mute_button_rect.centery)
        draw_text('Quit', font, BUTTON_TEXT_COLOR, screen, quit_button_rect.centerx, quit_button_rect.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    print("Play button clicked")  # Debug print
                    click_sound.play()
                    game_loop()
                if mute_button_rect.collidepoint(event.pos):
                    is_muted = not is_muted
                    pygame.mixer.music.set_volume(0 if is_muted else 1)
                    bounce_sound.set_volume(0 if is_muted else 1)
                    pickup_sound.set_volume(0 if is_muted else 1)
                    click_sound.set_volume(0 if is_muted else 1)
                    jump_sound.set_volume(0 if is_muted else 1)
                    death_sound.set_volume(0 if is_muted else 1)
                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

def game_loop():
    global player_image_original  # Declare player_image_original as global
    print("Game loop started")  # Debug print

    # Reset player image to original
    player_image = player_image_original.copy()
    player_rect = player_image.get_rect()

    # Rectangle position and velocity
    rect_x = SCREEN_WIDTH // 2
    rect_y = SCREEN_HEIGHT // 2  # Spawn in the middle of the screen
    rect_vel_y = 0
    rect_vel_x = -5  # Initial horizontal velocity

    # Ball position
    ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
    ball_y = random.randint(BALL_SPAWN_MARGIN, SCREEN_HEIGHT - BALL_SIZE - BALL_SPAWN_MARGIN)

    # Score
    score = 0

    # Step 3: Create the main game loop
    clock = pygame.time.Clock()
    running = True
    flipped = False  # Track if the player image is flipped

    while running:
        # Step 4: Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                rect_vel_y = JUMP_STRENGTH
                jump_sound.play()

        # Apply gravity
        rect_vel_y += GRAVITY
        rect_y += rect_vel_y
        rect_x += rect_vel_x

        # Update player rect position
        player_rect.topleft = (rect_x, rect_y)

        # Check for collision with the top or the bottom of the screen
        if rect_y > SCREEN_HEIGHT - player_rect.height or rect_y < 0:
            death_sound.play()
            running = False  # Exit the game loop and return to the main menu

        # Check for collision with the left and right walls
        if rect_x <= 0 or rect_x >= SCREEN_WIDTH - player_rect.width:
            rect_vel_x = -rect_vel_x  # Reverse direction
            flipped = not flipped  # Toggle the flipped state
            player_image = pygame.transform.flip(player_image, True, False)  # Mirror the player image
            bounce_sound.play()

        # Check for collision with the ball
        if (rect_x < ball_x + BALL_SIZE and
            rect_x + player_rect.width > ball_x and
            rect_y < ball_y + BALL_SIZE and
            rect_y + player_rect.height > ball_y):
            score += 1
            ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
            ball_y = random.randint(BALL_SPAWN_MARGIN, SCREEN_HEIGHT - BALL_SIZE - BALL_SPAWN_MARGIN)
            pickup_sound.play()

        # Step 6: Rendering
        screen.fill(BG_COLOR)
        screen.blit(player_image, player_rect)
        pygame.draw.ellipse(screen, BALL_COLOR, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
        draw_text(f'Score: {score}', font, BUTTON_TEXT_COLOR, screen, 70, 30)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    print("Game loop ended")  # Debug print
    main_menu()

# Start the game with the main menu
main_menu()