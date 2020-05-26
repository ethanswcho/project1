import arcade
from objects.sprite_wrapper import SpriteWrapper

# Constants
CHARACTER_SCALING = 0.6


class PlayerSprite(SpriteWrapper):

    def __init__(self, window: arcade.Window, coordinates: tuple):
        super().__init__(window, coordinates,
                         ":resources:images/animated_characters/zombie/zombie_idle.png", CHARACTER_SCALING)
        window.player_sprite = self
        window.player_list.append(self)
