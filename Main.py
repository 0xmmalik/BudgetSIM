#####################
# IMPORT STATEMENTS #
#####################
import pygame
assert pygame.init() == (6, 0)
from pygame.locals import *
from random import random, randint
from time import sleep
import webbrowser

##########
# IMAGES  #
##########
load = pygame.image.load
screen1 = load("img/screen1.png")

opioidEpidemic = load("img/opioidepidemic.png")
iraqWar = load("img/iraqwar.png")

spinner = load("img/spinner.png")
cont = load("img/continue.png")
info = load("img/info.png")

p_bar = load("img/progress_bar.png")

#################
# INSTANTIATING   #
#################
FONT = pygame.font.Font("img/pixelated.ttf", 50)
SPINNERS = [(50, 165), (250, 165), (475, 165), (715, 165), (75, 275), (400, 275), (675, 275)]
values = [14, 14, 14, 14, 14, 14, 15]
txt = []
screen = pygame.display.set_mode((1000, 500))
cursor = load("img/cursor.png").convert_alpha()
pygame.display.set_caption("Congressional Budget Manager -- MM Olde Games")
#pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) # set base cursor to invisible

# Military, Education, Healthcare, Transportation, Public Welfare, Employment, Foreign Relations
events = [
    (opioidEpidemic, (5, 14, 55, 8, 8, 5, 5), "https://www.drugabuse.gov/drugs-abuse/opioids/opioid-overdose-crisis"),
    (iraqWar, (50, 5, 5, 5, 5, 5, 25), "https://en.wikipedia.org/wiki/Iraq_War?scrlybrkr=5065a312")
    ]

for i in range(len(values)):
    txt.append(FONT.render(str(values[i]), False, (0, 0, 0)))

def checkSpinner(spinner):
    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= spinner[0] and pygame.mouse.get_pos()[0] <= spinner[0] + 42 and pygame.mouse.get_pos()[1] >= spinner[1] and pygame.mouse.get_pos()[1] <= spinner[1] + 38:
        return("up")
    elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= spinner[0] and pygame.mouse.get_pos()[0] <= spinner[0] + 42 and pygame.mouse.get_pos()[1] >= spinner[1] + 38 and pygame.mouse.get_pos()[1] <= spinner[1] + 76:
        return("down")
    return False

def checkContinue():
    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1] >= 450:
        return True
    return False

def checkInfo():
    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] <= 50 and pygame.mouse.get_pos()[1] <= 50:
        return True
    return False

def blitSpinners():
    for i in range(len(SPINNERS)):
        screen.blit(spinner, SPINNERS[i])
        screen.blit(txt[i], (SPINNERS[i][0] + 50, SPINNERS[i][1] + 10))
    screen.blit(cont, (0, 450))
    screen.blit(info, (0, 0))
    #screen.blit(cursor, pygame.mouse.get_pos())
    pygame.display.flip()

##################
# MAIN FUNCTION  #
##################
initScr = True
while initScr:
    screen.blit(screen1, (0, 0))
    screen.blit(cursor, pygame.mouse.get_pos())
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            initScr = False

for i in range(3): # three events will be simulated
    eventID = randint(0, len(events) - 1)
    screen.blit(events[eventID][0], (0, 0))
    blitSpinners()
    settingBudget = True
    while settingBudget:
        for event in pygame.event.get():
            for i in range(len(SPINNERS)):
                if checkSpinner(SPINNERS[i]) == "up" and values[i] < 100:
                    values[i] += 1
                    txt[i] = FONT.render(str(values[i]), False, (0, 0, 0))
                elif checkSpinner(SPINNERS[i]) == "down" and values[i] > 0:
                    values[i] -= 1
                    txt[i] = FONT.render(str(values[i]), False, (0, 0, 0))
                screen.blit(events[eventID][0], (0, 0))
                blitSpinners()
            if checkContinue() and sum(values) == 100:
                settingBudget = False
            elif checkContinue() and sum(values) != 100:
                if sum(values) < 100:
                    screen.blit(FONT.render("Need " + str(100 - sum(values)) + " more!", False, (255, 255, 255)), (50, 400))
                    pygame.display.flip()
                else:
                    screen.blit(FONT.render("Need " + str(sum(values) - 100) + " less!", False, (255, 255, 255)), (50, 400))
                    pygame.display.flip()
            if checkInfo():
                webbrowser.open(events[eventID][2])
            if event.type == pygame.QUIT:
                pygame.display.quit()
    score = 600
    for i in range(len(values)):
        score -= abs(values[0] - events[eventID][1][i])
    score = score // 6 - 60
    viewingScore = True
    drawingBar = int(score / 40 * 1000)
    initDrawingBar = drawingBar
    if drawingBar <= 0:
        drawingBar = 1
    screen.fill((0, 0, 0))
    while drawingBar:
        pygame.event.get()
        screen.blit(p_bar, (initDrawingBar - drawingBar, 250))
        sleep(0.005)
        drawingBar -= 1
        pygame.display.flip()
    screen.blit(FONT.render("Event score: " + str(score) + "/40", False, (255, 255, 255)), (0, 0))
    screen.blit(cont, (0, 450))
    pygame.display.flip()
    while viewingScore:
        pygame.event.clear()
        for event in pygame.event.get():
            if checkContinue() and sum(values) == 100:
                viewingScore = False
pygame.display.quit()
