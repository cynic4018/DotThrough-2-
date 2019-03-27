import arcade.key
from random import randint

DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_OFFSETS = {DIR_STILL: (0, 0),
               DIR_UP: (0, 1),
               DIR_RIGHT: (1, 0),
               DIR_DOWN: (0, -1),
               DIR_LEFT: (-1, 0)}


class Character:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL
        self.hit = False

    def move(self, direction):
        if self.x >= self.world.width - 30:
            self.x = self.world.width - 30
        if self.y >= self.world.height - 30:
            self.y = self.world.height - 30
        if self.x <= 30:
            self.x = 30
        if self.y <= 30:
            self.y = 30

        self.x += DIR_OFFSETS[direction][0] * 10
        self.y += DIR_OFFSETS[direction][1] * 10

    def is_hit(self, stage_one_objects):
        if self.x == stage_one_objects.x - 40 or self.x == stage_one_objects.x + 40 or self.x == stage_one_objects.x:
            if stage_one_objects.y - 40 <= self.y  <= stage_one_objects.y + 40:
                return True


    def update(self, delta):
        if self.hit == True:
            self.x = 0
            self.y = 0
            output = "Game Over"
            arcade.draw_text(output,
                             500,
                             500,
                             arcade.color.WHITE_SMOKE, 50)
            self.hit = False

        self.move(self.direction)



class StageOneObjects:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y


class World:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.character = Character(self, 30, height // 2)

        self.stage_one_objects = StageOneObjects(self,  width // 2, height // 2)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.character.direction = DIR_UP
        if key == arcade.key.DOWN:
            self.character.direction = DIR_DOWN
        if key == arcade.key.LEFT:
            self.character.direction = DIR_LEFT
        if key == arcade.key.RIGHT:
            self.character.direction = DIR_RIGHT

    def update(self, delta):
        self.character.update(delta)

        if self.character.is_hit(self.stage_one_objects):
            self.character.hit = True
