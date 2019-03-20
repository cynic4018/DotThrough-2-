import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class FieldWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.GRAY)
    def on_draw(self):
        arcade.start_render()

def main():
    window = FieldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
