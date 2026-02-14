import arcade
from pyglet.event import EVENT_HANDLE_STATE

import game.consts as consts
import game.entities.player as player

class GameView(arcade.Window):

    def __init__(self):
        super().__init__(
            consts.WIDTH,
            consts.HEIGHT,
            consts.PROGRAM_TITLE,
            center_window=True
        )

        self.player = player.Player()

    def setup(self) -> None:
        pass

    def on_update(self, delta_time) -> None:
        self.player.on_update()

    def on_draw(self) -> None:
        self.clear(arcade.color.BLACK)

        self.player.on_draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.player.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        self.player.on_key_release(symbol, modifiers)

    def run_prog(self) -> None: #don't rename "run"
        self.setup()
        arcade.run()
