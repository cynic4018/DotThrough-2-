import arcade
from models import Character, World

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()


class FieldWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.character_sprite = ModelSprite('images/character.png',
                                            model=self.world.character)
        self.object_cannot_touch_sprite = ModelSprite('images/pillar.png',
                                               model=self.world.stage_one_objects)
        self.exit_gate_sprite = ModelSprite('images/Exit_gate.png',
                                            model=self.world.exit_gate)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def update(self, delta):
        self.world.update(delta)


    def on_draw(self):
        arcade.start_render()

        self.object_cannot_touch_sprite.draw()
        self.exit_gate_sprite.draw()
        self.character_sprite.draw()

        arcade.draw_text(self.world.character.status,
                         self.world.width // 3.25,
                         self.world.height // 1.25,
                         arcade.color.RED_ORANGE,
                         50)
        arcade.draw_text(self.world.character.desc_status,
                         self.world.width // 2.9,
                         self.world.height // 1.35,
                         arcade.color.WHITE_SMOKE,
                         15)




def main():
    window = FieldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
