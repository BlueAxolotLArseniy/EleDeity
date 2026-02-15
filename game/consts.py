import game.func_common as func_common

WINDOW_PROPORTIONS = 16 / 9
WINDOW_SCALE = 0.5

phys_w, phys_h, scale = func_common.get_screen_specs()

WIDTH = int((phys_w / 2) / scale)
HEIGHT = int((phys_h / 2) / scale)

PROGRAM_TITLE = "EleDeity"

PLAYER_MOVEMENT_SPEED = 6
GRAVITY = -1
PLAYER_MOVEMENT_SLOWDOWN = 0.95

# func_common.get_monitor_scale()