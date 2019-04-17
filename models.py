import arcade
import sys
from random import randint



DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
MOVEMENT_SPEED = 10

DIR_OFFSETS = {DIR_STILL: (0, 0),
               DIR_UP: (0, 1),
               DIR_RIGHT: (1, 0),
               DIR_DOWN: (0, -1),
               DIR_LEFT: (-1, 0)}


class Character:
    MAX_STAGE = 2

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL
        self.stage_name = "STAGE 01"
        self.status = ""
        self.desc_status = ""
        self.stage_count = 1
        self.next_stage_status = False
        self.restart = False
        self.hit = False
        self.exit_hit = False

    def move(self, direction):
        if self.x >= self.world.width - 30:
            self.x = self.world.width - 30
        if self.y >= self.world.height - 30:
            self.y = self.world.height - 30
        if self.x <= 30:
            self.x = 30
        if self.y <= 30:
            self.y = 30

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
                return True

    def is_exithit(self, objects, hit_x, hit_y):
        if objects.x - hit_x <= self.x <= objects.x + hit_x:
            if objects.y - hit_y <= self.y  <= objects.y + hit_y:
                return True

    def update(self, delta):
        self.move(self.direction)

        if self.restart == True:
            self.x = 30
            self.y = self.world.height // 2
            self.status = ""
            self.desc_status = ""
            self.hit = False
            self.restart = False
        elif self.next_stage_status == True:
            if self.stage_count < self.MAX_STAGE:
                self.x = 30
                self.y = self.world.height // 2
                self.status = ""
                self.desc_status = ""
                self.stage_count += 1
                self.stage_name = "STAGE 0" + str(self.stage_count)
                self.exit_hit = False
                self.next_stage_status = False

                # stage2 objects
                if self.stage_count == 2:
                    self.stage_objects1 = arcade.Sprite("images/pillar.png")
                    self.stage_objects1.center_x = self.world.width // 1.5
                    self.stage_objects1.center_y = self.world.height // 1.5

                    self.stage_objects2 = arcade.Sprite("images/pillar.png")
                    self.stage_objects2.center_x = self.world.width // 3
                    self.stage_objects2.center_y = self.world.height // 3

                    self.world.object_list.append(self.stage_objects1)
                    self.world.object_list.append(self.stage_objects2)


        if self.hit == True:
            self.status = "Game Over"
            self.desc_status = "Press -SPACEBAR- for restart!!"

        elif self.exit_hit == True:
            if self.stage_count < self.MAX_STAGE:
                self.status = "Stage Clear"
                self.desc_status = "Press -ENTER- for restart!!"
            else:
                self.status = "Game Clear"
                self.desc_status = "Cogratulation!! you clear game"


class ExitObjects:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y



class World:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.character = Character(self, 30, height // 2)

        self.object_list = arcade.SpriteList()

        #stage1 objects
        self.stage_objects = arcade.Sprite("images/pillar.png")
        self.stage_objects.center_x = self.width // 2
        self.stage_objects.center_y = self.height // 2
        self.object_list.append(self.stage_objects)

        self.exit_gate = ExitObjects(self, width-10, height // 2)

    def update(self, delta):
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
            self.character.next_stage_status = True

        if key == arcade.key.UP:
            self.character.direction = DIR_UP
        if key == arcade.key.DOWN:
            self.character.direction = DIR_DOWN
        if key == arcade.key.LEFT:
            self.character.direction = DIR_LEFT
        if key == arcade.key.RIGHT:
            self.character.direction = DIR_RIGHT


    def on_key_release(self, key, key_modifiers):
        self.character.direction = DIR_STILL




