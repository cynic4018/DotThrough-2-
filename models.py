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


class Character:
    MAX_STAGE = 3

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
                if self.stage_count == 3 \
                        and objects.center_x - hit_x <= 335 <= objects.center_x + hit_x \
                        and objects.center_y - hit_y <= 560  <= objects.center_y + hit_y:
                    return False
                elif self.stage_count == 3 \
                        and objects.center_x - hit_x <= 604 <= objects.center_x + hit_x \
                        and objects.center_y - hit_y <= 560  <= objects.center_y + hit_y:
                    return False
                else:
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
                    self.stage2_objects1 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects1.center_x = 264
                    self.stage2_objects1.center_y = 40

                    self.stage2_objects2 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects2.center_x = 264
                    self.stage2_objects2.center_y = 120

                    self.stage2_objects3 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects3.center_x = 264
                    self.stage2_objects3.center_y = 200

                    self.stage2_objects4 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects4.center_x = 264
                    self.stage2_objects4.center_y = 344

                    self.stage2_objects5 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects5.center_x = 264
                    self.stage2_objects5.center_y = 424

                    self.stage2_objects6 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects6.center_x = 264
                    self.stage2_objects6.center_y = 504

                    self.stage2_objects7 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects7.center_x = 264
                    self.stage2_objects7.center_y = 584

                    self.stage2_objects8 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects8.center_x = 420
                    self.stage2_objects8.center_y = 0

                    self.stage2_objects9 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects9.center_x = 420
                    self.stage2_objects9.center_y = 80

                    self.stage2_objects10 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects10.center_x = 420
                    self.stage2_objects10.center_y = 160

                    self.stage2_objects11 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects11.center_x = 420
                    self.stage2_objects11.center_y = 320

                    self.stage2_objects12 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects12.center_x = 420
                    self.stage2_objects12.center_y = 400

                    self.stage2_objects13 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects13.center_x = 420
                    self.stage2_objects13.center_y = 480

                    self.stage2_objects14 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects14.center_x = 420
                    self.stage2_objects14.center_y = 560

                    self.stage2_objects15 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects15.center_x = 578
                    self.stage2_objects15.center_y = 40

                    self.stage2_objects16 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects16.center_x = 578
                    self.stage2_objects16.center_y = 120

                    self.stage2_objects17 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects17.center_x = 578
                    self.stage2_objects17.center_y = 275

                    self.stage2_objects18 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects18.center_x = 578
                    self.stage2_objects18.center_y = 355

                    self.stage2_objects19 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects19.center_x = 578
                    self.stage2_objects19.center_y = 435

                    self.stage2_objects20 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects20.center_x = 578
                    self.stage2_objects20.center_y = 515

                    self.stage2_objects21 = arcade.Sprite("images/pillar.png")
                    self.stage2_objects21.center_x = 578
                    self.stage2_objects21.center_y = 595

                    self.world.object_list.append(self.stage2_objects1)
                    self.world.object_list.append(self.stage2_objects2)
                    self.world.object_list.append(self.stage2_objects3)
                    self.world.object_list.append(self.stage2_objects4)
                    self.world.object_list.append(self.stage2_objects5)
                    self.world.object_list.append(self.stage2_objects6)
                    self.world.object_list.append(self.stage2_objects7)
                    self.world.object_list.append(self.stage2_objects8)
                    self.world.object_list.append(self.stage2_objects9)
                    self.world.object_list.append(self.stage2_objects10)
                    self.world.object_list.append(self.stage2_objects11)
                    self.world.object_list.append(self.stage2_objects12)
                    self.world.object_list.append(self.stage2_objects13)
                    self.world.object_list.append(self.stage2_objects14)
                    self.world.object_list.append(self.stage2_objects15)
                    self.world.object_list.append(self.stage2_objects16)
                    self.world.object_list.append(self.stage2_objects17)
                    self.world.object_list.append(self.stage2_objects18)
                    self.world.object_list.append(self.stage2_objects19)
                    self.world.object_list.append(self.stage2_objects20)
                    self.world.object_list.append(self.stage2_objects21)


                # stage3 objects
                if self.stage_count == 3:
                    self.stage3_objects1 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects1.center_x = 265
                    self.stage3_objects1.center_y = 40

                    self.stage3_objects2 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects2.center_x = 265
                    self.stage3_objects2.center_y = 120

                    self.stage3_objects3 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects3.center_x = 305
                    self.stage3_objects3.center_y = 160

                    self.stage3_objects4 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects4.center_x = 344
                    self.stage3_objects4.center_y = 200

                    self.stage3_objects5 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects5.center_x = 255
                    self.stage3_objects5.center_y = 300

                    self.stage3_objects6 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects6.center_x = 215
                    self.stage3_objects6.center_y = 380

                    self.stage3_objects7 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects7.center_x = 255
                    self.stage3_objects7.center_y = 380

                    self.stage3_objects8 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects8.center_x = 255
                    self.stage3_objects8.center_y = 460

                    self.stage3_objects9 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects9.center_x = 295
                    self.stage3_objects9.center_y = 510

                    self.stage3_objects10 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects10.center_x = 335
                    self.stage3_objects10.center_y = 560

                    self.stage3_objects11 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects11.center_x = 344
                    self.stage3_objects11.center_y = 344

                    self.stage3_objects12 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects12.center_x = 384
                    self.stage3_objects12.center_y = 393

                    self.stage3_objects13 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects13.center_x = 424
                    self.stage3_objects13.center_y = 433

                    self.stage3_objects14 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects14.center_x = 444
                    self.stage3_objects14.center_y = 513

                    self.stage3_objects15 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects15.center_x = 464
                    self.stage3_objects15.center_y = 433

                    self.stage3_objects16 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects16.center_x = 504
                    self.stage3_objects16.center_y = 393

                    self.stage3_objects17 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects17.center_x = 544
                    self.stage3_objects17.center_y = 353

                    self.stage3_objects18 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects18.center_x = 444
                    self.stage3_objects18.center_y = 260

                    self.stage3_objects19 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects19.center_x = 444
                    self.stage3_objects19.center_y = 180

                    self.stage3_objects20 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects20.center_x = 484
                    self.stage3_objects20.center_y = 140

                    self.stage3_objects21 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects21.center_x = 524
                    self.stage3_objects21.center_y = 100

                    self.stage3_objects22 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects22.center_x = 564
                    self.stage3_objects22.center_y = 60

                    self.stage3_objects23 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects23.center_x = 604
                    self.stage3_objects23.center_y = 20

                    self.stage3_objects24 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects24.center_x = 604
                    self.stage3_objects24.center_y = 560

                    self.stage3_objects25 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects25.center_x = 644
                    self.stage3_objects25.center_y = 520

                    self.stage3_objects26 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects26.center_x = 684
                    self.stage3_objects26.center_y = 480

                    self.stage3_objects27 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects27.center_x = 724
                    self.stage3_objects27.center_y = 440

                    self.stage3_objects28 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects28.center_x = 724
                    self.stage3_objects28.center_y = 360

                    self.stage3_objects29 = arcade.Sprite("images/pillar.png")
                    self.stage3_objects29.center_x = 684
                    self.stage3_objects29.center_y = 320

                    self.world.object_list.append(self.stage3_objects1)
                    self.world.object_list.append(self.stage3_objects2)
                    self.world.object_list.append(self.stage3_objects3)
                    self.world.object_list.append(self.stage3_objects4)
                    self.world.object_list.append(self.stage3_objects5)
                    self.world.object_list.append(self.stage3_objects6)
                    self.world.object_list.append(self.stage3_objects7)
                    self.world.object_list.append(self.stage3_objects8)
                    self.world.object_list.append(self.stage3_objects9)
                    self.world.object_list.append(self.stage3_objects10)
                    self.world.object_list.append(self.stage3_objects11)
                    self.world.object_list.append(self.stage3_objects12)
                    self.world.object_list.append(self.stage3_objects13)
                    self.world.object_list.append(self.stage3_objects14)
                    self.world.object_list.append(self.stage3_objects15)
                    self.world.object_list.append(self.stage3_objects16)
                    self.world.object_list.append(self.stage3_objects17)
                    self.world.object_list.append(self.stage3_objects18)
                    self.world.object_list.append(self.stage3_objects19)
                    self.world.object_list.append(self.stage3_objects20)
                    self.world.object_list.append(self.stage3_objects21)
                    self.world.object_list.append(self.stage3_objects22)
                    self.world.object_list.append(self.stage3_objects23)
                    self.world.object_list.append(self.stage3_objects24)
                    self.world.object_list.append(self.stage3_objects25)
                    self.world.object_list.append(self.stage3_objects26)
                    self.world.object_list.append(self.stage3_objects27)
                    self.world.object_list.append(self.stage3_objects28)
                    self.world.object_list.append(self.stage3_objects29)



        if self.hit == True:
            self.status = "Game Over"
            self.desc_status = "Press -SPACEBAR- for restart"

        elif self.exit_hit == True:
            if self.stage_count < self.MAX_STAGE:
                self.status = "Stage Clear"
                self.desc_status = "Press -ENTER- for go next !!"
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




