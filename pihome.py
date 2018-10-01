#!/usr/bin/python2.7
import pygame
from pygame.locals import *
import time
import sys
import pgbutton
import datetime

pygame.init()
pygame.font.init()

date = time.strftime("%d")

WIDTH = 800
HEIGHT = 480

GREY = pygame.Color(68, 68, 68)
LIGHTGREY = pygame.Color(169, 169, 169)
DARKGREY = pygame.Color(255, 255, 255)

bodyfont = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 14)


def dateSuffix():
	digits = [int(digit) for digit in str(date)]
	
	if digits[-1] == 1:
		return "st"
	elif digits[-1] == 2:
		return "nd"
	elif digits[-1] == 3:
		return "rd"
	elif digits[-1] >= 4:
		return "th"
	elif digits[-1] == 0:
		return "th"

def init():
	running = True

def cleanup():
	pygame.quit()
	sys.exit()
	
def main_menu():
	
	global DISPLAYSURF
	DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
	
	timeButtonObj = pgbutton.PgButton((50, 50, 120, 60), "Time and Date")
	weatherButtonObj = pgbutton.PgButton((630, 50, 120, 60), "Weather")
	
	exitButtonObj = pgbutton.PgButton((740, 50, 40, 20))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				cleanup()
			
			if 'click' in timeButtonObj.handleEvent(event):
				setup_time()
			
			if 'click' in weatherButtonObj.handleEvent(event):
				setup_weather()
				
		pygame.Surface.fill(DISPLAYSURF, GREY)
		timeButtonObj.draw(DISPLAYSURF)
		weatherButtonObj.draw(DISPLAYSURF)
		pygame.display.update()	
	 	
def setup_time():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				cleanup()
		pygame.Surface.fill(DISPLAYSURF, GREY)
		#currentTime = datetime.strptime("%A, %d %B, %H:%M:%S")
		currentTime = time.strftime("%A, %d" + dateSuffix() + " %B, %H:%M:%S")
		print currentTime
		pygame.display.update()

def setup_weather():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				cleanup()
			
			#if 
				
		pygame.Surface.fill(DISPLAYSURF, DARKGREY)
		pygame.display.update()
		

if __name__ == "__main__":
	init()
	main_menu()
	raw_input()
	setup_time()
	raw_input()

