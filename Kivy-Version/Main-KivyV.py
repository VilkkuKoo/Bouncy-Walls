from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.clock import Clock
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 30
BALL_SPAWN_MARGIN = 50
GRAVITY = 0.2
JUMP_STRENGTH = -5
PLAYER_SIZE = (50, 50)

Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)

class BouncyWallsApp(App):
    def build(self):
        self.score = 0
        self.high_score = 0
        self.is_muted = False
        self.main_layout = FloatLayout()

        self.player_image = Image(source='Python-Version/Assets/sprites/player1.png', size_hint=(None, None), size=PLAYER_SIZE)
        self.player_image.pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.main_layout.add_widget(self.player_image)

        self.ball_image = Image(source='Python-Version/Assets/sprites/ball.png', size_hint=(None, None), size=(BALL_SIZE, BALL_SIZE))
        self.ball_image.pos = (random.randint(BALL_SPAWN_MARGIN, SCREEN_WIDTH - BALL_SPAWN_MARGIN), random.randint(BALL_SPAWN_MARGIN, SCREEN_HEIGHT - BALL_SPAWN_MARGIN))
        self.main_layout.add_widget(self.ball_image)

        self.score_label = Label(text=f'Score: {self.score}', pos=(70, 30), size_hint=(None, None))
        self.main_layout.add_widget(self.score_label)

        self.high_score_label = Label(text=f'High Score: {self.high_score}', pos=(70, 70), size_hint=(None, None))
        self.main_layout.add_widget(self.high_score_label)

        self.play_button = Button(text='Play', size_hint=(None, None), size=(200, 50), pos=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
        self.play_button.bind(on_press=self.start_game)
        self.main_layout.add_widget(self.play_button)

        self.mute_button = Button(text='Mute', size_hint=(None, None), size=(200, 50), pos=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
        self.mute_button.bind(on_press=self.toggle_mute)
        self.main_layout.add_widget(self.mute_button)

        self.quit_button = Button(text='Quit', size_hint=(None, None), size=(200, 50), pos=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 90))
        self.quit_button.bind(on_press=self.stop)
        self.main_layout.add_widget(self.quit_button)

        return self.main_layout

    def start_game(self, instance):
        self.score = 0
        self.player_image.pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.ball_image.pos = (random.randint(BALL_SPAWN_MARGIN, SCREEN_WIDTH - BALL_SPAWN_MARGIN), random.randint(BALL_SPAWN_MARGIN, SCREEN_HEIGHT - BALL_SPAWN_MARGIN))
        self.play_button.disabled = True
        self.mute_button.disabled = True
        self.quit_button.disabled = True
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def toggle_mute(self, instance):
        self.is_muted = not self.is_muted
        self.mute_button.text = 'Unmute' if self.is_muted else 'Mute'

    def update(self, dt):
        self.player_image.y += GRAVITY
        if self.player_image.y < 0 or self.player_image.top > SCREEN_HEIGHT:
            self.end_game()
        if self.player_image.x < 0 or self.player_image.right > SCREEN_WIDTH:
            self.player_image.x = SCREEN_WIDTH // 2
            self.player_image.y = SCREEN_HEIGHT // 2
        if self.player_image.collide_widget(self.ball_image):
            self.score += 1
            self.ball_image.pos = (random.randint(BALL_SPAWN_MARGIN, SCREEN_WIDTH - BALL_SPAWN_MARGIN), random.randint(BALL_SPAWN_MARGIN, SCREEN_HEIGHT - BALL_SPAWN_MARGIN))
            self.score_label.text = f'Score: {self.score}'
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.text = f'High Score: {self.high_score}'

    def end_game(self):
        Clock.unschedule(self.update)
        self.play_button.disabled = False
        self.mute_button.disabled = False
        self.quit_button.disabled = False

if __name__ == '__main__':
    BouncyWallsApp().run()