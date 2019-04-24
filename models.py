import arcade
import sys
from random import randint

DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
MOVEMENT_SPEED = 8

DIR_OFFSETS = {DIR_STILL: (0, 0),
               DIR_UP: (0, 1),
               DIR_RIGHT: (1, 0),
               DIR_DOWN: (0, -1),
               DIR_LEFT: (-1, 0)}


class StageObject:
    MAX_STAGE = 6
    LOCATION1 = [[400, 300]]
    LOCATION2 = [[304, 40], [304, 120], [304, 200], [304, 280], [409, 320], [409, 400],
                 [409, 480], [409, 560]]
    LOCATION3 = [[264, 40], [264, 120], [264, 200], [264, 344], [264, 344], [264, 424],
                 [264, 504], [264, 584], [420, 0], [420, 80], [420, 160], [420, 320],
                 [420, 400], [420, 480], [420, 560], [578, 40], [578, 120], [578, 275],
                 [578, 355], [578, 435], [578, 515], [578, 595]]
    LOCATION4 = [[335, 40], [375, 120], [414, 200], [325, 263], [365, 343], [405, 423],
                 [444, 503], [484, 583]]
    LOCATION5 = [[265, 40], [265, 120], [305, 160], [344, 200], [255, 300], [215, 380],
                 [255, 380], [255, 460], [295, 510], [335, 560], [344, 344], [384, 393],
                 [424, 433], [444, 513], [464, 433], [504, 393], [544, 353], [444, 260],
                 [444, 180], [484, 140], [524, 100], [564, 60], [604, 20], [604, 560],
                 [644, 510], [684, 480], [724, 440], [724, 360], [684, 320]]
    LOCATION6 = [[265, 40], [265, 170], [265, 300], [265, 431], [265, 565], [360, 0],
                 [360, 130], [360, 260], [360, 391], [360, 525], [452, 50], [452, 180],
                 [452, 310], [452, 441], [452, 574], [538, 0], [538, 130], [538, 260],
                 [538, 392], [538, 525]]

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

        self.stage_name = "STAGE 00"
        self.status = ""
        self.desc_status = ""
        self.tutorial_text = "Go 2 ExitGate → "
        self.stage_count = 0
        self.next_stage_status = False


    def make_objects(self, LOCATION):
        for i in LOCATION:
            self.stage = arcade.Sprite("images/pillar.png")
            self.stage.center_x = i[0]
            self.stage.center_y = i[1]

            self.world.object_list.append(self.stage)

    def update(self, delta):
        if self.stage_count == 1:
            self.tutorial_text = ""
        if self.world.character.restart == True:
            self.world.character.x = 30
            self.world.character.y = self.world.height // 2
            self.status = ""
            self.desc_status = ""
            self.world.character.hit = False
            self.world.character.restart = False
        elif self.next_stage_status == True:
            if self.stage_count < self.MAX_STAGE:
                self.world.character.x = 30
                self.world.character.y = self.world.height // 2
                self.status = ""
                self.desc_status = ""
                self.stage_count += 1
                self.stage_name = "STAGE 0" + str(self.stage_count)
                self.world.character.exit_hit = False
                self.next_stage_status = False

                # stage1 objects
                if self.stage_count == 1:
                    self.make_objects(self.LOCATION1)

                # stage2 objects
                if self.stage_count == 2:
                    self.make_objects(self.LOCATION2)

                # stage3 objects
                if self.stage_count == 3:
                    self.make_objects(self.LOCATION3)

                # stage4 objects
                if self.stage_count == 4:
                    self.make_objects(self.LOCATION4)

                # stage5 objects
                if self.stage_count == 5:
                    self.make_objects(self.LOCATION5)

                # stage6 objects
                if self.stage_count == 6:
                    self.make_objects(self.LOCATION6)



class ExitObjects:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y


class Character:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL

        self.hit = False
        self.exit_hit = False
        self.restart = False
        self.animation = 1


    def move(self, direction):
        if self.x >= self.world.width - 20:
            self.x = self.world.width - 20
        if self.y >= self.world.height - 20:
            self.y = self.world.height - 20
        if self.x <= 20:
            self.x = 20
        if self.y <= 20:
            self.y = 20

        if self.hit == True:
            self.x += 0
            self.y += 0
        elif self.exit_hit == True:
            self.x += 0
            self.y += 0

        else:
            self.x += DIR_OFFSETS[direction][0] * MOVEMENT_SPEED
            self.y += DIR_OFFSETS[direction][1] * MOVEMENT_SPEED


    def is_hit(self, objects, hit_x, hit_y):
        if objects.center_x - hit_x <= self.x <= objects.center_x + hit_x:
            if objects.center_y - hit_y <= self.y  <= objects.center_y + hit_y:
                if self.world.stage_objects.stage_count == 5 \
                        and objects.center_x - hit_x <= 335 <= objects.center_x + hit_x \
                        and objects.center_y - hit_y <= 600  <= objects.center_y + hit_y:
                    return False
                elif self.world.stage_objects.stage_count == 5 \
                        and objects.center_x - hit_x <= 604 <= objects.center_x + hit_x \
                        and objects.center_y - hit_y <= 600 <= objects.center_y + hit_y:
                    return False
                else:
                    return True

    def is_exithit(self, objects, hit_x, hit_y):
        if objects.x - hit_x <= self.x <= objects.x + hit_x:
            if objects.y - hit_y <= self.y  <= objects.y + hit_y:
                    return True

    def update(self, delta):
        self.move(self.direction)

        if self.hit == True:
            self.world.stage_objects.status = "Game Over"
            self.world.stage_objects.desc_status = "Press -SPACEBAR- for restart"

        elif self.exit_hit == True:
            if self.world.stage_objects.stage_count < self.world.stage_objects.MAX_STAGE:
                self.world.stage_objects.status = "Stage Clear"
                self.world.stage_objects.desc_status = "Press -ENTER- for go next !!"
            else:
                self.world.stage_objects.status = "Game Clear"
                self.world.stage_objects.desc_status = "Cogratulation!! you clear game"


class World:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.character = Character(self, 30, height // 2)

        self.object_list = arcade.SpriteList()

        self.stage_objects = StageObject(self, width // 2 , height // 2)

        self.exit_gate = ExitObjects(self, width-10, height // 2)






    def update(self, delta):
        self.stage_objects.update(delta)
        self.character.update(delta)


        for i in self.object_list:
            if self.character.is_hit(i, 40, 60):
                self.character.hit = True

        if self.character.is_exithit(self.exit_gate, 30, 30):
            self.character.exit_hit = True
            for i in self.object_list:
                self.object_list.remove(i)


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.character.hit == True:
            self.character.restart = True

        if key == arcade.key.ENTER and self.character.exit_hit == True:
            self.stage_objects.next_stage_status = True

        if self.character.animation == 4:
            self.character.animation = 1
        if key == arcade.key.UP:
            self.character.direction = DIR_UP
            self.character.animation += 1
        if key == arcade.key.DOWN:
            self.character.direction = DIR_DOWN
            self.character.animation += 1
        if key == arcade.key.LEFT:
            self.character.direction = DIR_LEFT
            self.character.animation += 1
        if key == arcade.key.RIGHT:
            self.character.direction = DIR_RIGHT
            self.character.animation += 1


    def on_key_release(self, key, key_modifiers):
        self.character.direction = DIR_STILL


