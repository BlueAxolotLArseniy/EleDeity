import arcade
import game.consts as consts
import game.loader as loader

class Player(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self._player = arcade.Sprite(loader.player_image)
        self._player.position = 640, 360

        self._player_list = arcade.SpriteList()
        self._player_list.append(self._player)

        self._speedy = 0
        self._speedx = 0

        self._directions = {
            "LEFT": False,
            "RIGHT": False
        }

    def on_update(self) -> None:
        # self._player.center_y += self._speedy
        self._player.center_x += self._speedx

        self._speedy += consts.GRAVITY

        if self._directions["LEFT"]:
            self._speedx = -consts.PLAYER_MOVEMENT_SPEED
        elif not self._directions["LEFT"] or self._directions["RIGHT"]:
            self._speedx *= consts.PLAYER_MOVEMENT_SLOWDOWN
        if self._directions["RIGHT"]:
            self._speedx = consts.PLAYER_MOVEMENT_SPEED

        print(self._speedy)

        self._player_list.update()

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.A:
            self._directions["LEFT"] = True
        if symbol == arcade.key.D:
            self._directions["RIGHT"] = True
        if symbol == arcade.key.SPACE or symbol == arcade.key.W:
            pass

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.A:
            self._directions["LEFT"] = False
        if symbol == arcade.key.D:
            self._directions["RIGHT"] = False

    def on_draw(self) -> None:
        self._player_list.draw()
