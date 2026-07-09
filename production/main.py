import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


# --------------------------------
# Button wiring from your schematic
#
# SW1 -> D0
# SW2 -> D1
# SW3 -> D2
#
# Each switch goes to GND when pressed.
# --------------------------------
button_pins = (
    board.D0,  # SW1: Fast Forward
    board.D1,  # SW2: Play / Pause
    board.D2,  # SW3: Rewind
)


class MyKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # This is for individual buttons wired directly to GND
        self.matrix = KeysScanner(
            pins=button_pins,
            value_when_pressed=False,
            pull=True,
        )


keyboard = MyKeyboard()

# Needed for media keys: volume, mute, play/pause, fast-forward, rewind
keyboard.extensions.append(MediaKeys())


# --------------------------------
# Rotary encoder wiring from your schematic
#
# Encoder A  -> D4
# Encoder B  -> D3
# Encoder S1 -> D5
# Encoder C/S2 -> GND
# --------------------------------
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D4, board.D3, board.D5),
)


# --------------------------------
# Rotary encoder functions
#
# Rotate left  -> Volume Down
# Rotate right -> Volume Up
# Press encoder -> Mute
# --------------------------------
encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU, KC.MUTE),
    )
]


# --------------------------------
# Button functions
#
# SW1 -> Fast Forward
# SW2 -> Play / Pause
# SW3 -> Rewind
# --------------------------------
keyboard.keymap = [
    [
        KC.MFFD,  # SW1: Fast Forward
        KC.MPLY,  # SW2: Play / Pause
        KC.MRWD,  # SW3: Rewind
    ]
]


if __name__ == "__main__":
    keyboard.go()