
class Settings():
    """Класс для хранения настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed_factor = 0.5
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 240, 60, 60
        self.bullet_allowed = 3
        self.super_bullet = True

        # Настройка пришельцев
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп рста стоимости пришельцев.
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.1

        # Подсчет очков.
        self.alien_points = 50

        # fleet_direction = 1 обозначает движение вправо; -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

