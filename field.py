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
        super().__init__(width, height, "・2　DotThrough")

        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.color_status_text = arcade.color.RED_ORANGE

        self.color_map_in_stage = arcade.color.ORANGE_RED
        self.color_map_not_in_stage = arcade.color.LIGHT_GRAY

        self.object_cant_touch_stage_sprite = self.world.object_list

        self.star_sprite = self.world.star_list

        self.exit_gate_sprite = ModelSprite('images/Exit_gate.png',
                                            model=self.world.exit_gate,
                                            scale=0.1)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def update(self, delta):
        self.world.update(delta)

        self.character_sprite = ModelSprite('images/character.png'
                                            if self.world.character.animation == 1
                                            else 'images/character2.png'
                                            if self.world.character.animation == 2
                                            else 'images/character3.png'
                                            if self.world.character.animation == 3
                                            else 'images/character4.png',
                                            model=self.world.character,
                                            scale=0.1)


    def on_draw(self):
        arcade.start_render()

        self.character_sprite.draw()
        self.object_cant_touch_stage_sprite.draw()
        self.star_sprite.draw()
        self.exit_gate_sprite.draw()

        #define the stage location in map
        arcade.draw_rectangle_filled(30,
                                     SCREEN_HEIGHT - 30,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 1
                                     else self.color_map_not_in_stage)

        arcade.draw_rectangle_filled(50,
                                     SCREEN_HEIGHT - 30,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 2
                                     else self.color_map_not_in_stage)

        arcade.draw_rectangle_filled(70,
                                     SCREEN_HEIGHT - 30,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 3
                                     else self.color_map_not_in_stage)

        arcade.draw_rectangle_filled(30,
                                     SCREEN_HEIGHT - 50,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 4
                                     else self.color_map_not_in_stage)

        arcade.draw_rectangle_filled(50,
                                     SCREEN_HEIGHT - 50,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 5
                                     else self.color_map_not_in_stage)

        arcade.draw_rectangle_filled(70,
                                     SCREEN_HEIGHT - 50,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 6
                                     else self.color_map_not_in_stage)

        arcade.draw_rectangle_filled(30,
                                     SCREEN_HEIGHT - 70,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 7
                                     else self.color_map_not_in_stage)

        arcade.draw_rectangle_filled(50,
                                     SCREEN_HEIGHT - 70,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 8
                                     else self.color_map_not_in_stage)

        arcade.draw_rectangle_filled(70,
                                     SCREEN_HEIGHT - 70,
                                     15,
                                     15,
                                     self.color_map_in_stage
                                     if self.world.stage_objects.stage_count == 9
                                     else self.color_map_not_in_stage)


        arcade.draw_text(self.world.stage_objects.stage_name,
                         10,
                         SCREEN_HEIGHT-105,
                         self.color_map_in_stage,
                         15,
                         bold=2)

        #star collects
        arcade.draw_rectangle_filled(SCREEN_WIDTH-90,
                                     SCREEN_HEIGHT-30,
                                     20,
                                     20,
                                     arcade.color.GOLDEN_POPPY
                                     if self.world.stage_objects.stage_stars >= 1
                                     else arcade.color.EERIE_BLACK,
                                     tilt_angle = 45)

        arcade.draw_rectangle_filled(SCREEN_WIDTH - 60,
                                     SCREEN_HEIGHT - 30,
                                     20,
                                     20,
                                     arcade.color.YELLOW_ORANGE
                                     if self.world.stage_objects.stage_stars >= 2
                                     else arcade.color.EERIE_BLACK,
                                     tilt_angle=45)

        arcade.draw_rectangle_filled(SCREEN_WIDTH - 30,
                                     SCREEN_HEIGHT - 30,
                                     20,
                                     20,
                                     arcade.color.ORANGE
                                     if self.world.stage_objects.stage_stars == 3
                                     else arcade.color.EERIE_BLACK,
                                     tilt_angle=45)


        if self.world.character.hit == True:
            self.color_status_text = arcade.color.RED_ORANGE
        elif self.world.character.exit_hit == True:
            if self.world.stage_objects.stage_count < self.world.stage_objects.MAX_STAGE:
                self.color_status_text = arcade.color.GREEN
            else:
                self.color_status_text = arcade.color.ORANGE_PEEL

        arcade.draw_text(self.world.stage_objects.status,
                         SCREEN_WIDTH // 3.25,
                         SCREEN_HEIGHT // 1.25,
                         self.color_status_text,
                         50,
                         bold=2)

        arcade.draw_text(self.world.stage_objects.desc_status,
                         SCREEN_WIDTH // 2.9,
                         SCREEN_HEIGHT // 1.35,
                         self.color_status_text,
                         15,
                         bold=2)

        arcade.draw_text(self.world.stage_objects.tutorial_text,
                         SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT // 2,
                         arcade.color.ORANGE_RED,
                         30,
                         bold=7)



def main():
    window = FieldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
