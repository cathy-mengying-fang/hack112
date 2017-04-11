import cv2
import numpy
import pygame, sys
from pygame.locals import *
import os
import _thread
from queue import Queue

RED = (255,0,0)
GREEN = (0, 255, 0)
ACOLOR = BCOLOR = CCOLOR = DCOLOR = ECOLOR = FCOLOR = GCOLOR = RED
pygame.init()
camera = cv2.VideoCapture(0)
#converts open cv to pygame
result = ""

screen_width, screen_height = 640, 480
screen=pygame.display.set_mode((screen_width,screen_height))

b1 = "c:/Users/Sophie/Documents/Classes/15112/hackathon/musicSample.jpg"
back = pygame.image.load(b1).convert()

def getCamFrame(camera):
    retval,im=camera.read()
    frame=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    frame=numpy.rot90(frame)
    frame=pygame.surfarray.make_surface(frame) #I think the color error lies in this line?
    return frame, im

def blitCamFrame(frame,screen):
    screen.blit(frame,(0,0))

screen.fill(0) #set pygame screen to black
clock = pygame.time.Clock()
playing = True
x = screen_width
fileWidth = 2557


def surface_to_string(surface):
    """Convert a pygame surface into string"""
    return pygame.image.tostring(surface, 'RGB')


def detect_faces(im, messageChannel):
    #Detects faces based on haar. Returns points
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('/Users/Sophie/Desktop/haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    # ensure at least some circles were found
    if len(faces) > 0:
        # convert the (x, y) coordinates and radius of the circles to integers
        faces = numpy.round(faces[0, :]).astype("int")
        faceList = list(faces)
        x1=640-faceList[0] - faceList[2]
        faceList[0] = x1
        y1=faceList[1]
        x2=faceList[2]
        y2=faceList[3]
        pygame.draw.rect(screen, (255,255,255), (x1, y1, x2, y2), 4)
        letterA = pygame.font.SysFont(None, 48)
        text = letterA.render("A", True, (255, 255, 255))
        screen.blit(text,(48, 286))
        messageChannel.put(faceList, False)


timePassed = 0
messageChannel = Queue(100)

while playing:
    clock.tick(100)
    timePassed+=100
    if messageChannel.qsize() > 0:
        msg = messageChannel.get(False)
    else:
        msg = ""
    if isinstance(msg, list):
        x1 = msg[0]
        y1 = msg[1]
        x2 = msg[2]
        y2 = msg[3]

        targetY, targetWidth, targetHeight = 300-35,70,70
        targetA = 60-35
        targetB = targetA + 85
        targetC = targetB + 85
        targetD = targetC + 85
        targetE = targetD + 85
        targetF = targetE + 85
        targetG = targetF + 85

        # if this version of the object in target range

        if y1+y2 >= targetY and y1< targetY + targetHeight:
            if x1+x2 >= targetA and x1< targetA + targetWidth:
                result ="A"

            elif x1+x2 >= targetB and x1< targetB + targetWidth:
                result ="B"
            elif x1+x2 >= targetC and x1< targetC + targetWidth:
                result ="C"
            elif x1+x2 >= targetD and x1< targetD + targetWidth:
                result ="D"
            elif x1+x2 >= targetE and x1< targetE + targetWidth:
                result ="E"
            elif x1+x2 >= targetF and x1< targetF + targetWidth:
                result ="F"
            elif x1+x2 >= targetG and x1< targetG + targetWidth:
                result ="G"
        print(result)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("Pressed a key")
        if event.type == pygame.QUIT:
            playing = False

    frame, im = getCamFrame(camera)
    blitCamFrame(frame,screen)
    
    # detect faces in the image
    if timePassed%250==0:
        _thread.start_new_thread(detect_faces, (im,messageChannel))

    screen.blit(back, (x, 0))
    x -= 2
    if x == -fileWidth:
        x = screen_width
   
    #music tracker
    pygame.draw.line(screen, (255, 0,0), (screen_width/2,0), (screen_width/2,100), 10)
  
    
    if result=="A":
        ACOLOR = GREEN
    if result != "A":
        ACOLOR = RED
    if result == "B":
        BCOLOR = GREEN
    if result != "B":
        BCOLOR = RED
    if result == "C":
        CCOLOR = GREEN
    if result != "C":
        CCOLOR = RED
    if result == "D":
        DCOLOR = GREEN
    if result != "D":
        DCOLOR = RED
    if result == "E":
        ECOLOR = GREEN
    if result != "E":
        ECOLOR = RED
    if result == "F":
        FCOLOR = GREEN
    if result != "F":
        FCOLOR = RED
    if result == "G":
        GCOLOR = GREEN
    if result != "G":
        GCOLOR = RED

    pygame.draw.circle(screen, ACOLOR,(60, 300), 35)
    letterA = pygame.font.SysFont(None, 48)
    text = letterA.render("A", True, (255, 255, 255))
    screen.blit(text,(48, 286))
    #B circle
    pygame.draw.circle(screen, BCOLOR, (145,300), 35)
    letterB = pygame.font.SysFont(None, 48)
    text = letterB.render("B", True, (255, 255, 255))
    screen.blit(text,(133, 286))
    #C circle
    pygame.draw.circle(screen, CCOLOR, (225,300), 35)
    letterC = pygame.font.SysFont(None, 48)
    text = letterC.render("C", True, (255, 255, 255))
    screen.blit(text,(213, 286))
    #D circle
    pygame.draw.circle(screen, DCOLOR, (310,300), 35)
    letterD = pygame.font.SysFont(None, 48)
    text = letterD.render("D", True, (255, 255, 255))
    screen.blit(text,(298, 286))
    #E circle
    pygame.draw.circle(screen, ECOLOR, (395,300), 35)
    letterE = pygame.font.SysFont(None, 48)
    text = letterE.render("E", True, (255, 255, 255))
    screen.blit(text,(383, 286))
    #F circle
    pygame.draw.circle(screen, FCOLOR, (475,300), 35)
    letterF = pygame.font.SysFont(None, 48)
    text = letterF.render("F", True, (255, 255, 255))
    screen.blit(text,(465, 286))
    #G circle
    pygame.draw.circle(screen, GCOLOR, (555,300), 35)
    letterG = pygame.font.SysFont(None, 48)
    text = letterG.render("G", True, (255, 255, 255))
    screen.blit(text,(543, 286))    
  
    pygame.display.update()
    pygame.display.flip()



