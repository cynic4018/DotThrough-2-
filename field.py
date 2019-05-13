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
    GAME_MODE = 0
    H2P = 1
    def __init__(self, width, height):
        super().__init__(width, height, "・2　DotThrough")

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.color_status_text = arcade.color.RED_ORANGE

        self.color_map_in_stage = arcade.color.ORANGE_RED
        self.color_map_not_in_stage = arcade.color.LIGHT_GRAY

        self.star_sprite = self.world.star_list

        self.exit_gate_sprite = ModelSprite('images/Exit_gate.png',
                                            model=self.world.exit_gate,
                                            scale=1)
        self.start_button = arcade.Sprite('images/Start.png',
                                          scale=0.35,
                                          center_x= SCREEN_WIDTH // 2,
                                          center_y= SCREEN_HEIGHT // 4)


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ENTER and self.GAME_MODE == 1:
            self.H2P += 1
        if self.GAME_MODE == 2:
            self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        if self.GAME_MODE == 2:
            self.world.on_key_release(key, key_modifiers)

    def on_mouse_press(self, x:float, y:float, button, key_modifiers):
        if self.GAME_MODE == 0:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if self.start_button.center_y - 25 <= y <= self.start_button.center_y + 25\
                    and self.start_button.center_x - 85 <= x <= self.start_button.center_x + 85:

                    self.GAME_MODE = 1


    def update(self, delta):
        self.world.update(delta)

        self.character_sprite = ModelSprite('images/character.png'
                                            if self.world.character.animation == 1
                                            else 'images/character2.png'
                                            if self.world.character.animation == 2
                                            else 'images/character3.png'
                                            if self.world.character.animation == 3
                                            else 'images/character4.png',
                                            model=self.world.character)

        self.object_cant_touch_stage_sprite = self.world.object_list


    def on_draw(self):
        arcade.start_render()

        if self.GAME_MODE == 0:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2,
                                          SCREEN_HEIGHT // 2,
                                          SCREEN_WIDTH,
                                          SCREEN_HEIGHT,
                                          arcade.load_texture("images/Interface.png"))

            self.start_button.draw()

        elif self.GAME_MODE == 1:
            if self.H2P == 1:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2,
                                            SCREEN_HEIGHT // 2,
                                            SCREEN_WIDTH,
                                            SCREEN_HEIGHT,
                                            arcade.load_texture("images/ControlG.png"))
            elif self.H2P == 2:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2,
                                              SCREEN_HEIGHT // 2,
                                              SCREEN_WIDTH,
                                              SCREEN_HEIGHT,
                                              arcade.load_texture("images/H2P1.png"))
            elif self.H2P == 3:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2,
                                              SCREEN_HEIGHT // 2,
                                              SCREEN_WIDTH,
                                              SCREEN_HEIGHT,
                                              arcade.load_texture("images/H2P2.png"))
            elif self.H2P == 4:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2,
                                              SCREEN_HEIGHT // 2,
                                              SCREEN_WIDTH,
                                              SCREEN_HEIGHT,
                                              arcade.load_texture("images/H2P3.png"))
            elif self.H2P == 5:
                self.H2P = 1
                self.GAME_MODE = 2

        elif self.GAME_MODE == 2:
            arcade.set_background_color(arcade.color.BLACK_OLIVE)
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
                                        if self.world.stage_objects.stage_count == 8
                                        else self.color_map_not_in_stage)

            arcade.draw_rectangle_filled(50,
                                        SCREEN_HEIGHT - 50,
                                        15,
                                        15,
                                        self.color_map_in_stage
                                        if self.world.stage_objects.stage_count == 9
                                        else self.color_map_not_in_stage)

            arcade.draw_rectangle_filled(70,
                                        SCREEN_HEIGHT - 50,
                                        15,
                                        15,
                                        self.color_map_in_stage
                                        if self.world.stage_objects.stage_count == 4
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
                                        if self.world.stage_objects.stage_count == 6
                                        else self.color_map_not_in_stage)

            arcade.draw_rectangle_filled(70,
                                        SCREEN_HEIGHT - 70,
                                        15,
                                        15,
                                        self.color_map_in_stage
                                        if self.world.stage_objects.stage_count == 5
                                        else self.color_map_not_in_stage)


            arcade.draw_text(self.world.stage_objects.stage_name,
                            15,
                            SCREEN_HEIGHT-105,
                            self.color_map_in_stage,
                            15,
                            bold=True)


            #star collects
            if self.world.stage_objects.stage_count != 0:
                arcade.draw_rectangle_filled(SCREEN_WIDTH-90,
                                            SCREEN_HEIGHT-30,
                                            20,
                                            20,
                                            arcade.color.GOLDEN_POPPY
                                            if len(self.world.star_list) <= 2 \
                                               and self.world.character.keep_star == True
                                            else arcade.color.EERIE_BLACK,
                                            tilt_angle = 45)

                arcade.draw_rectangle_filled(SCREEN_WIDTH - 60,
                                            SCREEN_HEIGHT - 30,
                                            20,
                                            20,
                                            arcade.color.YELLOW_ORANGE
                                            if len(self.world.star_list) <= 1 \
                                               and self.world.character.keep_star == True
                                            else arcade.color.EERIE_BLACK,
                                            tilt_angle=45)

                arcade.draw_rectangle_filled(SCREEN_WIDTH - 30,
                                            SCREEN_HEIGHT - 30,
                                            20,
                                            20,
                                            arcade.color.ORANGE
                                            if len(self.world.star_list) == 0 \
                                               and self.world.character.keep_star == True
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
                             font_size=50,
                             bold=True)

            arcade.draw_text(self.world.stage_objects.desc_status,
                            SCREEN_WIDTH // 2.8,
                            SCREEN_HEIGHT // 1.35,
                            self.color_status_text,
                            font_size=15,
                            bold=True)

            arcade.draw_text(self.world.stage_objects.tutorial_text,
                            SCREEN_WIDTH // 2,
                            SCREEN_HEIGHT // 2.15,
                            arcade.color.ORANGE_RED,
                            font_size=30,
                            bold=True)



def main():
    window = FieldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
