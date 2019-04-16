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

        self.color_status_text = arcade.color.RED_ORANGE

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

        #define the stage in map
        arcade.draw_rectangle_filled(30,
                                     SCREEN_HEIGHT-30,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)

        arcade.draw_rectangle_filled(50,
                                     SCREEN_HEIGHT - 30,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)

        arcade.draw_rectangle_filled(70,
                                     SCREEN_HEIGHT - 30,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)

        arcade.draw_rectangle_filled(30,
                                     SCREEN_HEIGHT - 50,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)

        arcade.draw_rectangle_filled(50,
                                     SCREEN_HEIGHT - 50,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)

        arcade.draw_rectangle_filled(70,
                                     SCREEN_HEIGHT - 50,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)

        arcade.draw_rectangle_filled(30,
                                     SCREEN_HEIGHT - 70,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)

        arcade.draw_rectangle_filled(50,
                                     SCREEN_HEIGHT - 70,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)

        arcade.draw_rectangle_filled(70,
                                     SCREEN_HEIGHT - 70,
                                     15,
                                     15,
                                     arcade.color.ORANGE_RED)



        arcade.draw_text(self.world.character.stage_name,
                         10,
                         SCREEN_HEIGHT-100,
                         arcade.color.WHITE,
                         15,
                         bold=2)


        if self.world.character.hit == True:
            self.color_status_text = arcade.color.RED_ORANGE
        elif self.world.character.exit_hit == True:
            self.color_status_text = arcade.color.GREEN

        arcade.draw_text(self.world.character.status,
                         SCREEN_WIDTH // 3.25,
                         SCREEN_HEIGHT // 1.25,
                         self.color_status_text,
                         50)

        arcade.draw_text(self.world.character.desc_status,
                         SCREEN_WIDTH // 2.9,
                         SCREEN_HEIGHT // 1.35,
                         arcade.color.WHITE_SMOKE,
                         15)




def main():
    window = FieldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
