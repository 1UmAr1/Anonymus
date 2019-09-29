import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import functions as gf
from pygame.sprite import Group
from scoreboard import Scoreboard
from button import Button
from game_stats import GameStats


def run_game():
    pygame.init()
    ai_settings = Settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    alien = Alien(ai_settings, screen)
    pygame.display.set_caption("Invasion2.0")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # main loop
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)



run_game()
