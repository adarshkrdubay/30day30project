class Settings:
    def __init__(self):
        self.screen_width =1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.bullet_speed=1.5
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color=(60,60,60)
        self.bullet_allowed = 3
        self.alien_speed=1.0
        self.fleet_drop_speed = 5
        self.fleet_direction =1
        self.ship_limit=3
        self.speedup_scale= 1.1
        self.alien_point = 50
        self.alien_row=10
        self.score_scale = 1.5
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed= 1.0
        self.fleet_direction = 1
        self.alien_row=10
    def increase_speed (self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_row   -= 1
        self.alien_point = int(self.alien_point * self.score_scale)
        print(self.alien_point)
        