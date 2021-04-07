from tkinter import *
from panda3d.core import loadPrcFileData
from panda3d.core import NodePath
from panda3d.core import PointLight
from panda3d.core import DirectionalLight
from math import pi, sin, cos
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import sys
import os
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from direct.showbase import Loader
from direct.gui.DirectDialog import DirectDialog,OkDialog

from panda3d.core import TextNode
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

import random
from panda3d.core import *

import time
import random
import sys

# just of effects. add a delay of 1 second before performing any action
SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_FACE = 6

# snake takes you down from 'key' to 'value'
snakes_x = [5.0,25.0,65.0,75.0,3.0,23.0,63.0,73.0]
snakes_y = [74.0,94.0,76.0,96.0]

ladders_x=[65.0,75.0,5.0,45.0,55.0,63.0,73.0,3.0,43.0,53.0]
ladders_y=[4.0,14.0,24.0,34.0,54.0,16.0,6.0,26.0,36.0,56.0]

y1=[14.0,34.0,54.0,74.0,94.0,16.0,36.0,56.0,76.0,96.0]

questions = {
    "up": [{"zk":0,"makeup":0,"mello":0,"op":0}],
    "down": False,
    "left": False,
    "right": False,
    "rotate": False,
}

keyMap = {
    "up": False,
    "down": False,
    "left": False,
    "right": False,
    "rotate": False,
}

def dice_roll(self,number):
            i = number
            if i==1:
                self.dicemain.setHpr(0, -180, 0)
                self.dicemain.setPos(50, -9.5,40 )
            if i==2:
                self.dicemain.setHpr(0, 0, 90)
                self.dicemain.setPos(45, -7.5,40 )
            if i==3:
                self.dicemain.setHpr(0, 0, -90)
                self.dicemain.setPos(55, -7.5,40 )
            if i==4:
                self.dicemain.setHpr(90, 0, 0)
                self.dicemain.setPos(50, -7.5,40 )
            if i==5:
                self.dicemain.setHpr(0, -90, 0)
                self.dicemain.setPos(50, -13.5,40 )
            if i==6:
                self.dicemain.setHpr(0, 90, 0)
                self.dicemain.setPos(50, -3.5,40 )

def updateKeyMap(key, state):
    time.sleep(1)
    keyMap[key] = state

def get_dice_value():
                dice_value = random.randint(1, DICE_FACE)
                print("Its a " + str(dice_value))
                # time.sleep(1)
                return dice_value

def ladder1(self,a,b):
    if a==65.0 and b==4.0:
        return 1
    if a==75.0 and b==14.0:
        return 2
    if a==5.0 and b==24.0:
        return 3
    if a==45.0 and b==34.0:
        return 4
    if a==55.0 and b==54.0:
        return 5
def ladder2(a,b):
    if a==63.0 and b==6.0:
        return 1
    if a==73.0 and b==16.0:
        return 2
    if a==3.0 and b==26.0:
        return 3
    if a==43.0 and b==36.0:
        return 4
    if a==53.0 and b==56.0:
        return 5
def ladder3(a,b):
    if a==65.0 and b==6.0:
        return 1
    if a==75.0 and b==16.0:
        return 2
    if a==5.0 and b==26.0:
        return 3
    if a==45.0 and b==36.0:
        return 4
    if a==55.0 and b==56.0:
        return 5
def ladder4(a,b):
    if a==63.0 and b==4.0:
        return 1
    if a==73.0 and b==14.0:
        return 2
    if a==3.0 and b==24.0:
        return 3
    if a==43.0 and b==34.0:
        return 4
    if a==53.0 and b==54.0:
        return 5

def snakes1(a,b):
    if a==5.0 and b==74.0:
        return 1
    if a==25.0 and b==94.0:
        return 2
    if a==65.0 and b==94.0:
        return 3
    if a==75.0 and b==74.0:
        return 4
def snakes2(a,b):
    if a==3.0 and b==76.0:
        return 1
    if a==23.0 and b==96.0:
        return 2
    if a==63.0 and b==96.0:
        return 3
    if a==73.0 and b==76.0:
        return 4
def snakes3(a,b):
    if a==5.0 and b==76.0:
        return 1
    if a==25.0 and b==96.0:
        return 2
    if a==65.0 and b==96.0:
        return 3
    if a==75.0 and b==76.0:
        return 4
def snakes4(a,b):
    if a==3.0 and b==74.0:
        return 1
    if a==23.0 and b==94.0:
        return 2
    if a==63.0 and b==74.0:
        return 3
    if a==73.0 and b==74.0:
        return 4

class MyGame(ShowBase):
    def update(self, task):
        dt= random.randint(1, 6)
        pos1 = self.goti1.getPos()
        pos2 = self.goti2.getPos()
        pos3 = self.goti3.getPos()
        pos4 = self.goti4.getPos()

        def question_ask_snakes(self,w1,w2,h):
            self.w3=w1
            self.q3=w2
            self.h=h

            def check1():
                self.set_background_color(0.5, 0,0.3,0)
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                self.cam.setPos(50 , 40, 280)
                self.textNode_1.setPos(24,104,20.03)

                if self.h==1:
                    pos2.x = self.w3
                    pos2.y = self.q3
                    self.goti2.setPos(pos2)
                if self.h==2:
                    pos1.x = self.w3
                    pos1.y = self.q3
                    self.goti1.setPos(pos1)
                if self.h==3:
                    pos3.x = self.w3
                    pos3.y = self.q3
                    self.goti3.setPos(pos3)
                if self.h==4:
                    pos4.x = self.w3
                    pos4.y = self.q3
                    self.goti4.setPos(pos4)
                
            def check2():
                self.set_background_color(0.5, 0,0.3,0)
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                self.cam.setPos(50 , 40, 280)
                self.textNode_2.setPos(24,104,20.03)
                
            m= random.randint(1, 10)
            if m==1:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-230 , 40, 280)
                b1 = DirectButton(text=("  H Parameters  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  Z Parameters  "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  ABCD Parameters  "),
                 scale=.08,command=check1)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=(" Y Parameters  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==2:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-480 , 40, 280)
                b1 = DirectButton(text=("  V1 and V2  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  I1 and I2 "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  V1 and I1  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  V1 and I2  "),
                 scale=.08,command=check1)
                b4.setPos(0.3,0.5,-0.1)
            if m==3:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-720 , 40, 280)
                b1 = DirectButton(text=("  3  "),
                 scale=.08,command=check1)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  -2 "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  -3  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  2  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==4:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-960 , 40, 280)
                b1 = DirectButton(text=("  z11 = z22  "),
                 scale=.08,command=check1)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  z11 = z12  "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  z12 = z22  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  z12 = z21  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==5:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-1200 , 40, 280)
                b1 = DirectButton(text=("  Open circuit Impedance Parameter  "),
                 scale=.05,command=check2)
                b1.setPos(-0.6,0.5,0.2)
                b2 = DirectButton(text=("  Short circuit Admittance Parameter  "),
                 scale=.05,command=check2)
                b2.setPos(0.4,0.5,0.2)
                b3 = DirectButton(text=("  Open circuit Admittance Parameter  "),
                 scale=.05,command=check2)
                b3.setPos(-0.6,0.5,-0.1)
                b4 = DirectButton(text=("  Open circuit Impedance Parameter  "),
                 scale=.05,command=check1)
                b4.setPos(0.4,0.5,-0.1)
            if m==6:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-1400 , 40, 280)
                b1 = DirectButton(text=("  V1 and I2  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  I1 and I2  "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  V1 and V2  "),
                 scale=.08,command=check1)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=(" V2 and I1  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==7:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-1600 , 40, 280)
                b1 = DirectButton(text=("  V2/I1 (I2=0)  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  I2/V1 (V2=0) "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  V1/I2 (I1=0)  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  I1/V2 (V1=0)  "),
                 scale=.08,command=check1)
                b4.setPos(0.3,0.5,-0.1)
            if m==8:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-1800 , 40, 280)
                b1 = DirectButton(text=("  H  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  Z "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  ABCD  "),
                 scale=.08,command=check1)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  Y  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==9:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-2000 , 40, 280)
                b1 = DirectButton(text=("  Voltage  "),
                 scale=.08,command=check1)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  Both Current & Voltage  "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  Current  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  None of these  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==10:
                self.set_background_color(0.126, 0.526,0,0)
                self.cam.setPos(-2200 , 40, 280)
                b1 = DirectButton(text=("  Short Circuited  "),
                 scale=.05,command=check2)
                b1.setPos(-0.6,0.5,0.2)
                b2 = DirectButton(text=("  Open Circuited  "),
                 scale=.05,command=check1)
                b2.setPos(0.4,0.5,0.2)
                b3 = DirectButton(text=("  Applied Voltage  "),
                 scale=.05,command=check2)
                b3.setPos(-0.6,0.5,-0.1)
                b4 = DirectButton(text=("  None of these  "),
                 scale=.05,command=check2)
                b4.setPos(0.4,0.5,-0.1)

        def question_ask(self,x2,y2,gh):
            self.x3=x2
            self.y3=y2
            self.gh=gh

            def check1():
                self.set_background_color(0.5, 0,0.3,0)
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                self.cam.setPos(50 , 40, 280)
                self.textNode_1.setPos(24,104,20.03)
                mu=1
                print(mu)
            def check2():
                self.set_background_color(0.5, 0,0.3,0)
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                self.cam.setPos(50 , 40, 280)
                self.textNode_2.setPos(24,104,20.03)
                
                if self.gh==1:
                    pos2.x = self.x3
                    pos2.y = self.y3
                    self.goti2.setPos(pos2)
                if self.gh==2:
                    pos1.x = self.x3
                    pos1.y = self.y3
                    self.goti1.setPos(pos1)
                if self.gh==3:
                    pos3.x = self.x3
                    pos3.y = self.y3
                    self.goti3.setPos(pos3)
                if self.gh==4:
                    pos4.x = self.x3
                    pos4.y = self.y3
                    self.goti4.setPos(pos4)
                mu=0
                print(mu)
            m= random.randint(1, 10)
            if m==1:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(250 , 40, 280)
                b1 = DirectButton(text=("  H Parameters  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  Z Parameters  "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  ABCD Parameters  "),
                 scale=.08,command=check1)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=(" Y Parameters  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==2:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(500 , 40, 280)
                b1 = DirectButton(text=("  V1 and V2  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  I1 and I2 "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  V1 and I1  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  V1 and I2  "),
                 scale=.08,command=check1)
                b4.setPos(0.3,0.5,-0.1)
            if m==3:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(750 , 40, 280)
                b1 = DirectButton(text=("  3  "),
                 scale=.08,command=check1)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  -2 "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  -3  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  2  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==4:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(960 , 40, 280)
                b1 = DirectButton(text=("  z11 = z22  "),
                 scale=.08,command=check1)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  z11 = z12  "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  z12 = z22  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  z12 = z21  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==5:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(1220 , 40, 280)
                b1 = DirectButton(text=("  Open circuit Impedance Parameter  "),
                 scale=.05,command=check2)
                b1.setPos(-0.6,0.5,0.2)
                b2 = DirectButton(text=("  Short circuit Admittance Parameter  "),
                 scale=.05,command=check2)
                b2.setPos(0.4,0.5,0.2)
                b3 = DirectButton(text=("  Open circuit Admittance Parameter  "),
                 scale=.05,command=check2)
                b3.setPos(-0.6,0.5,-0.1)
                b4 = DirectButton(text=("  Open circuit Impedance Parameter  "),
                 scale=.05,command=check1)
                b4.setPos(0.4,0.5,-0.1)
            if m==6:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(1400 , 40, 280)
                b1 = DirectButton(text=("  V1 and I2  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  I1 and I2  "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  V1 and V2  "),
                 scale=.08,command=check1)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=(" V2 and I1  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==7:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(1600 , 40, 280)
                b1 = DirectButton(text=("  V2/I1 (I2=0)  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  I2/V1 (V2=0) "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  V1/I2 (I1=0)  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  I1/V2 (V1=0)  "),
                 scale=.08,command=check1)
                b4.setPos(0.3,0.5,-0.1)
            if m==8:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(1800 , 40, 280)
                b1 = DirectButton(text=("  H  "),
                 scale=.08,command=check2)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  Z "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  ABCD  "),
                 scale=.08,command=check1)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  Y  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==9:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(2000 , 40, 280)
                b1 = DirectButton(text=("  Voltage  "),
                 scale=.08,command=check1)
                b1.setPos(-0.5,0.5,0.2)
                b2 = DirectButton(text=("  Both Current & Voltage  "),
                 scale=.08,command=check2)
                b2.setPos(0.3,0.5,0.2)
                b3 = DirectButton(text=("  Current  "),
                 scale=.08,command=check2)
                b3.setPos(-0.5,0.5,-0.1)
                b4 = DirectButton(text=("  None of these  "),
                 scale=.08,command=check2)
                b4.setPos(0.3,0.5,-0.1)
            if m==10:
                self.set_background_color(0.326, 0.526,0.26,0)
                self.cam.setPos(2200 , 40, 280)
                b1 = DirectButton(text=("  Short Circuited  "),
                 scale=.05,command=check2)
                b1.setPos(-0.6,0.5,0.2)
                b2 = DirectButton(text=("  Open Circuited  "),
                 scale=.05,command=check1)
                b2.setPos(0.4,0.5,0.2)
                b3 = DirectButton(text=("  Applied Voltage  "),
                 scale=.05,command=check2)
                b3.setPos(-0.6,0.5,-0.1)
                b4 = DirectButton(text=("  None of these  "),
                 scale=.05,command=check2)
                b4.setPos(0.4,0.5,-0.1)
            

           

        if keyMap["left"]:
            self.textNode_2.setPos(24000,104,20.03)
            self.textNode_1.setPos(24000,104,20.03)
            dice_roll(self,dt)
            print(dt)
            for i in range (0,dt):
                if pos2.y in y1:
                        pos2.x -=  10
                else :
                        pos2.x +=  10
                x2=pos2.x
                while x2==95.0:
                    pos2.y +=10
                    x2 +=1
                x2=pos2.x
                while x2==5.0:
                    x2=pos2.x
                    def won():
                        sys.exit()
                    if pos2.y in y1:
                        if pos2.y==94.0:
                            self.set_background_color(0.126, 0,0,0.5)
                            self.cam.setPos(10050 , 40, 280)
                            dialog = OkDialog(dialogName="YesNoCancelDialog", text="CONGRATULATIONS....\nPlayer 1 won the game ",command=won)
                        pos2.y +=  10
                    
                    x2 +=1
            print(pos2.x)
            if pos2.x in ladders_x and pos2.y in ladders_y:
                j1=ladder1(self,pos2.x,pos2.y)
                x2=pos2.x
                y2=pos2.y
                if j1==1:
                    pos2.x = 55.0
                    pos2.y = 34.0
                    f=question_ask(self,x2,y2,1)
                if j1==2:
                    pos2.x = 95.0
                    pos2.y =94.0
                    f=question_ask(self,x2,y2,1)
                if j1==3:
                    pos2.x = 15.0
                    pos2.y = 84.0
                    f=question_ask(self,x2,y2,1)
                if j1==4:
                    pos2.x = 35.0
                    pos2.y = 84.0
                    f=question_ask(self,x2,y2,1)
                if j1==5:
                    pos2.x = 65.0
                    pos2.y = 84.0
                    f=question_ask(self,x2,y2,1)
            if pos2.x in snakes_x and pos2.y in snakes_y:
                print(pos2.x,pos2.y)
                j1=snakes1(pos2.x,pos2.y)
                w1=pos2.x
                w2=pos2.y
                if j1==1:
                    pos2.x = 35.0
                    pos2.y = 14.0
                    f=question_ask_snakes(self,w1,w2,1)
                if j1==2:
                    pos2.x = 55.0
                    pos2.y = 14.0
                    f=question_ask_snakes(self,w1,w2,1)
                if j1==3:
                    pos2.x = 35.0
                    pos2.y = 64.0
                    f=question_ask_snakes(self,w1,w2,1)
                if j1==4:
                    pos2.x = 25.0
                    pos2.y = 24.0
                    f=question_ask_snakes(self,w1,w2,1)
                # pos2.x = ladders_x.get(pos2.x)
                # pos2.y = ladders_y.get(pos2.y)


        if keyMap["right"]:
            self.textNode_2.setPos(24000,104,20.03)
            self.textNode_1.setPos(24000,104,20.03)
            dice_roll(self,dt)
            for i in range (0,dt):
                if pos1.y in y1:
                    pos1.x -=  10
                else :
                    pos1.x +=  10
                x2=pos1.x
                while x2==95.0:
                    pos1.y +=10
                    x2 +=1
                x2=pos1.x
                while x2==5.0:
                    x2=pos1.x
                    def won(arg):
                        sys.exit()
                    if pos1.y in y1:
                        if pos1.y==96.0:
                            self.set_background_color(0.126, 0,0,0.5)
                            self.cam.setPos(10050 , 40, 280)
                            dialog = OkDialog(dialogName="YesNoCancelDialog", text="CONGRATULATIONS....\nPlayer 2  won the game ",command=won)
                        pos1.y +=  10
                    x2 +=1
            if pos1.x in ladders_x and pos1.y in ladders_y:
                x2=pos1.x
                y2=pos1.y
                j1=ladder3(pos1.x,pos1.y)
                if j1==1:
                    pos1.x = 55.0
                    pos1.y = 36.0
                    f=question_ask(self,x2,y2,2)
                if j1==2:
                    pos1.x = 95.0
                    pos1.y =96.0
                    f=question_ask(self,x2,y2,2)
                if j1==3:
                    pos1.x = 15.0
                    pos1.y = 86.0
                    f=question_ask(self,x2,y2,2)
                if j1==4:
                    pos1.x = 35.0
                    pos1.y = 86.0
                    f=question_ask(self,x2,y2,2)
                if j1==5:
                    pos1.x = 65.0
                    pos1.y = 86.0
                    f=question_ask(self,x2,y2,2)
            if pos1.x in snakes_x and pos1.y in snakes_y:
                print(pos1.x,pos1.y)
                j1=snakes3(pos1.x,pos1.y)
                w1=pos1.x
                w2=pos1.y
                if j1==1:
                    pos1.x = 35.0
                    pos1.y = 16.0
                    f=question_ask_snakes(self,w1,w2,2)
                if j1==2:
                    pos1.x = 55.0
                    pos1.y = 16.0
                    f=question_ask_snakes(self,w1,w2,2)
                if j1==3:
                    pos1.x = 35.0
                    pos1.y = 66.0
                    f=question_ask_snakes(self,w1,w2,2)
                if j1==4:
                    pos1.x = 25.0
                    pos1.y = 26.0
                    f=question_ask_snakes(self,w1,w2,2)

        if keyMap["up"]:
            self.textNode_2.setPos(24000,104,20.03)
            self.textNode_1.setPos(24000,104,20.03)
            dice_roll(self,dt)
            for i in range (0,dt):
                if pos3.y in y1:
                    pos3.x -=  10
                else :
                    pos3.x +=  10
                x2=pos3.x
                while x2==93.0:
                    pos3.y +=10
                    print("y :",pos3.y)
                    x2 +=1
                x2=pos3.x
                while x2==3.0:
                    x2=pos3.x
                    def won():
                        sys.exit()
                    if pos3.y in y1:
                        if pos3.y==94.0:
                            self.set_background_color(0.126, 0,0,0.5)
                            self.cam.setPos(10050 , 40, 280)
                            dialog = OkDialog(dialogName="YesNoCancelDialog", text="CONGRATULATIONS....\nPlayer 3  won the game ",command=won)
                        pos3.y +=  10
                    x2 +=1
            if pos3.x in ladders_x and pos3.y in ladders_y:
                j1=ladder4(pos3.x,pos3.y)
                x2=pos3.x
                y2=pos3.y
                if j1==1:
                    pos3.x = 53.0
                    pos3.y = 34.0
                    f=question_ask(self,x2,y2,3)
                if j1==2:
                    pos3.x = 93.0
                    pos3.y =94.0
                    f=question_ask(self,x2,y2,3)
                if j1==3:
                    pos3.x = 13.0
                    pos3.y = 84.0
                    f=question_ask(self,x2,y2,3)
                if j1==4:
                    pos3.x = 33.0
                    pos3.y = 84.0
                    f=question_ask(self,x2,y2,3)
                if j1==5:
                    pos3.x = 63.0
                    pos3.y = 84.0
                    f=question_ask(self,x2,y2,3)
            print(pos3.x,pos3.y)
            if pos3.x in snakes_x and pos3.y in snakes_y:
                j1=snakes4(pos3.x,pos3.y)
                w1=pos3.x
                w2=pos3.y
                if j1==1:
                    pos3.x = 33.0
                    pos3.y = 14.0
                    f=question_ask_snakes(self,w1,w2,3)
                if j1==2:
                    pos3.x = 53.0
                    pos3.y = 14.0
                    f=question_ask_snakes(self,w1,w2,3)
                if j1==3:
                    pos3.x = 33.0
                    pos3.y = 64.0
                    f=question_ask_snakes(self,w1,w2,3)
                if j1==4:
                    pos3.x = 23.0
                    pos3.y = 24.0
                    f=question_ask_snakes(self,w1,w2,3)
        if keyMap["down"]:
            self.textNode_2.setPos(24000,104,20.03)
            self.textNode_1.setPos(24000,104,20.03)
            dice_roll(self,dt)
            print(dt)
            for i in range (0,dt):
                if pos4.y in y1:
                    pos4.x -=  10
                else :
                    pos4.x +=  10
                x2=pos4.x
                while x2==93.0:
                    pos4.y +=10
                    x2 +=1
                    
                x2=pos4.x
                while x2==3.0:
                    def won():
                        sys.exit()
                    if pos4.y in y1:
                        if pos4.y==96.0:
                            self.set_background_color(0.126, 0,0,0.5)
                            self.cam.setPos(10050 , 40, 280)
                            dialog = OkDialog(dialogName="YesNoCancelDialog", text="CONGRATULATIONS....\nPlayer 4  won the game ",command=won)
                        pos4.y +=  10
                    x2 +=1
            if pos4.x in ladders_x and pos4.y in ladders_y:
                print(pos4.x,pos4.y)
                j1=ladder2(pos4.x,pos4.y)
                x2=pos4.x
                y2=pos4.y
                if j1==1:
                    pos4.x = 53.0
                    pos4.y = 36.0
                    f=question_ask(self,x2,y2,4)
                if j1==2:
                    pos4.x = 93.0
                    pos4.y =96.0
                    f=question_ask(self,x2,y2,4)
                if j1==3:
                    pos4.x = 13.0
                    pos4.y = 86.0
                    f=question_ask(self,x2,y2,4)
                if j1==4:
                    pos4.x = 33.0
                    pos4.y = 86.0
                    f=question_ask(self,x2,y2,4)
                if j1==5:
                    pos4.x = 63.0
                    pos4.y = 86.0
                    f=question_ask(self,x2,y2,4)
            print(pos4.x,pos4.y)
            if pos4.x in snakes_x and pos4.y in snakes_y:
                print(pos4.x,pos4.y)
                j1=snakes2(pos4.x,pos4.y)
                w1=pos4.x
                w2=pos4.y
                if j1==1:
                    pos4.x = 33.0
                    pos4.y = 16.0
                    f=question_ask_snakes(self,w1,w2,4)
                if j1==2:
                    pos4.x = 53.0
                    pos4.y =16.0
                    f=question_ask_snakes(self,w1,w2,4)
                if j1==3:
                    pos4.x = 33.0
                    pos4.y = 66.0
                    f=question_ask_snakes(self,w1,w2,4)
                if j1==4:
                    pos4.x = 23.0
                    pos4.y = 26.0
                    f=question_ask_snakes(self,w1,w2,4)

        self.goti1.setPos(pos1)
        self.goti2.setPos(pos2)
        self.goti3.setPos(pos3)
        self.goti4.setPos(pos4)


        return task.cont
    def  __init__(self):
        super().__init__()
        self.set_background_color(0.71, 0.4, 0,0)
        self.cam.setPos(-110 , -5, 280)
        self.cam.setHpr(0 , -90, 0)

        dlight1 = DirectionalLight('dlight1')
        # dlight1.setColor((20,20,0,0))
        self.plnp1 = self.render.attachNewNode(dlight1)
        self.plnp1.setPos(50,45,250)
        self.plnp1.setHpr(0 , -90, 0)
        self.render.setLight(self.plnp1)
        def exit_page():
            sys.exit()
        def welcome_msg():
            b.destroy()
            b1.destroy()
            b2.destroy()
            self.cam.setPos(250 , 40, 270)
            # self.cam.setPos(-100 , 45, 280)
            msg = """
            Welcome to Snakes and Ladders Game Quiz !!!!

Rules:
1. Initally all the players are at starting position i.e. 0. 
   Take it in turns to roll the dice. 
   Move forward the number of spaces shown on the dice.
2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
4. The first player to get to the FINAL position is the winner.
5. Hit enter to roll the dice.

"""
            settings = TextNode('text')
            text.setText(msg)
            textNode = self.render.attachNewNode(text)
            textNode.setScale(3.5)
            textNode.setHpr(0,-90,0)
            textNode.setPos(250,60,20.03)

        def setText():
            self.set_background_color(0.5, 0,0.3,0)
            self.cam.setPos(50 , 40, 280)
            b.destroy()
            b1.destroy()
            b2.destroy()
            i=0
            while i<1:
                self.accept("arrow_left-up", updateKeyMap,["left", False])
                self.accept("arrow_left", updateKeyMap,["left", True])

                self.accept("arrow_right", updateKeyMap,["right", True])
                self.accept("arrow_right-up", updateKeyMap,["right", False])

                self.accept("arrow_up", updateKeyMap,["up", True])
                self.accept("arrow_up-up", updateKeyMap,["up", False])

                self.accept("arrow_down", updateKeyMap,["down", True])
                self.accept("arrow_down-up", updateKeyMap,["down", False])

                self.accept("space-down", updateKeyMap,["rotate", True])
                self.accept("space-up", updateKeyMap,["rotate", False])

                self.speed = 50
                self.angle = 0

                self.taskMgr.add(self.update, "update")

                i=i+1

        b = DirectButton(text=("Settings"),
                 scale=.08, command=welcome_msg)
        b.setPos(0.5,0,0)

        b1 = DirectButton(text=("Start Game"),
                 scale=.08, command=setText)
        b1.setPos(-0.5,0,0)

        b2 = DirectButton(text=("Exit    "),
                 scale=.08, command=exit_page)
        b2.setPos(0.1,0,-0.50)
        
        text = TextNode('text')
        text.setText("Play and Learn !")
        text.setAlign(TextNode.ACenter)
        textNode_3 = self.render.attachNewNode(text)
        textNode_3.setScale(6)
        textNode_3.setHpr(0,-90,0)
        textNode_3.setPos(-110,24,20.03)
        text = TextNode('text')
        text.setText("SNAKES AND LADDERS QUIZ ")
        text.setAlign(TextNode.ACenter)
        textNode_3 = self.render.attachNewNode(text)
        textNode_3.setScale(6)
        textNode_3.setHpr(0,-90,0)
        textNode_3.setPos(-110,34,20.03)
        textNode_3.setColor(100, 0.5, 0.5, 1)
        text = TextNode('text')
        text.setText("WELCOME TO ")
        text.setAlign(TextNode.ACenter)
        textNode_4 = self.render.attachNewNode(text)
        textNode_4.setScale(8)
        textNode_4.setHpr(0,-90,0)
        textNode_4.setPos(-110,44,20.03)

        text = TextNode('text')
        text.setText("SORRY !!!! Wrong Answer ")
        text.setAlign(TextNode.ACenter)
        self.textNode_2 = self.render.attachNewNode(text)
        self.textNode_2.setScale(5)
        self.textNode_2.setHpr(0,-90,0)
        self.textNode_2.setPos(24000,104,20.03)
        text = TextNode('text')
        text.setText("CONGRATULATIONS !!!! Correct Answer  ")
        text.setAlign(TextNode.ACenter)
        self.textNode_1 = self.render.attachNewNode(text)
        self.textNode_1.setScale(5)
        self.textNode_1.setHpr(0,-90,0)
        self.textNode_1.setPos(24000,104,20.03)
#1
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(244,94,20.03)
        text = TextNode('text')
        text.setText("Transmission Parameters are also known as")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(244,74,20.03)
#2
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(484,94,20.03)
        text = TextNode('text')
        text.setText(" For H parameter the equations are expressed in terms of ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(484,74,20.03)
#3
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(724,94,20.03)
        text = TextNode('text')
        text.setText("In the given equation V1 = 2I1 + 3I2 , Z12 = ?")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(724,74,20.03)
#4
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(964,94,20.03)
        text = TextNode('text')
        text.setText("Categorise the correct condition of symmetry observed in Z-parameters?")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(964,74,20.03)
#5
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(1204,94,20.03)
        text = TextNode('text')
        text.setText("Z Parameter is also known as")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(1204,74,20.03)
      
        self.textNode_1.setPos(24000,104,20.03)
#6
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(1404,94,20.03)
        text = TextNode('text')
        text.setText(" For Z parameter the equations are expressed in terms of")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(1404,74,20.03)
#7
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(1604,94,20.03)
        text = TextNode('text')
        text.setText("  How is Y12 calculated in terms of current and voltage gain? ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(1604,74,20.03)
#8
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(1804,94,20.03)
        text = TextNode('text')
        text.setText(" Cascade connections of two port network is analysed \nthrough ________ Parameters.")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(1804,74,20.03)
#9
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(2004,94,20.03)
        text = TextNode('text')
        text.setText(" From below which variable act as Independent variable in Y Parameters:")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(2004,74,20.03)
#10
        text = TextNode('text')
        text.setText("To climb ladder answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(2204,94,20.03)
        text = TextNode('text')
        text.setText("For calculation of Z11 and Z21, Output port is:")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(2204,74,20.03)

        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-244,94,20.03)
        text = TextNode('text')
        text.setText("Transmission Parameters are also known as")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-244,74,20.03)
#2
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-484,94,20.03)
        text = TextNode('text')
        text.setText(" For H parameter the equations are expressed in terms of ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-484,74,20.03)
#3
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-724,94,20.03)
        text = TextNode('text')
        text.setText("In the given equation V1 = 2I1 + 3I2 , Z12 = ?")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-724,74,20.03)
#4
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-964,94,20.03)
        text = TextNode('text')
        text.setText("Categorise the correct condition of symmetry observed in Z-parameters?")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-964,74,20.03)
#5
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-1204,94,20.03)
        text = TextNode('text')
        text.setText("Z Parameter is also known as")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-1204,74,20.03)
      
        self.textNode_1.setPos(24000,104,20.03)
#6
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-1404,94,20.03)
        text = TextNode('text')
        text.setText(" For Z parameter the equations are expressed in terms of")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-1404,74,20.03)
#7
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-1604,94,20.03)
        text = TextNode('text')
        text.setText("  How is Y12 calculated in terms of current and voltage gain? ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-1604,74,20.03)
#8
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-1804,94,20.03)
        text = TextNode('text')
        text.setText(" Cascade connections of two port network is analysed \nthrough ________ Parameters.")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-1804,74,20.03)
#9
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-2004,94,20.03)
        text = TextNode('text')
        text.setText(" From below which variable act as Independent variable in Y Parameters:")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-2004,74,20.03)
#10
        text = TextNode('text')
        text.setText("To avoid SNAKE BITE answer the following question ")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-2204,94,20.03)
        text = TextNode('text')
        text.setText("For calculation of Z11 and Z21, Output port is:")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(-2204,74,20.03)
     
        self.goti1 = self.loader.loadModel("create.egg")
        self.goti1.setHpr(0, 0, 0)
        self.goti1.setScale(1, 1, 0.02)
        self.goti1.setColor(0, 0.20, 0, 0.9)
        self.goti1.setPos(-5, 6, 22)
        self.goti1.reparentTo(self.render)

        self.goti2 = self.loader.loadModel("create1.egg")
        self.goti2.setHpr(0, 0, 0)
        self.goti2.setScale(1, 1, 0.02)
        self.goti2.setColor(0, 0, 0, 0)
        self.goti2.setPos(-5, 4, 22)
        self.goti2.reparentTo(self.render)

        self.goti3 = self.loader.loadModel("create2.egg")
        self.goti3.setHpr(0, 0, 0)
        self.goti3.setScale(1, 1, 0.02)
        self.goti3.setColor(0, 0, 0, 0)
        self.goti3.setPos(-7, 4, 22)
        self.goti3.reparentTo(self.render)

        self.goti4 = self.loader.loadModel("create3.egg")
        self.goti4.setHpr(0, 0, 0)
        self.goti4.setScale(1, 1, 0.02)
        self.goti4.setColor(0, 0, 0, 0)
        self.goti4.setPos(-7, 6, 22)
        self.goti4.reparentTo(self.render)

        self.dice = self.loader.loadModel("models/box")
        self.dice.setHpr(0, 0, 0)
        self.dice.setScale(20, 15, 20)
        self.dice.setColor(0.1,0.1 , 12, 0)
        self.dice.setPos(40, -20, 0)
        self.dice.reparentTo(self.render)

        self.dicemain = loader.loadModel("creatingenv.egg")
        self.dicemain.reparentTo(self.render)
        self.dicemain.setColor(60, 0, 40, 0)
        self.dicemain.setPos(50, -7.5,40 )
        self.dicemain.setHpr(0,0, 0)
        self.dicemain.setScale(1, 1, 1)

        self.box = self.loader.loadModel("models/box")
        self.box.setHpr(0, 0, 0)
        self.box.setScale(100, 100, 20)
        self.box.setColor(0, 128, 0, 0)
        self.box.setPos(0, 0, 0)
        self.box.reparentTo(self.render)

        myNodePath = loader.loadModel("LUDO.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(0, 60, 0.6, 0)
        myNodePath.setPos(0, 20, 20.4)
        myNodePath.setHpr(-10, -90, 0)
        myNodePath.setScale(1, 0.5, 1.5)

        myNodePath = loader.loadModel("ludo1.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(0, 40, 0, 0.6)
        myNodePath.setPos(73, 20, 20.4)
        myNodePath.setHpr(-15, -90, 0)
        myNodePath.setScale(1, 0.5, 1.5)

        myNodePath = loader.loadModel("LUDO2.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(0, 60, 40, 40)
        myNodePath.setPos(40, 38, 20.4)
        myNodePath.setHpr(10, -90, 0)
        myNodePath.setScale(1, 0.5, 1.5)

        myNodePath = loader.loadModel("LUDO3.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(40, 60, 40, 0)
        myNodePath.setPos(62, 8, 20.4)
        myNodePath.setHpr(20, -90, 0)
        myNodePath.setScale(1, 0.3, 1.5)

        myNodePath = loader.loadModel("LUDO3.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(0, 0.6, 0, 0)
        myNodePath.setPos(53, 58, 20.4)
        myNodePath.setHpr(-18, -90, 0)
        myNodePath.setScale(1, 0.3, 1.5)

        myNodePath = loader.loadModel("LUDOsap.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(60, 0, 40, 0)
        myNodePath.setPos(60, 70, 30.4)
        myNodePath.setHpr(90, 0, 0)
        myNodePath.setScale(0.5, 0.5, 0.5)

        myNodePath = loader.loadModel("LUDOsap1.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(600, 0, 0, 0)
        myNodePath.setPos(32, 91, 30.4)
        myNodePath.setHpr(90, 180, 0)
        myNodePath.setScale(0.4, 0.5, 0.3)

        myNodePath = loader.loadModel("LUDOsap.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(60, 0, 40, 0)
        myNodePath.setPos(59, 88, 30.4)
        myNodePath.setHpr(90, 0, 0)
        myNodePath.setScale(0.3, 0.4, 0.5)

        myNodePath = loader.loadModel("LUDOsap1.egg")
        myNodePath.reparentTo(self.render)
        myNodePath.setColor(600, 0, 0, 0)
        myNodePath.setPos(12, 71, 30.4)
        myNodePath.setHpr(90, 180, 0)
        myNodePath.setScale(0.3, 0.4, 0.2)

        text = TextNode('text')
        text.setText("1")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,4,20.03)
        text = TextNode('text')
        text.setText("2")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,4,20.03)
        text = TextNode('text')
        text.setText("3")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,4,20.03)
        text = TextNode('text')
        text.setText("4")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,4,20.03)
        text = TextNode('text')
        text.setText("5")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,4,20.03)
        text = TextNode('text')
        text.setText("6")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,4,20.03)
        text = TextNode('text')
        text.setText("7")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,4,20.03)
        text = TextNode('text')
        text.setText("8")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,4,20.03)
        text = TextNode('int')
        text.setText("9")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,4,20.03)
        text = TextNode('int')
        text.setText("10")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,4,20.03)

        
        text = TextNode('text')
        text.setText("11")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,14,20.03)
        text = TextNode('text')
        text.setText("12")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,14,20.03)
        text = TextNode('text')
        text.setText("13")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,14,20.03)
        text = TextNode('text')
        text.setText("14")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,14,20.03)
        text = TextNode('text')
        text.setText("15")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,14,20.03)
        text = TextNode('text')
        text.setText("16")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,14,20.03)
        text = TextNode('text')
        text.setText("17")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,14,20.03)
        text = TextNode('text')
        text.setText("18")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,14,20.03)
        text = TextNode('int')
        text.setText("19")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,14,20.03)
        text = TextNode('int')
        text.setText("20")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,14,20.03)

        
        text = TextNode('text')
        text.setText("21")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,24,20.03)
        text = TextNode('text')
        text.setText("22")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,24,20.03)
        text = TextNode('text')
        text.setText("23")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,24,20.03)
        text = TextNode('text')
        text.setText("24")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,24,20.03)
        text = TextNode('text')
        text.setText("25")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,24,20.03)
        text = TextNode('text')
        text.setText("26")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,24,20.03)
        text = TextNode('text')
        text.setText("27")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,24,20.03)
        text = TextNode('text')
        text.setText("28")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,24,20.03)
        text = TextNode('int')
        text.setText("29")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,24,20.03)
        text = TextNode('int')
        text.setText("30")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,24,20.03)

        
        text = TextNode('text')
        text.setText("31")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,34,20.03)
        text = TextNode('text')
        text.setText("32")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,34,20.03)
        text = TextNode('text')
        text.setText("33")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,34,20.03)
        text = TextNode('text')
        text.setText("34")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,34,20.03)
        text = TextNode('text')
        text.setText("35")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,34,20.03)
        text = TextNode('text')
        text.setText("36")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,34,20.03)
        text = TextNode('text')
        text.setText("37")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,34,20.03)
        text = TextNode('text')
        text.setText("38")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,34,20.03)
        text = TextNode('int')
        text.setText("39")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,34,20.03)
        text = TextNode('int')
        text.setText("40")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,34,20.03)

        
        text = TextNode('text')
        text.setText("41")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,44,20.03)
        text = TextNode('text')
        text.setText("42")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,44,20.03)
        text = TextNode('text')
        text.setText("43")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,44,20.03)
        text = TextNode('text')
        text.setText("44")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,44,20.03)
        text = TextNode('text')
        text.setText("45")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,44,20.03)
        text = TextNode('text')
        text.setText("46")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,44,20.03)
        text = TextNode('text')
        text.setText("47")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,44,20.03)
        text = TextNode('text')
        text.setText("48")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,44,20.03)
        text = TextNode('int')
        text.setText("49")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,44,20.03)
        text = TextNode('int')
        text.setText("50")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,44,20.03)

        
        text = TextNode('text')
        text.setText("51")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,54,20.03)
        text = TextNode('text')
        text.setText("52")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,54,20.03)
        text = TextNode('text')
        text.setText("53")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,54,20.03)
        text = TextNode('text')
        text.setText("54")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,54,20.03)
        text = TextNode('text')
        text.setText("55")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,54,20.03)
        text = TextNode('text')
        text.setText("56")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,54,20.03)
        text = TextNode('text')
        text.setText("57")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,54,20.03)
        text = TextNode('text')
        text.setText("58")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,54,20.03)
        text = TextNode('int')
        text.setText("59")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,54,20.03)
        text = TextNode('int')
        text.setText("60")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,54,20.03)

        
        text = TextNode('text')
        text.setText("61")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,64,20.03)
        text = TextNode('text')
        text.setText("62")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,64,20.03)
        text = TextNode('text')
        text.setText("63")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,64,20.03)
        text = TextNode('text')
        text.setText("64")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,64,20.03)
        text = TextNode('text')
        text.setText("65")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,64,20.03)
        text = TextNode('text')
        text.setText("66")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,64,20.03)
        text = TextNode('text')
        text.setText("67")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,64,20.03)
        text = TextNode('text')
        text.setText("68")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,64,20.03)
        text = TextNode('int')
        text.setText("69")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,64,20.03)
        text = TextNode('int')
        text.setText("70")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,64,20.03)

        text = TextNode('text')
        text.setText("71")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,74,20.03)
        text = TextNode('text')
        text.setText("72")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,74,20.03)
        text = TextNode('text')
        text.setText("73")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,74,20.03)
        text = TextNode('text')
        text.setText("74")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,74,20.03)
        text = TextNode('text')
        text.setText("75")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,74,20.03)
        text = TextNode('text')
        text.setText("76")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,74,20.03)
        text = TextNode('text')
        text.setText("77")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,74,20.03)
        text = TextNode('text')
        text.setText("78")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,74,20.03)
        text = TextNode('int')
        text.setText("79")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,74,20.03)
        text = TextNode('int')
        text.setText("80")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,74,20.03)

        
        text = TextNode('text')
        text.setText("81")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,84,20.03)
        text = TextNode('text')
        text.setText("82")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,84,20.03)
        text = TextNode('text')
        text.setText("83")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,84,20.03)
        text = TextNode('text')
        text.setText("84")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,84,20.03)
        text = TextNode('text')
        text.setText("85")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,84,20.03)
        text = TextNode('text')
        text.setText("86")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,84,20.03)
        text = TextNode('text')
        text.setText("87")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,84,20.03)
        text = TextNode('text')
        text.setText("88")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,84,20.03)
        text = TextNode('int')
        text.setText("89")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,84,20.03)
        text = TextNode('int')
        text.setText("90")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,84,20.03)

        
        text = TextNode('text')
        text.setText("91")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(94,94,20.03)
        text = TextNode('text')
        text.setText("92")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(84,94,20.03)
        text = TextNode('text')
        text.setText("93")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(74,94,20.03)
        text = TextNode('text')
        text.setText("94")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(64,94,20.03)
        text = TextNode('text')
        text.setText("95")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(54,94,20.03)
        text = TextNode('text')
        text.setText("96")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(44,94,20.03)
        text = TextNode('text')
        text.setText("97")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(34,94,20.03)
        text = TextNode('text')
        text.setText("98")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(24,94,20.03)
        text = TextNode('int')
        text.setText("99")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(14,94,20.03)
        text = TextNode('int')
        text.setText("100")
        text.setAlign(TextNode.ACenter)
        textNode = self.render.attachNewNode(text)
        textNode.setScale(5)
        textNode.setHpr(0,-90,0)
        textNode.setPos(4,94,20.03)

        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 0, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 0, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 10, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 10, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 20, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 20, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 30, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 30, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 40, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 40, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 50, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 50, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 60, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 60, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 70, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 70, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 80, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 80, 20)
            self.box1.reparentTo(self.render)
        for i in range(1,11,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(0, 40, 0.128, 0)
            self.box1.setPos(i*10, 90, 20)
            self.box1.reparentTo(self.render)
        for i in range(0,10,2):
            self.box1 = self.loader.loadModel("models/box")
            self.box1.setHpr(0, 0, 0)
            self.box1.setScale(10, 10, 0.02)
            self.box1.setColor(128, 0, 0, 0)
            self.box1.setPos(i*10, 90, 20)
            self.box1.reparentTo(self.render)



        


        
app = MyGame()
app.run()
