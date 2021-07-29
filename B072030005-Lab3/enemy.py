#!/usr/bin/env python
# coding: utf-8

# In[38]:

import time
import pygame
import math
import os
from settings import PATH2

from settings import PATH

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    def __init__(self,mode):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 0.1
        self.max_health = 1
        #self.path = PATH[path_num]
        if mode == 0:
            self.path = PATH
        else:
            self.path = PATH2
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path [self.path_index]
        self.clock = pygame.time.Clock()



    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        #print([self.x, self.y,self.x+self.health,self.y+10])
        #self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        #print([self.x, self.y,self.x+self.health,self.y+10])
        max_health = pygame.draw.rect(win, (0, 255, 0), [self.x, self.y - self.height ,self.max_health*40,10])
        health_bar = pygame.draw.rect(win, (255, 0, 0), [self.x, self.y - self.height ,self.health*40,10])
        # ...(to be done)

    def move(self):


        """
        Enemy move toward path points every frame
        :return: None
        """
        # ...(to be done)
        self.clock.tick(600)
        for i in range(len(self.path)-4):
            

            ax,ay= self.path[self.path_index]
            bx,by= self.path[self.path_index+1]
            distance_A_B = math.sqrt((ax - bx)**2 + (ay - by)**2)
            max_count = int(distance_A_B / self.stride)  # total footsteps that needed from A to B

            if self.move_count < max_count:
                unit_vector_x = (bx - ax) / distance_A_B
                unit_vector_y = (by - ay) / distance_A_B
                delta_x = unit_vector_x * self.stride
                delta_y = unit_vector_y * self.stride

                # update the coordinate and the counter
                self.x += delta_x
                self.y += delta_y
                self.move_count += 1
            else:
                self.move_count = 0
                self.path_index += 1

         
                
class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0
        self.campaign_max_count = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = []  # don't change this line until you do the EX.3 
        self.clock = pygame.time.Clock()

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """

        '''
        for i in self.reserved_members:
            self.clock.tick(120)

            self.expedition.append(i)

            self.reserved_members.pop()


            #if FPS == 120:
               #break
        '''
        self.clock.tick(120)
        if self.reserved_members!=[]:
            self.expedition.append(self.reserved_members.pop())
                
        # Hint: self.expedition.append(self.reserved_members.pop())
        # ...(to be done)

        pass

    def generate(self, num,mode):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        
        """
        #if event.type == pygame.QUIT:
       #        run = False
        for i in range(num):
            self.reserved_members.append(Enemy(mode))

        #=self.append(num)
        

        #self.
        # ...(to be done)
        #pass

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)


# In[ ]:





# In[ ]:




